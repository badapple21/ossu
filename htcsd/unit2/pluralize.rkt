;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname pluralize) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; pluralize : string -> string
;; adds an s to the end of a word

(check-expect (pluralize "Farm") "Farms")
(check-expect (pluralize "Key Board") "Key Boards")

;; (define (pluralize s) This is the stub
;; "He")

;; (define (pluralize s) This is the template
;; (... s ...))

(define (pluralize s)
  (string-append s "s"))

