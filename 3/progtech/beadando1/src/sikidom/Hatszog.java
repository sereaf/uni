package sikidom;

/**
 * A hatszögeket reprezentáló osztály.
 */
public class Hatszog extends Sikidom {
    /**
     * A hatszög oldalának hossza.
     */
    double oldal;

    /**
     * Új hatszög létrehozása a megadott koordinátákkal és oldalmérettel.
     *
     * @param x a hatszög x-koordinátája
     * @param y a hatszög y-koordinátája
     * @param oldal a hatszög oldalának hossza
     */
    public Hatszog(double x, double y, double oldal) {
        super(x, y);
        this.oldal = oldal;
    }

    /**
     * A hatszög területének kiszámítása.
     *
     * @return a hatszög területe
     */
    @Override
    public double befoglaloTerulet() {
        double magassag = Math.sqrt(3) * oldal;
        return oldal * magassag;
    }

    /**
     * A hatszög szöveges reprezentációjának visszaadása.
     *
     * @return a hatszög szöveges reprezentációja
     */
    @Override
    public String toString() {
        return "Hatszog: " + super.toString();
    }
}