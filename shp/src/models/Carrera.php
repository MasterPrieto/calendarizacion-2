<?php
class Carrera extends ActiveRecord\Model{
    static $table_name = 'Carrera';

    static $belongs_to = array(
        array('instituto')
    );

}
?>
