<?php
class Proyectoalumno extends ActiveRecord\Model{
    static $table_name = 'proyectoalumno';

    static $belongs_to = array(
        array('proyecto'),
        array('alumno')
    );

}
?>
