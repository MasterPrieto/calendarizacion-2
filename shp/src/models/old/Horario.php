<?php
class Horario extends ActiveRecord\Model{
    static $table_name = "horario";

    static $belongs_to = array(
        array('asignacion'),
        array('localizacion')
    );

    static $PROPOSITO_CLASE     =  0;
    static $PROPOSITO_ASESORIA  = 1;

    static $proposito_values    = array(
        0 => 'Clase',
        1 => 'Asesorias');
    static $dia_values          = array(
        'L' => 'Lunes',
        'M' => 'Martes',
        'X' => 'Mi&eacute;rcoles',
        'J' => 'Jueves',
        'V' => 'Viernes');

    ////////////

    static function horario_de($profesor_id, $anio, $periodo){

        $asgs    = Asignacion::all(array('conditions' =>
                     array('profesor_id = ? and anio = ? and periodo = ?',
                         $profesor_id, $anio, $periodo)));

        $horarios = array();
        foreach ($asgs as $asg){
            $ahorarios = $asg->horarios;
            if ($ahorarios){
                foreach ($ahorarios as $aho){
                    $horarios[] = $aho;
                }
            }
        }

        $tabla = array(
            8   => array('L' => NULL, 'M' => NULL, 'X' => NULL,
                                'J' => NULL, 'V' => NULL),
            9  => array('L' => NULL, 'M' => NULL, 'X' => NULL,
                                'J' => NULL, 'V' => NULL),
            10 => array('L' => NULL, 'M' => NULL, 'X' => NULL,
                                'J' => NULL, 'V' => NULL),
            11 => array('L' => NULL, 'M' => NULL, 'X' => NULL,
                                'J' => NULL, 'V' => NULL),
            12 => array('L' => NULL, 'M' => NULL, 'X' => NULL,
                                'J' => NULL, 'V' => NULL),
            13 => array('L' => NULL, 'M' => NULL, 'X' => NULL,
                                'J' => NULL, 'V' => NULL),
            16 => array('L' => NULL, 'M' => NULL, 'X' => NULL,
                                'J' => NULL, 'V' => NULL),
            17 => array('L' => NULL, 'M' => NULL, 'X' => NULL,
                                'J' => NULL, 'V' => NULL),
            18 => array('L' => NULL, 'M' => NULL, 'X' => NULL,
                                'J' => NULL, 'V' => NULL)
                            );

        foreach ($horarios as $h){
            $tabla[$h->hora][$h->dia] = $h;
        }

        return $tabla;
    }

    /////////////////////////////////////////////////////

    function get_nombre_dia(){
        return self::$dia_values[$this->dia];
    }

    function get_nombre(){
        return $this->nombreProposito().': '.
            dh($this->nombre_dia) . ' '.
            $this->hora . ' hr. '.
            $this->asignacion->nombre;
    }


    function nombreProposito(){
        return self::$proposito_values[$this->proposito];
    }




}
?>
