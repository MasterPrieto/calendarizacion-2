;;; La cosa va asi. Este es un web service para optimizar problemas genericos.
;;; El funcionamiento va de la siguiente manera:
;;; - Hay un server, que es quien controla las solicitudes y su estado.
;;; - Hay un despachador, que es un thread que lee de un canal todos los
;;;   procesamientos que van saliendo. Este mete datos al canal del
;;;   comunicador. Luego, llama al ejecutor.
;;; - El ejecutor ejecuta en un thread la metaheuristica y mete los resultados
;;;   al canal del despachador. Tambien mete los resultados a la base de datos.
;;; - El comunicador toma cada cosa del canal y la envia a la url proporcionada
;;;   por el server. Osea, es un cliente para mandar los nuevos resultados al
;;;   sistema de calendarizacion de horarios, el cual tiene un web service para
;;;   recibir esos nuevos datos. El comunicador es un thread aparte tambien.
;;;
;;; En teoria esto debe de funcionar bien y es muy poco codigo sinceramente.
;;;
;;; UPDATE:
;;; Todavia no tengo el traductor. Osea, eso no va a salir. No tengo una
;;; metaheuristica. Eso tampoco.
;;; El servidor puede estar manejando procesos tontos que solo me permitan
;;; probar el comportamiento de este sistema como tal. Lo otro lo tendre que
;;; probar aparte, pero ciertamente no lo necesito :-)   Estamos?  Osea,
;;; puedes sacar este servidor pronto y sin tanto royo, ok? Si no te sale la
;;; parte funcional, hazlo imperativo!!! no te puedes poner enfadoso en ese
;;; aspecto, sale?
;;;
;;;
;;;
;;;
;;; Ahora, la metaheuristica ... como le mandamos las cosas??
;;;
;;; (do (require '[seo.core :as seoc] :reload))

(ns seo.core
  (:use org.httpkit.server)
  (:require [clojure.core.async :as async])
  (:use seo.routes)
;  (:use seo.processes)
;  (:use seo.dispatcher)
)

; DEVELOPMENT
;
;(do
;  (require '[clojure.core.async :as async])
;  (use 'org.httpkit.server)
;  (use 'seo.routes)
;  )



;;; GLOBALS ;;;

; Los procesos estan en seo.processes

; Parametros globales para los procesos
; :max-processes es el numero de procesos o runners que puede tener este
; servidor. Por default son el doble de los cores disponibles.
(def ^:dynamic params
  (atom {
         :max-processes (* 2 (.availableProcessors (Runtime/getRuntime)))
         :iterations 100000
         }))

; Para el canal de procesos corriendo o "runners"
(def ^:dynamic runners (atom nil)) 

; Flag para parar el proceso de lectura de runners
(def ^:dynamic runners-flag (atom true))


;;; WEB SERVER ;;;

(defonce webserver (atom nil))


(defn stop-server
  []
  (when-not (nil? @webserver)
    ;; espera 10000ms para que terminen las peticiones pendientes.
    (@webserver :timeout 10000)
    (reset! webserver nil)
    (reset! runners-flag false)
;    (stop-runners runners (processes))
    (async/close! @runners)
    ))

(defn start-server
  ([]
   (start-server {}))
  ([params]
   (do
     (reset! webserver (run-server #'app {:port 8080}))
     (reset! runners-flag true)
     (reset! runners (async/chan (:max-processes @params)))
     ;(init-procs)
     ;(enqueue-procs runners (processes))
     ;(start-dispatcher runners runners-flag (processes))
     )))

(defn -main
  ([]
   ;; La variable 'app' esta en seo.routes.
   ;;
   ;; The #' is useful, when you want to hot-reload code
   ;; You may want to take a look: https://github.com/clojure/tools.namespace
   ;; and http://http-kit.org/migration.html#reload
   ;;
     (start-server))
  ([&args]
   (-main {})))

