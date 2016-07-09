<!-- include google analytics code -->
 <?php include_once("analyticstracking.php") ?>
<!-- menu bar -->
<!--<nav class="navbar">
    <ul class="nav nav-pills pull-right">
       <li role="presentation" <?php if ($thisPage=="index") 
{echo " class='active'";} ?> ><a href="index.php">Home</a></li>
       <li role="presentation" <?php if ($thisPage=="meditation") 
{echo " class='active'";} ?> ><a href="signup.php">Start Experimenting</a></li>
      <li role="presentation" <?php if ($thisPage=="about") 
echo " class='active'";  ?>><a href="about.php">About Causali</a></li>
      <li role="presentation" <?php if ($thisPage=="mylab") 
echo " class='active'";  ?>><a href="signin.php">My Lab</a></li>

      <li role="presentation"<?php if ($thisPage=="contact") 
echo " class='active'";  ?>><a href="contact.php">Contact</a></li>
  </ul>
/nav>-->

<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand"href="#"><img alt="Brand" src="frontend_play/assets/logo10_big.tiff"  style="width:100px" ></a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
    	<ul class="nav navbar-nav pull-right">
    		<li role="presentation" <?php if ($thisPage=="index") 
    		{echo " class='active'";} ?> ><a href="index.php">Home</a></li>
    		<li role="presentation" <?php if ($thisPage=="meditation") 
    		{echo " class='active'";} ?> ><a href="signup.php">Start Experimenting</a></li>
    		<li role="presentation" <?php if ($thisPage=="about") 
    		echo " class='active'";  ?>><a href="about.php">About Causali</a></li>
    		<li role="presentation" <?php if ($thisPage=="mylab") 
    		echo " class='active'";  ?>><a href="signin.php">My Lab</a></li>

    		<li role="presentation"<?php if ($thisPage=="contact") 
    		echo " class='active'";  ?>><a href="contact.php">Contact</a></li>
        
      </ul>
     
    </div><!-- /.navbar-collapse -->
  <!</div><!-- /.container-fluid -->
</nav>