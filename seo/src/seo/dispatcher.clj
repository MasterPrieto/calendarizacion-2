;;; Despachador de procesos.
;;;
;;; Por una parte el despachador toma el proceso y lo manda a guardar.
;;;
;;;
;;;
;;; Su chamba tambien es
;;; - tomar nota del tiempo
;;; - ejecutar la metaheuristica
;;;   - si es nueva, empezar de cero
;;;   - si hubo cambios, empezar de cero
;;;   - si no hubo cambios, seguir con el estado previo
;;; - meter los datos al canal de procesos
(ns seo.dispatcher
  (:require [clojure.core.async :as async])
  )


(defn dispatcher-server
  [channel flag procs]
  "Que hace el server:
  - Toma a un proceso del canal de procesos.
  - Busca el proceso en la lista de procesos. Si lo encuentra, ...
  - "
  (while flag
    (let [proc (<!! channel)
          pid (proc :id)
          process (get procs pid :noencontrado) ]
      (if (not= process :noencontrado)
        (do     ; proceso encontrado
            (println "Remetiendo proceso " pid)
            (reset! procs (assoc @procs pid process))
            (println "Guardando avances en base de datos")
            (println "Reejecutando proceso")
            (execute-runner proc channel)
            )
        (do 
          (println "Cerrando proceso " pid " en base de datos"))))))
      
