from FieldElement import FieldElement

a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)
print(a == b)
print(a == a)
print(FieldElement.__add__(a,b) == c)
