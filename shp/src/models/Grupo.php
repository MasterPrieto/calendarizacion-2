<?php
class Grupo extends ActiveRecord\Model{
    static $table_name = 'grupo';

    static $belongs_to = array(
        array('carrera')
    );

}
?>
