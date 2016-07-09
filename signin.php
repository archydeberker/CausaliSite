<!DOCTYPE html>
<html lang="en">
  <head>
    
  <?php $thisPage="mylab"; ?>
  <?php include_once('assetHeader.php') ?>
  </head>

  <body>

    <div class="container">
      <div class="header clearfix">
        <?php include_once('header.php') ?>
        
      </div>

      <div class="jumbotron"><p class="lead"> We are working on an online sign-in system and dashboard.</p>

      <p class="lead">At present, to view your results you can enter your email address here to be sent a link to them.</p></div>

      <div class="col-lg-6 col-lg-offset-3" >
      <form class="form-signin">
        <h3 class="form-signin-heading" align="center">Send me my results!</h3>

        <label for="inputEmail" class="sr-only">Email address</label>
        <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
        <!--<label for="inputPassword" class="sr-only">Password</label>-->
        <!--<input type="password" id="inputPassword" class="form-control" placeholder="Password" required>-->
        <br>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      </form>

      <footer class="footer">
        <p>&copy; 2016 Causali, Inc.</p>
      </footer>
    </div>

    </div> <!-- /container -->


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
