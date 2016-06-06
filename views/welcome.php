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
<!-- PHP bit to send email and capture data -->
<?php
// Send
$temp1 = $_POST["name"];
$temp2 = $_POST["email"];
exec("python ../mail/archyEmail.py $temp1 $temp2");
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