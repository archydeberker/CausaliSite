<html>
<body>

Your trial hash: <?php echo $_GET["trialhash"]; ?><br>
Your rating: <?php echo $_GET["rating"]; ?>


<?php
// Send
$temp1 = $_GET["trialhash"];
$temp2 = $_GET["rating"];
// exec("python depositResults.py $temp1 $temp2");
// this way we use the function in db_utils. HAS NOT BEEN TESTED
exec('python -c "from database.db_utils import store_response; store_response($temp1, $temp2)"');
?>

</body>
</html>