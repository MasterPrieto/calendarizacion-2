<?php
class Alumno extends ActiveRecord\Model{
    static $table_name = "alumno";

    static $has_many = array(
        array('puas', 'class_name' => 'Publicacionalumno')
    );

    function nombreCompleto(){
        return $this->nombres.' '.$this->apellidos;
    }
}
?>
