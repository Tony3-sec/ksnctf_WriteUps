<?php

$salt = 'FLAG_????????????????'; //secret, length is 21

$shipname = array(
    'Nagato', //0
    'Mutsu', //1
    'Kongo', //2
    'Hiei', //3
    'Haruna', //4
    'Kirishima', //5
    'Fuso', //6
    'Yamashiro', //7
    'Ise', //8
    'Hyuga', //9
    "Yamato [Congratulations! The flag is $salt. ??????????????????????????????????????.]", //10
);

//  Check signature and read
if (isset($_COOKIE['ship']) and
    isset($_COOKIE['signature']) and
    hash('sha512', $salt.$_COOKIE['ship']) === $_COOKIE['signature'])
    $ship = explode(',', $_COOKIE['ship']); //$ship is an array for ship number
else
    $ship = array();

if (isset($_POST['submit']))
{
    //  Gacha
    if ($_POST['submit'] === 'Gacha')
    {
        //  Yamato is ultra rare
        // append to array
        $ship[] = mt_rand(0, count($shipname)-2); //11-2 = 9 so you will never get Yamato

        $s = implode(',', $ship);
        $sign = hash('sha512', $salt.$s);

        setcookie('ship', $s);
        setcookie('signature', $sign);
    }

    //  Clear
    if ($_POST['submit'] === 'Clear')
    {
        setcookie('ship', '', 0);
        setcookie('signature', '', 0);
    }

    header("Location: {$_SERVER['REQUEST_URI']}");
    exit();
}

?>
<!DOCTYPE html>
<html>
  <head>
    <title>KanGacha</title>
  </head>
  <body>
    <h1>KanGacha</h1>
    <form method="POST">
      <input type="submit" name="submit" value="Gacha">
      <input type="submit" name="submit" value="Clear">
    </form>
    <ul>
<?php
for ($i=0; $i<count($ship); $i++)
    echo "<li>{$shipname[$ship[$i]]}</li>\n"; //read and print ship name from Cookie
?>
    </ol>
  </body>
</html>
