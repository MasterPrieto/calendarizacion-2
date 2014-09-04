<?php

// TODO Agregar TITULO !!!
class Tesislinea extends ActiveRecord\Model{
    static $table_name = "tesislinea";

    static $belongs_to = array(
        array('tesis'),
        array('linea')
    );

    function get_nombre(){
        return $this->tesis->nombre . ' - '.$this->linea->nombre;
    }
}
?>
