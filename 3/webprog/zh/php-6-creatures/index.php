<?php 
        $creatures = json_decode(file_get_contents('creatures.json'), true);
?>

<?php 
    if (count($_POST) > 0) {
        $volt = false; 
        for ($i = 0; $i < count($creatures); $i++) {
            if ($creatures[$i]['creature'] === $_POST['creature']) {
                $creatures[$i]['count'] += $creatures[$i]['count'] + $_POST['count'];
                $volt = true;
            }
        }
        /* foreach ($creatures as $c) {
            if ($c['creature'] === $_POST['creature']) {
                $c['count'] += $c['count'] + $_POST['count'];
                $volt = true;
            }
        } */

        if (!$volt) {
            $data = [
                "creature" => $_POST['creature'],
                "count"=> intval($_POST['count']),
            ];
            $creatures = array_merge($creatures, $data);
        }
    }
?>

<!DOCTYPE html>
<html lang="hu">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>6. feladat</title>
    <link rel="stylesheet" href="index.css" />
</head>

<body>
    <h1>6. Lények</h1>
    
    <h2>Új észlelés felvitele</h2>
    <form action="add.php" method="POST">
        Lény neve: <input type="text" name="creature"><br>
        Észlelések száma: <input type="number" name="count"><br>
        <button>Mentés</button>
    </form>

    <h2>Korábbi észlelések</h2>
    
    <?php foreach ($creatures as $c): ?>
        <li><?php echo $c["creature"]; ?>: <?php echo $c["count"]; ?> <button>Törlés</button> <button>Elrejtés</button></li>
    <?php endforeach; ?>
</body>
</html>