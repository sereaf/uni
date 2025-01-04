<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>5. feladat</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>5. Meghívó</h1>
    <form action="index.php" method="GET" novalidate>
        <label for="full_name">Gyermek neve:</label>
        <input type="text" name="full_name">
        <span class="error-message">
        <?php 
            if (count($_GET) > 0) {
                if ($_GET["full_name"] === "") {
                    echo "Kötelező!!!";
                } elseif (strlen($_GET["full_name"]) < 6) {
                    echo "A név hossza minimum 6 karakter!!!";
                } elseif (!str_contains($_GET["full_name"], " ")) {
                    echo "A név legalább egy szóközt kell tartalmazzon!!!";
                }
            }
        ?>
        </span>
       
        <label for="wizards">Varázsló felmenők száma:</label>
        <input type="text" name="wizards">
        <span class="error-message">
        <?php 
            if (count($_GET) > 0) {
                if ($_GET["wizards"] === "") {
                    echo "Kotelezo!!!";
                } elseif (!ctype_digit($_GET["wizards"])) {
                    echo "A varázsló felmenők száma egész szám!!!";
                } elseif ($_GET["wizards"] < 1 || $_GET["wizards"] > 256) {
                    echo "A varázsló felmenők száma legalább 1, legfeljebb 256 lehet!!!";
                }
            } 
        ?>
        </span>
       
        <label for="pet">Kísérő állat:</label>
        <select name="pet">
            <option value="owl">Bagoly</option>
            <option value="cat">Macska</option>
            <option value="toad">Varangy</option>
            <option value="rat">>Patkány</option>
        </select>
        <span class="error-message">
        <?php 
            if (count($_GET) > 0) {
                if ($_GET["pet"] === "") {
                    echo "Kotelezo!!!";
                } elseif (!$_GET["pet"] === "owl" || !$_GET["pet"] === "cat" || !$_GET["pet"] === "toad" || !$_GET["pet"] === "rat") {
                    echo "Az állat csak a megadott listabeli értéket veheti fel (owl, cat, toad, rat)!!!";
                }
            }
        ?>
        </span>

        <input type="checkbox" name="agree">
        <label for="agree" style="display: inline-block">Hozzájárulok az adatkezeléshez</label>
        <span class="error-message">
        <?php 
            if (count($_GET) > 0) {
                if (!isset($_GET["agree"])) {
                    echo "Kotelezo!!!";
                }
            }
        ?>
        </span>

        <input type="submit" value="Hozzáadás">
    </form>
    
    <?php if (true): ?>
    <div id="success">
        <h2>Köszönjük a jelentkezést!</h2>
        Amennyiben a gyermek felvétele mellett döntünk, hamarosan bagollyal értesíteni fogjuk.
    </div>
    <?php endif; ?>

    <div class="help">
        <h2>Segítség a teszteléshez</h2>
        <ul>
            <li><a href="index.php?">Nincs elküldött adat</a></li>
            <li><a href="index.php?full_name=L&wizards=4&pet=owl&agree=on">Túl rövid név</a></li>
            <li><a href="index.php?full_name=LunaLovegood&wizards=4&pet=owl&agree=on">Nincs szóköz a névben</a></li>
            <li><a href="index.php?full_name=Luna%20Lovegood&wizards=four&pet=owl&agree=on">Felmenők száma nem szám</a></li>
            <li><a href="index.php?full_name=Luna%20Lovegood&wizards=3.14&pet=owl&agree=on">Felmenők száma nem egész</a></li>
            <li><a href="index.php?full_name=Luna%20Lovegood&wizards=0&pet=owl&agree=on">Felmenők száma túl kevés</a></li>
            <li><a href="index.php?full_name=Luna%20Lovegood&wizards=300&pet=owl&agree=on">Felmenők száma túl sok</a></li>
            <li><a href="index.php?full_name=Luna%20Lovegood&wizards=4&agree=on">Hiányzó állat</a></li>
            <li><a href="index.php?full_name=Luna%20Lovegood&wizards=4&pet=lizard&agree=on">Érvénytelen állat</a></li>
            <li><a href="index.php?full_name=Luna%20Lovegood&wizards=4&pet=owl">Adatkezelési hozzájárulás hiányzik</a></li>
            <li><a href="index.php?full_name=Luna%20Lovegood&wizards=4&pet=owl&agree=on">Minden rendben</a></li>
        </ul>
    </div>
</body>
</html>