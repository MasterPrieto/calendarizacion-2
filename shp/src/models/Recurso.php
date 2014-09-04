<?php

class Materia extends ActiveRecord\Model{
    static $table_name = 'materia';

    static $belongs_to = array(
        array('carrera')
    );


}
?>
