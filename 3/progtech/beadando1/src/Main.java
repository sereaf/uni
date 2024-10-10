import java.util.ArrayList;
import java.io.IOException;

import sikidom.*;


public class Main {
    public static void main(String[] args) {
        Sikidomok s = new Sikidomok();
        s.read("./src/test1.txt");
        s.maxTerulet();
    }
}