#lang scheme
(define (is-prime n divisor)
  (cond
    ((= n 2) #t) ;case to check if num is 2(lowest prime)
    ((= divisor 1) #t)
    ((= (remainder n divisor) 0) #f) ;if remainder = 0 then not prime
    (else (is-prime n (- divisor 1)))))

(define (listPrimesBelow n current result)
  (cond
    ((= n 1) result)
    ((< current 2) result) ;base case = 2 smallest prime
    ((is-prime current (floor (/ current 2))) ;n/2 then round down
     (listPrimesBelow n (- current 1) (cons current result)))
    
    (else (listPrimesBelow n (- current 1) result))))

(listPrimesBelow 20 19 '()) ;n=20 current is 19 (n-1) and result is empty to start


(define (bst? list)
  (if (null? list) ;base case when list is empty and conditions below never trigger
      #t
      (let ((current (car list)) ;define current node left and right child nodes for this iter
            (leftchild (cadr list))
            (rightchild (caddr list)))
        
        (and (or (null? leftchild) (and (bst? leftchild) (< (car leftchild) current)))
             (or (null? rightchild) (and (bst? rightchild) (>= (car rightchild) current)))))))

;test cases
(bst? '(4 (2 (1 () ()) (3 () ())) (6 (5 () ()) ()))) ; #t
(bst? '(4 (2 (1 () ()) (3 () ())) (6 (9 () ()) ()))) ; #f
(bst? '(4 (2 (1 () ()) (3 () ())) (1 (5 () ()) ()))) ; #f
(bst? '(4 (7 (1 () ()) (3 () ())) (6 (5 () ()) ()))) ; #f
(bst? '(4 (2 (1 () ()) (1 () ())) (6 (5 () ()) ()))) ; #f
(bst? '(4 (2 (4 () ()) (3 () ())) (6 (5 () ()) ()))) ; #f
(bst? '(4 (2 (1 () ()) (3 () ())) (6 () (9 () ())))) ; #t