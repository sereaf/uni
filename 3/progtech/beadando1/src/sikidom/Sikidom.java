package sikidom;

/**
 * Absztrakt osztály, mely a síkidomok közös tulajdonságait és metódusait
 * tartalmazza.
 */
public abstract class Sikidom {
    /**
     * A síkidom x-koordinátája.
     */
    protected double x;

    /**
     * A síkidom y-koordinátája.
     */
    protected double y;

    /**
     * Új síkidom létrehozása a megadott koordinátákkal.
     *
     * @param x a síkidom x-koordinátája
     * @param y a síkidom y-koordinátája
     */
    public Sikidom(double x, double y) {
        this.x = x;
        this.y = y;
    }

    /**
     * A síkidom területének kiszámítása.
     *
     * @return a síkidom területe
     */
    public abstract double befoglaloTerulet();

    /**
     * Visszaadja a síkidom adatait szöveges formában.
     *
     * @return a síkidom szöveges reprezentációja
     */
    @Override
    public String toString() {
        return "x=" + x + ", y=" + y + ", terulet=" + befoglaloTerulet();
    }
}