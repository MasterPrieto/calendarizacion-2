<?php
class Programa extends ActiveRecord\Model{
    static $table_name = "programa";

    static $has_many = array(
        array('asignaturas', 'class_name' => 'Asignatura')
    );
}
?>
