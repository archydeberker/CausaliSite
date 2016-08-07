<!DOCTYPE html>
<html lang="en">

<head>
  <?php $thisPage="index"; ?>
  <?php include_once('assetHeader.php') ?>
</head>

  <body>
  <!-- PHP bit to store data and send email -->
  <?php
  $name = $_POST["inputName"];
  $email = $_POST["inputEmail"];
  $instructionTime  = $_POST["instructionTime"];
  $responseTime = $_POST["responseTime"];
  // $timezone = $_POST["userTimeZone"];
  $timezone = "fooblebar timezone";

  # quoting arguments is NOT recommended (https://blogs.msdn.microsoft.com/twistylittlepassagesallalike/2011/04/23/everyone-quotes-command-line-arguments-the-wrong-way/)
  exec("python database/signup_meditation.py '$name' '$email' '$instructionTime' '$responseTime' '$timezone'");
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
      <p class="lead">Welcome aboard, <?php echo $name; ?>!</p>
      <p class="center">Your email address is: <?php echo $email; ?></p>
      <p class="center">We have sent you a confirmation email. Tomorrow is your first day on the experiment, we hope you enjoy!</p>

      <p> If you're looking to get started with guided meditations, check out <a href="https://www.headspace.com"> Headspace </a> for free 10-minute sessions</p>
    </div>


    <footer class="footer">
      <p>&copy; 2016 Causali, Inc.</p>
    </footer>

  </div> <!-- /container -->

  <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  <script src="frontend_play/assets/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
