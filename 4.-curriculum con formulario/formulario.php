<html>
<body bgcolor="#FFEBAE">
	<center>
		<font face="Verdana">
			<h1>Confirmacion de datos</h1>
			<fieldset>
				<legend><h2>Solicitud de empleo</h2></legend>
				<?php
				$menu='$_POST[menu]';
				$dia='$_POST[dia]';
				echo "puesto: ".$_POST['menu'];
				echo "<p>";
				echo "Fecha de hoy: ".$_POST['dia'];
				echo "<p>";
?>
			</fieldset>
			<fieldset>
				<legend><h2>Datos Personales</h2></legend>
				<?php
				$nombre= '_POST[nombre]';
				$apellidos= '_POST[apellidos]';
				$edad='_POST[edad]';
				$fecha= '_POST[fecha]';
				$nacionalidad= '_POST[nacionalidad]';
				$genero= '_POST[genero]';
				$telefono= '_POST[telefono]';
				$Muni= '_POST[Muni]';
				$coloni= '_POST[coloni]';
				$calle= '_POST[calle]';
				$correo= '_POST[correo]';
				$Estado= '_POST[Estado]';
				echo "Nombre: ".$_POST['nombre'];
				echo "<p>";
				echo "Apellidos: ".$_POST['apellidos'];
				echo "<p>";
				echo "Edad: ".$_POST['edad'];
				echo "<p>";
				echo "Fecha de nacimiento: ".$_POST['fecha'];
				echo "<p>";
				echo "Tu Nacionalidad: ".$_POST['nacionalidad'];
				echo "<p>";
				echo "Genero: ".$_POST['genero'];
				echo "<p>";
				echo "Telefono: ".$_POST['telefono'];
				echo "<p>";
				echo "Genero: ".$_POST['genero'];
				echo "<p>";
				echo "Municipio: ".$_POST['muni'];
				echo "<p>";
				echo "Colonia: ".$_POST['coloni'];
				echo "<p>";
				echo "Calle: ".$_POST['calle'];
				echo "<p>";
				echo "Correo Eñectronico: ".$_POST['correo'];
				echo "<p>";
				echo "Estado Civil: ".$_POST['Estado'];
				echo "<p>";

?>
</fieldset>
</font>
</center>
</body>
</html>
