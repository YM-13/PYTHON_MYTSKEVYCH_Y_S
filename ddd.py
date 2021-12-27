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
#     string_sentence = reversed(string_sentence.split())
#     return ' '.join(string_sentence)
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
