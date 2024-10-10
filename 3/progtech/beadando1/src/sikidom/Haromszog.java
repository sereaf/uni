package sikidom;

/**
 * A háromszögeket reprezentáló osztály.
 */
public class Haromszog extends Sikidom {
    /**
     * A háromszög oldalának hossza.
     */
    double oldal;

    /**
     * Új háromszög létrehozása a megadott koordinátákkal és oldalmérettel.
     *
     * @param x a háromszög x-koordinátája
     * @param y a háromszög y-koordinátája
     * @param oldal a háromszög oldalának hossza
     */
    public Haromszog(double x, double y, double oldal) {
        super(x, y);
        this.oldal = oldal;
    }

    /**
     * A háromszög területének kiszámítása.
     *
     * @return a háromszög területe
     */
    @Override
    public double befoglaloTerulet() {
        double magassag = (Math.sqrt(3) / 2) * oldal;
        return oldal * magassag;
    }

    /**
     * A háromszög szöveges reprezentációjának visszaadása.
     *
     * @return a háromszög szöveges reprezentációja
     */
    @Override
    public String toString() {
        return "Haromszog: " + super.toString();
    }
}