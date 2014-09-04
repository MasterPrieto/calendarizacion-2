<?php
function mfdvar($name, $value, $eol, $boundary){
    return
        '--' . $boundary .$eol.
        'Content-Disposition: form-data; name="'.$name.'" '.$eol.$eol.
        $value.$eol;
}

/* Hace login en el isstema como si fuera un usuario
 *
 */
function check_utm_session($destination, $user, $password, $domain){
    $eol = "\r\n";
    $boundary=md5(time());

    $head = '';
    $data = '';

    $data .= mfdvar('.cgifields', 'httpcompress', $eol, $boundary);
    $data .= mfdvar('.cgifields', 'autologin', $eol, $boundary);

    $data .= mfdvar('loginname', $user, $eol, $boundary);
    $data .= mfdvar('password', $password, $eol, $boundary);
    $data .= mfdvar('logindomain', $domain, $eol, $boundary);
    $data .= mfdvar('loginbutton', 'Acceder', $eol, $boundary);
    $data .= mfdvar('httpcompress', '1', $eol, $boundary);
    $data .= '--' . $boundary . '--';

    $content = $head . $data;

    $params = array('http' =>
        array( 'method' => 'POST',
            'header' => 'Content-Type: multipart/form-data; '.
                'boundary=' . $boundary.$eol.
                'Content-Length: '. strval(strlen($data)).$eol,
            'content' => $data));

    $ctx = stream_context_create($params);
    $response = file_get_contents($destination, false, $ctx);

    // Busca la palabra "session" en la respuesta del openwebmail
    if (preg_match('/session/i', $response)){
        return true;
    }else{
        return false;
    }
}

////////////////////////////////////////////
if (! DEBUG){
    function login_profesor($user, $pass){
        $domain = 'correo.utm.mx';
        // TODO ARREGLAR
        $res = check_utm_login(UTM_TEACHER_LOGIN, $user, $pass, $domain);
        if ($res){
            
            $_SESSION['user_type'] = TIPO_ADMIN;
        }
        return $res;
    }

    function login_alumno($user, $pass){
        $domain = 'ndikandi.utm.mx';
        $res = check_utm_login(UTM_STUDENT_LOGIN, $user, $pass, $domain);
        if ($res){
            $_SESSION['user_type'] = Admin::$ROL_ALUMNO;
            return true;
        }else{
            logout();
            return false;
        }
    }

}else{// DEBUG
    function login_profesor($user, $pass){
        $pr = Profesor::find(array('conditions' =>
            array('correo' => $user.'@mixteco.utm.mx')));
        if ($pr){

            $_SESSION['user_type'] = Admin::$ROL_PROFESOR;
            $_SESSION['user_id']   = a;
            return true;
        }else{
            logout();
            return false;
        }
    }

    function login_alumno(){
        $_SESSION['user_type'] = TIPO_ALUMNO;
        return true;
    }
}

function logout(){
    unset($_SESSION['user']);
    unset($_SESSION['user_type']);
    unset($_SESSION['correo']);
    unset($_SESSION['user_name']);
}

////////////////////////////////////////////
/*

    function login($user){
        $_SESSION['uid'] = $user->id;
        return $user;
    }


    function logout(){
        unset($_SESSION['uid']);
    }

    function is_logged(){
        $res = false;
        if (isset($_SESSION['uid']) && $_SESSION['uid'] > 0){
            $res = true;
        }
        return $res;
    }

    function usuario_actual(){
        $us = null;
        if (is_logged()){
            $us = Profesor::find($_SESSION['uid']);
        }
        return $us;
    }


    function is_admin(){
        $res = false;
        $us  = usuario_actual();

        if ($us &&
                $us->admin &&
                $us->admin->rol === Admin::$ROL_ADMIN)
                $res = true;
        return $res;
    }
 */

?>
