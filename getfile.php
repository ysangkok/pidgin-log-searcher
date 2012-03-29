<?php
define("P","/home/janus/.purple/logs/jabber/ysangkok@gmail.com/vogelnatalia970@gmail.com/");

$s=basename($_GET["f"]);

chdir(P);

$arr=explode("\n",file_get_contents($s));

$i=1;
foreach ($arr as &$v) {
	echo "<a name='n$i' href='#'></a>";
	echo "$v\n";
	$i++;
}

/*
$f=fopen($s,"rb");
fpassthru($f);
fclose($f);
*/
?>
