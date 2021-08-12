<?php
	$ladoa= $_GET['ladoa'];
	$ladob= $_GET['ladob'];
	$ladoc= $_GET['ladoc'];

	if($ladoa==$ladob && $ladoa==$ladoc){
		echo "equilatero";
	}else{
		if(($ladoa==$ladob && $ladoa!=$ladoc)||($ladoa==$ladoc && $ladoa!=$ladob) ||($ladoc==$ladob && $ladoa!=$ladoc)){
			echo "isoceles";
		}else{
			if($ladoa!=$ladob && $ladoa!=$ladoc && $ladoc!= $ladob){
				echo "escaleno";
			}
		}
	}
?>