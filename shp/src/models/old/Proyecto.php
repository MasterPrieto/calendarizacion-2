<?php
class Proyecto extends ActiveRecord\Model{
    static $table_name = "proyecto";

    static $belongs_to = array(
        array('apoyo')
    );

    static $has_many = array(
        array('proyectoprofesores', 'class_name' => 'Proyectoprofesor'),
        array('profesores', 'through' => 'proyectoprofesores',
                            'class_name' => 'Profesor'),

        array('pras', 'class_name' => 'Proyectoalumno'),
        array('prps', 'class_name' => 'Proyectoprofesor'),
        array('lineas', 'through' => 'proyectolinea')
    
    );

    //////////////////////////
    static $ESTADO_SOLICITUD = 0;
    static $ESTADO_ACTIVO    = 1;
    static $ESTADO_TERMINADO = 2;

    static $estado_values = array(
        0 => 'Solicitud',
        1 => 'Activo',
        2 => 'Terminado',
        3 => 'Cancelado'
    );

    static $colaboracion_values = array(
        0 => 'Inter disciplinar',
        1 => 'Multi disciplinar',
        2 => 'Multi institucional'
    );

    static $educacional_values = array(
        0 => 'No',
        1 => 'Si'
        );

    static $pertenencia_values = array(
        0 => 'Local',
        1 => 'Regional',
        2 => 'Nacional',
        3 => 'Internacional'
    );

    static $sector_values = array(
        0 => 'P&uacute;blico',
        1 => 'Privado'
    );

    //////////////////////////

    function nombreEstado(){
        return self::$estado_values[$this->estado];
    }

    function nombreColaboracion(){
        return self::$colaboracion_values[$this->colaboracion];
    }

    function nombrePertenencia(){
        return self::$pertenencia_values[$this->pertenencia];
    }

    function nombreSector(){
        return self::$sector_values[$this->sector];
    }

    function profesores(){
        $profes = array();
        foreach ($this->prps as $prp){
            $profes[] = $prp->profesor;
        }
        return $profes;
    }

    function alumnos(){
        $alumnos = array();
        foreach ($this->pras as $pra){
            $alumnos[] = $pra->alumno;
        }
        return $alumnos;
    }

}
?>
