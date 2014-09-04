

(require '[clojure.core.async :as async])

(def c1 (async/chan))

(def ^:dynamic *flag* (atom true))

(def t1 (async/thread
          (while @*flag*
            (let [v (async/<!! c1)]
              (if (nil? v)
                (reset! *flag* false)
                (println "Recibido " v))))))

(async/>!! c1 (str (rand)))
(async/close! c1)
(async/close! t1)

(async/<!! (async/thread (Thread/sleep 5000) (println "hola") 5))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; SEO en partes :-D



(require '[clojure.core.async :as async])
(require '[clj-time.core :as t])
(require '[clojure.core.reducers :as r])

(def ^:dynamic *params*
  (atom {
         :max-processes (* 2 (.availableProcessors (Runtime/getRuntime)))
         :iterations 100000
         }))

(def ^:dynamic runners (atom nil))
(def ^:dynamic runners-flag (atom true))

(def ^:dynamic *procs*
  "Procesos de optimizacion que se han solicitado y que estan activos.
  Es un hashmap de la siguiente manera
  { :id XYZ
    :kb {}
    :soft {} ; constraints
    :hard {} ; constraints
  }
  TODO Especificar mejor."
  (atom nil))


(def ^:dynamic *algos* (atom {}))
(def ^:dynamic *algo-default* (atom nil)) ; TODO Definir uno base, cual sea.

;;;;;;;;;;;;;;;;;; GENERICO MH

(defn register-algorithm
  [namea fna]
  "Registra un algoritmo"
  (swap! *algos* assoc namea fna))

(defn register-default-algorithm
  [namea]
  "Registra el algoritmo default en *algorithm-default*."
  (reset! *algo-default* namea))

(defn duration-hm
  "Obtiene el hashmap de la duracion entre dos intervalos de tiempos tipo
  clj-time. Devuelve un hashmap con las claves:

  :millis, :seconds, :minutes, :hours y :days"
  ([ini fin]
   (let [inter (t/interval ini fin)]
     {
      :millis (mod (t/in-millis inter) 1000)
      :seconds (mod (t/in-seconds inter) 60)
      :minutes (mod (t/in-minutes inter) 60)
      :hours (mod (t/in-hours inter) 24)
      :days (t/in-days inter)
      }))
  ([ini]
   (duration-hm ini ini))
  ([]
   (let [du (t/now)]
     (duration-hm du du))))

;(defn merge-fault-constraints
;  "Recibe el hashmap de contraints rotos acumulados y un hashmap de los
;  nuevos constraints rotos a integrar en el acumulado. Es como un merge
;  de dos arreglos asociativos sinceramente."
;
;  ([acu faultc]
;   (merge-fault-constraints acu faultc ALGO))
;  ([acu fault ckeys]
;   nil))


;;;;;; Evaluation sub-dsl for constraint counting and more
;;;
;;; Constraints are like
;;; { :soft { :s1 true :s2 false :sN true} :hard {:h1 false :h2 false }}
;;; TODO Mejor trabajar con false y true :-)

(defn failed-cts
  [results ctype]
  "Devuelve la cantidad de constraints fallidas del tipo ctype."
  (let [con (results ctype)
        valss (vals con)]
    (count (filter false? valss))))

(defn fulfilled-cts
  [results ctype]
  "Devuelve la cantidad de constraints cumplidos del tipo ctype."
  (let [con (results ctype)
        valss (vals con)]
    (count (filter true? valss))))


(defn count-cts
  [results ctype]
  "Devuelve la cantidad de constraints del tipo ctype."
  (count (results ctype)))

;;;;;;

(defn random-cts
  [sol ctx]
  "Recibe un solucion y un contexto y devuelve un random para true o false."
  (let [r (rand)]
    (if (> r 0.5)
      true
      false)))

(defn evaluator-cts
  "Evaluador de restricciones. Devuelve lo necesario para que una fn objetivo
  sepa que fue bien o mal y pueda devolver una evaluacion acorde a eso.
  
  Solo evalua las restricciones. Utilizar las funciones failed-cts,
  fulfilled-cts y count-cts para checar la cantidad de restricciones rotas o
  complidas.
  
  Test:
  (evaluator-cts :sol :ctx {:soft {:s1 random-cts :s2 random-cts} :hard {:h1 random-cts :h2 random-cts :h3 random-cts}})



  Retorna por ejemplo:
  { :soft { :s1 true :s2 false :sN true}
    :hard { :h1 false :h2 true :hN false} }
  {:soft {...}} // Si no hay restricciones duras.
  {}  // Si no hay restricciones."
  ([sol ctx consts]
   (evaluator-cts sol ctx consts :soft (keys (consts :soft)) {}))
  ([sol ctx consts ctype ckeys res]
   (if (not (empty? ckeys))
     (let [ckey (first ckeys)
           cfn ((consts ctype) ckey)
           cval (cfn sol ctx)
           nres (assoc-in res [ctype ckey] cval)]
       (recur sol ctx consts ctype (rest ckeys) nres))
     (if (not= ctype :hard)
       (recur sol ctx consts :hard (keys (consts :hard)) res)
       res))))

(defn long-sample-process
  []
  "Este es un proceso de ejemplo que reduce una lista grandisima de numeros.
  Tarda como 30-40 segundos en una iMac con i7."
  (reduce + (range 1000000000N)))

(defn short-sample-process
  []
  "Ejemplo de proceso de corta duracion para las pruebas"
  (reduce + (range 10)))

(defn generic-mh
  [params pdata]
  "Marca la estructura de un algoritmo metaheuristico.
  "
  (let [t (short-sample-process)]
    []))

(defn algorithm-select
  [namealg]
  "Selecciona un algoritmo a partir de su nombre (keyword), tomando el
  algoritmo de los algoritmos registrados en la variable de entorno
  *algos*. Si no se manda un valor se toma el *algorithm-default*"
  (if (not (nil? namealg))
    (@*algos* namealg)
    (@*algos* @*algo-default*)))

;;;;;;;;;;;;;;;;;;;;;;;; FIN GENERICO MH
;;;;;;;;;;;;;;;;;;;;;;;; INI TRADUCCION Y API METAHEURISTICO MH

;;; ACCESO A PROBLEMA
;;;
;;; Esta api depende de la organizacion del problema. La organizacion depende
;;; mucho de si aceptamos horas de teoria y practica en distintos lugares, y si
;;; permitimos horarios quebrados.
;;;
;;; Si tenemos lo de los espacio fijos, osea, si una asignatura se da en dos o
;;; tres espacios distintos, entonces todas las asignaturas se podrian dar en
;;; dos o tres espacios distintos. Esto va a dejar la representacion de la
;;; solucion muy larga pero igualmente facil de operar, ya que esos bounds van
;;; a ser fijos en 0 y no van a afectar, pero ese espacio tiene que estar ahi.
;;;
;;; Ahorita tenemos dos, aunque solo se va a utilizar una por ahora:
;;;
;;; Horarios iguales, suponiendo que las asignaturas solo pueden tener horas
;;; de teoria y tal vez practica en dos lugares dinstintos. Podrian agregarse
;;; N tipos de espacios, pero creo que son suficientes:
;;;
;;;    0     1      2  |   0        1    2  ....
;;;   
;;; [ Grp | Asgt | Prf | Espa/Teo | H | Dur | Espa/Pract | H  | D]
;;;
;;; Horarios quebrados, manejandose los espacios y las horas en los dias de la
;;; semana o dias de clases. Esto cambia MUCHO las funciones de acceso a los
;;; problemas. Creo que deberiamos plantear esto, aunque la solucion puede que
;;; sea mas facil.
;;;
;;; TODO
;;; ERROR Oyes genio, en el de horas fijas, como vas a saber que dias son de
;;; teoria y que dias son de practica? :-O
;;;
;;; Cuando cambian las restricciones, la funcion objetivo se recrea y las
;;; soluciones actuales se reevaluan y se reordenan. Cuando cambian los bounds,
;;; es necesario reiniciar la metaheuristica ya que las funciones pueden ser
;;; inviables desde los bounds, y eso no se checa con las restricciones
;;; fuertes normales.

(def ^:dynamic *mhcpos* ; Describe como esta organizada cada asignacion
  {
   :group     0
   :lecture   1
   :teacher   2
   :schedules 3  ; Posicion de inicio del horario
   :schedule  3   ; Tamanio de cada horario
   :space     0
   :hour      1
   :duration  2
   })


(defn mhcvalue
  [prob sol nassig vari]
  "Obtiene un valor especifico del vector que representa una solucion de
  maestros/horarios/cursos. De un nassig (int) toma un valor vari (keyword).

  vari = :group :lecture :teacher

  (mhcvalue {:assignations 1 :assignation-size 18 :working-days 5} [:g1 :m1 :p1 :e1 :h1 :d1 :e2 :h2 :d2 :e3 :h3 :d3 :e4 :h4 :d4 :e5 :h5 :d5] 0 :lecture)
  "
  (let [wdays (prob :working-days)
        cachosize (prob :assignation-size)
        pos (+ (* cachosize nassig) (*mhcpos* vari))]
    (get sol pos)))

(defn mhcschedule
  [prob sol nassig day vari]
  "
  prob - Hashmap with problem variables.
  sol - Solution vector.
  nassig - Assignation number to locate the correct variables.
  day - Day to take variables of. From 0 to (dec (prob :working-days)).
  vari - Can be :space :hour or :duration.

  Test:
  (mhcschedule {:assignations 1 :assignation-size 18 :working-days 5} [:g1 :m1 :p1 :e1 :h1 :d1 :e2 :h2 :d2 :e3 :h3 :d3 :e4 :h4 :d4 :e5 :h5 :d5] 0 4 :space)
  "
  (let [wdays (prob :working-days)
        cachosize (prob :assignation-size)
        inipos (+ (* cachosize nassig) (*mhcpos* :schedules))
        pos (+ inipos (* (*mhcpos* :schedule) day) (*mhcpos* vari))]
    (get sol pos)))


(defn profesor_
  [prob sol  cacho]
  "Retorna el profesor de la seccion cacho de la solucion sol, segun los
  parametros reportados en el hash map del problema prob.

  prob - Problem definition (from knowledge base hash-map).
  sol - vector solucion
  cacho - el numero de cacho o seccion de la cual se va a extraer el profesor."
  nil)

(defn grupo_
  [prob sol cacho]



(defn translate-cts
  [kb consts]
  "Traductor de restricciones en una semantica generica a codigo clojure
  ejecutable.

  kb es la base de conocimiento actual. Hay muchos detalles importantes ahi.
  consts es un hashmap de restricciones con las claves :soft y :hard."
  nil)

;;;;;;;;;;;;;;;;;;;;;;;; FIN TRADUCCION MH
;;;;;;;;;;;;;;;;;;;;;;;; INI PROCESOS INI
(defn processes
  "Retorna el atomo que guarda los procesos"
  []
  *procs*)

(defn gen-pid
  "Genera una keyword que es un identificador unico para un id de proceso."
  []
  (keyword (str (java.util.UUID/randomUUID))))

(defn process-new
  "Define un nuevo proceso  a partir de los datos de solicitud y lo mete en
  el hashmap de procesos.
  
  Un proceso es:
  {
    :id ; Id unico en toda la base de datos y en todo el hash de procesos.
    :started-at (t/now) ; Fechahora a la que incio.
    :ended-at nil   ; Fechahora a la que termino.
    :status :active ; :active :stopped :closed
    :kb {}  ; Knowledge base hashmap. Si cambia, hay que reiniciar la busqueda.
            ; Incluye la clave :problem { :bounds ... } 
    :results [] ; Arreglo de soluciones. TODO definir el formato de las
                ; soluciones, dependiendo de lo que se pida en la KB.
    :duration (duration-hm) ; Duracion del proceso. Cuenta sumando cachos de
                            ; tiempo en ejecucion.
    :iterations 0           ; Iteraciones que lleva.
    :soft {}
    :hard {} 
    :old {   ;Se van agregando cuando cambian nada mas.
      :soft {}
      :hard {}
      :kb {}  ; Si no la pongo aqui, no voy a saber que cosas cambiaron.
      :results {} 
    }

  }
  
  Como cambia? Se manda a ejecutar el proceso (metadatos) y se devuelve un
  nuevo hash con casi los mismos datos, pero con los datos necesarios nuevos
  y actualizados despues de la ejecucion del algoritmo de optimizacion.
  "
  [procs data]
  (merge data
         {:id (gen-pid)
          :status :active ; :active :stopped :closed
          :kb ; Knowledge base
          :results [] ; Arreglo de soluciones para este 
          :iterations 0
          :started-at (t/now)
          :ended-at nil
          :duration (duration-hm)
          :old {
                :soft {}
                :hard {}
                :kb nil
                :results nil
              }
          ;:fnobj (translator ....) ; Aqui va la traduccion?
          }))

(defn store-process
  "Guarda el proceso dentro de los procesos y retorna el hash de proceso."
  ([procs proc]
   (swap! procs assoc (proc :id) proc)
   procs)
  ([proc]
   (store-process (processes) proc))
  ([]
   (processes)))

;(defn merge-process
;  "Mezcla un viejo proceso con un nuevo proceso. La idea es que no se
;  sobreescriban las cosas base como el :status y que se agregen correctamente
;  las cosas como los viejos valores, los viejos resultados, etc.
;  TODO: Definir mejor"
;  [old neww]
;  (merge old neww))

(defn enqueue-process
  "Mete un proceso (sus datos) a al canal de los procesos en ejecucion o
   \"runners\". Hay que especificar el canal."
  [proc chann]
  (async/>!! chann proc))

(defn take-process
  "Retorna un proceso de un canal. Es para abstraer esta parte de la api de
  manejo de canales."
  [chann]
  (async/<!! chann))

(defn execute-process
  "Este es uno de los buenos, ya que me va a ejecutar el proceso con la
  metaheuristica seleccionada (en donde) y va a devolver el proceso
  con los nuevos datos, ademas de actualizarlo en el estado global de
  procesos.

  TODO
  Falta ver cuando llamar al traductor y cuando actualizar ciertos
  valores como los resultados viejos (si esque sirven de algo).


  npdata {
  :id (pdata :id)
  :kb (pdata :kb)
  :constraints (pdata :constraints)
  :ofn (pdata :ofn)
  :results [
  {:value nil
  :broken-constraints {
  :soft []
  :hard []}
  }]
  :tmp (long-sample-process)
  :started-at started-at
  }"
  [params pdata chanel]
  (let [started-at (t/now)
        algo (algorithm-select (:algorithm params))
        results (generic-mh params pdata)
        finished-at (t/now)
        nduration (merge-with +
                              (pdata :duration)
                              (duration-hm started-at finished-at))
        npdata (assoc pdata :duration nduration
                      :iterations (+ (pdata :iterations) (params :iterations)))
        ]
    (do
      (println "Actualizando proceso " (npdata :id))
      (store-process (merge-process pdata npdata)) ;; puede fallar!
      (println "Remetiendo proceso a la cola de mensajes")
      (enqueueu-process npdata)
      npdata)))

;; Servidor de ejecucion de proceso.
;;
;; Cuando se actualizan los datos de un proceso? como es su ciclo de vida?
;;
(defn dispatcher-server
  [channel flag params procs]
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
            (println "Reejecutando proceso")
            (execute-process params proc channel)
            )
        (do 
          (println "Cerrando proceso " pid " en base de datos"))))))

; A ver, como hacemos el traductor?
; Las colisiones de cosas se deben a la combinacion de restricciones
; relacionadas con el tiempo en recursos individuales. Podemos generalizar
; TODAS las colisiones posibles (digo yo) en un plan, porque creo que de
; estas no han salido.
;
; Sobre las otras restricciones, ya te dije, patrones de igualacion.
; Va a ser complicadita esta parte, pero no deberia de ser tan dificil.
;
;
;
