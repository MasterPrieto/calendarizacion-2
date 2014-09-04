<?php
class Apoyo extends ActiveRecord\Model{
    static $table_name = "apoyo";

    static $has_many = array(
        array('proyectos', 'class_name' => 'Proyecto')
    );
}
?>
