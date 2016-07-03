<!DOCTYPE html>
<html lang="en">
<head>
  <?php $thisPage="meditation"; ?>
  <?php include_once('assetHeader.php') ?>

  <!-- Custom styles for timepicker-->
  <link type="text/css" href="frontend_play/dist/css/bootstrap-timepicker.min.css" />
  <script type="text/javascript" src="frontend_play/dist/js/jquery.js"></script>
  <script type="text/javascript" src="frontend_play/dist/js/bootstrap.min.js"></script>
  <script type="text/javascript" src="frontend_play/dist/js/bootstrap-timepicker.min.js"></script>

  
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
        <div class='jumbotron'> <p class="lead"> This experiment is going to help you figure out whether meditating makes you calmer. </div></p>
      <form class="form-signin" action="./welcome.php" method="post">

        <div class="row">
          <div class="col-sm-6 col-md-4">
            <div class="thumbnail">
              <img src="frontend_play/assets/ruler.jpg" alt="...">
              <div class="caption">
                <h3 style="min-height: 120px">We'll use email to run the experiment and collect data.</h3>
                <p style="min-height: 100px">What email address would you like us to use?</p>
                  <div class="input-group-archy">
                <input type="email" name="inputEmail" class="form-control" placeholder="Email" required autofocus>
                  </div>
              </div>
            </div>
          </div>
          <div class="col-sm-6 col-md-4">
            <div class="thumbnail">
              <img src="frontend_play/assets/meditation.jpg" alt="...">
              <div class="caption">
                <h3 style="min-height: 120px">Your instruction email tells you whether to meditate</h3>
                <p style="min-height: 100px">What time would you like to receive your instruction email?</p>
                
                <div class="input-group-archy">
                  <input id="timepicker1" type="text" class="form-control input-small" default-time="7.00 AM"> 
                </div>  
                <script type="text/javascript">
                  $('#timepicker1').timepicker({defaultTime: "7.00 AM"});
                </script>
              </div>
            </div>
          </div>
          <div class="col-sm-6 col-md-4">
            <div class="thumbnail">
              <img src="frontend_play/assets/smiley.jpg" alt="...">
              <div class="caption">
                <h3 style="min-height: 120px">Later that day, we'll ask you how you're feeling</h3>
                <p style="min-height: 100px">What time would you like to receive your response email?</p>
                 <div class="input-group-archy">
                <input id="timepicker2" type="text" class="form-control input-small" default-time="4.00 PM"> 
                 <script type="text/javascript">
                  $('#timepicker2').timepicker({defaultTime: "4.00 PM"});
                </script>
              </div>
              </div>
              </div>
            </div>
          </div>

          <div class= "col-sm-12 col-md-12">
          <div class= "col-sm-6 col-sm-offset-3">
          <div class="input-group-archy-2">
          <input type="text" name="inputName" class="form-control" placeholder="Finally, what's your name?" required>
          </div>
          <br>
          </div>
           </div>
     
        
      <button class="btn btn-lg btn-primary btn-block" type="submit">Sign Up</button>
       </div>

    <footer class="footer">
      <p>&copy; 2016 Causali, Inc.</p>
    </footer>

  </div> <!-- /container -->


  <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  <script src="frontend_play/assets/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
