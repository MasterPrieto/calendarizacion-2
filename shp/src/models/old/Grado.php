<?php
class Grado extends ActiveRecord\Model{
    static $table_name = "grado";

    static $belongs_to = array(
        array('profesor', 'class_name' => 'Profesor'),
        array('disciplina', 'class_name' => 'Disciplina'),
        array('area', 'class_name' => 'Area')
    );

    static $nivel_values = array(
        0 => 'Licenciatura',
        1 => 'Maestr&iacute;a',
        2 => 'Doctorado'
    );


    ///////////////////////////////

    // Grados terminados de un profesor, osea, con el obtenido_el
    // diferente del default 0000-00-00.
    static function terminados($pid){
        $cond ='profesor_id = ? and obtenido_el != "0000-00-00"';
        $grados =
            self::find('all', array(
            'conditions' => array($cond, $pid),
            'order' => 'obtenido_el ASC'));
        return $grados;
    }

    function get_nombre(){
        return $this->titulo.', '.$this->universidad;
    }

    function nombreNivel(){
        return self::$nivel_values[$this->nivel];
    }

    ///////////////////////////////

}
?>
