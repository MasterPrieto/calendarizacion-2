<?php
/**
 * Funciones para apoyar el manejo del dominio en el scaffolder.
 *
 * Requiere acceso a los Models.
 *
 *
 */

// Devuelve la clave foranea de la asociacion con nombre $attr en la tabla
// $tabla.
function get_relation_fk($attr, $tabla){
    $relacion = $tabla->get_relationship($attr);
    if (count($relacion->foreign_key) < 2){
        $fk = null;
        if (count($relacion->foreign_key) > 0)
            $fk = $relacion->foreign_key[0];
        return $fk;
    }else{
        throw new Exception("La relacion $attr tiene una
            clave foranea compuesta.");
    }
}

// Devuelve la clase de una relacion recibiendo el nombre del atributo y la
// metainformacion de la tabla.
function get_relation_class($attr, $tabla){
    $relacion = $tabla->get_relationship($attr);
    $cn = $relacion->class_name;
    return $cn;
}


/**
 * Crea un control html de un formulario para poder agregar o editar el valor
 * de un atributo siemple o medio simple utilizando la metainformacion del
 * atributo y la informacion extra colocada en el arreglo $meta de la clase.
 *
 * $attr  - Nombre del atributo.
 * $info  - informacion de phpactivercord sobre el atributo.
 * $meta  - metainformacion del arreglo Clase::$meta[$attr].
 * $value - Valor del atributo en este momento.
 *
 * Del arreglo $meta se manejan los siguientes atributos:
 * autofocus- true/false para tener autofocus o no
 * noedit   - true/false para devolver un label y no un control.
 * hidden   - true/false para no mostrar el control.
 * type     - "hora", "horas", "fecha", "color",. Para tipos raritos.
 * //size     - "area", "normal", etc. Para saber si es un textarea.
 * //            Default es normal.
 * values   - array(array(0, "Inactive",), array(1, 'Active'))
 *            Es para campos enteros cuyo valor es una opcio que aparte
 *            aparte tiene un nombre en html.
 * tip      - Es un tooltip.
 * fname    - "Friendly name", usado para el label.
 *
 * Retorna el control en HTML
 */
function create_control($attr, $info, $meta, $value = null){
    $jquery_date_format = 'dd/mm/yy';
    $control = 'NO SOPORTADO';

    if (!$meta)
        $meta = array();
    if (!$info)
        $info = array();

    if (preg_match("/.*_id$/", $attr) ||
        $attr == 'id') // $tabla->pk[0]) // si es igual a *_id o a id
        return null;

    if (isset($meta['hidden']) && $meta['hidden'])
        return null;

    $title  = isset($meta['tip']) ? $meta['tip'] : '';
    $afocus = isset($meta['autofocus']) ? 'autofocus="autofocus"' : '';


    if (isset($meta['noedit']) && $meta['noedit'])
        return "<label title='$title'>".h($value).'</label>';

    if (isset($meta['values']) && is_array($meta['values'])){
        $values = $meta['values'];  // array(array(0, "V1"), array(1, "V1"))
        $control    = "<select name='$attr' title='$title' $afocus>";

        foreach ($values as $val){
            $vval   = $val[0];
            $vlabel = $val[1];

            $selected   = $vval == $value
                ? 'selected="selected"' : '';
            $control .= "<option value='$vval' $selected>$vlabel</option>";
        }
        $control    .= '</select>';
        return $control;
    }

    if (isset($meta['type'])){  // Un tipo especial
        switch ($meta['type']){
        case 'hour':
            $control = 'HOUR';
            break;
        case 'hours':
            $control = 'HOURS';
            break;

        }
        return $control;
    }

    switch ($info->raw_type){
    case 'text':
        $control = "<textarea name='$attr' $afocus title='$title'>$value</textarea>";
        break;
    case 'date':
        $icono = site_url().'public/images/calendar.gif';
        $control = "<script>
            $(function() {
                $( '#$attr' ).datepicker({
                    dateFormat: '$jquery_date_format',
                        changeMonth: true,
                        changeYear: true,

                        showOn: 'button',
                        buttonImage: '$icono',
                        buttonImageOnly: true
        });
        });</script>";
        $control .= "<input type='text' id='$attr' name='$attr' value='$value' $afocus title='$title' />" ;
        break;
    default:
        $nvalue = h($value);
        $control = "<input type='text' name='$attr' value=\"$nvalue\" $afocus title='$title'/>";
        break;
    }
    return $control;
}

function create_label($attr, $info, $meta){
    $lab   = isset($meta['fname'])? $meta['fname'] : ucfirst($attr);
    //$label = "<label for='$attr'>".$lab."</label>";
    $label = "<label>".$lab."</label>";
    return $label;
}
