import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.List;
import javax.swing.Timer;
import java.sql.*;
import java.util.*;
import javax.swing.*;

/**
 * A Player osztály egy játékost reprezentál a játékban, névvel, színnel,
 * pozícióval, iránnyal és élő státusszal.
 * 
 * Főbb attribútumok:
 * - name: A játékos neve.
 * - color: A játékos színe.
 * - x, y: A játékos aktuális pozíciója a játéktéren.
 * - direction: A játékos mozgásának iránya (0: fel, 1: jobbra, 2: le, 3:
 * balra).
 * - alive: A játékos élő státusza (igaz, ha a játékos él, hamis, ha meghalt).
 * 
 * Főbb metódusok:
 * - move(): A játékos mozgatása az aktuális irányba.
 * - getName(), getColor(), getX(), getY(), isAlive(): Getter metódusok az
 * attribútumok lekérdezéséhez.
 * - setAlive(boolean alive), setDirection(int direction): Setter metódusok az
 * attribútumok beállításához.
 */
class Player {
    private final String name;
    private final Color color;
    private int x, y;
    private int direction;
    private boolean alive;

    public Player(String name, Color color, int startX, int startY) {
        this.name = name;
        this.color = color;
        this.x = startX;
        this.y = startY;
        this.direction = 1;
        this.alive = true;
    }

    public String getName() {
        return name;
    }

    public Color getColor() {
        return color;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public boolean isAlive() {
        return alive;
    }

    public void setAlive(boolean alive) {
        this.alive = alive;
    }

    public void setDirection(int direction) {
        this.direction = direction;
    }

    public void move() {
        switch (direction) {
            case 0:
                y--;
                break;
            case 1:
                x++;
                break;
            case 2:
                y++;
                break;
            case 3:
                x--;
                break;
        }
    }
}

/**
 * A DatabaseManager osztály a játékosok pontszámainak kezelésére szolgáló Derby
 * adatbázis kezelésére szolgáló metódusokat biztosít.
 * Tartalmazza az adatbázis inicializálásának, a játékos pontszámok
 * frissítésének és a legjobb játékosok lekérdezésének funkcióit.
 * 
 * Főbb funkciók:
 * - Adatbázis inicializálása: Létrehozza a szükséges táblákat, ha még nem
 * léteznek.
 * - Pontszám frissítése: Frissíti a megadott játékos pontszámát, vagy új
 * bejegyzést hoz létre, ha a játékos még nem létezik.
 * - Legjobb játékosok lekérdezése: Lekérdezi a legjobb játékosokat pontszám
 * szerint csökkenő sorrendben.
 * 
 * Metódusok:
 * - updateScore(String playerName): Frissíti a megadott játékos pontszámát.
 * - getTopPlayers(): Lekérdezi a legjobb játékosokat pontszám szerint csökkenő
 * sorrendben.
 */
class DatabaseManager {
    private static final String DERBY_URL = "jdbc:derby:trondb;create=true";

