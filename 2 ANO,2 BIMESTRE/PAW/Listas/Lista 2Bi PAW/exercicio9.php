<?php
	$altura= $_GET['altura'];
	$peso= $_GET['peso'];
	$imc=0;

	$imc= $peso/($altura/100)**2;
	if($imc<20){
		echo "abaixo do peso ideal";
	}else{
		if($imc>=20 && $imc<25){
			echo "peso ideal";
		}else{
			if($imc>=25 && $imc<30){
				echo "acima do peso ideal";
			}else{
				if($imc>=30 && $imc<40){
					echo "obeso";
				}else{
					if($imc>=40){
						echo "obeso mórbido";
					}
				}
			}
		}
	}
?>