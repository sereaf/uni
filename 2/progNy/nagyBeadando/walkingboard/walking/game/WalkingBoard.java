package walking.game;

import java.util.Arrays;

import walking.game.util.Direction;

public class WalkingBoard {
    public static final int BASE_TILE_SCORE = 3;
    private int[][] tiles;
    private int x;
    private int y;

    public WalkingBoard(int size) {
        this.tiles = new int[size][size];
        for (int i = 0; i < this.tiles.length; i++) {
            for (int j = 0; j < this.tiles[i].length; j++) {
                this.tiles[i][j] = BASE_TILE_SCORE;
            }
        }
        this.x = 0;
        this.y = 0;
    }

    public WalkingBoard(int[][] tiles) {
        this.tiles = new int[tiles.length][tiles.length];
        for (int i = 0; i < tiles.length; i++) {
            this.tiles[i] = Arrays.copyOf(tiles[i], tiles[i].length);
        }
        for (int i = 0; i < this.tiles.length; i++) {
            for (int j = 0; j < this.tiles[i].length; j++) {
                if (this.tiles[i][j] <= BASE_TILE_SCORE) {
                    this.tiles[i][j] = BASE_TILE_SCORE;
                }
            }
        }
        this.x = 0;
        this.y = 0;
    }

    public int[][] getTiles() {
        int[][] outTiles = new int[this.tiles.length][this.tiles.length];
        for (int i = 0; i < this.tiles.length; i++) {
            outTiles[i] = Arrays.copyOf(this.tiles[i], this.tiles[i].length);
        }
        return outTiles;
    }

    public int[] getPosition() {
        return new int[] { this.x, this.y };
    }

    public boolean isValidPosition(int x, int y) {
        return x >= 0 && x < tiles.length && y >= 0 && y < tiles[0].length;
    }

    public int getTile(int x, int y) {
        if (!isValidPosition(x, y)) {
            throw new IllegalArgumentException();
        }
        return this.tiles[x][y];
    }

    public static int getXStep(Direction direction) {
        switch (direction) {
            case LEFT:
                return -1;
            case RIGHT:
                return 1;
            default:
                return 0;
        }
    }

    public static int getYStep(Direction direction) {
        switch (direction) {
            case UP:
                return -1;
            case DOWN:
                return 1;
            default:
                return 0;
        }
    }

    public int moveAndSet(Direction direction, int value) {
        final int newX = this.x + getXStep(direction);
        final int newY = this.y + getYStep(direction);
        if (isValidPosition(newX, newY)) {
            this.x = newX;
            this.y = newY;
            final int oldValue = getTile(newX, newY);
            tiles[newX][newY] = value;
            return oldValue;
        }
        return 0;
    }
}
