<?php
	$idade= $_GET['idade'];
	$dias=0;
	$horas=0;
	$minutos=0;
	$segundos=0;

	$dias= $idade*356;
	$horas= $dias*24;
	$minutos=$horas* 60;
	$segundos=$minutos*60;
		echo "$dias <br> $horas <br> $minutos <br> $segundos";
	?>