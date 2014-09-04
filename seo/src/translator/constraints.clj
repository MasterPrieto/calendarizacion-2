(ns translator.constraints
;  (:require [clojure.data.json :as json] )
)
;;; Evaluacion de constraints y manejo de la semantica?



(def ^:dynamic *dias* 5) ;;; Define el numero de dias a planificar
;(def ^:dynamic *

(def contexto
  {
   :problem {
             :bounds []
             :dias 5
             :grupos 10
    }
   :grupo {
           1 {:id 1 :nombre "1002"}
           }
   :materia {
             1 {:id 1 :nombre "Metaheuristicas"}
             }
   :profesor {
              1 {:id 1 :nombre "Jose FM"}
              }
   :espacio  {
              1 {:id 1 :nombre "Aula 1"}
              }
   :PAPI ; problem API
   {
    :cacho    (fn [sol cual] (subvec (
    :grupo    (fn [cacho] (get cacho 0))
    :materia  (fn [cacho] (get cacho 1))
    :profesor (fn [cacho] (get cacho 2))
    :dias     (fn [cacho] (subvec cacho 3))
    ;; [ G M P H0 D0 E0 H1 D1 E1 ... Hdias-1 Ddias-1 Edias-1 ]
    :hora      (fn [cacho dia] (get cacho (+ 3 (* 3 dia))))
    :duracion  (fn [cacho dia] (get cacho (+ 3 (* 3 dia) 1)))
    :espacio   (fn [cacho dia] (get cacho (+ 3 (* 3 dia) 2)))
   
    }
  ;; (((contexto :PAPI) :duracion) [:g :m :p :h0 :d0 :e0 :h1 :d1 :e1] 1) => :d1

   :CAPI ; context API
   {
    :inst (fn [ctx entity id] ( (ctx entity) id))
   }
})

(def colision
  []




(def problema
  [1 1 1 ])



;; Colision de valores
;; Se necesitan acumulados, los cuales me digan cuantas veces se colisionan
;; los valores de attributos a analizar.

