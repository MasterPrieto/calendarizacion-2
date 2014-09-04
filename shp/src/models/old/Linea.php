<?php
class Linea extends ActiveRecord\Model{
    static $table_name = "linea";

    static $has_many = array(
        array('tesislineas', 'class_name' => 'Tesislinea')
        );
}
?>
