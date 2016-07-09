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
   
    </div>

    <div class="jumbotron">
      <h1> </h1>
      <p class="lead">Causali brings the power of the scientific method to your life to help you find ways to be happier, healthier, and more productive.</p>
      <p> Try out our first experiment: </p>
      <p style="font-size:3vw"><a class="btn btn-lg btn-success responsive-width multi-line-button" href="signup.php" role="button">Does meditation make me calmer?</a></p>
      <h5>Already have an account? <a href="signin.php"> Sign in </a> </h5>
    </div>

    <div class="row marketing">

      <div class="col-lg-6">

        <div class='media'>
          <div class="media-body">
           <h4>Science, done properly</h4>
           <p>With rigorous randomisation and statistics, Causali generates conclusions you can trust.</p>
         </div>
         <div class="media-right media-middle">
          <span class="glyphicon glyphicon-education"></span>
        </div>
      </div>

      <div class='media'>
        <div class="media-body">
          <h4>Data, beautiful data</h4>
          <p> See your data blossom in custom graphs and analyses.</p>
        </div>
        <div class="media-right media-middle">
          <span class="glyphicon glyphicon-stats"></span>
        </div>
      </div>


      <!-- <img src="assets/brand/bootstrap-solid.svg" align="right" width="50px" height="50px" class="img-responsive inline-block"> -->


      <!-- <img src="assets/brand/bootstrap-solid.svg" align="right" width="50px" height="50px" class="img-responsive inline-block"> -->

    </div>

    <div class="col-lg-6">
      <div class='media'>
        <div class="media-body">
          <h4>How does it work?</h4>
          <p> Sign up for an experiment to receive daily emails telling you what action to take, and provide feedback via prompt emails.</p>
        </div>
        <div class="media-right media-middle">
          <span class="glyphicon glyphicon-cog"></span> 
        </div>  

        <div class='media'>
          <div class="media-body">
            <h4>Share your science</h4>
            <p> Compare your findings with your friends.</p>
          </div>
          <div class="media-right media-middle">
            <span class="glyphicon glyphicon-user"></span> 

          </div>


        </div>
      </div>
    </div>
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
