<!DOCTYPE html>
<html lang="en">

<head>
  <?php $thisPage="index"; ?>
  <?php include_once('assetHeader.php') ?>
</head>

  <body>
  <!-- PHP bit to store data and send email -->
  <?php
  $email = $_GET["email"];
  $user  = $_GET["user_id"];
  $exp   = $_GET["exp_id"];

  # quoting arguments is NOT recommended (https://blogs.msdn.microsoft.com/twistylittlepassagesallalike/2011/04/23/everyone-quotes-command-line-arguments-the-wrong-way/)
  exec("python database/verify_and_initialise_exp.py '$email' '$user' '$exp'");
  ?>

  <div class="container">
    <div class="header clearfix">
      <?php include_once('header.php') ?>
    </div>

    <div class="jumbotron">
      <h1> </h1>
      <p class="center">Your email address has been verified. We'll start your experiment soon :)</p>

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
