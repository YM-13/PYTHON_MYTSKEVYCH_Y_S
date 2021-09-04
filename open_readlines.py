# 00:43:30  .readlines()!!! дает нам строку с информацией о разбивки на визуальные строки
# делает все символы видимыми, нарезку строк тоже (\n)

look = open("text_l_5.txt", "r", encoding="utf-8")
content = look.readlines()
print(content)
look.close()
