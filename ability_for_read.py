# 00:48:00 print  заканчивается всегда \n, а у нас итак \n был вписан, поэтому мы его просим
# "end=" пожалуйста, ничего сам не делай, у нас достаточно переходов на новую строку

look = open("text_l_5.txt", "r", encoding="utf-8")

for i in look:
    print(i, end="")

look.close()

# ----------------------- list comprehentios ------------------

look = open("text_l_5.txt", "r", encoding="utf-8")
cont = [i for i in look]

print(cont)

look.close()