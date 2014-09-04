;;; Manejo de procesos
(ns seo.processes
  (:require [clojure.core.async :as async])
  (:require [clj-time.core :as t])
  )

(def ^:dynamic *procs*
  "Procesos de optimizacion que se han solicitado y que estan activos.
  Es un hashmap de la siguiente manera
  { :id XYZ
    :kb {}
    :soft {} ; constraints
    :hard {} ; constraints
  }
  TODO Especificar mejor."
  (aton nil))

(defn processes
  []
  "Retorna el atomo que guarda los procesos"
  *procs*)


(defn gen-pid
  []
  "Genera una keyword que es un identificador unico para un id de proceso."
  (keyword (str (java.util.UUID/randomUUID))))

(defn process-new
  [procs data]
  "Define un nuevo proceso  a partir de los datos de solicitud y lo mete en
  el hashmap de procesos.
  
  data es {
    :kb {}
    :constraints {
      soft: {}
      hard: :{} }
    :old-constraints [] ; Se van agregando cuando cambian nada mas.
    
  }
  "
  (merge data
         {:id (gen-pid)
          :status :active ; :active :stopped :closed
          :results []
          :old-results [] ;
          :started-at (t/now)
          :ended-at nil
          :duration {:years 0 :months 0 :days 0 :hours 0
                     :minutes 0 :seconds 0 :mili 0} ; Se acumula como las iters
          :old-constraints []
          ;:fnobj (translator ....) ; Aqui va la traduccion?
          }))

(defn store-process
  [procs proc]
  "Guarda el proceso dentro de los procesos y retorna el hash de proceso."
  (swap! procs assoc (proc :id) proc)
  procs)

;(defn process-update
;  []
;  "Actualiza los datos del proceso para iniciar una nueva corrida del mismo.
;  Que cosas cambian:
;  - La hora de reinicio del proceso
;  - La kb
;  - Los soft y hard constraints
;  - El status
;  - Los datos de inicio (puede haber un estado inicial)
;
;
;  "
;  nil)

;(defn process-stop
;  []
;  ""
;  nil)



;(defn init-procs
;  []
;  "Inicializa el hmap que guarda los procesos."
;  (if (nil? @*procs*)
;    (reset! *procs* {})))


