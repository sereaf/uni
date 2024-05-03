package walking.game;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;


public class WalkingBoardWithPlayersTest {
    @Test
    void walk1() {
        int[][] board = new int[][]{
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        WalkingBoardWithPlayers game = new WalkingBoardWithPlayers(board, 3);
        int[] scores = game.walk(2, 3, 1, 1);
        System.out.println(scores);
        assertArrayEquals(new int[]{3, 0, 0}, scores);
    }

    @Test
    void walk2() {
        WalkingBoardWithPlayers game = new WalkingBoardWithPlayers(5, 4);
        int[] scores = game.walk(1, 1, 1, 1);
        assertArrayEquals(new int[]{0, 1, 2, 3}, scores);
    }
}
