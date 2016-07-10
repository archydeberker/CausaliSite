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

  // sanitise input
  $email_clean = filter_var($email, FILTER_SANITIZE_STRING);

  exec("python database/unsubscribe_user.py $email_clean");
  ?>

    <div class="container">
      <div class="header clearfix">
        <?php include_once('header.php') ?>
      <p>
        <h3 class="text-muted" ">Causali</h3> 
      </p>
    </div>

    <div class="jumbotron">
      <h1>We have ended all your experiments.</h1>
      <p class="lead">We have closed all experiments for <?php echo $email_clean; ?>. You will not receive any more emails until you sign up for another experiment.</p>
      <p>Thanks for your interest in Causali.</p>
    </div>


  <footer class="footer">
    <p>&copy; 2016 Causali, Inc.</p>
  </footer>

</div> <!-- /container -->
</div>

<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="frontend_play/assets/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
