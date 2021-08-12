<?php
	$nota= $_GET['nota'];
	$nota2o= $_GET['nota2'];
	$nota3= $_GET['nota3'];
	$media=0;

	$media= ($nota + $nota +$nota)/3;
	if($media>=7){
		echo "aprovado";
	}else{
		echo "reprovado";
	}
	?>