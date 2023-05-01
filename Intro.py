print("Hi guys,I am Monish")
#Basic print syntex.
print("Hi guys,I am monish")
print("monish")

#numbers is of three types.....they are integers,complex,flot
#can do mathametical problem in the print space
print(10)

# Variable : common usage term availed for multiple function
Mobile=10000
print(Mobile)
Name='Monish'
print(Name,Mobile)

# Creating Invoice
Mobile1,Mobile2,Mobile3=100,200,300
Custemer_name='Monish'
print(Mobile3)
print(Custemer_name)

#Strings : comprising aplphabets,numerics,special charecters
#Condition : use (' ') (" ")
string="By next year I am going to turn 31"
print(string)

#Creating Paragraph : use keyword "para" and closing with 3" like (""" """)
para="""          this
is
my
laptop.
i will not give it to any one      """
print(para)

#Intro of ARRAY
#printing of exact positioning of a letter in a word
#0,1,2,3,4,5........
Word1='Brilliant'
print(Word1[5])

#Slicing : cutting needed words among the input
print(Word1[1:4])

#Calculating LENGTH of th sttring
print(len(para))

#Strip : Removing space between the sentence
print(para)

#upper() : change into capital letters
print(Word1.upper())

#lower () : change in to lower
print(Word1.lower())

#Replace : replacing missing letter with the mistaken word
Mistaken_word="Monish kumar"
print(Mistaken_word.replace('r','r N'))

#split : splitting the existing words with needable space
print(Mistaken_word.split('ish'))

#Boolean datatype : find keyword in the paragraph,using key function "in"
Find_para="this is the best place to explore my ability,which grow my IQ level"
print('expore'in Find_para)

print(1==2-0)
#Casting : changing in to Float/Integer
Number1=float(12)
Number2=int(12.1)
print(Number1,Number2)

#list : giving different items under one heading
Relation=['father','mother','brother','sisterinlaw']
print(Relation[0])
print(Relation)
#append : adding item to the existing list
Relation.append('daughter_in_law')
print(Relation)

#Tuples : it is like list.but it cannot be changed thier items.
#their difference is their bracket ; ()
Relation2=('father','mother','brother','sisterinlaw')
print(Relation2)

Relation3={'father','mother','brother','sisterinlaw'}
print(Relation3)
Relation3.add("daughter_in_law")
print(Relation3)

#Dictionary  : storing data (key and their value)
My_data={"name":"Monish","age":31}
print(My_data.get("age"))

##if , elif , else statement : providing if condition for the statement
Age = 31
if Age > 18:
    print('You can fuck in upcomming night')
elif Age == 18:
    print("Now you can apply for tinder ID")
else:  print("Wait for a while to turn 18")

#Another example for if statement
Monish = 'Nallavan'
if Monish == "kettavan":
    print("Thappu")
else:
    print('sokka sonnapa ne')

#using And , or statement in if statement         #Nesting of if statement
Hungry,Not_Hungry = 'Tea',"mooditu_poda"
if Hungry == 'Tea' and Not_Hungry == 'mooditu_poda':
    print('sariyaga_sonneergal')
    if Hungry == "Tea":
            print('Setha porunga potu tharen')
else:
    print('Innoruvati sariyanu parupu')

#Functions : can use keyfunction repatedly without writing the whole code
def Multiply():
    a = 10
    b = 20
    print(a * b)
 #Calling function
Multiply()
#another example of function
def Mr(Monish1):
    print("welcome,"+Monish1)
Mr("Monish1'Monish1'")

#another function (return)
def fun(a):
    return a+500
print(fun(50))

#Loop : types---1.for loop
        #sequential traversal of list or string or array
Menu = ('dosa','poori','idly','pongal')
dosa = ('masal_dosai','podi_dosa','nei_dosa')
for item in Menu:
    if item == 'dosa':
        print("dosa is available")
        for item in dosa:
            if item == 'podi_dosa':
                print('podi_dosa is available')


    #Range in loop :Ex-5 ;0,1,2,3,4
for Num1 in range(10,100,10):
    print(Num1)

# While loop :
n = 1
while n < 10:
    print(n)
    n += 1

#Lambda : single line code for different usage
Add_Num = lambda Number: Number + 100
print(Add_Num(55))