<?php
/* TODO: Agregar los campos que vienen en el programa de estudios en este modelo.
 *
 *
 */
class Asignatura extends ActiveRecord\Model{
    static $table_name = "asignatura";

    static $belongs_to = array(
        array('programa', 'class_name' => 'Programa')
    );

    static $has_many = array(
        array('unidades', 'class_name' => 'Unidad')
    );

}
?>
