<!DOCTYPE html>
<html lang="en">
  <head>
  <?php $thisPage="signup"; ?>
  <?php include_once('assetHeader.php') ?>

    <!-- Custom styles for timepicker-->
    <link type="text/css" href="../dist/css/bootstrap-timepicker.min.css" />
    <script type="text/javascript" src="../dist/js/jquery.js"></script>
    <script type="text/javascript" src="../dist/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="../dist/js/bootstrap-timepicker.min.js"></script>

  
  <!-- Time picker comes from here: https://jdewit.github.io/bootstrap-timepicker/ -->

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="container">
      <div class="header clearfix">
       
      <?php include_once('header.php') ?>
        <h3 class="text-muted">Causali</h3>
      </div>

      <form class="form-signin">

        <h2 class="form-signin-heading" align="center">Sign up to Causali</h2>
        <br>


        <h4> Your details </h4>
        <label for="inputName" class="sr-only">Name</label>
        <input type="email" id="inputEmail" class="form-control" placeholder="Name" required autofocus>
        <label for="inputEmail" class="sr-only">Email Address</label>
        <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required>
        <label for="inputPassword" class="sr-only">Choose A Password</label>
        <input type="password" id="inputPassword" class="form-control" placeholder="Choose A Password" required autofocus>
        <br>
        
       <!--  <div class="dropdown theme-dropdown clearfix">
        <a id="dropdownMenu1" href="#" class="sr-only dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="false" aria-expanded="false">Dropdown <span class="caret"></span></a>
        
        <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
          <li> <a href="#">7.00</a></li>
          <li><a href="#">7.30</a></li>
          <li><a href="#">8.00</a></li>
          <li role="separator" class="divider"></li>
          <li><a href="#">Separated link</a></li>
        </ul>
      </div> -->

      <h4> Experiment preferences </h4>
      <p> What time would you like your instruction email? </p>
      <div class="input-group bootstrap-timepicker timepicker">
        <input id="timepicker1" type="text" class="form-control input-small" default-time="7.00 AM">
        <span class="input-group-addon"><i class="glyphicon glyphicon-time" style="font-size: 17px"></i></span>
      </div>

      <script type="text/javascript">
        $('#timepicker1').timepicker({defaultTime: "7.00 AM"});
      </script>
  

      <p> What time would you like your reporter email? </p>
      <div class="input-group bootstrap-timepicker timepicker">
        <input id="timepicker2" type="text" class="form-control input-small">
        <span class="input-group-addon"><i class="glyphicon glyphicon-time" style="font-size: 17px"></i></span>
      </div>

      <script type="text/javascript">
        $('#timepicker2').timepicker({defaultTime: "4.00 PM"});
      </script>
  
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign Up</button>
      </form>

      <footer class="footer">
        <p>&copy; 2016 Causali, Inc.</p>
      </footer>

    </div> <!-- /container -->


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
