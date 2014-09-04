<?php
class Unidad extends ActiveRecord\Model{
    static $table_name = "unidad";

    static $belongs_to = array(
        array('asignatura')
    );
}
?>
