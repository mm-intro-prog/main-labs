class Person:
    name = ''
    age = 0

    def say_name_and_age(self):
        print("Hello, my name is " + name + " and I'm " + str(age) + " years old.")

    def say_hello(self):
        print("Hello!")

print
print("Make a new person and say name and age:")
person1 = Person()
person1.say_name_and_age()

print
print("Set the name and age, then say the name and age again:")
person1.name = "Buffy"
person1.age = 16
person1.say_name_and_age()

print
print("Make another person and say name and age:")
person2 = Person()
person2.name = "Willow"
person2.age = 15
person2.say_name_and_age()

print
print("Just say hello:")
person1.say_hello()
