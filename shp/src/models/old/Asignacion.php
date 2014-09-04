<?php
class Asignacion extends ActiveRecord\Model{
    static $table_name = "asignacion";

    static $belongs_to = array(
        array('profesor'),
        array('asignatura')
    );

    static $has_many = array(
        array('horarios', 'class_name' => 'Horario')
    );

    //static $after_save = array('actualizar_horario');
    static $before_destroy = array('eliminar_horarios');


    // Para el scaffolder de la edicion
    static $edition_map     = array();
    static $edition_filter  = array();
    static $edition_order   = array();
    /* ---------------------------- */

    function get_nombre(){
        return $this->profesor->nombre.': '.
            $this->asignatura->nombre.' - '.
            $this->anio. $this->periodo . ' - '.
            $this->grupo;
    }

    /* Elimina los horarios ligados a esta asignacion.
     */
    public function eliminar_horarios(){
        foreach ($this->horarios as $horario){
            $horario->delete();
        }
    }

}// End class

Asignacion::$edition_map['asignatura'] = function ($asg){
    $o = new stdClass();
    $o->id = $asg->id;
    $o->nombre = $asg->programa->nombre .' - '. $asg->nombre;
    return $o;
};

Asignacion::$edition_order['asignatura'] = function ($a, $b){
    return $a->nombre > $b->nombre;
};

Asignacion::$edition_map['profesor'] = function ($o){
    $d = new stdClass();
    $d->id = $o->id;
    $d->nombre = $o->nombre .' - '. $o->nombre_estado;
    return $d;
};

Asignacion::$edition_order['profesor'] = function ($a, $b){
    return $a->nombre > $b->nombre;
};

?>
