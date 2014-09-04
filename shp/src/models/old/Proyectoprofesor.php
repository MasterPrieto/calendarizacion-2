<?php
class Proyectoprofesor extends ActiveRecord\Model{
    static $table_name = 'proyectoprofesor';

    static $belongs_to = array(
        array('proyecto'),
        array('profesor')
    );

}
?>
