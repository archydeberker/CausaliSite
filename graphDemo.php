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

  <!--Load the AJAX API-->
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  
  <?php 

  $temp1 = '578bee08c209cf00a5b6e330';
  $temp2 = '578bee07c209cf00a5b6e32e';
  
  exec("python database/get_resultstable.py $temp1 $temp2", $data_table); 

  $data_table = $data_table[0];

  ?>

  <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawCustomChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.


      // function drawChart() {

      //   // Create the data table.
      //   var data = new google.visualization.DataTable();
      //   data.addColumn('string', 'Topping');
      //   data.addColumn('number', 'Slices');
      //   data.addRows([
      //     ['Mushrooms', 3],
      //     ['Onions', 1],
      //     ['Olives', 1],
      //     ['Zucchini', 1],
      //     ['Pepperoni', 2]
      //     ]);

      //   // Set chart options
      //   var options = {'title':'How Much Pizza I Ate Last Night',
      //   'width':400,
      //   'height':300};

      //   // Instantiate and draw our chart, passing in some options.
      //   var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
      //   chart.draw(data, options);
      // }


      function drawCustomChart(data) {

        // get data table
        var jsonData = '<?php echo $data_table ?>';

        var data = new google.visualization.DataTable(jsonData);

        // Set chart options
        var options = {'title':'Effect of meditation on happiness',
        'hAxis': {'title': 'happiness'}
        'legend': {'position': 'none'},
        'width':400,
        'height':300};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
        chart.draw(data, options);

      }

    </script>



    
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
        <div class='jumbotron'> <p class="lead"> <div id="chart_div"></div></p></div>

        <footer class="footer">
          <p>&copy; 2016 Causali, Inc.</p>
        </footer>

      </div> <!-- /container -->


      <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
      <script src="frontend_play/assets/js/ie10-viewport-bug-workaround.js"></script>
    </body>
    </html>
