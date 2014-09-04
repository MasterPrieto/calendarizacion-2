<?php

/* Devuelve un text con todos los caracteres especiales pasados a su
 * representacion en html entities.
 */

if (! defined('ENT_HTML5'))
    define('ENT_HTML5', null);

function debuga($arr){
    echo '<pre>';
    print_r($arr);
    echo '</pre>';
}

function h($texto){
    $ntext = htmlentities($texto, ENT_HTML5, "UTF-8");
    if (empty($ntext)){
        // Al final todos los textos van a quedar con UTF-8 :-)
        $ntext = htmlentities($texto, ENT_HTML5 | ENT_IGNORE, "ISO-8859-1");
    }
    if (empty($ntext)){
        $ntext = $texto;
    }
    return $ntext;
    //return $texto;
}

// Contrario a h()
function dh($texto){
    return html_entity_decode($texto, ENT_HTML5, 'UTF-8');
}

// Formato para la fecha estandard
function ffecha(){
    return 'd/m/Y';
}


?>
