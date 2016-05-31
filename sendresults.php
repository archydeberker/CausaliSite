<html>
<body>

Your trial hash: <?php echo $_GET["trialhash"]; ?><br>
Your rating: <?php echo $_GET["rating"]; ?>


<?php
// Send
$temp1 = $_GET["trialhash"];
$temp2 = $_GET["rating"];
exec("python archyEmail.py $temp1 $temp2");
?>

</body>
</html>