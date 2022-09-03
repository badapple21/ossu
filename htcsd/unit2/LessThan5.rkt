;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname LessThan5) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Less Than 5 Number -> Boolean
;; returns true if n is less then 5
(check-expect (LessThan5 2) true)
(check-expect (LessThan5 7) false)


;;(define (LessThan5 n) false) ;stub

;;(define (LessThan5 n)        ;template
;;  (... n))

(define (LessThan5 n)
  (< n 5))