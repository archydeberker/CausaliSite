<!DOCTYPE html>
<html lang="en">

<head>
  <?php $thisPage="index"; ?>
  <?php include_once('assetHeader.php') ?>
</head>

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