<?php
// Template para elegir profesor/periodo y destino

$pselected[$periodo] = 'selected=\'selected\''
?>
<div style='text-align: center;'>
<form action=''>
    <label for="anio">A&ntilde;o: </label>
    <input type='text' value='<?php echo $anio; ?>' name='anio' id='anio' />
    <label for="periodo">Periodo </label>
    <select id='periodo' name='periodo'>
        <option value='A' <?php echo $pselected['A']; ?> >A</option>
        <option value='B' <?php echo $pselected['B']; ?> >A</option>
    </select>
</form>
</div>
