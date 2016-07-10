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

<!-- PHP stuff to send rating -->
<?php
// Send
$temp1 = $_GET["trialhash"];
$temp2 = $_GET["rating"];
exec("python database/store_response.py $temp1 $temp2");
?>

<div class="container">
    <div class="header clearfix">
      <?php include_once('header.php') ?>
      <p>
        <h3 class="text-muted" ">Causali</h3> 
      </p>
    </div>

    <div class="jumbotron">
      <h1> </h1>
      <p class="lead">Thanks for submitting your response!</p>
    </div>


    <footer class="footer">
      <p>&copy; 2016 Causali, Inc.</p>
    </footer>

  </div> <!-- /container -->

</body>
</html>