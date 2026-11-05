from family import Family
from person import Person

p1 = Person("Sally", 55, "F")
p2 = Person("Arthur", 57, "M")
c1 = Person("Joel", 28, "M")
c2 = Person("Judy", 32, "F")
c3 = Person("Michael", 16, "M")
f1 = Family(p1, p2, c1, c2, c3)
print(f1)

p1 = Person("Jerry", 55, "M")
p2 = Person("Jane", 57, "F")
c1 = Person("Robert", 28, "M")
c2 = Person("Tanya", 32, "F")
f2 = Family(p1, p2, c1, c2)
print(f2)

print("f1 < f2:", f1 < f2)
print("f1 > f2:", f1 > f2)
print("f1 == f2:", f1 == f2)