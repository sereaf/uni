package sikidom;

/**
 * A kört reprezentáló osztály.
 */
public class Kor extends Sikidom {
    /**
     * A kör sugara.
     */
    double r;

    /**
     * Új kör létrehozása a megadott koordinátákkal és sugárral.
     *
     * @param x a kör x-koordinátája
     * @param y a kör y-koordinátája
     * @param r a kör sugara
     */
    public Kor(double x, double y, double r)  {
        super(x, y);
        this.r = r;
    }

    /**
     * A kör területének kiszámítása.
     *
     * @return a kör területe
     */
    @Override
    public double befoglaloTerulet() {
        return 4 * r * r;
    }

    /**
     * A kör szöveges reprezentációjának visszaadása.
     *
     * @return a kör szöveges reprezentációja
     */
    @Override
    public String toString() {
        return "Kor: " + super.toString();
    }
}