<?php
class Proyectolinea extends ActiveRecord\Model{
    static $table_name = 'proyectolinea';

    static $belongs_to = array(
        array('proyecto'),
        array('linea')
    );

}
?>
