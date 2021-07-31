#Q1
'''s='w'
s1=s[0:2]
s2=s[-2:]
s3=s1+s2
if(len(s3)<=2):
    print("Empty String")
else:
    print(s3)
'''

#Q2
'''a=[10,20,30,40,50]
print(max(a))'''

#Q3
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)'''

#operators

#Q1
'''radius = float(input("Enter radius:"))
pi = 3.14
Area = pi * radius * radius
print("Area = " + str(Area))'''

#Q2
'''a= int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)'''
#Q3
'''from datetime import date
d1 = date(2014, 7, 2)
d2 = date(2014, 7, 11)
result = d2 - d1
print(result.days)'''

#Q4
'''def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))'''
#Q5
'''def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))'''
#Q6
'''num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("Odd number")
else:
    print("Even Number")'''

#LOOPs
#Q1
'''a=[10,20,30,40]
res=''
for i in a:
    res+=str(i)
print(res)'''
#Q2
'''c1 = set(["White", "Black", "Red"])
c2 = set(["Red", "Green"])
print(c1.difference(c2))'''

#Functions
#Q1
'''def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print(gcd(10,5))'''
#Q2
'''def func(a,b):
    res=a+b
    return(res**2)
print(func(4,3))'''

#classes and OOPS
#Question-1
'''class Country():
  AVG_POPULATION=192
  def _init_(self,country_name,country_code):
    try:
      if type(country_name) == str and type(country_code) == str and len(country_code)==3:
        self.country_name=country_name
        self.country_code=country_code
      else:
        raise ValueError('Enter a string.')
    except ValueError :
      print("Please Enter the proper value")

  def country_short_form(self,countryName):
    if (type(countryName)== str and len(countryName)>=2):
      shortName=countryName[0]+countryName[1]
      return shortName.upper()
    else:
      return "Provide the proper country name"

  @classmethod
  def is_densly_populated(cls,population):
    if (type(population)== int):
      if(population > cls.AVG_POPULATION):
        return True
      else:
        return False
    else:
      print("please enter the numeric value")

  @staticmethod
  def world_avg_population(array):
    try:
      if(len(array)>0):
        sum=0
        for i in array:
          sum=sum+i
        return (sum/len(array))
      else:
        print("Enter appropriate array")
    except:
      print("Enter the list of integer values")
  
  @property
  def formatted_country_name(self):
    return "{0} ( {1} )".format(self.country_name,self.country_code)
  
  #Getters
  def get_country_name(self):
    return self.country_name

  def get_country_code(self):
    return self.country_code

  #setters
  def set_country_name(self,country_name):
    try:
      if type(country_name) == str:
        self.country_name=country_name
      else:
        raise ValueError('Enter a string.')
    except ValueError :
      print("Please provide the string value")
  
  def set_country_code(self,country_code):
    try:

      if type(country_code) == str and len(country_code)==3:
        self.country_code=country_code
      else:
        raise ValueError('Enter a string.')
    except ValueError :
      print("Please Enter the proper value")

  #deleters
  def del_country_name(self):
    print("Deleted country_name property")
    del self.country_name

  def del_country_code(self):
    print("Deleted country_code property")
    del self.country_code'''
#Q2
'''import math

class Shape:
    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Rectangle(Shape):

    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_area(self):
        return self.__length * self.__breadth


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


r1 = Rectangle(10.5, 2.5)

print("Area of rectangle r1:", r1.get_area())
print("Perimeter of rectangle r1:", r1.get_perimeter())
print("Color of rectangle r1:", r1.get_color())

c1 = Circle(12)
print("\nArea of circle c1:", format(c1.get_area(), "0.2f"))
print("Perimeter of circle c1:", format(c1.get_perimeter(), "0.2f"))
print("Color of circle c1:", c1.get_color())

'''

#Exceptions
#Q1
# KeyboarInterrupt Exception
"""try:
    inp = input()
    print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')"""
#ZeroDivisionError
'''try:  
    a = 100 / 0
    print (a)
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
else:  
    print ("Success, no error!")'''
#Attribute Error
'''class Attributes(object):
    a = 2
    print (a)

try:
    object = Attributes()
    print (object.attribute)
except AttributeError:
    print ("Attribute Exception Raised.")
'''
#lookup Error
'''try:  
    a = {1:'a', 2:'b', 3:'c'}  
    print (a[4])  
except LookupError:  
    print ("Key Error Exception Raised.")
else:  
    print ("Success, no error!")

'''
#NameError
'''try:
    print (ans)
except NameError:  
    print ("NameError: name 'ans' is not defined")
else:  
    print ("Success, no error!")'''

#Q2
'''class Person:
  def __init__(self, name, age,email,phone):
    self.name = name
    self.age = age
    self.email=email
    self.phone=phone

p1 = Person("John", 36,"john@gmail.com","9920987620")
import re
class NameException(Exception,p1):
    try:
        regex_name = re.compile(r'^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$',re.IGNORECASE)
        res = regex_name.search(p1.name)
        if res:
            print("Valid")
    except:
        print("Invalid Name")'''
#Regex 
import re 
if re.search('(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},\s+\d{4}',"28 June 2021"):
    print("True")
else:
    print("False")
#Q1
'''import re
date="June 03,2007"
pattern=(('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\.)?(\w*)?(\.)?(\s*\d{0,2}\s*),(\s*\d{4})', re.S + re.I).findall('Some wrong date is Septeme 28, 2002date') + ['n/a'])[0]
res=re.match(pattern,date)
if res:
    print("true")
else:
    print("false")
'''
#Decorator
'''import timeit

def timer(function):
  def new_function():
    start_time = timeit.default_timer()
    function()
    elapsed = timeit.default_timer() - start_time
    print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
  return new_function()

@timer
def addition():
  total = 0
  for i in range(0,1000000):
    total += i
  return total'''

#Modules
#Q1
'''import math   
a = math.pi / 6
print ("The value of sine of pi / 6 is : ", end ="") 
print (math.sin(a)) '''

#Q2
''''import city
city.city_name("Mumbai")
city.city_code("401107")'''

#Packages
#Q1
import json
#converts python object into json object
'''student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
           "102":{"class":'V', "Name":'David',  "Roll_no":8},
           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}
print(json.dumps(student))

#converts python sring to json string
string1 = 'Python and JSON'
print(json.dumps(string1))'''

# Serializing JSON and writing JSON file
'''details = {
        "name": "Felix Maina",
        "years": 21,
        "school": "Makerere"
}
with open("details.json", "w") as file_object:
    print(json.dump(details, file_object))'''

#Q2
'''import Animal.appearance,Animal.habitat
Animal.appearance.eye_color()
Animal.appearance.color()
Animal.habitat.type()
Animal.habitat.kingdom()'''
#File Handling
#Q1
'''f=open("file.txt","w")
f.write("This is the write command")
f=open("file.txt","a")
f.write("Add new line ")
f=open("file.txt","r")
print(f.read())

'''
#Q2
'''import csv
filename = "addresses.csv"
fields = []
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))
print('Field names are:' + ', '.join(field for field in fields))
  
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s"%col),
    print('\n')
#write operation
rows=[['peter','skstone','PD','202025']]
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
for row in rows[:5]:
    for col in row:
        print("%10s"%col),
    print('\n')'''