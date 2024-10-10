package sikidom;

/**
 * A négyzetet reprezentáló osztály.
 */
public class Negyzet extends Sikidom {
    /**
     * A négyzet oldalának hossza.
     */
    double oldal;

    /**
     * Új négyzet létrehozása a megadott koordinátákkal és oldalmérettel.
     *
     * @param x a négyzet x-koordinátája
     * @param y a négyzet y-koordinátája
     * @param oldal a négyzet oldalának hossza
     */
    public Negyzet(double x, double y, double oldal)  {
        super(x, y);
        this.oldal = oldal;
    }

    /**
     * A négyzet területének kiszámítása.
     *
     * @return a négyzet területe
     */
    @Override
    public double befoglaloTerulet() {
        return oldal * oldal;
    }

    /**
     * A négyzet szöveges reprezentációjának visszaadása.
     *
     * @return a négyzet szöveges reprezentációja
     */
    @Override
    public String toString() {
        return "Negyzet: " + super.toString();
    }
}