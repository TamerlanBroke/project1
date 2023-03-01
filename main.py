color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")
if (color1 == "красный" or color2 == "красный") and (color1 == "синий" or color2 == "синий"):
    print("фиолетовый")
elif (color1 == "красный" or color2 == "красный") and (color1 == "желтый" or color2 == "желтый"):
    print("оранжевый")
elif (color1 == "синий" or color2 == "синий") and (color1 == "желтый" or color2 == "желтый"):
    print("зеленый")
elif color1 == color2 and (color1 == "синий" or color1 == "красный" or color1 == "желтый"):
    print(color1)
else:
    print("Ошибка в выборе цветов")