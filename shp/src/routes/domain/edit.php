<?php
/* Funcion para editar en el scaffolding.
 *
 * Las directivas de seguridad van a ser basicas: Solo los administradores
 * pueden entrar a estas paginas.
 * Los administradores pueden cambiar todo lo que necesiten por ahora.
 *
 * Las vistas van a ser tambien medio programadas y van a recibir un
 * arreglo de metainformacion para crear la interfaz. Van a ser muy dinamicas
 * pero basicas por ahora. La idea es tenerlas para hoy y no para una semana
 * despues.
 */
require_once(CA_HP_PATH.'domain.php');
//require_once(CA_HP_PATH.'domain.php');    // TODO agregar helper de domain.

function edit(){
    $clase = stash('clase');
    $obj   = stash('obj');

    $tabla = $clase::table();
    //->get_relationship('instituto'));

    if (isset($_POST['guardar'])){
        unset($_POST['guardar']);

        try{
            $obj->update_attributes($_POST);
            $obj->save();
        }catch(Exception $e){
            $error = extract_error($e);
            show_error("No se pudo guardar la instancia
               tipo $clase con ID: $obj->id:<br/>$error", $e);
            return;
        }

        stash('msg', "Instancia guardada exitosamente.");
    }

    render('domain'.DS.'edit',
        array('clase' => $clase, 'obj' => $obj, 'tabla' => $tabla));
}

function edit_relation(){
    $clase    = stash('clase');
    $obj      = stash('obj');
    $attr     = stash('attr_base');
    $relation = stash('relation');

    $tabla = $clase::table();
    //->get_relationship('instituto'));

    if (isset($_POST['guardar'])){
        unset($_POST['guardar']);

//         $obj->update_attributes($_POST);
//         $obj->save();
//        stash('msg', "Instancia guardada exitosamente.");
    }

    render('domain'.DS.'edit-relation',
        array('clase' => $clase, 'obj' => $obj, 'tabla' => $tabla,
              'attr_base' => $attr, 'relation' => $relation));
}

?>
