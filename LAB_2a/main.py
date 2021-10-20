# 2.1 Вивід констант:
print("1st const: ", True)
print("2nd const: ", False)
print("3rd const: ", NotImplemented)

# 2.2 Вивід за допомогою вбудованих функцій:
print("35 in hex system: ", hex(35))
print("2 to the power of 4: ", pow(2,4))
print("Finding max number of 4,2,1,6,3 :",max(4,2,1,6,3))


# 2.3 Вивід результатів роботи циклу та розгалуження
x= [1 for i in range(10)]
print(x)

a=7
print("A equals 7" if a == 7 else "A not equals 7")

# 2.4 Вивід результату роботи `try`->`except`->`finally`:
y=[3,8]
print("Print fifth element of the array[]?: ")
try:
    print(y[5])
except Exception as e:
    print(e)
finally:
    print("We got it finnaly")


# 2.5 Вивід результату роботи контекст-менеджера `with`:
i=1
with open("README.md", "r") as file:
    for line in file:
        print("Row " + str(i) + ": " + line)
        i=i+1

# 2.6 Вивід результату роботи з `lambdas`:
new_lambda = lambda first_number, second_number: f'Sum= {first_number + second_number}'
print("Lambda`s location in memmory: ", new_lambda)
print("Call lambda: ", new_lambda(5, 6))
