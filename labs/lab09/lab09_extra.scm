;; Extra Scheme Questions ;;


; Q5
(define lst
  '((1) 2 (3 . 4) 5)
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (cond
      ((null? lst) '())
      ((= (car lst) item)  (remove item (cdr lst)))
      (else (cons (car lst) (remove item (cdr lst))))
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (define x (max a b))
  (define b (min a b))
  (cond
      ((= x 0) b)
      ((= b 0) x)
      ((= (modulo x b) 0) b)
      (else (gcd b (modulo x b)))
  )
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  (if (null? s)
      nil
      (cons (car s) (filter (lambda (x) (not (= (car s) x))) (no-repeats (cdr s))))
  )
)

; Q10
(define (substitute s old new)
  (if (null? s)
      s
      (if (not (pair? (car s)))
          (if (eq? (car s) old)
              (cons new (substitute (cdr s) old new))
              (cons (car s) (substitute (cdr s) old new))
          )
          (cons (substitute (car s) old new) (substitute (cdr s) old new))
      )
  )
)

; Q11
(define (sub-all s olds news)
  (if (null? olds)
      s
      (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
  )
)
