<nav>
    <ul class="nav nav-pills pull-right">
       <li role="presentation" <?php if ($thisPage=="index") 
{echo " class='active'";} ?> ><a href="../ver2/index.php">Home</a></li>
	<ul class="nav nav-pills pull-right">
       <li role="presentation" <?php if ($thisPage=="meditation") 
{echo " class='active'";} ?> ><a href="../ver2/signup.php">Start Experimenting</a></li>
      <li role="presentation" <?php if ($thisPage=="about") 
echo " class='active'";  ?>><a href="../ver2/about.php">About Causali</a></li>
      <li role="presentation"<?php if ($thisPage=="contact") 
echo " class='active'";  ?>><a href="../ver2/contact.php">Contact</a></li>
  </ul>
</nav>