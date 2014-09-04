<?php
class Tipoespacio extends ActiveRecord\Model{
    static $table_name = 'tipoespacio';

    static $has_many = array(
        array('espacios', 'class_name' => 'Espacio')
    );

}
?>
