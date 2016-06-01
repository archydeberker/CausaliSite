<html>
<body>

Welcome <?php echo $_POST["name"]; ?><br>
Your email address is: <?php echo $_POST["email"]; ?>

<?php
// The message
$message = "Line 1\r\nLine 2\r\nLine 3";

// In case any of our lines are larger than 70 characters, we should use wordwrap()
$message = wordwrap($message, 70, "\r\n");

// Send
$temp1 = $_POST["name"];
$temp2 = $_POST["email"];
exec("python archyEmail.py $temp1 $temp2");
?>

</body>
</html>