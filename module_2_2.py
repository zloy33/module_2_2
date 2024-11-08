first = int(input("number_1: "))
second = int(input("number_2: "))
third = int(input("number_3: "))
if first != second and first != third and second != third:
    print(0)
if first == second and first == third and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
