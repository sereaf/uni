package sikidom;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Sikidomok {
    ArrayList<Sikidom> sikidomok = new ArrayList<>();

    public void read(String filePath) {
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            int _ = Integer.parseInt(reader.readLine());
            while ((line = reader.readLine()) != null) {
                String[] s = line.split(" ");
                switch (s[0]) {
                    case "K":
                        sikidomok.add(new Kor(Double.parseDouble(s[1]), Double.parseDouble(s[2]), Double.parseDouble(s[3])));
                        break;
                    case "N":
                        sikidomok.add(new Negyzet(Double.parseDouble(s[1]), Double.parseDouble(s[2]), Double.parseDouble(s[3])));
                        break;
                    case "HA":
                        sikidomok.add(new Hatszog(Double.parseDouble(s[1]), Double.parseDouble(s[2]), Double.parseDouble(s[3])));
                        break;
                    case "H":
                        sikidomok.add(new Haromszog(Double.parseDouble(s[1]), Double.parseDouble(s[2]), Double.parseDouble(s[3])));
                        break;
                    default:
                        break;
                }
            }
            System.out.println("Beolvasott sikidomok: " + sikidomok);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void maxTerulet() {
         int maxIndex = 0;
            for (Sikidom sikidom : sikidomok) {
                double t = sikidom.befoglaloTerulet();
                if (t > sikidomok.get(maxIndex).befoglaloTerulet()) {
                    maxIndex = sikidomok.indexOf(sikidom);
                }
            }

            System.out.println("Legnagyobb teruletu: " + sikidomok.get(maxIndex).toString());
    }
}
