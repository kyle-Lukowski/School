#lang scheme
(car (cdr (cdr '(apple orange pear grapefruit)))) ;#1

(car (car (cdr '((apple orange) (pear graperuit))))) ;#2

(car (cdr (cdr (car '(((apple)(orange)(pear)(grapefruit))))))) ;#3

(car (cdr (cdr'(apple (orange) ((pear)) (((grapefruit))))))) ;#4

(car (cdr (cdr'((((apple))) ((orange)) (pear) grapefruit)))) ;#5

(cdr (car'((((apple) orange) pear) grapefruit))) ;#6

(cons 12 (car '(18) )) ;#7

(cons 18 (cons 12 '())) ;8

(define list1 '(18 151)) ;#9
(define list2(cons 12 (cons 14 '())))
(cons list1 (cons list2 '()))