<!DOCTYPE html>
<html lang="en">
  <head>
    
  <?php $thisPage="signin"; ?>
  <?php include_once('assetHeader.php') ?>
  </head>

  <body>

    <div class="container">
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
              <li role="presentation" class="active"><a href="experiments.html">My Lab</a></li>
              <li role="presentation"><a href="about.html">About Causali</a></li>
              <li role="presentation"><a href="contact.html">Contact</a></li>
          </ul>
        </nav>
        <h3 class="text-muted">Causali</h3>
      </div>

      <form class="form-signin">
        <h2 class="form-signin-heading" align="center">Sign in to Causali</h2>
        <label for="inputEmail" class="sr-only">Email address</label>
        <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
        <label for="inputPassword" class="sr-only">Password</label>
        <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
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
