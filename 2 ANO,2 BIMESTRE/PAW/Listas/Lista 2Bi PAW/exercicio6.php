<?php
	$lata= $_GET['lata'];
	$garrafa= $_GET['garrafa'];
	$garrafa2= $_GET['garrafa2'];
	$total=0;


	$lata= $lata*350;
	$garrafa2= $garrafa2*2000;
	$garrafa= $garrafa*600;
	$total= $garrafa2+$garrafa+$lata;
	$total= $total/1000;
		echo $total;
	?>