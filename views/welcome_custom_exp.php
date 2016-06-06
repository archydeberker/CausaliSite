<!DOCTYPE html>
<html>
<title>ZAP science</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="stylesheet.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
</style>

<body>
<?php
// Send
$temp1 = $_POST["name"];
$temp2 = $_POST["email"];
$temp3 = $_POST["timezone"];
$temp4 = $_POST["exp_name"];
$temp5 = $_POST["condition1"];
$temp6 = $_POST["nTrials1"];
$temp7 = $_POST["condition2"];
$temp8 = $_POST["nTrials2"];
$temp9 = $_POST["dependent"];
$temp10 = $_POST["ITI"];
$temp11 = $_POST["instruction_time"];
$temp12 = $_POST["response_time"];

// replace default argument by NULL, which should be read by python as None.
$temp1 = !empty($temp1) ? "'$temp1" : "NULL";
$temp2 = !empty($temp2) ? "'$temp2'" : "NULL";
$temp3 = !empty($temp3) ? "'$temp3'" : "NULL";
$temp4 = !empty($temp4) ? "'$temp4'" : "NULL";
$temp5 = !empty($temp5) ? "'$temp5'" : "NULL";
$temp6 = !empty($temp6) ? "'$temp6'" : "NULL";
$temp7 = !empty($temp7) ? "'$temp7'" : "NULL";
$temp8 = !empty($temp8) ? "'$temp8'" : "NULL";
$temp9 = !empty($temp9) ? "'$temp9'" : "NULL";
$temp10 = !empty($temp10) ? "'$temp10'" : "NULL";
$temp11 = !empty($temp11) ? "'$temp11'" : "NULL";
$temp12 = !empty($temp12) ? "'$temp12'" : "NULL";

// $command = "from database.db_utils import register_user_experiment; register_user_experiment($temp1, $temp2, $temp3, $temp4, $temp5, $temp6, $temp7, $temp8, $temp9, $temp10, $temp11, $temp12)";
// // echo "<script>console.log(""$command"");</script>";
// // exec("python ../mail/archyEmail.py $temp1 $temp2");
// exec('python -c "' . escapeshellarg($command) . '"');

// first argument is the function inside php_to_python, next are all the arguments
$command = "python php_to_python.py register_user_experiment $temp1, $temp2, $temp3, $temp4, $temp5, $temp6, $temp7, $temp8, $temp9, $temp10, $temp11, $temp12";
error_log(escapeshellarg($command));
exec(escapeshellarg($command)) ;
?>

<!-- Page content -->
<div class="container"> <!-- one big div to contain all content -->
	<!-- Header -->
	<div class="header">
		<?php include 'header.php'; ?>
	</div>




	<!-- Content -->
  	<div class="page-content center padding-64">
	    <h2 class="wide">ZAP science</h2>
	    <p class="center">Welcome <?php echo $_POST["name"]; ?></p>
		<p class="center">Your email address is: <?php echo $_POST["email"]; ?></p>
		<p class="center">We have sent you a confirmation email. Tomorrow you will start the experiment.</p>
  	</div>








  	<!-- Footer -->
  	<div class="footer">
		<?php include 'footer.php'; ?>
	</div>
</div>  
<!-- End Page Content -->
</div>

</body>
</html>