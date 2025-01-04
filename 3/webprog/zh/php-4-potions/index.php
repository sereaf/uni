<?php
    include_once(__DIR__. '/data.php');
?>

<?php 
$legendaryCount = 0;
foreach ($potions as $p) {
    if ($p['rarity'] === 'legendary') {
        $legendaryCount += 1;
    }
}
?>

<?php 
$potionSum = 0;
foreach ($potions as $p) {
    $potionSum += $p['value'];
}
?>

<?php 
$maxValue = $potions[0];
foreach ($potions as $p) {
    if ($p['value'] > $maxValue['value'] && $p['rarity'] !== 'legendary') {
        $maxValue = $p;
    }
}
?>

<!DOCTYPE html>
<html lang="hu">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>4. feladat</title>
    <link rel="stylesheet" href="index.css" />
</head>

<body>
    <h1>4. Bájitalok</h1>
    <table>
        <thead>
            <tr>
                <th>Név</th>
                <th>Szín</th>
                <th>Ár</th>
            </tr>
        </thead>
        <tbody>
        <?php foreach ($potions as $potion): ?>
            <tr <?php if ($potion === $maxValue) {
                    echo "class='highlighted'";
                } ?>>
                <th style="color: <?php 
                if ($potion['rarity'] === 'common') {
                    echo "green";
                } elseif ($potion['rarity'] === 'rare') {
                    echo "blue";
                } elseif ($potion['rarity'] === 'epic') {
                    echo "purple";
                } elseif ($potion['rarity'] === 'legendary') {
                    echo "orange";
                }
                ?>;"><?php echo $potion['name']; ?></th>
                <th style="background-color: <?php echo $potion['color']; ?>;"></th>
                <th><?php echo $potion['value']; ?></th>    
            </tr>
        <?php endforeach; ?>          
        </tbody>
    </table>

    <b>A legendás bájitalok száma: <?php echo $legendaryCount; ?> db<br>
    <b>A bájitalok összértéke: <?php echo $potionSum; ?> arany
</body>
</html>

