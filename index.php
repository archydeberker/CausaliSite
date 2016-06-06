<!DOCTYPE html>
<html>
<title>ZAP science</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="views/stylesheet.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
</style>

<body>
<!-- Page content -->
<div class="container"> <!-- one big div to contain all content -->
	<!-- Header -->
	<div class="header">
		<?php include 'views/header.php'; ?>
	</div>
	<!-- Content -->
  	<div class="page-content center padding-64">
	    <h2 class="wide">ZAP science</h2>
	    <p class="center">Enter your details here to participate in the experiment.</p>
	    <form class="form" action="views/welcome.php" method="post">
			<input type="text" name="name" placeholder="name"><br>
			<input type="text" name="email" placeholder="email"><br><br>
			<input type="submit">
		</form>
  	</div>
  	<!-- Footer -->
  	<div class="footer">
		<?php include 'views/footer.php'; ?>
	</div>
</div>  
<!-- End Page Content -->
</div>

</body>
</html>