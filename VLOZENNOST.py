s_1 = "ABC"
s_2 = "123"
s_3 = "*$%"
#перебор пароля, вложенность
new_1 = [n_1 + n_2 + n_3 for n_1 in s_1 for n_2 in s_2 for n_3 in s_3]
print(new_1)


# Вложенность внутри выглядит так:
# for n_1 in s_1:
#     for n_2 in s_2
#         for n_3 in s_3