<!DOCTYPE html>
<html lang="en">

<head>
  <?php $thisPage="index"; ?>
  <?php include_once('assetHeader.php') ?>
</head>

  <body>
  <!-- PHP bit to store data and send email -->
  <?php
  $type = $_POST["emailType"];
  $email = $_POST["inputEmail"];
  // default name
  //$name = "Prof";

  // sanitise input
  $email_clean = filter_var($email, FILTER_SANITIZE_EMAIL);

  exec("python database/test_email.py $type $email_clean");
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
      <p class="center">Your email address is: <?php echo $email; ?></p>
      <p class="center">We have sent you the test email you requested, of type <em> <?php echo $type; ?> </em></p>
    </div>


    <footer class="footer">
      <p>&copy; 2016 Causali, Inc.</p>
    </footer>

  </div> <!-- /container -->

  <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  <script src="frontend_play/assets/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
