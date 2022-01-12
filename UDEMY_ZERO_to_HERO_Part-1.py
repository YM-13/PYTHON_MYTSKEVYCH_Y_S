# d = {'year': 2021}
# d['month'] = 12
# d['day'] = 18
# print(d)
#################################################################################

# print(set('Mississippi'))

#################################################################################
# d = {'year': 2021}
# d['month'] = 12
# d['day'] = 18
# print(d)
#################################################################################
# with open('test.txt, mode= w') as f:
#     f.write('Hello World')
# print(f)
#################################################################################

# print(['1'])
#
# my_list = [1]
# my_list.append('two')
# my_list = my_list + [3.14159]
# print(my_list)
#################################################################################
# print(not 1 == 1)
#
# print(2 <= 3 >= 1)
#################################################################################
# mylist = [1,2,3,4,5,6,7,8,9,10]
# list_sum = 0
# for num in mylist:
#     list_sum = list_sum + num
# print(list_sum)
#################################################################################
# mylist = [1, 2, 3]
#################################################################################
# for num in range(3, 10, 2):
#     print(num)
#################################################################################
# result = input('TOTOSHKA: ')
# print(result)
#################################################################################
# mystring = 'hello'
# mylist = [num**2 for num in range(0, 11) if num % 2 ==0]
# # for letter in mystring:
# #     mylist.append(letter)
# print(mylist)
#################################################################################
# celcius = [0, 10, 20, 34.5]
# #fahrenheit = [ ( (9/5)*temp + 32) for temp in celcius]
# fahrenheit = []
# for temp in celcius:
#     fahrenheit.append(((9/5)*temp + 32))
# print(fahrenheit)
#################################################################################
# result = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
# print(result)
#################################################################################
# mylist = []
# for x in [2, 4, 6]:
#     for y in [100, 200, 300]:
#         mylist.append(x * y)
# print(mylist)
#################################################################################
# mylist = [x*y for  x in [2, 4, 6] for y in [100, 200, 300]]
# print(mylist)
#################################################################################
# st = 'Print only the words that start with s in this sentence'
# st = st.split()
# mylist = []
# for word in st:
#     if word[0] == 's':
#         mylist.append(word)
# print(mylist)
#################################################################################
# st = 'Print only the words that start with s in this sentence'
# for word in st.split():
#     if word[0] == 's':
#         print(word)
# mylist = [num for num in range(0, 11) if num % 2 == 0]
# print(mylist)
#################################################################################
# print(list(range(0, 11, 2)))
#################################################################################
# mylist = [num for num in range(1, 51) if num % 3 == 0]
# print(mylist)
#################################################################################
# print([num for num in range(1, 51) if num % 3 == 0])
#################################################################################
# st = 'Print every word in this sentence that has an even number of letters'
# st = st.split()
# for word in st:
#     if len(word) % 2 == 0:
#         print(word)
#################################################################################
# st = 'Print every word in this sentence that has an even number of letters'
# for word in st.split():
#     if len(word) % 2 == 0:
#         print(word + '-- has an even length')
#################################################################################
# st = 'Print every word in this sentence that has an even number of letters'
# print([word for word in st.split() if len(word) % 2 == 0])
#################################################################################
# for num in range(1, 101):
#     if num % 3 ==0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     elif num % 3 ==0 and num % 5 == 0:
#         print(FizzBuzz)
#     else:
#         print(num)
#################################################################################
# st = 'Create a list of the first letters of every word in this string'
# mylist = []
# for word in st.split():
#     mylist.append(word[0])
# print(mylist)
#################################################################################
# st = 'Create a list of the first letters of every word in this string'
# mylist = [word[0] for word in st.split()]
# print(mylist)
#################################################################################
# mylist = [1, 2, 3]
# help(mylist.insert)
#################################################################################
# def say_hello(name='Default'):
#     print(f'Hello {name}')
#################################################################################

# work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

# def employee_check(work_hours):
#     current_max = 0
#     employee_of_month = ''
#     for employee, hours in work_hours:
#         if hours > current_max:
#             current_max = hours
#             employee_of_month = employee
#     else:
#         pass
#
#     return (employee_of_month, current_max)
#
# result = employee_check(work_hours)
# name, hours, location = employee_check(work_hours)
#
# print(hours)
#################################################################################

