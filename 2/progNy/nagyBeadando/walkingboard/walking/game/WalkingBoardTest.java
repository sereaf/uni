package walking.game;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.ValueSource;
import walking.game.util.Direction;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class WalkingBoardTest {

    @ParameterizedTest
    @ValueSource(ints = {1, 2, 3, 4, 5})
    void testSimpleInit(int size) {
        WalkingBoard board = new WalkingBoard(size);
        assertEquals(size, board.getTiles().length);
        assertEquals(size, board.getTiles()[0].length);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                assertEquals(WalkingBoard.BASE_TILE_SCORE, board.getTile(i, j));
            }
        }
    }

    @ParameterizedTest
    @CsvSource(textBlock = """
               1, 1, 2
               2, 2, 1
            """)
    void testCustomInit(int x, int y, int expected) {
        int[][] tiles = new int[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                tiles[i][j] = expected;
            }
        }
        WalkingBoard board = new WalkingBoard(tiles);
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                assertEquals(WalkingBoard.BASE_TILE_SCORE, board.getTile(i, j));
            }
        }
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                tiles[i][j] = 5;
            }
        }
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                assertEquals(WalkingBoard.BASE_TILE_SCORE, board.getTile(i, j));
            }
        }

        board.getTiles()[x][y] = 10;
        assertEquals(WalkingBoard.BASE_TILE_SCORE, board.getTile(x, y));
    }


    @Test
    public void testMoves() {
        WalkingBoard board = new WalkingBoard(5);
        board.moveAndSet(Direction.RIGHT, 10);
        assertEquals(10, board.getTile(1, 0));
        board.moveAndSet(Direction.DOWN, 20);
        assertEquals(20, board.getTile(1, 1));
        board.moveAndSet(Direction.LEFT, 30);
        assertEquals(30, board.getTile(0, 1));
        board.moveAndSet(Direction.UP, 40);
        assertEquals(40, board.getTile(0, 0));
    }
}
