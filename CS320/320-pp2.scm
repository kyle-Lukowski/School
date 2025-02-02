#lang Scheme

; Scheme starter code for COMPSCI 320 Programming Project 2
; Zach Oster, 2023-11-20

; Don't edit this line unless pp2csv.scm is in a different folder/directory.
; You will need this line to import the CSV-reading code.
(require rnrs "./pp2csv.scm")

; You can uncomment this line to see the internal representation of the data set.
; It should be commented out (or deleted) in your final submitted version.
(define my-data (read-billdata "cs320-F23-pp2-data.csv"))

; My CSV reader produces a list of records, where each record is represented as
; a data structure called an "association list" or an "alist". This is similar
; to a Python dictionary: for example, you can use (cdr (assoc field-id record))
; to look up the value of the field-id field in the given record. See the
; is_Canadian and postcode_begins_with functions, below, for examples.

; I *strongly* recommend that you use _The Scheme Programming Language_, online
; at https://scheme.com/tspl4/, to help you understand my sample code and look
; for possible ways to solve these problems. The Index link at the end might be
; especially helpful; it was for me!

; Insert your code below. You will need to write the following functions.

;;; Extract function: complete this first! It's probably easier than you think.
(define extract
  (lambda (query-func billdata-path)
    (let ((billdata (read-billdata billdata-path)))
       (filter query-func billdata))))


;;; Query functions

; Sample query function: returns true for each customer who is in Canada.
; Input: an association list containing one customer's billing data
; Output: true if the customer's address is in Canada, false otherwise
(define is_Canadian
  (lambda (customer)
    ; note: string=? is like eq? or equal?, but specifically for strings
    (string=? (cdr (assoc "Country" customer)) "CA")))

; ordered_this_month: true iff the customer ordered any items this
; month; expects one argument, an association list containing
; one customer's billing data
(define ordered_this_month
  (lambda (customer)
    (let ((ordered (assoc "Items Ordered This Month" customer)))
      (and ordered
           (> (string->number (cdr ordered)) 0)))))


; has_zero_balance: true iff the customer has a zero balance; expects no
; arguments
(define has_zero_balance
  (lambda (customer)
    (let ((balance-assoc (assoc "Amount To Pay" customer)))
      (and balance-assoc
           (= (string->number (cdr balance-assoc)) 0)))))

; Sample query function (actually a factory function): expects a string.
; Creates and returns a function, which returns true iff a given customer's
; postal code begins with the string that was used as an argument to this
; factory function.
; * Example uses of this function:
; ((postcode_begins_with "547") (car (read-billdata billdata-path))) => #f
; ((postcode_begins_with "53") (car (read-billdata billdata-path))) => #t
(define postcode_begins_with
  (lambda (prefix)
    (lambda (customer)
      (let ((prefix-length (string-length prefix))
            (customer-postcode (cdr (assoc "Postal Code" customer))))
        (string=? prefix
                  (substring customer-postcode 0 prefix-length))))))
                  

; due_before: a factory function. Expects an integer that encodes a date.
; Creates and returns a function, which returns true iff the customer's
; due date is before the given date.
;   * Your due_before function will use a lambda nested inside a lambda,
;     similar to postcode_begins_with, but the comparison will be different.
(define due_before
  (lambda (target-date)
    (lambda (customer)
      (let ((customer-due-date-string (cdr (assoc "Due Date" customer))))
        (let ((customer-due-date (string->number customer-due-date-string)))
          (< customer-due-date target-date))))))





   

;;; Main program

; You can hard-code the data set's location into your main program. This code
; assumes that the data set is in the same directory/folder as the code.
(define billdata_path "./cs320-F23-pp2-data.csv")

; Fill in code below here to generate the report.
; I've included some sample code to give you some ideas, but the sample
; code **will not work** until you complete the extract function.



; This function prints a string, followed by a newline.
; It will make your output code shorter and easier to read.
(define println
  (lambda (str)
    (display str)
    (newline)))

(display "----------") ;first filter
(newline)
(display "Number of customers who ordered this month: ")
(println
 (length
  (filter (lambda (customer)
            (ordered_this_month customer))
          (extract ordered_this_month billdata_path))))

(display "----------") ;second filter
(newline)
(display "Total number of customers from postal code 51390 who ordered this month: ")
(println
 (length
  (filter (lambda (customer)
            (and (string=? (cdr (assoc "Postal Code" customer)) "53190")
                 (ordered_this_month customer)))
          (extract ordered_this_month billdata_path))))
 
(display "----------") ;filter 3
(newline)
(display "Average Amount To Pay for customers who ordered this month:")
(newline)
(let* ((total (map (lambda (customer)
                               (string->number (cdr (assoc "Amount To Pay" customer))))
                             (extract ordered_this_month billdata_path)))
       (average-amount (/ (apply + total) (length total))))
  (println average-amount))

(display "----------") ;fourth filter
(newline)
(display "Number of customers who have zero balance: ")
(println
 (length
  (filter (lambda (customer)
            (has_zero_balance customer))
          (extract has_zero_balance billdata_path))))

(display "----------") ;filter 5
(newline)
(display "Number of customers who are overdue")
(newline)
(let ((count
       (length (extract (due_before 20231205) billdata_path))))
  (println count))

(display "----------")
(newline)
(display "Average Balance of overdue customer")
(newline)
(let* ((due-customers (extract (due_before 20231205) billdata_path))
       (balances (map (lambda (customer)
                        (string->number (cdr (assoc "Amount To Pay" customer))))
                      due-customers))
       (average-balance (if (not (= 0 (length balances)))
                           (/ (apply + balances) (length balances))
                           0)))
  (println average-balance))
