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



file = open("expenses.txt", "w")
for expense in expenses:
    file.write(expense["category"] + " - " + str(expense["amount"]) + "\n")
file.close()