<?php
class Admin extends ActiveRecord\Model{
    static $table_name = 'admin';

    static $ROL_ADMIN       = 0;
    static $ROL_JEFE        = 1;
    static $ROL_PROFESOR    = 2;
    static $ROL_ALUMNO      = 3;
    static $ROL_EXTERNO     = 4;

    static $belongs_to = array(
        array('profesor', 'class_name' => 'Profesor')
    );

    static $rol_values = array(
        0 => 'Admin',
        1 => 'Jefe',
        2 => 'Profesor',
        3 => 'Alumno',
        4 => 'Externo'
    );

    function get_nombre_rol () {
        return self::$rol_values[$this->rol];
    }

    function get_nombre(){
        return $this->nombre_rol. ' '.$this->profesor->nombre;
    }

}
?>
