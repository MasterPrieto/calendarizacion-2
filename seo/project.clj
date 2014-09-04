(defproject seo "0.1.0-SNAPSHOT"
  :description "Servidor de optimizaci&oacute;n"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.6.0"]
 
                 [com.datomic/datomic-free "0.9.4815"]
                 [org.clojure/data.json "0.2.4"]
                 [http-kit "2.1.16"]
                 [compojure "1.1.8"]

                 [expectations "2.0.6"]
                 [lein-ancient "0.5.5"]
                
                 [clj-time "0.7.0"]
                 [org.clojure/core.async "0.1.303.0-886421-alpha"]

                 ]
  :plugins [[lein-autoexpect "1.2.2"]
            [lein-expectations "0.0.7"]])
