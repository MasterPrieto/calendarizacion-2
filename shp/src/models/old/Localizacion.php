<?php
class Localizacion extends ActiveRecord\Model{
    static $table_name = "localizacion";

    static $has_many = array(
        array('horarios', 'class_name' => 'horario')
    );
}
?>
