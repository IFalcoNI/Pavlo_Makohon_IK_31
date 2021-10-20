# **Лабораторна робота №2А**

---

## Послідовність виконання лабораторної роботи:

#### 1. Переглянув офіційну документацію для **_Python_**.

#### 2. Створив файл **_main.py_** для виконання прикладів.

1. Вивід констант:

```python
print("1st const: ", True)
print("2nd const: ", False)
print("3rd const: ", NotImplemented)
```

2. Вивід за допомогою вбудованих функцій:

```python
print("35 in hex system: ", hex(35))
print("2 to the power of 4: ", pow(2,4))
print("Finding max number of 4,2,1,6,3 :",max(4,2,1,6,3))
```

3. Вивід результатів роботи циклу та розгалуження

```python
x= [1 for i in range(10)]
print(x)
a=7
print("A equals 7" if a == 7 else "A not equals 7")
```

4. Вивід результату роботи `try`->`except`->`finally`:

```python
y=[3,8]
print("Print fifth element of the array[]?: ")
try:
    print(y[5])
except Exception as e:
    print(e)
finally:
    print("We got it finnaly")
```

5. Вивід результату роботи контекст-менеджера `with`:

```python
i=1
with open("README.md", "r") as file:
for line in file:
    print("Row " + str(i) + ": " + line)
    i=i+1
```

6. Вивід результату роботи з `lambdas`:

```python
new_lambda = lambda first_number, second_number: f'Sum= {first_number + second_number}'
print("Lambda`s location in memmory: ", new_lambda)
print("Call lambda: ", new_lambda(5, 6))
```

#### 3. Створив такі файли:

```text
LAB_2a/
├── modules/
│   └── common.py
├── __init__.py
└── __main__.py
```

1.  Перейшовши у папку з даними файлами запустив виконання програми цією командою:

    ```sh
    python3 .
    ```

    Виконання команди:

    ```text
    falcon@Makohons-MBP LAB_2a % python3 .
    We are in the __main__
    2021-10-20 19:12:21.894883
    darwin
    test

    ```

1.  Після запуску команди `python3 .` програма в першому рядку виводить назву файла який виконувався, в другому рядку виводиться час і дата виконання даної програми, в третьому рядку виводиться ос на якій було запущено програму і в четвертому рядку виведено текст "test".

    a. Після запуску команди: `python3 . -h` в консоль виводиться інформація про додаткові параметри та їх використання. Результат виконання команди:

    ```text
    falcon@Makohons-MBP LAB_2a % python3 . -h
    usage: . [-h] [-o OPT] [-l]

    Приклад передачі аргументів у Python програму.

    optional arguments:
     -h, --help            show this help message and exit
     -o OPT, --optional OPT
                        Цей параметр є вибірковим.
     -l, --logs            Якщо виконати команду з цим параметром будуть виводитись логи.
    ```

    b. Після запуску команди: `python3 . -o "Цей текст також має вивестись"` в консоль виводиться інформація така сама як і в пункті 2. тільки додається текст про те що з консолї було передано аргумент і саме повідомлення яке ми передаємо. Результат виконання команди:

    ```text
    falcon@Makohons-MBP LAB_2a % python3 . -o "Цей текст також має вивестись"
    We are in the __main__
    2021-10-20 19:15:25.634435
    darwin
    З консолі було передано аргумент
     ========== >> Цей текст також має вивестись << ==========
    test
    ```

    c. Дитально ознайомився з аргументами.
    d. Ознайомився з логуванням і запустив команду `python3 . --logs`.
    Результат виконання команди:

    ```text
    falcon@Makohons-MBP LAB_2a % python3 . --logs
    2021-10-20 19:16:00,971 root INFO: Тут буде просто інформативне повідомлення
    2021-10-20 19:16:00,971 root WARNING: Це Warning повідомлення
    2021-10-20 19:16:00,971 root ERROR: Це повідомлення про помилку
    test
    ```

1.  Створив власну функцію у файлі `common.py` яка буде виводить всі парні числа від 0 до 100, якщо у функцію передати значення True і непарні якщо значення False. Виклик цієї функцію виконую з `__main__` .
    Код власної функції:
    ```python
    def filtr_number(filtr):
    numbers = range(0, 101)
    if filtr == "True":
    output = "Even number: "
    elif filtr == "False":
    output = "Odd number: "

        for num in numbers:
            if (filtr == "True") & (num % 2 == 0):
                output += str(num) + " "
            elif (filtr == "False") & (num % 2 != 0):
                output += str(num) + " "
        return output
        ```
        Результат виконання з параметром `-o True`:
        ```text
        falcon@Makohons-MBP LAB_2a % python3 . -o True
        We are in the __main__
        2021-10-20 19:25:08.672916
        darwin
        Even number: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100
        З консолі було передано аргумент
        ========== >> True << ==========
        test
        ```
        Результат виконання з параметром `-o False`:
        ```text
        falcon@Makohons-MBP LAB_2a % python3 . -o False
        We are in the __main__
        2021-10-20 19:25:22.313023
        darwin
        Odd number: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99
        З консолі було передано аргумент
        ========== >> False << ==========
        test
        ```

1.  Створив функцію яка може виконуватись з помилкою. У випадку її виникнення виводить `ERROR` повідомлення за допомогою логування використовуючи бібліотеку `logging`.
    Якщо функція виконалася без помилки то виводить `INFO` повідомлення.
    Код функції:
    `python def view_array(): x = [1, 2, 3, 4] print("Масив X[]:", x) index = int(input("Enter number of element: ")) try: print(f"X[{index}] = {x[index]}") except IndexError: logging.error("Out of range") else: logging.info("Correct!!!") `
    Результат виконання з помилкою:
    `text falcon@Makohons-MBP LAB_2a % python3 . We are in the __main__ 2021-10-20 19:34:40.169469 darwin Масив X[]: [1, 2, 3, 4] Enter number of element: 5 2021-10-20 19:34:42,772 root ERROR: Out of range test `
    Результат виконання без помилки:
    `text falcon@Makohons-MBP LAB_2a % python3 . We are in the __main__ 2021-10-20 19:35:14.214831 darwin Масив X[]: [1, 2, 3, 4] Enter number of element: 1 X[1] = 2 2021-10-20 19:35:15,951 root INFO: Correct!!! test `
