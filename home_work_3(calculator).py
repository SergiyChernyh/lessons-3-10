#############################  1111111111111111111   ###############################
# value = 5
# new_value = 90
# if new_value < 100:
#  new_value = value / 2
# else:
#  new_value = - value
# print(new_value)

####################################  2222222222222  ########################################

# value = 200
# new_value = 90
# if value < 100:
#  new_value = 1
# else:
#  new_value = 0
# print(new_value)
########################################    3333333333333333333      ###########################

# value = 20
# if value < 100:
#   new_value = True
# else:
#  new_value = False
# print(new_value)

####################################   4444444444444444444444      ############################

# my_str = "asd4"
# if len(my_str) < 5:
#     my_str = my_str * 2
# print(my_str)

####################################    555555555555555555         ###################################
# my_str = "asd5"
# if len(my_str) < 5:
#   my_str = my_str + my_str[::-1]
# print(my_str)

######################################   666666666666666666        ###################################


# c = 0             # цикл проверки значения 1
# b = 0             # цикл проверки значения 2
# d = 0             # цикл проверки оператора ввода
# e = 0             # цикл проверки деления на  "0"

is_tru_yes_no = True
while is_tru_yes_no:
 is_true = True
 result = 0
 #while c == 0:
 while is_true:
  try:
      value_1 = float(input("веддите 1 число: "))
      #c = 1
      is_true = False

  except ValueError:
   print ("неправильное число, повторите ввод")
 is_true = True
 # while e == 0:
 while is_true:
  is_true_in_while = True

  # while b == 0:
  while is_true_in_while:
   try:
     value_2 = float(input("веддите 2 число: "))
     #d = 0
     is_true_in_while = False
   except ValueError:
    print("неправильное число, повторите ввод")
  is_true_in_while = True


  #while d == 0:
  while is_true_in_while:
   try:
    value_operator = int(input("Please choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/' \n Your answer: "))
  #  if value_operator == 5 or value_operator == 6 or value_operator == 7 or value_operator == 8 or value_operator == 9 or value_operator == 0:
    #if value_operator != 1 and value_operator != 2 and value_operator != 3 and value_operator != 4:
    if value_operator not in [1,2,3,4]:
     print("неправильное число, повторите ввод")
    else:
#    print("test")
     if value_2 == 0 and value_operator == 4:
      print("деление на '0' повторите ввод")
     #b = 0
      is_true_in_while = False
     #d = 1
#     print("test1", b, d)
     else:
         is_true_in_while = False
         is_true = False

    # # d = 1
    #  e = 1
#     print("test4", d)
   except ValueError:
     print("неправильное число, повторите ввод")

#print("test3")
 if value_operator == 1:
  result = value_1 + value_2

 elif value_operator == 2:
  result = value_1 - value_2

 elif value_operator == 3:
  result = value_1 * value_2

 elif value_operator == 4:
# print("test2")
  result = value_1 / value_2

 print(result)
 yes_no = input(" продолжить '1': , выйти '0': ")
 if yes_no == 1:
  is_tru_yes_no = True

 else:
  is_tru_yes_no = False