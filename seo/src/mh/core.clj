(ns mh.core
  "Este es el core de las metaheuristicas. Aqui se pondran un monton de
  funciones que se utilizan en varias metaheuristicas, como son la generacion
  de soluciones aleatorias, el manejo de randoms, entre otros. Tambien habra
  funciones utiles para las pruebas."
  )


(defn merge-fault-constraints
  ([acu faultc]
   "Recibe el hashmap de contraints rotos acumulados y un hashmap de los
   nuevos constraints rotos a integrar en el acumulado. Es como un merge
   de dos arreglos asociativos sinceramente."
   (merge-fault-constraints acu faultc )
  ([acu fault ckeys]
   )



(defn random-ofn
  []
  "Funcion objetivo random.
  
  Ejemplifica lo que deberia de hacer una funcion objetivo real.
  La funcion objetivo recibe una solucion a evaluar, la base de conocimiento
  y el acumulado de restricciones rotas.
  Retorna un hashmap como el valor de la evaluacion de la solucion y con el
  acumulado de restricciones rotas actualizado:
  {
    :value INT
    :fault-constraints 
      {:soft {
        }
      :hard {
      
        }}}"
  {})


(defn generic-mh
  [pa kb fnobj ]
  "Marca la estructura de un algoritmo metaheuristico.
  
  pa  - Parameters:
  kb  - Knowledge base:
  cn  - Constraints:
  ofn - Objective function:"
  nil)
