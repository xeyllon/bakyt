class Car:
    color = ["black", "white", "pink"]
    wheels_count = 4
    
bmw = Car()
audi = Car()

print(bmw.color)
print(bmw.wheels_count)

bmw.color = "white"
audi.speed = 300

print(bmw.color)
print(audi.speed)

print("class", Car.__dict__)
print("bmw", bmw.__dict__)
print("audi", audi.__dict__)
