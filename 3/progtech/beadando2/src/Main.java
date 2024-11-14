import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;
import java.util.ArrayList;
import java.util.List;

/**
 * Represents a player in the game.
 */
class Player {
    private String color;

    /**
     * Constructs a Player with the specified color and initial tiles.
     *
     * @param color the color of the player
     */
    public Player(String color) {
        this.color = color;
    }

    /**
     * Returns the color of the player.
     *
     * @return the color of the player
     */
    public String getColor() {
        return color;
    }

     /**
     * Returns the number of tiles left for the player on the board.
     *
     * @param board the game board
     * @return the number of tiles left
     */
    public int getTilesLeft(int[][] board) {
        int count = 0;
        for (int[] row : board) {
            for (int cell : row) {
                if (cell == (color.equals("White") ? 1 : -1)) {
                    count++;
                }
            }
        }
        return count;
    }
}

/**
 * Represents the game board.
 */
class GameBoard extends JPanel {
    private int[][] board;
    private int n;
    private int movesLeft;
    private int selectedX = -1, selectedY = -1;
    private Player player1, player2;
    private Player currentPlayer;
    private static final int WHITE_PIECE = 1;
    private static final int BLACK_PIECE = -1;

    /**
     * Constructs a GameBoard with the specified size.
     *
     * @param n the size of the board
     */
    public GameBoard(int n) {
        this.n = n;
        this.board = new int[n][n];
        this.movesLeft = 5 * n;
        this.player1 = new Player("White");
        this.player2 = new Player("Black");
        this.currentPlayer = player1;
        initializeBoard();
        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                int x = e.getY() / 50;
                int y = e.getX() / 50;
                if (x >= 0 && x < n && y >= 0 && y < n && board[x][y] != 0 &&
                        ((board[x][y] == 1 && currentPlayer == player1) || (board[x][y] == -1 && currentPlayer == player2))) {
                    selectedX = x;
                    selectedY = y;
                    repaint();
                }
            }
        });
    }

    /**
     * Initializes the game board with random positions for the tiles.
     */
    private void initializeBoard() {
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            int x, y;
            do {
                x = rand.nextInt(n);
                y = rand.nextInt(n);
            } while (board[x][y] != 0);
            board[x][y] = 1;
        }
        for (int i = 0; i < n; i++) {
            int x, y;
            do {
                x = rand.nextInt(n);
                y = rand.nextInt(n);
            } while (board[x][y] != 0);
            board[x][y] = -1;
        }
    }

    /**
     * Moves the selected tile in the specified direction.
     *
     * @param direction the direction to move the tile
     */
    public void move(String direction) {
        if (selectedX == -1 || selectedY == -1) return;

        int dx = 0, dy = 0;
        switch (direction) {
            case "UP" -> dx = -1;
            case "DOWN" -> dx = 1;
            case "LEFT" -> dy = -1;
            case "RIGHT" -> dy = 1;
        }

        int x = selectedX, y = selectedY;
        List<int[]> piecesToMove = new ArrayList<>();

        while (isValid(x, y) && isWhiteOrBlackCell(x, y)) {
            piecesToMove.add(new int[]{x, y});
            x += dx;
            y += dy;
        }

        for (int i = piecesToMove.size() - 1; i >= 0; i--) {
            int[] pos = piecesToMove.get(i);
            int newX = pos[0] + dx;
            int newY = pos[1] + dy;
            if (isValid(newX, newY)) {
                board[newX][newY] = board[pos[0]][pos[1]];
                board[pos[0]][pos[1]] = 0;
            } else {
                board[pos[0]][pos[1]] = 0;
            }
        }

        movesLeft--;

        selectedX = selectedY = -1;
        currentPlayer = (currentPlayer == player1) ? player2 : player1;
        repaint();
    }

    private boolean isWhiteOrBlackCell(int x, int y) {
        return board[x][y] == WHITE_PIECE || board[x][y] == BLACK_PIECE;
    }

    /**
     * Checks if the specified coordinates are valid on the board.
     *
     * @param x the x-coordinate
     * @param y the y-coordinate
     * @return true if the coordinates are valid, false otherwise
     */
    private boolean isValid(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }

    /**
     * Checks if the game is over.
     *
     * @return true if the game is over, false otherwise
     */
    public boolean isGameOver() {
        return movesLeft <= 0 || player1.getTilesLeft(board) == 0 || player2.getTilesLeft(board) == 0;
    }

    /**
     * Returns the winner of the game.
     *
     * @return the winner of the game
     */
    public String getWinner() {
        if (player1.getTilesLeft(board) > player2.getTilesLeft(board)) return "White wins!";
        if (player2.getTilesLeft(board) > player1.getTilesLeft(board)) return "Black wins!";
        return "Draw!";
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                g.setColor(board[i][j] == 1 ? Color.WHITE : (board[i][j] == -1 ? Color.BLACK : Color.GRAY));
                g.fillRect(j * 50, i * 50, 50, 50);
                g.setColor(Color.BLACK);
                g.drawRect(j * 50, i * 50, 50, 50);
            }
        }
        if (selectedX != -1 && selectedY != -1) {
            g.setColor(Color.RED);
            g.drawRect(selectedY * 50, selectedX * 50, 50, 50);
        }

        g.setColor(Color.BLACK);
        g.drawString("Current Player: " + currentPlayer.getColor(), 10, n * 50 + 20);
        g.drawString("White Tiles Left: " + player1.getTilesLeft(board) + ", Black Tiles Left: " + player2.getTilesLeft(board), 10, n * 50 + 40);
    }
}

