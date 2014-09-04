<?php
class Profesor extends ActiveRecord\Model{

    static $table_name = 'profesor';

    static $ESTADO_INACTIVO     = 0;
    static $ESTADO_ACTIVO       = 1;
    static $ESTADO_SABATICO     = 2;
    static $ESTADO_FALLECIDO    = 3;

    static $estado_default = 1;

    static $estado_values = array(
       0  => 'Inactivo',
       1  => 'Activo',
       2  => 'Sab&aacute;tico',
       3  => 'Fallecido'
   );


    static $genero_values = array(
        'H' => 'Hombre',
        'M' => 'Mujer');

    // RELATIONS
    static $belongs_to = array(
        array('instituto')
    );

    static $has_one = array(
        array('admin', 'class_name' => 'Admin')
    );

    static $has_many = array(
        array('grados', 'class_name' => 'Grado'),
        array('logros', 'class_name' => 'Logro'),
        array('tesis',  'class_name' => 'Tesis'),

        array('proyectoprofesores', 'class_name' => 'Proyectoprofesor'),
        array('proyectos',     'through' => 'proyectoprofesores',
                               'class_name' => 'Proyecto'),
        array('publicacionprofesores', 'class_name' => 'Publicacionprofesor'),
        array('publicaciones', 'through' => 'publicacionprofesores',
                               'class_name' => 'Publicacion'),

//        array('prps', 'class_name' => 'Proyectoprofesor'),
//        array('pups', 'class_name' => 'Publicacionprofesor'),

        array('asignaciones', 'class_name' => 'Asignacion'),
        array('horarios',     'class_name' => 'Horario')
    );


    ///////////////////////////////
    // DOMAIN REST INTERFACE FOR:

    /*
    // domain/clase/index
    static function index(){
        $res = array();
        $prs = self::find('all');
        usort($prs, function($a, $b){
            return strcmp($a->apellidos, $b->apellidos);
        });
        $res['instancias'] =  $prs;
//        $res['campos'] = array('id', 'nombre', 'correo', 'instituto');
        return $res;
    }
     */
    ///////////////////////////////////////////////////////////////

    static function mostrables($iid){
        return self::all(array
            ('conditions' => array(
                'instituto_id = ? and
                (estado=? or estado=?)',
                $iid,
                self::$ESTADO_ACTIVO,
                self::$ESTADO_SABATICO),
            'order' => 'apellidos asc'));
    }

    ////////////////////////////////////////////////////////////////

    function get_nombre(){
        return $this->nombres." ".$this->apellidos;
    }

    function get_nombre_formal(){
        return $this->abrev.' '.$this->nombre;
    }

    function get_nombre_estado(){
        return self::$estado_values[$this->estado];
    }

    function nombreCompleto(){
        //$n = $this->nombres." ".$this->apellidos;
        //return ucwords(strtolower($n));
        return $this->nombres." ".$this->apellidos;
    }

    function nombreFormal(){
        //$n = ucwords(strtolower($this->nombreCompleto()));
        //return $this->abrev.' '.$n;
        return $this->abrev.' '.$this->nombreCompleto();
    }

    function proyectos($activos = true){
        $proyectos = array();
        foreach ($this->prps as $prps){
            $proyecto = $prps->proyecto;
            if (! $activos)
                $proyectos[] = $prps->proyecto;
            else
                if ($proyecto && $proyecto->estado != Proyecto::$ESTADO_TERMINADO){
                    $proyectos[] = $prps->proyecto;
                }
        }
        usort($proyectos, function ($a, $b){
            return $a->iniciado_el < $b->iniciado_el;
        });
        return $proyectos;
    }

    function publicaciones(){
        $publicaciones = array();
        foreach ($this->pups as $pups){
            $publicaciones[] = $pups->publicacion;
        }

        usort($publicaciones, function ($a, $b){
            return $a->anio < $b->anio;
        });
         
        return $publicaciones;
    }

    function ofertas(){
        $ofertas = array();

        return $ofertas;
    }

    function localizacion(){
        $loc   = array();
        $loc[] = $this->instituto->nombre;
        if (!empty($this->oficina)){
            $loc[] = $this->oficina;
        }
        return implode(', ', $loc);
    }

    function nombreEstado(){
        return self::$estado_values[$this->estado];
    }

}// END






?>
