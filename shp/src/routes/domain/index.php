<?php
/* Funcion para editar en el scaffolding
 *
 *
 *
 *
 *
 *
 */

function toindex(){
    //    redirect()
    $keys = array_keys($_GET);
    $url  = site_url().MR.$_SERVER['QUERY_STRING'];
    $last = substr($url, -1);

    $url .= $last == '/' ? '' : '/';
    $url .= 'index';

    nredirect($url);
}

function index(){
    echo "index";
    $clase  = stash('clase');
    $attrs  = $clase::table()->columns;
    $params = stash('params');

    if (method_exists($clase, 'index')){
        $data   = $clase::index();
        $objs   = $data['instancias'];

        $campos = $data['campos'];
        if (is_array($campos)){
            $nattrs = array();
            foreach ($campos as $campo){
                unset($attrs[$campo]);
                $nattrs[$campo] = $attrs[$campo];
            }
            $attrs = $nattrs;
        }
    }else{
        $objs  = $clase::find('all');
    }
    $exceptos = array();
    if (isset($params['excepto'])){
        $exceptos = explode(',', $params['excepto']);
        foreach ($exceptos as $excepto){
            unset($attrs[$excepto]);
        }
    }

    $sexcepto   = implode(',', $exceptos);
    $urlexcepto = site_url().MR."/domain/$clase/p&excepto=";
    if (!empty($sexcepto))
        $urlexcepto .= $sexcepto.',';

    render('domain'.DS.'index',
        array('clase' => $clase, 'objs' => $objs, 'attrs' => $attrs,
              'urlexcepto' => $urlexcepto));

}

?>