# def myfunc(name):
#     print('Hello {}'.format(name))
# myfunc('Hose')
#################################################################################
# def myfunc(a):
#     if a == True:
#         return 'Hello'
#     elif a == False:
#         return 'Goodbye'
# result = myfunc(2 == 2)
# print(result)
#################################################################################
# def myfunc(x, y, z):
#     if z == True:
#         return x
#     if z == False:
#         return y
# result = myfunc(1, 3, 2 == 2)
# print(result)
#################################################################################
# def myfunc(a, b):
#     sum_num = a + b
#     return sum_num
# result = myfunc(2, 6)
# print(result)
#################################################################################

# def myfunc(*args):
#     # mylist = []
#     # for num in args:
#     #     if num % 2 == 0:
#     #         mylist.append(num)
#     #     else:
#     #         pass
#     # return mylist
#     mylist = [num for num in args if num % 2 == 0]
#     return mylist
#
# #result = myfunc(2, 3, 5, 90)
# print(myfunc(2, 3, 5, 90, 77, 80))
#################################################################################
# def myfunc(in_string):
#     mylist = [l for l in in_string]
#     mylist_out = [a.lower() if mylist.index(a) % 2 == 0 else a.upper() for a in mylist]
#     mylist_out = ''.join(mylist_out)
#
#     # mylist_out = []
#     # for a in mylist:
#     #     if mylist.index(a) % 2 == 0:
#     #         mylist_out.append(a.lower())
#     #     else:
#     #         mylist_out.append(a.upper())
#     # mylist_out = ''.join(mylist_out)
#
#     return mylist_out
# print(myfunc('Stradivary'))
#################################################################################

