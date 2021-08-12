<?php
	$celcius=0;
	$f= $_GET['f'];

	if($f>=40 && $f<=70){
	$celcius= 5/9*($f-32);
	echo $celcius;
	echo "<br/>";
	echo $f;
	}else{
		echo 'digitação errada';
	}	
?>