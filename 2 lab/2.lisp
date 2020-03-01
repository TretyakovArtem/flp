;; функция принимает список и меняет первый
;; и второй элемент местами

(defun shuffle(n)
    (print(CONS (CADR n) (CONS (CAR n) (CONS (CADDR n) ())) )))

( shuffle '(4 5 6 7))