<!DOCTYPE html>
<html lang="en">
<head>
  <?php $thisPage="meditation"; ?>
  <?php include_once('assetHeader.php') ?>

  <!-- Custom styles for timepicker-->
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
        </div>
        <div class='jumbotron'> <p class="lead"> Use this page to send a test-email. 
        </div></p>

        <div class='col-md-6 col-md-offset-3'>

          <form class="form-signin" action="./testemail.php" method="post" style= "display: inline-block; text-align: center">
            <div class="input-group-archy" style=" display: inline-block; text-align: center">
              <input type="email" name="inputEmail" class="form-control" placeholder="Email Address" style="width=0.1em" required autofocus>
            </div>    

            <p style="text-align:center">
              <h3> What kind of email would you like to send?</h3>
              <br>
              <select name="emailType">
                <option value="">Select...</option>
                <option value="signup">Signup</option>
                <option value="instruct">Instruction</option>
                <option value="probe">Probe</option>
              </select>
            </p>



            <button class="btn btn-lg btn-primary btn-block responsive-width" type="submit">Send Test Email</button>

          </div> 

        
        
        </div> <!-- /container -->


        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <script src="frontend_play/assets/js/ie10-viewport-bug-workaround.js"></script>
      </body>
      </html>
