for i in range(5):
    print("Hello World!")
    print("current number in the sequence : ", i)

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(10))

for i in range(10):
    if i == 5:
        continue
    print(i)
        
person = ("n", 6)
print(person)
print("Name : ", person[0])
print("Age : ", person[1])

names = ["Alice", "BoB", ]
print(names)


names.append("h")
print(names)

for name in names:
    print(name)

people = [("Alice",25),("Bob",30)]
first_person = people[0]

print(first_person)

for person in people:
    name = person[0]
    age = person[1]
    print(f"Name : {name}, Age: {age}")

names_set = {"m", "u", "e"}
print(names_set)

names_set.add("er")
print(names_set)

names_set.remove("m")
print(names_set)

for name in names_set:
    print(name)