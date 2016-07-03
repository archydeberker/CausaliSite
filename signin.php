<!DOCTYPE html>
<html lang="en">
  <head>
    
  <?php $thisPage="index"; ?>
  <?php include_once('assetHeader.php') ?>
  </head>

  <body>

    <div class="container">
      <div class="header clearfix">
        <?php include_once('header.php') ?>
        <h3 class="text-muted">Causali</h3>
      </div>

      <form class="form-signin">
        <h2 class="form-signin-heading" align="center">Sign in to Causali</h2>
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

    </div> <!-- /container -->


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
