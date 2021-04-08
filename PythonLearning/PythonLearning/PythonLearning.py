# REMEMBER INDENTING FOR PYTHON, NO NEED FOR SEMI COLONS IN PY

#PRINTING

'''
Names are case-sensitive and may begin with:
   letters, $, _
After, may include
   letters, numbers, $, _
Convention says
   Start with a lowercase word, then additional words are separated
   by underscores
   ex. my_first_variable
'''


print("!")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

#VARIABLES

name = "Mike"    # Strings
age = 30         # Integer
gpa = 3.5         # Decimal
is_tall = True    # Boolean -> True/False


print( int(3.14) )
print( float(3) )
print( str(True) )
print( int("50") + int("70") )


character_name = "George"
character_age = "70"

print("There once was a man named " + character_name)
print("He was " + character_age + " years old")

character_age = "80"

print("He really liked the name " + character_name)
print("But didn't like being " + character_age)


greeting = "Hello"
#indexes:   01234

print( len(greeting) )
print( greeting[0] )
print( greeting[-1] )
print( greeting.find("llo") )
print( greeting.find("z") )
print( greeting[2:] )
print( greeting[2:3] )

#MATH


print( 2 * 3 )       # Basic Arithmetic: +, -, /, *
print( 2**3 )        # Basic Arithmetic: +, -, /, *
print( 10 % 3 )      # Modulus Op. : returns remainder of 10/3
print( 1 + 2 * 3 )   # order of operations
print(10 / 3.0)      # int's and doubles


num = 10
num += 100 # +=, -=, /=, *=
print(num)

++num
print(num)

# Math module has useful math methods
import math #should be done at start
print( pow(2, 3) )
print( math.sqrt(144) )
print( round(2.7) )

#simple calculator

num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
print(num1 + num2)

#better calculator

num1 = int(input("num1: "))
op = input("Operator: ")
num1 = int(input("num1: "))

if op == "+":
     print(num1 + num2)
elif op == "-":
     print(num1 - num2)
elif op == "/":
     print(num1 / num2)
elif op == "*":
     print(num1 * num2)
else:
     print("Invalid Operator")



#EXPONENT FUNCTION


def raise_to_power(base_num, pow_num):
     result = 1
     for index in range(pow_num):
          result *= base_num
     return result


#MADLIB

color = input("Enter a color: ")
pluralNoun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are", color)
print(pluralNoun + " are blue")
print("I love", celebrity)

#LIST

friends = []
friends.append("Oscar")
friends.append("Angela")
friends.insert(1, "Kevin")

# friends.remove("Kevin")
print( friends )
print( friends.index("Oscar") )
print( friends.count("Angela") )
friends.sort()
print( friends )
friends.clear()
print( friends )


#2D Array / LIST


number_grid = [ [1, 2], [3, 4] ]

number_grid[0][1] = 99
print(number_grid[0][0])
print(number_grid[0][1])

for row in number_grid:
     for row in col:
          print(col)



#TUPLES


lucky_numbers = (4, 8, "fifteen", 16, 23, 42.0)
#      indexes  0  1       2      3   4   5

# lucky_numbers[0] = 90  # tuples are immutable
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[-1])
print(lucky_numbers[2:])
print(lucky_numbers[2:4])
print(len(lucky_numbers))

#FUNCTIONS

def sayHi(name):
    print("Hello " + name + " you are " + str(age))

sayHi("Mike", 24)

#return statement


def add_numbers(num1, num2=99):
     return num1 + num2

sum = add_numbers(4, 3)
print(sum)

#IF STATEMENTS


is_student = False
is_smart = False

if is_student and is_smart:
	print("You are a student")
elif is_student and not(is_smart):
	print("You are not a smart student")
else:
	print("You are not a student and not smart")


# >, <, >=, <=, !=, ==
if 1 > 3:
	print("number omparison was true")


if "dog" == "cat":
   print("string omparison was true")


#WHILE

index = 1
while index <= 5:
  print(index)
  index += 1


#DO WHILE

index = 1
while True:
  print(index)
  index += 1
  if index > 5:
    break;


#FOR

for index in range(5):
    print(index)

lucky_nums = [4, 8, 15, 16, 23, 42]
for lucky_num in lucky_nums:
    print(lucky_num)

for letter in "Giraffe":
    print(letter)



#DICTIONARIES


test_grades = {
    "Andy" : "B+",
    "Stanley" : "C",
    "Ryan" : "A",
    3 : 95.2
}

print( test_grades["Andy"] )
print( test_grades.get("Ryan", "No Student Found") )
print( test_grades[3] )


#GUESSING GAME 


secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
     if guess_count < guess_limit:
          guess = input("Enter a guess: ")
          guess_count += 1
     else:
          out_of_guesses = True

if out_of_guesses:
     print("You Lose!")
else:
     print("You Win!")



#TRANSLATOR FUNCTION


def translate(phrase):
     translation = ""
     for letter in phrase:
          if letter.lower() in "aeiou":
               if letter.isupper():
                    translation = translation + "G"
               else:
                    translation = translation + "g"
          else:
               translation = translation + letter
     return translation


 #TRY CATCH

 
# code asks user for number and divides 10 by it
# enter '0' to trigger exception
try:
    answer = 10 / int(input("Enter Number: "))
except ZeroDivisionError as e:
    print(e)
except:
    print("Caught any exception")



# READ FILE


employee_file = open("employees.txt", "r")

for employee in employee_file.read_lines():
     print(employee)

employee_file.close()


# WRITE FILE


employee_file = open("employees.txt", "w") # also try "a" for append

employee_file.write("\nKelly - Customer Service")

employee_file.close()


#MODULES


import module_name
import module2_name as module2


#CLASSES AND OOP

class Book:
  def __init__(self, title, author, numPages):
      self.title = title
      self.author = author
      self.numPages = numPages

book1 = Book("Harry Potter", "JK Rowling", 500);
# book1.title = "Half-Blood Prince"

print(book1.title)

#QUIZ FUNCTION



class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What color are apples?\n(a) Red/Green\n(b)Orange",
     "What color are bananas?\n(a) Red/Green\n(b)Yellow",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)


# CLASS METHODS / OBJECT FUNCTIONS



class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def has_honors(self):
         if self.gpa >= 3.5:
               return True
         return False



#INHERITANCE


class Chef:
   def make_chicken(self):
       print("The chef makes chicken")

   def make_salad(self):
       print("The chef makes salad")

   def make_special_dish(self):
       print("The chef makes bbq ribs")

class ItalianChef(Chef):
   def make_pasta(self):
       print("The chef makes pasta")

   def make_special_dish(self):
       print("The chef makes chicken parm")


myChef = Chef()
myChef.make_chicken()

myItalianChef = ItalianChef()
myItalianChef.make_chicken()



# OPT FOR LIVE CODING PYTHON INTO UNIX SHELL => SEE "PYTHON INTERPRETER" 

















