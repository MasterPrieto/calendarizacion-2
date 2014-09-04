<?php
class Publicacionprofesor extends ActiveRecord\Model{
    static $table_name = 'publicacionprofesor';

    static $belongs_to = array(
        array('profesor'),
        array('publicacion')
    );

}
?>
