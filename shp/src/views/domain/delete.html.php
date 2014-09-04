<?php
/*
 *
 *
 */

if ($eliminar != 0){
    // eliminado
?>

Instancia "<?php echo  $obj->nombre;  ?>" eliminada.


<?php
}else{
    // no eliminado
?>

<form method='POST'>
<span>Eliminar "<?php echo  $obj->nombre;  ?>"? </span><input type='checkbox' name='eliminar' value='1' />
<input type='submit' value='Eliminar' />
</form>


<?php
}
?>
