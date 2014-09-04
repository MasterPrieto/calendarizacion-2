<?php
/*
 *
 * Configuraciones:
 * - instituto_id
 * - anio_actual
 * - periodo_actual
 *
 *
 */
class Configuracion extends ActiveRecord\Model{
    static $table_name = 'configuracion';


    static function valor($configuracion){
        $cf = self::first(array('conditions' =>
            array('nombre = ?', $configuracion)));
        if ($cf)
            return $cf->valor;
        else
            return null;
    }

    static function instituto_id(){
        return self::valor('instituto_id');
    }

    static function anioActual(){
        return self::valor('anio_actual');
    }

    static function periodoActual(){
        return self::valor('periodo_actual');
    }

}

?>
