<?php
	$numero_kw= $_GET['numero_kw'];
	$valor_kw=0.12;
	$vt=0;

	$vt= $numero_kw*$valor_kw;
	$vt= $vt+ ($vt *12/100);
		echo $vt;
	?>