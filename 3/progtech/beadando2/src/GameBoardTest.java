/*import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

class GameBoardTest {

    @Test
    void testMoveLeft() {
        GameBoard board = new GameBoard(3);
        int[][] initialBoard = {
            {1, 0, 0},
            {-1, -1, 0},
            {1, 1, 1}
        };
        board.setBoard(initialBoard);
        board.selectTile(2, 2);
        board.move("LEFT");

        int[][] expectedBoard = {
            {1, 0, 0},
            {-1, -1, 0},
            {1, 1, 0}
        };
        assertArrayEquals(expectedBoard, board.getBoard(), "Moving left should shift the selected tile and all tiles to its left.");
    }

    @Test
    void testGameOverCondition() {
        GameBoard board = new GameBoard(3);
        int[][] boardState = {
            {1, -1, 0},
            {0, 0, 0},
            {0, 0, 0}
        };
        board.setBoard(boardState);
        assertTrue(board.isGameOver(), "The game should be over if one player has no tiles left.");
    }
}
*/