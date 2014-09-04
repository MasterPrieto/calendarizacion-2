<?php
class Publicacion extends ActiveRecord\Model{
    static $table_name = "publicacion";

    static $has_many = array(
        array('publicacionprofesores', 'class_name' => 'Publicacionprofesor'),
        array('publicacionalumnos', 'class_name' => 'Publicacionalumno'),
        array('profesores', 'through' => 'publicacionprofesores',
                            'class_name' => 'Profesor'),
        array('alumnos', 'through' => 'publicacionalumnos',
                            'class_name' => 'Alumno')

//        array('pups', 'class_name' => 'Publicacionprofesor'),
//        array('puas', 'class_name' => 'Publicacionalumno')
    );


    function get_nombre(){
        return $this->titulo;
    }
}
?>
