<?php
/* 
 *
 * PARAMAS??: valores default del sistema/valores default datos.
 */

function new_obj(){
    $clase = stash('clase');
    $tabla = $clase::table();

    $newid = null;
    $datos = null;
    if (isset($_POST['crear'])){
        unset($_POST['crear']);
        $datos = $_POST;

        try{
            $obj = $clase::create($datos);
//            $obj->save();

            $newid = $obj->id;
            $datos = null;
        }catch(Exception $e){
            $error = extract_error($e);
//            show_error("No se pudo crear la instancia
            //               tipo $clase:<br/>$error", $e);
            //return;
            stash('error', $error);
        }

        stash('msg', "Instancia creada exitosamente.");
    }

    render('domain'.DS.'new',
        array('clase' => $clase, 'tabla' => $tabla,
        'newid' => $newid, 'datos' => $datos ));
}
?>
