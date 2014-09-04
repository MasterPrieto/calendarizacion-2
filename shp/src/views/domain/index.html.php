<?php
/*
 *
 * PARAMETROS:
 * - $clase
 * - $objs
 * - $campos (op)
 * - $urlexcepto
 */


echo "<h3>Entidad $clase</h3>";
$curl = site_url().MR."/domain/$clase/new"; //TODO Pasar a route, sacar de aqui
echo "<a href='$curl'>Crear nueva instancia</a><br/><br/>";

echo '<table border="1px">';

/*
echo '<tr>';
    foreach ($campos as $campo){
        echo '<th>'.ucfirst(h($obj->$campo)).'</th>';
    }
echo '</tr>';

foreach ($objs as $obj){
    $eurl = site_url().MR."/domain/$clase/edit/".$obj->id;
    $vurl = site_url().MR."/domain/$clase/view/".$obj->id;
    $lurl = site_url().MR."/domain/$clase/delete/".$obj->id;

    echo '<tr>';
    foreach ($campos as $campo){
//        echo "<td>$obj->id</td>";
        //        echo "<td>".h($obj->nombre)."</td>";
        echo '<td>'.h($obj->$campo).'</td>';
    }
    echo "<td><a href='$vurl'>Ver</a> | 
    <a href='$eurl'>Editar</a> |
    <a href='$lurl'>Eliminar</a>
    </td>";
    echo '</tr>';
}
 */

echo '<th></th>'; // Para los enlaces
foreach ($attrs as $attr => $meta){
    $url = $urlexcepto.$attr;

    //echo "<th><a href='$url' title='Remover'>".ucfirst($attr).'</a></th>';
    echo "<th>".ucfirst($attr).'</th>';
}

// Las relaciones no valen para orden y no valen para filtros.
if (isset($clase::$belongs_to)){
    foreach($clase::$belongs_to as $bt){
        $nm = ucfirst($bt[0]);
        $pk = $clase::table()->get_relationship($bt[0])->foreign_key[0];

        $url = $urlexcepto.$attr;
        echo "<th>".ucfirst($nm).'</th>';
    }
}

echo '</tr>';

// --------------------------------

foreach ($objs as $obj){
    echo '<tr>';
    //$eurl = site_url().MR."/domain/$clase/edit/".$obj->id;
    //echo "<td><a href='$eurl'>$obj->id</a></td>";

    $eurl = site_url().MR."/domain/$clase/edit/".$obj->id;
    $vurl = site_url().MR."/domain/$clase/view/".$obj->id;
    $lurl = site_url().MR."/domain/$clase/delete/".$obj->id;
    echo "<td>
    <a href='$vurl' title='Ver'>V</a>|<a href='$eurl' title='Editar'>U</a>|<a href='$lurl' title='Eliminar'>D</a>
    </td>";

    foreach ($attrs as $attr => $meta){
        if (!is_object($obj->$attr))    // No es una relacion?
            $valor = h($obj->$attr);
        else
            $valor = h($obj->$attr->nombre); // Nombre de la relacion

//        if (preg_match("/.*_id$/", $attr))
//            continue;

        // Multivalores
        $nvalues = $attr.'_values';   // dia_values, proposito_values, etc.
        if (isset($clase::$$nvalues)){
            $valores = $clase::$$nvalues;
            $valor = $valores[$valor];
        }

        echo "<td>$valor</td>";
    }
    if (isset($clase::$belongs_to)){
        foreach($clase::$belongs_to as $bt){
            $nm = ucfirst($bt[0]);
            $pk = $clase::table()->get_relationship($bt[0])->foreign_key[0];
            $ob = $obj->$bt[0];
            if ($ob)
                $valor = h($ob->nombre);
            else
                $valor = "";
            echo "<td>$valor</td>";
        }
    }


    echo '</tr>';
}



echo '</table>';

?>
<div id="confirmar-borrar" title="¿Eliminar?">
<!-- 
<p><span class="ui-icon ui-icon-alert" style="float: left; margin: 0 7px 20px 0;"></span>These items will be permanently deleted and cannot be recovered. Are you sure?</p> -->
</div>
