#lang scheme
(define index-of
        (lambda (val lst)
          (cond
           ((eq? (car lst) val) 0)
           (else
           (+ 1 (index-of val (cdr lst)))))))

(define val 3)
(define list '(1 2 3))
(index-of val list)

(define (list-evens lst)
  (cond
    ((null? lst) '())   
    ((eq? (cdr lst) '()) '()) 
    (else (cons (car lst) (list-evens (cdr(cdr lst)))))))

(list-evens '(a great big world out there))
