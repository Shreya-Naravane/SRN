(defun factrec(n)
	(if(= n 0 )
	1
	(* n (factrec(- n 1)))))

(defun factloop(n)
	(defvar i nil)
	(defvar m 1)
	(loop for i from 1 to n
		do(setq m(* m i)))
	m)

(format t "Enter the number to find the factorial ~%")
(defvar k (read))
(format t"The factarial of number using recursion is ~d ~%"(factrec k))
(format t"The factorial of number looping method is ~d ~%"(factloop k))

