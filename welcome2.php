<?php
/*
 * Standard single-node URI format: 
 * mongodb://[username:password@]host:port/[database]
 */
$uri = "mongodb://peter:test@ds011943.mlab.com:11943/zapscience";
$client = new MongoClient($uri);
$db = $client->selectDB("zapscience");
$entries = $db->entries;
// To insert a dict, use the insert method.
$name = .$_POST["name"]
$email = .$_POST["email"]

$entries->insert(array(
	'name' => $name,
	'email' => $email
	),
);
    

$query = array('name' => $name);
$cursor = $songs->find($query);

foreach($cursor as $doc) {
    echo .$doc['name'];
	echo .$doc['email'];
}

// Only close the connection when your app is terminating
$client->close();
?>