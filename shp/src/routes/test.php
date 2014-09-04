<?php
/*
filter('pid', function ($pid) {
    try{
        $profesor = Profesor::find($pid);
        stash('profesor', $profesor);

    }catch(Exception $e){
        show_error('No se pudo encontrar al profesor con ID: '.
                    strval($pid) ,$e);
    }

});
 */

get('/test/methods', function(){ 
    json("Testeando el metodo GET");

});

post('/test/methods', function(){ 
    json("Testeando el metodo POST");

});

put('/test/methods', function(){ 
    json("Testeando el metodo PUT");

});

delete('/test/methods', function(){ 
    json("Testeando el metodo DELETE");

});

get('/test/charset', function(){
    echo "Default charset: ".ini_get('default_charset');
});

get('/test/afunctions', function(){ 
    $a = array(
        'f1' => function($a){
            return $a;
        });
    echo $a['f1']("Que pedo");
    print_r($a);

});


get('/test/domain', function(){
    header('Content-Type: text/plain');
    $in  = Instituto::find(4);
    print_r($in);
    echo "-------------------------------------------";

});
?>
