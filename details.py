
class Person:
    def __init__(person, name,age, houseN, stName):
        person.name = name
        person.age = age
        person.housen = houseN
        person.stName = stName
#ask for the respective inputs, name , age, house Number and street Name
ps = Person(input("Your Name: "),input("Your age: "), input("House Number: "), input("Street Name: "))
#print all gathered details
print("This is " + ps.name + " He is " + ps.age + " years old and lives at house number " + ps.housen + " on " + ps.stName)