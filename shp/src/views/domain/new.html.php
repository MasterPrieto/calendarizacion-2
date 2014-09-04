<?php
/* Parametros:
 *
 * $clase
 * $tabla
 * $newid
 * $datos
 */

$jquery_date_format = 'dd/mm/yy';


if ($newid){
    $url = site_url().MR.'/domain/'.$clase."/edit/$newid";
    echo "<div style='color: blue;'>".stash('msg');
    echo " <a href='$url'>Editar</a>";
    echo '</div>';

}
echo "<div style='color: red;'>".stash('error').'</div>';
echo "<h3>$clase</h3>";
echo "<form name='main' method='POST' accept-charset='uft-8' action=''>";
echo "<table>";
//////////////////////////////////////////////////

$attrs = $tabla->columns;
// TODO aplicar filtros de seguridad, etc.



echo "<tr>
    <td><label for='id'>Identificador:</td>
    <td></td>
    </tr>";

// --------------------------------
// ATRIBUTOS SIMPLES
foreach ($attrs as $attr => $meta){
    if (preg_match("/.*_id$/", $attr) ||
        $attr == $tabla->pk[0]) // si es igual a *_id o a id
        continue;

    $valor = (is_null($datos)) ? '' : $datos[$attr];
    $control = "No soportado.";

    // Multivalores
    $nvalues = $attr.'_values';   // dia_values, proposito_values, etc.
    if (isset($clase::$$nvalues)){
        if (isset($datos[$attr])){
            $val = $datos[$attr];
        }
        $nvaluesd = $attr.'_default';
        $control    = "<select name='$attr'>";
        foreach ($clase::$$nvalues as $valor => $etiqueta){
            if (is_null($datos)){
                $selected = (isset($clase::$$nvaluesd)
                                && $clase::$$nvaluesd == $valor)
                                ? 'selected=\'selected\'' : '';
            }else{
                $selected = ($valor == $val) 
                    ? 'selected=\'selected\'' : '';
            }
            $control .= "<option value='$valor' $selected>$etiqueta</option>";
        }
        $control    .= '</select>';
    }else if ($meta->raw_type == 'text'){ // texto
        $control = "<textarea name='$attr'>$valor</textarea>";
    }else if ($meta->raw_type == 'date'){   // fechas
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
        $control .=
            "<input type='text' id='$attr' name='$attr' value='$valor' />" ;
    }else{
        $control = "<input type='text' name='$attr' value=\"$valor\" />";
    }

    echo '<tr>';
    echo "<td ><label for='$attr'>".ucfirst($attr)."</label></td>";

    echo "<td >$control</td>";

    echo "</tr>\n";
}

// FOOTER
echo '<tr><td colspan="2"><hr/></td></tr>
    <tr>
    <td><input type="reset" value="Restaurar" /></td>
    <td><input style="font-weight: bolder;" name="crear" type="submit" value="Crear" />
        </td>
    </tr>';


////////////////
echo '</table>';
echo '</form>';

/*
echo '<pre>';
echo '--------------------------------'."\n";

print_r($tabla);
echo '</pre>';
 */
?>
