package walking.game;

import walking.game.player.MadlyRotatingBuccaneer;
import walking.game.player.Player;

public class WalkingBoardWithPlayers extends WalkingBoard {
    private Player[] players;
    private int round;
    public static final int SCORE_EACH_STEP = 13;

    public WalkingBoardWithPlayers(int[][] board, int playerCount) {
        super(board);
        if (playerCount < 2) {
            throw new IllegalArgumentException("Kettőnél kevesebb játékos");
        }
        initPlayers(playerCount);
    }

    public WalkingBoardWithPlayers(int size, int playerCount) {
        super(size);
        if (playerCount < 2) {
            throw new IllegalArgumentException("Kettőnél kevesebb játékos");
        }
        initPlayers(playerCount);
    }

    private void initPlayers(int playerCount) {
        players = new Player[playerCount];
        for (int i = 0; i < playerCount; i++) {
            players[i] = new Player();
        }
    }

    public int[] walk(int... stepCounts) {
        for (int s = 0; s < stepCounts.length; s++) {
                int i = s % players.length;
                if (players[i] instanceof MadlyRotatingBuccaneer) {
                    for (int j = 0; j < s/players.length; j++) {
                        players[i].turn();
                    }
                } else {
                    players[i].turn();
                }
                for (int j = 0; j < stepCounts[s]; j++) {
                    moveAndSet(players[i].getDirection(), Math.min(s, SCORE_EACH_STEP));
                    int [] pos = getPosition();
                    players[i].addToScore(getTile(pos[0], pos[1]));
                }
            
        }
        int[] points = new int[players.length];
        for (int i = 0; i < players.length; i++) {
            points[i] = players[i].getScore();
        }
        return  points;
    }
}
