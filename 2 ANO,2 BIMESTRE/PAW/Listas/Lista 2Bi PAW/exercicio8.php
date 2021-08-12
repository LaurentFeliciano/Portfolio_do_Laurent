<?php
	$idade= $_GET['idade'];
	if($idade<=7 && $idade>=5){
		echo "Infantil A";
	}else{
		if($idade<=11 && $idade>=8){
			echo "Infantil B";
		}else{
			if($idade<=13 && $idade>=12){
				echo "juvenil A";
			}else{
				if($idade<=17 && $idade>=14){
					echo "juvenil B";
				}else{
					if($idade>=18){
						echo "adultos";
					}
				}
			}
		}
	}
?>