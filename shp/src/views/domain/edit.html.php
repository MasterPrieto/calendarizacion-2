<?php
/* Parametros:
 *
 * $clase
 * $obj
 * $tabla
 */

$jquery_date_format = 'dd/mm/yy';



echo "<div style='color: blue;'>".stash('msg').'</div>';
echo "<form name='main' method='POST' accept-charset='uft-8' action=''>";
echo "<table>";
//////////////////////////////////////////////////

$attrs = $tabla->columns;
// TODO aplicar filtros de seguridad, etc.



// ID  ---------------------------------------
$eurl = site_url().MR."/domain/$clase/edit/".$obj->id;
echo "<tr>
    <td><label>Identificador:</label></td>
    <td><a href='$eurl'>$obj->id</a></td>
    </tr>";

// --------------------------------
// ATRIBUTOS SIMPLES

$meta = isset($clase::$meta) ? $clase::$meta : array();

foreach ($attrs as $attr => $info){
    if (preg_match("/.*_id$/", $attr) ||
        $attr == $tabla->pk[0]) // si es igual a *_id o a id
        continue;

    $valor = $obj->$attr;
    $ameta = isset($meta[$attr]) ? $meta[$attr] : array();   // Attribute meta
    $control = create_control($attr, $info, $ameta, $valor);

    $label = create_label($attr, $info, $ameta);

    echo '<tr>';
    echo "<td >$label</td>";

    echo "<td >$control</td>";

    echo "</tr>\n";
}

// ------------------------
// RELACIONES
/*

$rbt = isset($clase::$belongs_to) // BELONGS_TO
    ? $clase::$belongs_to : array();
foreach ($rbt as $bt){
    $attr   = $bt[0];
    $fk     = get_relation_fk($attr, $tabla);
    $cn     = get_relation_class($attr, $tabla);
    $fkmeta = $attrs[$fk];
    
    $ovalores = $cn::find('all');

    // Checa si hay maps, filtros u ordenes para esta clase y este atributo
    if (isset($clase::$edition_map) && isset($clase::$edition_map[$attr]))
        $ovalores = array_map($clase::$edition_map[$attr], $ovalores);
    if (isset($clase::$edition_filter) && isset($clase::$edition_filter[$attr]))
        $ovalores = array_filter($ovalores, $clase::$edition_filter[$attr]);
    if (isset($clase::$edition_order) && isset($clase::$edition_order[$attr]))
        usort($ovalores, $clase::$edition_order[$attr]);

    echo '<tr>';
    echo "<td ><label for='$fk'>".ucfirst($attr)."</label>:</td>";
    echo "<td ><select name='$fk'>";

    // Relaciones a nulos
    if ($fkmeta->nullable == 1){
        $selected = $obj->$fk == 0
            ? 'selected="selected"' : '';
        echo "<option value='0' $selected></option>";
    }

    foreach ($ovalores as $ov){
        $selected = $obj->$fk == $ov->id
            ? 'selected="selected"' : '';
        echo "<option value='$ov->id' $selected>".
            h($ov->nombre).'</option>';
    }
    echo '</select></td></tr>';

}

$rhm = isset($clase::$has_many) // HAS_MANY (buscando las THROUGH)
    ? $clase::$has_many : array();
foreach ($rhm as $hm){
    $attr   = $hm[0];

    if (isset($hm['through'])){
        $th = $hm['through'];
        $claseext   = get_relation_class($attr, $tabla);
        $claseuni = get_relation_class($th, $tabla);
        $fk = $tabla->table.'_id';

        print_r($claseext);
        print_r($claseuni);
    }
}

 */

// FOOTER
echo '<tr><td colspan="2"><hr/></td></tr>
    <tr>
    <td><input style="font-weight: bolder;" name="guardar" type="submit" value="Guardar" /></td>
    <td><input type="reset" value="Restaurar" /></td>
    </tr>';


////////////////
echo '</table>';
echo '</form>';

//--------------
// HAS_MANY links
/*
echo "<hr/>";
$hms = isset($clase::$has_many) // BELONGS_TO
    ? $clase::$has_many : array();
foreach ($hms as $hm){
    $attr = $hm[0];
    $fk     = get_relation_fk($attr, $tabla);
    $cn     = get_relation_class($attr, $tabla);

    // Solo many-to-many
    if (isset($hm['through'])){
        $url = site_url().MR.DS."domain/$clase/edit-relation/$obj->id/$attr";
        echo "<a href='$url'>".ucfirst($attr)."</a>&nbsp;
            <a href='$url'>$url</a><br/>";
    }

}
 */


// ----------------------------

?>