/**
 * Represents the main frame of the game.
 */
class MainFrame extends JFrame {
    private GameBoard gameBoard;
    private int n;

    /**
     * Constructs a MainFrame with the specified board size.
     *
     * @param n the size of the board
     */
    public MainFrame(int n) {
        this.n = n;
        this.gameBoard = new GameBoard(n);
        setTitle("Kitolás Játék");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        add(gameBoard, BorderLayout.CENTER);
        add(createControlPanel(), BorderLayout.SOUTH);

        adjustFrameSize();
    }

    /**
     * Creates the control panel with direction buttons.
     *
     * @return the control panel
     */
    private JPanel createControlPanel() {
        JPanel panel = new JPanel();
        JButton upButton = new JButton("Up");
        JButton downButton = new JButton("Down");
        JButton leftButton = new JButton("Left");
        JButton rightButton = new JButton("Right");

        Dimension buttonSize = new Dimension(60, 30);
        upButton.setPreferredSize(buttonSize);
        downButton.setPreferredSize(buttonSize);
        leftButton.setPreferredSize(buttonSize);
        rightButton.setPreferredSize(buttonSize);

        upButton.addActionListener(e -> handleMove("UP"));
        downButton.addActionListener(e -> handleMove("DOWN"));
        leftButton.addActionListener(e -> handleMove("LEFT"));
        rightButton.addActionListener(e -> handleMove("RIGHT"));

        panel.add(upButton);
        panel.add(downButton);
        panel.add(leftButton);
        panel.add(rightButton);
        return panel;
    }

    /**
     * Handles the move action in the specified direction.
     *
     * @param direction the direction to move
     */
    private void handleMove(String direction) {
        gameBoard.move(direction);
        gameBoard.repaint();

        if (gameBoard.isGameOver()) {
            JOptionPane.showMessageDialog(this, gameBoard.getWinner());
            startNewGame();
        }
    }

    /**
     * Starts a new game.
     */
    private void startNewGame() {
        gameBoard = new GameBoard(n);
        add(gameBoard, BorderLayout.CENTER);
        revalidate();
        repaint();
        adjustFrameSize();
    }


    /**
     * Adjusts the frame size based on the board size.
     */
    private void adjustFrameSize() {
        setPreferredSize(new Dimension(n * 50 + 100, n * 50 + 100));
        pack();
    }
}

/**
 * The main class to start the game.
 */
public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            int n = Integer.parseInt(JOptionPane.showInputDialog("Enter board size (3, 4, or 6):"));
            new MainFrame(n).setVisible(true);
        });
    }
}
