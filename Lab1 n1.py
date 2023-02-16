pas1 = input('Введите пароль:')

numeric = False
upper = False
lower = False
spec = False

for char in pas1:
    if char.isnumeric():
        numeric = True
    elif char.islower():
        lower = True
    elif char.isupper():
        upper = True
    elif char in "@#$%&?!":
        spec = True
if len(pas1) >= 6 and numeric and upper and lower and spec:
    print("Пароль подходит")
else:
    print("Усложните пароль")
pas2 = input('Введите пароль:')
while pas1 != pas2:
    print('Пароли не совпадают')
    pas2 = input("Попробуйте снова")
print("Пароли совпадают")