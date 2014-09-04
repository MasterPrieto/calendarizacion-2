<?php
class Logro extends ActiveRecord\Model{
    static $table_name = "Logro";

    static $belongs_to = array(
        array('profesor', 'class_name' => 'Profesor')
    );
}
?>
