<?php
class Profesor extends ActiveRecord\Model{

    static $table_name = 'profesor';


    static $meta = array(
        'nombre' => array(
            'autofocus' => true
        ),
        'activo' => array(
            'values' => array(array(0, 'Inactivo/Sab&aacute;tico'), array(1, 'Activo'))
        ),
        'horaspref' => array(
            'tip' => 'Horas de 0-24 separadas por comas. Ej: 9,10,16,17',
            'fname' => 'Horas preferentes'
        )
    );

    // RELATIONS
    static $belongs_to = array(
        array('instituto')
    );

    /*
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

    // $p1 = Profesor->find(1):
    // echo $p1->grados[0]->nombre;
    */

    static $has_many = array(
//        array('grados', 'class_name' => 'Grado'),
//        array('logros', 'class_name' => 'Logro'),
//        array('tesis',  'class_name' => 'Tesis'),

        array('profesormaterias', 'class_name' => 'Profesormateria'),
        array('materias',     'through' => 'profesormaterias',
                               'class_name' => 'Materia')
//        array('publicacionprofesores', 'class_name' => 'Publicacionprofesor'),
//        array('publicaciones', 'through' => 'publicacionprofesores',
//                               'class_name' => 'Publicacion'),

//        array('prps', 'class_name' => 'Proyectoprofesor'),
//        array('pups', 'class_name' => 'Publicacionprofesor'),

//        array('asignaciones', 'class_name' => 'Asignacion'),
//        array('horarios',     'class_name' => 'Horario')
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

    /*
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
     */

    ////////////////////////////////////////////////////////////////

//    function get_nombre(){
//        return $this->nombre." ".$this->apellidos;
//    }

    function get_nombre_formal(){
        return $this->abrev.' '.$this->nombre;
    }

    function get_nombre_estado(){
        return self::$estado_values[$this->estado];
    }


}// END






?>
