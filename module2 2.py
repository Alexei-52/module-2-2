first = (123)
second = (456)
third = (789)
if first == second and second == third:
    print(first,second,third)
elif first == second:
    print(first,second)
elif second == third:
    print( second,third)
elif first == third:
    print(first,third)
else:
    print(0)

