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
	<!-- <div class="page-content center padding-64">
	    <h2 class="w3-wide">ZAP science</h2>
	    <p class="w3-justify">Enter your details here to participate in the experiment.</p>
	    <p class="w3-justify">Specify the details of your experiment. We have already filled in default values, enter a value to change them.</p>
	    <form class="w3-form" action="views/welcome_custom_exp.php" method="post">
			Name<br><input type="text" size="70" name="name" placeholder="Your Name"><br><br>
			Email<br><input type="text" size="70" name="email" placeholder="Your email"><br><br>
			Offset from British winter time, +1 Amsterdam, -5 for New York.<br><input type="text" size="70" name="timezone" placeholder="0"><br><br>
			name of experiment (My Experiment)<br><input type="text" size="70" name="exp_name" placeholder="My Experiment"><br><br>
			1st condition, e.g. 'meditate'<br><input type="text" size="70" name="condition1" placeholder="condition1"><br><br>
			number of trials in 1st condition<br><input type="text" size="70" name="nTrials1" placeholder="10"><br><br>
			2nd condition, e.g. 'do not meditate'<br><input type="text" size="70" name="condition2" placeholder="condition2"><br><br>
			number of trials in 2nd condition<br><input type="text" size="70" name="nTrials2" placeholder="10"><br><br>
			outcome variable, e.g. happiness<br><input type="text" size="70" name="dependent" placeholder="happiness"><br><br>
			time between trials in hours<br><input type="text" size="70" name="ITI" placeholder="24"><br><br>
			hour of day to send condition, e.g. 7 for 7:00<br><input type="text" size="70" name="instruction_time" placeholder="7"><br><br>
			hour of day to ask for response, e.g. 15 for 15:00<br><input type="text" size="70" name="response_time" placeholder="15"><br><br>
			<br>
			<input type="submit">
		</form>
	</div> -->
	<!-- Content -->
	<div class="page-content center padding-64">
	    <h2 class="w3-wide">ZAP science</h2>
	    <p class="w3-justify">Enter your details here to participate in the experiment.</p>
	    <p class="w3-justify">Specify the details of your experiment. We have already filled in default values, enter a value to change them.</p>
	    <form class="w3-form" action="cg-bin/custom_exp_handler.py" method="post">
			Name<br><input type="text" size="70" name="name" placeholder="Your Name"><br><br>
			Email<br><input type="text" size="70" name="email" placeholder="Your email"><br><br>
			Offset from British winter time, +1 Amsterdam, -5 for New York.<br><input type="text" size="70" name="timezone" placeholder="0"><br><br>
			name of experiment (My Experiment)<br><input type="text" size="70" name="exp_name" placeholder="My Experiment"><br><br>
			1st condition, e.g. 'meditate'<br><input type="text" size="70" name="condition1" placeholder="condition1"><br><br>
			number of trials in 1st condition<br><input type="text" size="70" name="nTrials1" placeholder="10"><br><br>
			2nd condition, e.g. 'do not meditate'<br><input type="text" size="70" name="condition2" placeholder="condition2"><br><br>
			number of trials in 2nd condition<br><input type="text" size="70" name="nTrials2" placeholder="10"><br><br>
			outcome variable, e.g. happiness<br><input type="text" size="70" name="dependent" placeholder="happiness"><br><br>
			time between trials in hours<br><input type="text" size="70" name="ITI" placeholder="24"><br><br>
			hour of day to send condition, e.g. 7 for 7:00<br><input type="text" size="70" name="instruction_time" placeholder="7"><br><br>
			hour of day to ask for response, e.g. 15 for 15:00<br><input type="text" size="70" name="response_time" placeholder="15"><br><br>
			<br>
			<input type="submit" value='Submit' />
		</form>
	</div>

	<!-- Footer -->
  	<div class="footer">
		<?php include 'views/footer.php'; ?>
	</div>
</div>

</body>
</html>