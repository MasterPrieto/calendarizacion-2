<?php
require_once("config.php");


//include(CA_RT_PATH . 'test.php');    // TODO: SOLO DE PRUEBAS!!

include(CA_RT_PATH . 'index.php');  // Partes del index de computacion.
include(CA_RT_PATH . 'test.php');   //  Pruebas de las rutas soportadas.
include(CA_RT_PATH . 'domain.php');  // Scaffolder principal.
//include(CA_RT_PATH . 'horario.php');    // ws Horario


get('', function() {
    echo "Sistema temporal de captura de XYZ";
});

get('/403-error', function() {
    echo "A ocurrido un error: \n\n";
    echo '<pre>';
    print_r(stash('error'));
    echo '</pre>';

});


dispatch();

?>
