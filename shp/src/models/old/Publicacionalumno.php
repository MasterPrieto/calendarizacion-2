<?php
class Publicacionalumno extends ActiveRecord\Model{
    static $table_name = 'publicacionalumno';

    static $belongs_to = array(
        array('alumno'),
        array('publicacion')
    );

}
?>
