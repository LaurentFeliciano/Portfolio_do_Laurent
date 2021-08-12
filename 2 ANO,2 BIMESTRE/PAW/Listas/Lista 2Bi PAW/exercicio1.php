<?php
	$salario_bruto= $_GET['salario_bruto'];
	$horas_extras= $_GET['horas_extras'];
	$valor_horas_extras= $_GET['valor_horas_extras'];
	$salario_liquido=0;

	$salario_liquido= $salario_bruto + ($valor_horas_extras*$horas_extras);
	$salario_liquido= $salario_liquido- ($salario_liquido *8/100);
		echo $salario_liquido;
?>