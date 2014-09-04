<?php

function delete_obj(){
    $clase = stash('clase');
    $obj = stash('obj');

    $eliminar = isset($_POST['eliminar']) ? intval($_POST['eliminar']) : 0;
    if ( $eliminar != 0){
        // eliminar
        $obj->delete();
    }

    render("domain/delete", array('obj' => $obj, 'clase' => $clase, 'eliminar' => $eliminar));
}

?>
