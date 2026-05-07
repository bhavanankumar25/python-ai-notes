#code1

expenses= []
def add_expense(cat,amt):
   expense = {"category": cat, "amount": amt}
   expenses.append(expense)

add_expense("food", 300)
add_expense("cab", 100)
add_expense("shop", 500)

tot=0
for expense in expenses:
   tot+= expense["amount"] 

print("total amount: ", tot)



#code2

students = {"a":56, "b":75, "c":65, "d":97, "e":93}
for student, marks in students.items():
    if marks>=90:
        print(student + " : "+ str(marks)+ " - distiction")
    elif marks>=75:
       print(student +" : "+  str(marks)+ " - frst class")  
    elif marks>=60:
     print(student +" : "+  str(marks)+ " - second class")   
    else:  
       print(student +" : "+  str(marks)+ " - fail")  




#code3

name = input("Enter your name: ")
weight = float(input("Enter weight in kg: "))
height =float(input("Enter height in m: ")) 
calc=  weight / (height * height)
if calc<18.5:
   print(name+ " your BMI is " + str(round(calc,2))+ " underweight")
elif calc<=24.9:
   print(name+ " your BMI is " + str(round(calc,2))+ " normal")
elif calc<=29.9:
   print(name+ " your BMI is " + str(calc)+ " overweight")
else:
   print(name+ " your BMI is " + str(calc)+ " obese")
