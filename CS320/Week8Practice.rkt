#lang scheme
(define pairlist
 (lambda (lst1 lst2)
   (cond
     ((null? lst1) '()) ;if lists are not equal length then stop at shorer list
     ((null? lst2) '()) 
     (else (cons (list (car lst1) (car lst2))
            (pairlist (cdr lst1) (cdr lst2)))))))

;test cases
(pairlist '(1 2 3 4 5) '(6 7 8 9 10))
(pairlist '(x y z) '(1 2 3))
(pairlist '(10 20) '(3.33 6.67))
(pairlist '(1) '(40 80))
(pairlist '(10 20 30) '(2 4))

