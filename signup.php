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
        </div>
        <div class='jumbotron'> <p class="lead"> This experiment is going to help you figure out whether meditating makes you calmer. </div></p>
      <form class="form-signin" action="./welcome.php" method="post">

        <div class="media">
          <div class="media-left media-middle">
            <a href='#''>
              <img class="media-object" src="frontend_play/assets/ruler.jpg" alt="..."></a>
            </div>
            <div class="media-body">
              <h4 class="media-heading">We'll use email to run the experiment and collect data</h4>
              <p>What email address would you like us to use?</p>

              <div class="input-group-archy">
                <input type="email" name="inputEmail" class="form-control" placeholder="Email" style="width=0.1em" required autofocus>
              </div>
            </div>
          </div>
          
          <br>

          <div class="media">
            <div class="media-left media-middle">
              <a href='#''>
                <img class="media-object" src="frontend_play/assets/meditation.jpg" alt="..."></a>
              </div>
              <div class="media-body">
                <h4 class="media-heading">Your instruction email tells you whether to meditate</h4>
                <p>What time would you like to receive your instruction email?</p>

                <div class="input-group-archy">
                  <input name="instructionTime" type="time" class="form-control input-small" value="07:00"> 
                </div>
              </div>
          </div>
          
          <br>

          <div class="media">
            <div class="media-left media-middle">
              <a href='#''>
                <img class="media-object" src="frontend_play/assets/smiley.jpg" alt="..."></a>
              </div>
              <div class="media-body">
                <h4 class="media-heading">Later that day, we'll ask you how you're feeling</h4>
                <p>What time would you like to receive your response email?</p>

                <div class="input-group-archy">
                  <input name="responseTime" type="time" class="form-control input-small" value="16:00">
              </div>
            </div>
          </div>

          <br>



          <br>

          <div class="media">
            <div class="media-left media-middle">
              <a href='#''>
                <img class="media-object" src="frontend_play/assets/name.jpg" alt="..."></a>
              </div>
              <div class="media-body">
                <h4 class="media-heading">Don't be a stranger! </h4>
                <p>What's your name?</p>

                <div class="input-group-archy">
                  <input type="text" name="inputName" class="form-control" placeholder="Name?" required>
                </div>
              </div>
            </div> 

          <br> 
     
        
      <button class="btn btn-lg btn-primary btn-block responsive-width" type="submit">Sign Up</button>
       
       
    <footer class="footer">
      <p>&copy; 2016 Causali, Inc.</p>
    </footer>

  </div> <!-- /container -->


  <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
  <script src="frontend_play/assets/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
