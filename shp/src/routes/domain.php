<?php
/* Ruteador principal para los scaffoldings creados para las tablas del sistema
 * usando el ORM PHP-ActiveRecord como fuente de informacion.
 *
 * @author Jose Figueroa Martinez <jfigueroa@mixteco.utm.mx
 * @date 2013-05-03
 */

filter('clase', function ($clase) {
    if (isset($clase) &&
        is_subclass_of($clase, 'ActiveRecord\Model')){
            stash('clase', $clase);
    }else{
        show_error('Entidad del dominio inexistente: '.
            strval($clase));
    }
});

filter('id', function ($id) {
    try{
        $clase = stash('clase');
        $obj   = $clase::find($id);
        stash('obj', $obj);

    }catch(Exception $e){
        show_error("No se pudo encontrar la instancia de la
            clase $clase con ID: $id", $e);
    }

});

filter('attr', function ($attr) {
    try{
        $clase    = stash('clase');
        $obj      = stash('obj');
        $relation = $clase::table()->get_relationship($attr);
        if (!$relation){
            throw new Exception();
        }


        print_r($relation);
        stash('attr_base', $attr);
        stash('relation', $relation);

    }catch(Exception $e){
        show_error("No se pudo encontrar la instancia de la
            clase $clase con ID: $id", $e);
    }

});

/* Util para parametros GET.
 * 
 * Ruta: get('/domain/:clase/:p.*', 'index');
 * Url: http://localhost/computacion/sa/?/domain/Profesor/p&excepto=nacionalid,id,nombre
 *
 */
filter('p', function($params){
//    $aparams = array();
//    $a = explode('&', $params);
//    $i = 0;
//    while ($i < count($a)){
//        $b = split('=', $a[i]);
//        $pname  = urldecode($b[0]);
//        $pvalue = urldecode($b[1]);
//        $aparams[$name] = $pvalue;
//        $i++;
//    }
//    stash('params', $aparams);
    unset($_GET[0]);
    stash('params', $_GET);
});


require(CA_RT_PATH.'domain'.DS.'index.php');
get('/domain/:clase', 'toindex');
get('/domain/:clase/index', 'index');
get('/domain/:clase/index/:p.*', 'index');


require(CA_RT_PATH.'domain'.DS.'new.php');
get('/domain/:clase/new', 'new_obj');
post('/domain/:clase/new', 'new_obj');

require(CA_RT_PATH.'domain'.DS.'edit.php');
get('/domain/:clase/edit/:id', 'edit');
post('/domain/:clase/edit/:id', 'edit');

get('/domain/:clase/edit-relation/:id/:attr', 'edit_relation');
post('/domain/:clase/edit-relation/:id/:attr', 'edit_relation');

require(CA_RT_PATH.'domain'.DS.'delete.php');
get('/domain/:clase/delete/:id', 'delete_obj');
post('/domain/:clase/delete/:id', 'delete_obj');

require(CA_RT_PATH.'domain'.DS.'view.php');
get('/domain/:clase/view/:id', 'view');
//get('/domain/:clase/view/:id/:params.*', 'view_params');
get('/domain/:clase/view-partial/:id', 'view_partial');

//get('/domain/:clase/:p.*', 'index');
 

?>
