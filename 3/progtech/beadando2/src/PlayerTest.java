import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class PlayerTest {

    @Test
    void testGetTilesLeft() {
        int[][] board = {
            {1, -1, 0},
            {1, 1, -1},
            {0, -1, 1}
        };
        Player player = new Player("White");
        assertEquals(4, player.getTilesLeft(board), "White player should have 3 tiles on the board.");

        player = new Player("Black");
        assertEquals(3, player.getTilesLeft(board), "Black player should have 3 tiles on the board.");
    }
}