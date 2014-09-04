<?php

filter('pid', function ($pid) {
    try{
        $profesor = Profesor::find($pid);
        stash('profesor', $profesor);

    }catch(Exception $e){
        show_error('No se pudo encontrar al profesor con ID: '.
                    strval($pid) ,$e);
    }

});

get('/index/:pid/proyectos', function(){ 
    $pr = stash('profesor');
    $proyectos  = $pr->proyectos();
    
    header('profesor', h($pr->nombreCompleto()));
    render('index'.DS.'proyectos',
        array('proyectos' => $proyectos), false);

});

get('/index/:pid/proyectos-todos', function(){ 
    $pr = stash('profesor');
    $proyectos  = $pr->proyectos(false);
    
    header('profesor', h($pr->nombreCompleto()));
    render('index'.DS.'proyectos',
        array('proyectos' => $proyectos), false);

});

get('/index/:pid/horario', function(){ 
    $pr = stash('profesor');

    nocache();
    header('profesor', h($pr->nombreCompleto()));

    $canio          = Configuracion::anioActual();
    $cperiodo       = Configuracion::periodoActual();
    $tabla = Horario::horario_de($pr->id, $canio, $cperiodo);

   render('index'.DS.'horario',
          array('tabla' => $tabla), false); // NO layout

});

get('/index/:pid/publicaciones', function(){ 
    $pr = stash('profesor');

    nocache();
    header('profesor', h($pr->nombreCompleto()));

    $publicaciones  = $pr->publicaciones();
    //$canio          = Configuracion::anioActual();

    render('index'.DS.'publicaciones',
        array('publicaciones' => $publicaciones), false);
});

get('/index/:pid/ofertas', function(){ 
    $pr = stash('profesor');

    nocache();
    header('profesor', h($pr->nombreCompleto()));

        render('index'.DS.'ofertas',
          array(), false); // NO layout

});

get('/index', function(){

    $texto = "Partes principales del index de computacion:\n
        - index/(idprofesor)/publicaciones/(idprofesor)
        - index/proyectos/(idprofesor)
        - index/horario/(idprofesor)";

    echo '<pre>'.$texto.'</pre>';
});

?>
