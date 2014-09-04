<?php
class Espacio extends ActiveRecord\Model{
    static $table_name = 'espacio';

    static $belongs_to = array(
        array('tipoespacio')
    );

}
?>
