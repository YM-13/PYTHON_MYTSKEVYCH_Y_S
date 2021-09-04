#  00:56:00
# "wirelines" как "writ" но еще, он позволяет записывать в файл список, который
# содержит "строковые значения"
look = open("wl_text_l_5_(w_....).txt", "w", encoding="utf-8")
look.writelines([f"{[1, 2, 3, 4]}\n{2, 3, 4, 5}\nPy py\n", "Python python\n"])
look.close()
