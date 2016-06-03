<!DOCTYPE html>
<html>
<title>ZAP science</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
.w3-navbar, label {font-family: "Montserrat", sans-serif}
.mySlides {display:none;}
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
<div class="w3-content" style="max-width:1800px;margin-top:46px">
  <div class="w3-container w3-content w3-center w3-padding-64" style="max-width:800px">
    <h2 class="w3-wide">ZAP science</h2>
    <p class="w3-centered">Welcome <?php echo $_POST["name"]; ?></p>
	<p class="w3-centered">Your email address is: <?php echo $_POST["email"]; ?></p>
	<p class="w3-centered">We have sent you a confirmation email. Tomorrow you will start the experiment.</p>
    </div>
  </div>  

<!-- End Page Content -->
</div>

</body>
</html>