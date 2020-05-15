(defvar l '("shreya" 34 "red" 6.88 "apple"))
(format t "The list is : ~a ~%" l)
;;;;(foramt t "Enter the index of element which you want from the list ~%")
(defvar n(read))

(loop for i from 0 to (- n 1)
	do(setq l (cdr l)))

(format t "~a th element of list is ~a by looping method ~%" n (car l)) 
(defvar m (nth n '("shreya" 34 "red" 6.88 "apple")))
(format t "~a th element of list is ~a by function method ~%" n m) 
