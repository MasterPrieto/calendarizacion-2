(ns translator.core
  (:require [clojure.data.json :as json]
            ))

(defn hash-con-ids
  "Usada por hash2context.
  
  Convierte un arreglo de hash-maps en el que todos tienen una clave :id, en un
  hashmap en el que cada hash-map es un valor y la clave es el valor del :id."
  [li]
  (apply hash-map (interleave (map :id li) li)))

(defn hash2context
  "Convierte una cadena JSON del tipo   

  { entidad1 : [ {id : 23, nombre: \"Jose Figueroa\"}
                 {id : 25, nombre: \"Lluvia Carolina\"}
                 ... ]
    entidad2 : [....] 
    ... }

  a un hashmap del tipo 
  
  { 
    :entidad1 {
      23  { :id 23 :nombre \"Jose Figueroa\" }
      25  { :id 24 :nombre \"Lluvia Morales\" }}
    ... }
    :entidad2
    {
      ID1 { :id ID1 ... }
      ID2 { :id ID2 ... }
    }
  }
  "
  [hs]
  (apply hash-map (interleave (keys hs) (map hash-con-ids (vals hs)))))



;;;;;;;;;;;;;;;;;;;;;;;;

(defn json2context
  "Convierte un json del tipo 
  a un contexto."
  [jso]
  (hash2context (json/read-str jso :key-fn keyword)))



(defn inst
  "Retorna una instancia de un tipo de entidad de un hash-map contexto.
  TODO y si recibe una lista, debe devolver una lista!!!"
  [context ent id]
  ((context ent)
   id))


