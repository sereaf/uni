package walking.game.player;

import walking.game.util.Direction;

public class Player {
    private int score;
    protected Direction direction;

    public Player() {
        this.score = 0;
        this.direction = Direction.UP;
    }

    public int getScore() {
        return this.score;
    }

    public Direction getDirection() {
        return this.direction;
    }

    public void addToScore(int score) {
        this.score += score;
    }

    public void turn() {
        switch (this.direction) {
            case UP:
                this.direction = Direction.RIGHT;
                break;
            case RIGHT:
                this.direction = Direction.DOWN;
                break;
            case DOWN:
                this.direction = Direction.LEFT;
                break;
            case LEFT:
                this.direction = Direction.UP;
                break;
            default:
                break;
        }
    }
}