# def myfunc(in_string):
#     mylist = [l for l in in_string]
#     mylist_out = []
#     mylist_out = [a.lower() if mylist.index(a) % 2 == 0 else a.upper() for a in mylist]
#     return ''.join(mylist_out)
# print(myfunc('Stradivary'))
#################################################################################
# def myfunc(s): return ''.join(char.upper() if i % 2 else char.lower() for i, char in enumerate(s))
# print(myfunc('Stradivary'))
#################################################################################
# def myfunc(x):
#     out = []
#     for i in range(len(x)):
#         if i % 2 == 0:
#             out.append(x[i].lower())
#         else:
#             out.append(x[i].upper())
#     return ''.join(out)
#################################################################################
# Задание с гита
# def myfunc(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)
#
# print(myfunc(4, 7))
#################################################################################
# def myfunc(my_string):
#     my_string = my_string.split()
#     if my_string[0][0] == my_string[1][0]:
#         return True
#     else:
#         return False
#
# print(myfunc('Hello Helen'))
#################################################################################
# def makes_twenty(n1, n2):
#     if n1 + n2 == 20 or n1 == 20 or n2 == 20:
#         return True
#     else:
#         return False
# print(makes_twenty(20, 1))
#################################################################################
# def old_macdonald(my_string):
#     my_string = [l for l in my_string]
#
#     my_string[0] = my_string[0].upper()
#     my_string[3] = my_string[3].upper()
#     return ''.join(my_string)
#
# print(old_macdonald('macdonald'))
#################################################################################
# def old_macdonald(my_string):
#     my_string = my_string.capitalize()
#     my_string = [l for l in my_string]
#     my_string[3] = my_string[3].upper()
#     return ''.join(my_string)
#
# print(old_macdonald('macdonald'))
#################################################################################
# def revers_sentence(string_sentence):
#     string_sentence = string_sentence.split()
#     reverse_word_list = string_sentence[::-1]
#     return ' '.join(reverse_word_list)
# #    string_sentence = reversed(string_sentence.split())
# #    return ' '.join(string_sentence)
#
# print(revers_sentence('My love is it'))
#################################################################################
# def almost_there(n):
#     if 220 > n > 200 or n < 110:
#         return True
#     else:
#         return False
#
# print(almost_there(150))
#################################################################################
# def has_33(my_list):
#     fs = my_list[0]
#     for n in my_list[1:]:
#         if n == fs:
#             return True
#         else:
#             fs = n
#     return False
#
# print(has_33([3,1,3]))
#################################################################################
# def paper_doll(my_string):
#     my_string = [l for l in my_string]
#     new_string = ''.join([l * 3 for l in my_string])
#     return new_string
#
# print(paper_doll('Hello'))
#################################################################################
# def paper_doll(my_string): return ''.join([l * 3 for l in [l for l in my_string]])
# print(paper_doll('Hello'))
#################################################################################
# def blackjack(tp):
#     s = sum(tp)
#     if 21 == s or s < 21:
#         return s
#     elif s > 21
#
# print(blackjack((5,6,7)))
#################################################################################
# def blackjack(nums):
#     if sum(nums) <= 21:
#         return sum(nums)
#     elif sum(nums) > 21 and 11 in nums:
#         return sum(nums) - 10
#     else:
#         return 'BUST'
#
# print(blackjack((9, 9, 9)))
#################################################################################
# def spec_func(my_list):
#    # num_for_sum = []
#     if 6 in my_list:
#         a = my_list.index(6)
#         b = my_list.index(9) + 1
#         del my_list[a:b]
#     return sum(my_list)
#
#
# print(spec_func([2, 1, 6, 9, 11]))
#################################################################################
# def fined_007(my_list):
#     count_0 = 0
#     for n in my_list:
#         if n == 0:
#             count_0 +=1
#         else:
#             if n == 7 and count_0 == 2:
#                 return True
#         # else:
#         #     if count_0 > 0:
#         #         count_0 = 0
#     return False
#
# print(fined_007([1, 2, 4, 0, 0, 7, 5]))
# print(fined_007([1, 0, 2, 4, 0, 5, 7]))
# print(fined_007([1, 7, 2, 0, 4, 5, 0]))
#################################################################################
# def count_primes(n):
#     list_of_prime_num = []
#     couter_list = []
#     for i in range(2, n + 1):
#         for x in range(1, i + 1):
#             if i % x == 0:
#                 couter_list.append(x)
#         if len(couter_list) == 2:
#             list_of_prime_num.append(i)
#             couter_list = []
#         else:
#             couter_list = []
#     return f'{list_of_prime_num}\n{len(list_of_prime_num)}'
#
# print(count_primes(100))
#########################  55  ##################################################
# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return 'EVEN'
#     else:
#         return mystring[0]
# names = ['Andy', 'Eve', 'Sally']
# print(list(map(splicer, names)))
#################################################################################
# def check_even(num):
#     return num % 2 == 0
#
# mynums = [1, 2, 3, 4, 5, 6]
# print(list(filter(check_even, mynums)))
# for n in filter(check_even, mynums):
#     print(n)
###########  map + lambda    ######################################################
# mynums = [1, 2, 3, 4, 5, 6]
# m = list(map(lambda num: num ** 2, mynums))
# print(m)
###########  filter + lambda    ###################################################
# mynums = [1, 2, 3, 4, 5, 6]
# m = list(filter(lambda num: num % 2 == 0, mynums))
# print(m)
###########  filter + lambda + index - revers ######################################
# names = ['Andy', 'Eve', 'Sally']
# m = list(map(lambda x: x[::-1], names))
# print(m)
################  LEGB Rule  #######################################################
# GLOBAL
# name = 'THIS IS A GLOBAL STRING'
# def greet():
#     # ENCLOSING
#     #name = 'Sammy'
#
#     def hello():
#         # LOCAL
#         #name = 'I AM A LOCAL'
#         print('Hello ' + name)
#     hello()
#
# greet()
################  LEGB Rule  #######################################################
# x = 50
# def func(x):
#     print(f'X is {x}')
#     #LOCAL REASSIGNMENT
#     x = 200
#     print(f'I JUST {x}')
# func(x)
# print(x)
################  LEGB Rule  #######################################################
# x = 50
# def func():
#     global x
#     print(f'X is {x}')
#     #LOCAL REASSIGNMENT
#     x = '!!!NEW VALUE!!!'
#     print(f'I JUST CHANGE LOCAL TO GLOBAL X {x}')
# print(x)
# func()
# print(x)
################ !!! LEGB Rule !!! #################################################
# x = 50
# def func(x):
#     print(f'X is {x}')
#     #LOCAL REASSIGNMENT
#     x = '!!!NEW VALUE!!!'
#     print(f'I JUST CHANGE LOCAL TO GLOBAL X {x}')
#     return x
# #print(x)
# x = func(x)
# #print(x)
# ЗАДАНИЕ 57 #######################################################################
# def vol(rad): return 4 / 3 * 3.1415 * rad ** 3
# print(vol(2))
# ЗАДАНИЕ 57 #######################################################################
# def ran_check(num, low, high): return num in range(low, high+1)
# print(ran_check(3,1,10))
# ЗАДАНИЕ 57 #######################################################################
# def up_low(s):
#     l_c = 0
#     h_c = 0
#     for i in [l for l in s if l.isalpha()]:
#         if i.islower():
#             l_c += 1
#         else:
#             h_c += 1
#     return f'Letter in high case - {h_c}\nLetter in low case - {l_c}'
#
# print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))
# ИЛИ ИСПОЛЬЗУЯ DICTIONARY
# def up_low(s):
#     d={"upper":0, "lower":0}
#     for c in s:
#         if c.isupper():
#             d["upper"]+=1
#         elif c.islower():
#             d["lower"]+=1
#         else:
#             pass
#     print("Original String : ", s)
#     print("No. of Upper case characters : ", d["upper"])
#     print("No. of Lower case Characters : ", d["lower"])
# ЗАДАНИЕ 57 #######################################################################
# def unique_list(lst): return set(lst)
# print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
# ИЛИ
# def unique_list(lst):
#     # Also possible to use list(set())
#     x = []
#     for a in lst:
#         if a not in x:
#             x.append(a)
#     return x
# ЗАДАНИЕ 57 #######################################################################
# def multiply(numbers):
#     n = 1
#     for num in numbers:
#         n = n * num
#     return n
#
# print(multiply([1,2,3,-4]))
# ИЛИ ################################ https://www.youtube.com/watch?v=2ghKShXWuSs
# def multiply(my_num):
#     n = 1
#     for num in my_num:
#         n *= num  # ТОЖЕ, ЧТО И n = n * num
#     return n
#
# my_num = [1,2,3,-4]
# print(multiply(my_num))
# ЗАДАНИЕ 57 #######################################################################
# def palindrome(s):
#     f = 0
#     s_1 = [l for l in s]
#     s_2 = [l for l in reversed(s_1)]
#     for item in zip(s_1, s_2):
#         if item[0] != item[1]:
#             f += 1
#         else:
#             pass
#     return f == 0
#
# print(palindrome('heleh'))
# ИЛИ
# def palindrome(s):
#     s = s.replace(' ', '')
#     return s == s[::-1]
# print(palindrome('helleh'))
# ЗАДАНИЕ 57 #######################################################################
# import string
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     my_str = (''.join(str1.split())).lower()
#     co = 0
#     for i in alphabet:
#         if i not in my_str:
#             co += 1
#         else:
#             pass
#     if co == 0:
#         return True
#     else:
#         return False
#
# print(ispangram("The quick brown fox jumps over he lazy dog"))
# ИЛИ
# import string
#
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)
#     str1 = str1.replace(' ','')
#     str1 = str1.lower()
#     str1 = set(str1)
#     return str1 == alphaset
#
#
# print(ispangram("The quick brown fox jumps over the lazy dog"))
# ############################# СТОРОННИЙ РЕСУРС
# my_string = ['hello', 'hi', 'good morning']
# print(list(map(str.upper, my_string)))
# # lambda для создания анонимных функций:
# my_string = ['hello', 'hi', 'good morning']
# print(list(map(lambda num: num[::-1], my_string)))
# ######
# print(list(map(lambda num: num + '!', my_string)))
# ######
# b = list(map(list, my_string))
# c = list(map(sorted, b))
# print(c)
# ######
# s = list(map(int, input('!: ').split()))
# print(s)
##########################################
# def display(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)
#
# example_row = [1, 2, 3]
#
# display(example_row,example_row, example_row)
# # ИЛИ
# def display(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)
#
# row1 = [' ', ' ', ' ']
# row2 = [' ', ' ', ' ']
# row3 = [' ', ' ', ' ']
# row2[2] = 5
# display(row1, row2, row3)
####################################
def user_choice():
    choice = 'WRONG'
    while choice.isdigit() == False:
        choice = input("Insert the value:  ")
        if choice.isdigit() == False:
            print("It's incorrect data!")
    return int(choice)
print(user_choice())
#
def user_choice():
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Insert the value:  ")
        if choice.isdigit() == False:
            print("It's incorrect data!")

        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
    return int(choice)
print(user_choice())

