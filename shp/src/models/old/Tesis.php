<?php

// TODO Agregar TITULO !!!
class Tesis extends ActiveRecord\Model{
    static $table_name = "tesis";

    static $belongs_to = array(
        array('profesor'),
        array('alumno')
    );

    static $estado_values = array(
        
        );

    static $has_many = array(
        array('tesislineas', 'class_name' => 'Tesislinea'),
        array('lineas',     'through' => 'tesislineas',
                            'class_name' => 'Linea'),
        );

    // TODO cambiar "observaciones" por "titulo"
    function get_nombre(){
        return $this->observaciones;
    }
}
?>
