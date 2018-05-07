"""
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
"""
from math import sqrt

def main(number):
    if(checkIfPrime(number)):
        print("Prime")
    else:
        print("Not Prime")
    
def checkIfPrime(number):
    return [x for x in range(2,(int)(sqrt(number))) if(number%x==0)]

main(512)