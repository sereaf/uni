package walking.game.player;

import walking.game.util.Direction;

public class MadlyRotatingBuccaneer extends Player {
    private int turnCount;
    
    MadlyRotatingBuccaneer() {
        super();
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
