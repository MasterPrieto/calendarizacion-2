<?php
$app->path('horario', function($request) use ($app){

    $app->path('asignacion', function ($request) use ($app){

        // profesor
        $app->param('int', function($request, $pid) use ($app){
            // anio
            $app->param('int', function($request, $anio) use ($app, $pid){
                // periodo
                $app->param('slug', function($request, $periodo) use ($app, $pid, $anio){
                    if (!isset($_POST['anio'])){

                        $profesor     = Profesor::find($pid);
                        $asignaciones = Asignacion::all(array('conditions' =>
                            array('profesor_id=? and anio=? and periodo=?',
                                $profesor->id, $anio, $periodo)));
                        $tabla    = Horario::horario_de($profesor->id, $canio, $cperiodo);

                        return $app->template('horario'.DS.'asignacion',
                            array(      // Datos para el template
                                'profesor'          => $profesor,
                                'anio'              => $anio,
                                'periodo'           => $periodo,
                                'asignaciones'      => $asignaciones,
                                'tabla'             => $tabla,
                                'localizaciones'    => Localizacion::all()
                            ))->layout('default');
                    }else{
                        // Cambiando anio y periodo
                        return "TODAVIA NO SE PUEDE";
                    }

                });

                return false;
            });

//            $anio       = Configuracion::valor('anio_actual');
//            $periodo    = Configuracion::valor('periodo_actual');
//            $url        = MR.$app->request()->url().'/'.$anio.'/'.$periodo;

            //            return $app->response()->redirect($url);
            return false;
        });
         

        // asignaciones default
        //        $app->path('index', function ($request) use ($app){
            // Seleccionar profesor

            $profesores = Profesor::mostrables();
            $url_base   = MR.$app->request()->url().'/';
            $anio       = Configuracion::valor('anio_actual');
            $periodo    = Configuracion::valor('periodo_actual');

            return $app->template('profesor'.DS.'lista',
                array('profesores' => $profesores,
                      'url_base'   => $url_base,
                      'anio'       => $anio,
                      'periodo'    => $periodo));
//        });

  //      return false;

    });

    $app->param('int', function ($request, $hid) use ($app){

        return "Checando que hacer con el horario $hid";
    });


    $texto = "WS para los horarios:\n
        - new (con parametros post)
        - (idhorario)";

    return $app->response(200, $texto)
        ->contentType('text/plain');
    //        ->disableCache();
    //        ->header('Pragma', 'no-cache');

});
?>
