(ns seo.routes
  (:use compojure.core)
;  (:use seo.processes)
  (:require [compojure.route :as route]))

; Servidor Web
;
; Al ser un servicio web, todos los datos estructurados van por JSON.

(defroutes app
  ; TODO agregar ayuda sobre los posibles comandos.
  (GET "/" [] "<h1>Servidor de Optimizaci&oacute;n</h1> Mostrar ayuda!!")

  ;; SERVIDOR
  ; Parametros actuales
  (GET "/server" [] "Par&aacute;metros actuales")
  (POST "/server/:param/:valor" [param valor]
        (str "Cambiando el valor del parametro " param " por " valor))

  ;; PROCESOS
  ; Lista de procesos.
  (GET "/procesos" [] "Lista de procesos actuales") 
  ; Alta de un proceso, retorna un uid unico y otros datos del proceso..
  (PUT "/proceso" [] "Nuevo proceso")
  ; Estado de un proceso (cambios o nuevos resultados).
  (GET "/proceso/:pid" [pid] (str "Estado del proceso " pid)) 
  ; Detener un proceso. Los procesos no se borran.
  (DELETE "/proceso/:pid" [pid] (str "Deteniendo el proceso " pid))
  ; Cambiar los datos de un proceso
  (POST "/proceso/:pid" [pid] (str "Cambiando el proceso " pid " con variables POST"))
  (POST "/eliminar/:pid" [pid] (str "Borrar todos los valores del proceso " pid))
  
  ; Not found
  (route/not-found "<h1>P&aacute;gina no encontrada.</h1>"))

