"""code1
def greet(name):
    print("hello " + name + " lets build something")

greet("Bhavana")


for a in range(1, 11):
    if a % 2 != 0:
        print(a)



#code2
cities = {
    "Bangalore": "Karnataka",
    "Mumbai": "Maharashtra",
    "Chennai": "Tamil Nadu"
}
for city in cities:
    print(city)



#code3
friends = {"Bhavana": 22, "Priya": 25, "Raj": 20}
for friend, age in friends.items():
  if age>21:
        print(friend+ " is " +str(age)+ " years old ")
    
movies= ["notebook", "batman","frozen", "joker", "dune"]
for movie in movies:
    if len(movie) > 5:
     print(movie)
"""

#code4
numbers = [45, 23, 67, 12, 89]
print(len(numbers))   
print(sum(numbers))   
print(max(numbers))   
print(min(numbers))   