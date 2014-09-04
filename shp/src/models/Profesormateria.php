<?php
class Profesormateria extends ActiveRecord\Model{
    static $table_name = 'profesormateria';

    static $has_many = array(
        array('profesores', 'class_name' => 'Profesor'),
        array('materias', 'class_name' => 'Materia')
    );

}
?>
