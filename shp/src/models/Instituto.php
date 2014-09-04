<?php
class Instituto extends ActiveRecord\Model{
    static $table_name = 'instituto';

    static $has_many = array(
        array('profesores', 'class_name' => 'Profesor')
    );

}
?>
