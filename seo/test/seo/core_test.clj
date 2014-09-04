(ns seo.core-test
  (:require [expectations :refer :all]
            [seo.core :refer :all]))

;(deftest a-test
;  (testing "FIXME, I fail."
;    (is (= 0 1))))
;
(expect 1 1)
(expect 2 (+ 1 1))
(expect [2 3 4] [2 3 4])
