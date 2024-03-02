#samra ahmed
#samraaed3291@gmail.com
#Q1
#find the even number

num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")
    #to create multiplication table
    num = int(input("Enter a number: "))
print("Multiplication Table for", num)
for i in range(1, 11):
    print(num, "×", i, "=", num*i)
    
# To make Fizzbuzz Game 
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# To create Palindrome checker
word = input("Enter a word or phrase: ").lower()
reversed_word = word[::-1]
if word == reversed_word:
    print("Palindrome!")
else:
    print("Not a palindrome.")
# To create factorial checker
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, ":", factorial)
    
  # to create sum of digits
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    sum_of_digits += num % 10
    num //= 10
print("Sum of digits:", sum_of_digits)

# to create Prime number checker
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
    
 # to make Guess the word game
import random
words = ['python', 'java', 'ruby', 'javascript', 'swift', 'csharp']
word_to_guess=random.choice(words)
guessed_word = ['_' for _ in word_to_guess]

print("Welcome to Guess the Word Game!")
print(" ".join(guessed_word))

while '_' in guessed_word:
    letter = input("Guess a letter: ").lower()
    if letter in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == letter:
                guessed_word[i] = letter
        print(" ".join(guessed_word))
    else:
        print("Incorrect guess. Try again.")

print("Congratulations! You guessed the word:", word_to_guess)