    static {
        try {
            Class.forName("org.apache.derby.jdbc.EmbeddedDriver");
            try (Connection conn = DriverManager.getConnection(DERBY_URL)) {
                Statement stmt = conn.createStatement();
                try {
                    stmt.executeUpdate(
                            "CREATE TABLE players (" +
                                    "id INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1, INCREMENT BY 1), "
                                    +
                                    "name VARCHAR(50) NOT NULL, " +
                                    "score INTEGER DEFAULT 0, " +
                                    "CONSTRAINT player_pk PRIMARY KEY (id))");
                } catch (SQLException e) {
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void updateScore(String playerName) {
        try (Connection conn = DriverManager.getConnection(DERBY_URL)) {
            String sql = "MERGE INTO players USING SYSIBM.SYSDUMMY1 " +
                    "ON players.name = ? " +
                    "WHEN MATCHED THEN UPDATE SET score = score + 1 " +
                    "WHEN NOT MATCHED THEN INSERT (name, score) VALUES (?, 1)";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, playerName);
            stmt.setString(2, playerName);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static List<Map.Entry<String, Integer>> getTopPlayers() {
        List<Map.Entry<String, Integer>> topPlayers = new ArrayList<>();
        try (Connection conn = DriverManager.getConnection(DERBY_URL)) {
            String sql = "SELECT name, score FROM players ORDER BY score DESC FETCH FIRST 10 ROWS ONLY";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            while (rs.next()) {
                topPlayers.add(new AbstractMap.SimpleEntry<>(
                        rs.getString("name"),
                        rs.getInt("score")));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return topPlayers;
    }
}

/**
 * A GamePanel osztály a fő játéktér, ahol a játék logikája és a megjelenítés
 * történik.
 * A JPanel osztályt bővíti, és kezeli a játék állapotát, a játékosok mozgását,
 * valamint a játék rácsának megjelenítését.
 * 
 * Főbb funkciók:
 * - Játékosok mozgásának kezelése a billentyűzet bemenet alapján.
 * - Játék állapotának frissítése, beleértve az ütközések ellenőrzését és a
 * játék végét.
 * - Játék rácsának megjelenítése, beleértve a játékosok pozícióját és a rács
 * színeit.
 * - Játék vége párbeszédablak megjelenítése a győztes játékos nevével és a
 * menübe való visszatérés vagy a játék bezárásának lehetőségével.
 * 
 * Metódusok:
 * - GamePanel(MainFrame parent): Konstruktor, amely inicializálja a játéktáblát
 * és beállítja a billentyűzet figyelőket.
 * - startGame(Player p1, Player p2): Elindítja a játékot a megadott
 * játékosokkal.
 * - setupKeyListeners(): Beállítja a billentyűzet figyelőket a játékosok
 * mozgásának kezelésére.
 * - updateGame(): Frissíti a játék állapotát, beleértve a játékosok mozgását és
 * az ütközések ellenőrzését.
 * - checkCollision(Player player): Ellenőrzi, hogy a megadott játékos
 * ütközött-e a rács szélével vagy más játékossal.
 * - showGameOverDialog(Player winner): Megjeleníti a játék vége
 * párbeszédablakot a győztes játékos nevével.
 * - paintComponent(Graphics g): Megjeleníti a játék rácsát és a játékosok
 * pozícióját.
 */
class GamePanel extends JPanel {
    private static final int CELL_SIZE = 10;
    private final Color[][] gridColors = new Color[80][60];
    private boolean[][] grid;
    private Player player1;
    private Player player2;
    private Timer timer;
    private boolean gameOver;
    private MainFrame parentFrame;

    private static final Color OBSTACLE_COLOR = Color.WHITE;
    private static final int OBSTACLE_COUNT = 15;
    private final Random random = new Random();

    public GamePanel(MainFrame parent) {
        this.parentFrame = parent;
        setPreferredSize(new Dimension(800, 600));
        grid = new boolean[80][60];
        setFocusable(true);
        setupKeyListeners();
    }

    private void generateObstacles() {
        for (int i = 0; i < OBSTACLE_COUNT; i++) {
            int x = random.nextInt(60) + 10; // Avoid edges
            int y = random.nextInt(40) + 10; // Avoid edges
            grid[x][y] = true;
            gridColors[x][y] = OBSTACLE_COLOR;
        }
    }

    private void showGameOverDialog(Player winner) {
        String message = winner.getName() + " wins!";
        JDialog dialog = new JDialog(parentFrame, "Game Over", true);
        dialog.setLayout(new GridLayout(3, 1));

        JLabel winLabel = new JLabel(message, SwingConstants.CENTER);
        JButton menuButton = new JButton("Back to Menu");
        JButton exitButton = new JButton("Exit Game");

        menuButton.addActionListener(e -> {
            dialog.dispose();
            parentFrame.showMenu();
        });

        exitButton.addActionListener(e -> System.exit(0));

        dialog.add(winLabel);
        dialog.add(menuButton);
        dialog.add(exitButton);

        dialog.setSize(200, 150);
        dialog.setLocationRelativeTo(parentFrame);
        dialog.setVisible(true);
    }

    public void startGame(Player p1, Player p2) {
        player1 = p1;
        player2 = p2;
        grid = new boolean[80][60];
        gameOver = false;

        generateObstacles();

        grid[player1.getX()][player1.getY()] = true;
        grid[player2.getX()][player2.getY()] = true;
        gridColors[player1.getX()][player1.getY()] = player1.getColor();
        gridColors[player2.getX()][player2.getY()] = player2.getColor();

        timer = new Timer(100, e -> {
            if (!gameOver) {
                updateGame();
                repaint();
            }
        });
        timer.start();
    }

    private void setupKeyListeners() {
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                switch (e.getKeyCode()) {
                    case KeyEvent.VK_W:
                        player1.setDirection(0);
                        break;
                    case KeyEvent.VK_D:
                        player1.setDirection(1);
                        break;
                    case KeyEvent.VK_S:
                        player1.setDirection(2);
                        break;
                    case KeyEvent.VK_A:
                        player1.setDirection(3);
                        break;

                    case KeyEvent.VK_UP:
                        player2.setDirection(0);
                        break;
                    case KeyEvent.VK_RIGHT:
                        player2.setDirection(1);
                        break;
                    case KeyEvent.VK_DOWN:
                        player2.setDirection(2);
                        break;
                    case KeyEvent.VK_LEFT:
                        player2.setDirection(3);
                        break;
                }
            }
        });
    }

    private void updateGame() {
        if (player1.isAlive() && player2.isAlive()) {
            grid[player1.getX()][player1.getY()] = true;
            gridColors[player1.getX()][player1.getY()] = player1.getColor();
            grid[player2.getX()][player2.getY()] = true;
            gridColors[player2.getX()][player2.getY()] = player2.getColor();

            player1.move();
            player2.move();

            checkCollision(player1);
            checkCollision(player2);
        }
    }

    private void checkCollision(Player player) {
        int x = player.getX();
        int y = player.getY();

        if (x < 0 || x >= 80 || y < 0 || y >= 60 || grid[x][y]) {
            player.setAlive(false);
            gameOver = true;
            timer.stop();

            Player winner = (player == player1) ? player2 : player1;
            DatabaseManager.updateScore(winner.getName());
            parentFrame.updateLeaderboard();
            showGameOverDialog(winner);
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        for (int x = 0; x < 80; x++) {
            for (int y = 0; y < 60; y++) {
                if (grid[x][y]) {
                    if (x == player1.getX() && y == player1.getY()) {
                        g.setColor(player1.getColor());
                    } else if (x == player2.getX() && y == player2.getY()) {
                        g.setColor(player2.getColor());
                    } else if (gridColors[x][y] == OBSTACLE_COLOR) {
                        g.setColor(OBSTACLE_COLOR);
                    } else {
                        g.setColor(gridColors[x][y]);
                    }
                    g.fillRect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
                }
            }
        }
    }
}

/**
 * A MainFrame a Tron Game alkalmazás fő ablaka.
 * CardLayout-ot használ a különböző panelek közötti váltáshoz: menü, játék és
 * ranglista.
 * 
 * A MainFrame osztály a következő funkciókat tartalmazza:
 * - A főmenü megjelenítése, amely lehetőséget kínál új játék indítására, a
 * ranglista megtekintésére vagy az alkalmazás bezárására.
 * - A játékpanel beállítása, ahol a játék zajlik.
 * - A ranglista megjelenítése a legjobb játékosokkal.
 * - Játékos beállítási párbeszédablak megjelenítése a játékosnevek és színek
 * konfigurálásához az új játék indítása előtt.
 * 
 * Metódusok:
 * - MainFrame(): Konstruktor, amely inicializálja a keretet, beállítja a
 * paneleket és konfigurálja az elrendezést.
 * - showMenu(): Megjeleníti a főmenü panelt.
 * - createMenuPanel(): Létrehozza és konfigurálja a főmenü panelt új játék,
 * ranglista és kilépés gombokkal.
 * - createGamePanel(): Hozzáadja a játékpanelt a főpanelhez.
 * - createLeaderboardPanel(): Létrehozza és konfigurálja a ranglista panelt a
 * legjobb játékosok listájával és egy vissza gombbal.
 * - showPlayerSetup(): Megjelenít egy párbeszédablakot a játékosnevek és színek
 * beállításához az új játék indítása előtt.
 */
class MainFrame extends JFrame {
    private final CardLayout cardLayout;
    private final JPanel mainPanel;
    private final GamePanel gamePanel;
    private JTextArea leaderboardText;

    public MainFrame() {
        setTitle("Tron Game");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        cardLayout = new CardLayout();
        mainPanel = new JPanel(cardLayout);
        gamePanel = new GamePanel(this);

        createMenuPanel();
        createGamePanel();
        createLeaderboardPanel();

        add(mainPanel);
        pack();
        setLocationRelativeTo(null);
    }

    public void showMenu() {
        cardLayout.show(mainPanel, "menu");
    }

    private void createMenuPanel() {
        JPanel menuPanel = new JPanel(new GridLayout(3, 1, 10, 10));

        JButton newGameBtn = new JButton("New Game");
        JButton leaderboardBtn = new JButton("Leaderboard");
        JButton exitBtn = new JButton("Exit");

        newGameBtn.addActionListener(e -> showPlayerSetup());
        leaderboardBtn.addActionListener(e -> cardLayout.show(mainPanel, "leaderboard"));
        exitBtn.addActionListener(e -> System.exit(0));

        menuPanel.add(newGameBtn);
        menuPanel.add(leaderboardBtn);
        menuPanel.add(exitBtn);

        mainPanel.add(menuPanel, "menu");
    }

    private void createGamePanel() {
        mainPanel.add(gamePanel, "game");
    }

    void updateLeaderboard() {
        List<Map.Entry<String, Integer>> topPlayers = DatabaseManager.getTopPlayers();
        StringBuilder sb = new StringBuilder("Top Players:\n\n");
        for (Map.Entry<String, Integer> player : topPlayers) {
            sb.append(player.getKey()).append(": ").append(player.getValue()).append("\n");
        }
        leaderboardText.setText(sb.toString());
    }

    private void createLeaderboardPanel() {
        JPanel leaderboardPanel = new JPanel(new BorderLayout());
        JButton backBtn = new JButton("Back to Menu");
        backBtn.addActionListener(e -> cardLayout.show(mainPanel, "menu"));

        leaderboardText = new JTextArea();
        leaderboardText.setEditable(false);

        leaderboardPanel.add(new JScrollPane(leaderboardText), BorderLayout.CENTER);
        leaderboardPanel.add(backBtn, BorderLayout.SOUTH);

        updateLeaderboard();
        mainPanel.add(leaderboardPanel, "leaderboard");
    }

    private void showPlayerSetup() {
        JDialog dialog = new JDialog(this, "Player Setup", true);
        dialog.setLayout(new GridLayout(5, 2));

        JTextField p1Name = new JTextField();
        JTextField p2Name = new JTextField();
        JButton p1Color = new JButton("Select Color");
        JButton p2Color = new JButton("Select Color");

        Color[] colors = new Color[] { Color.RED, Color.BLUE };

        p1Color.addActionListener(e -> {
            Color c = JColorChooser.showDialog(dialog, "Choose Player 1 Color", Color.RED);
            if (c != null)
                colors[0] = c;
        });

        p2Color.addActionListener(e -> {
            Color c = JColorChooser.showDialog(dialog, "Choose Player 2 Color", Color.BLUE);
            if (c != null)
                colors[1] = c;
        });

        JButton startBtn = new JButton("Start Game");
        startBtn.addActionListener(e -> {
            if (!p1Name.getText().isEmpty() && !p2Name.getText().isEmpty()) {
                Player player1 = new Player(p1Name.getText(), colors[0], 20, 30);
                Player player2 = new Player(p2Name.getText(), colors[1], 60, 30);
                gamePanel.startGame(player1, player2);
                cardLayout.show(mainPanel, "game");
                gamePanel.requestFocus();
                dialog.dispose();
            }
        });

        dialog.add(new JLabel("Player 1 Name:"));
        dialog.add(p1Name);
        dialog.add(new JLabel("Player 1 Color:"));
        dialog.add(p1Color);
        dialog.add(new JLabel("Player 2 Name:"));
        dialog.add(p2Name);
        dialog.add(new JLabel("Player 2 Color:"));
        dialog.add(p2Color);
        dialog.add(new JLabel(""));
        dialog.add(startBtn);

        dialog.pack();
        dialog.setLocationRelativeTo(this);
        dialog.setVisible(true);
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            Class.forName("org.apache.derby.jdbc.EmbeddedDriver");
        } catch (ClassNotFoundException e) {
            System.err.println("Derby JDBC Driver not found.");
            return;
        }

        SwingUtilities.invokeLater(() -> {
            MainFrame frame = new MainFrame();
            frame.setVisible(true);
        });
    }
}
