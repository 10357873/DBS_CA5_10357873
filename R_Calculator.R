  #10357873 - Ciaran O'Driscoll - CA5
  #created 10 calcultor functions
  #Assumption  - all numbers to 5 decimal places
  #1. multiplication
  #2. division
  #3. exponent
  #4. square root
  #5. square  
  #6. cube
  #7. sine
  #8. cosine
  #9. tan
  #10. inversion
  
  multiply <- function(x,y){
    mult <- x * y
    return(mult)
  }
  
  divide <- function(x,y){
    div <- x / y
    div = round(div, digits = 5)
    return(div)
  }
  
  exponent <- function(x,y){
    exp <- x ** y
    return(exp)
  }
  
  square_root <- function(x){
    square <- sqrt(x)
    square = round(square, digits = 5)
    return(square)
  }
  
  square <- function(x){
    sqr <- x * x
    return(sqr)
  }
  
  cube <- function(x){
    cub<- x * x * x
    return(cub)
  }
  
  sine <- function(x){
    sin <- sin(x*pi/180)
    sin = round(sin, digits = 5)
    return(sin)
  }
  
  cosine <- function(x){
    cosin <- cos(x*pi/180)
    cosin = round(cosin, digits = 5)
    return(cosin)
  }
  
  tangent <- function(x){
    tang <- tan(x*pi/180)
    tang = round(tang, digits = 5)
    return(tang)
  }
  
  invert <- function(x){
    inv <- 1 / x
    inv = round(inv, digits = 5)
    return(inv)
  }
  
  
  
  multiply(4,2)
  multiply(3,6.5)
  divide(4,3)
  divide(3,0)
  exponent(2,3)
  exponent(4,3)
  square_root(16)
  square_root(10)
  square(4)
  square(5.25)
  cube(3)
  cube(-3)
  sine(90)
  sine(0)
  cosine(90)
  cosine(270)
  tangent(45)
  tangent(0)
  invert(4)
  invert(0.25)
  