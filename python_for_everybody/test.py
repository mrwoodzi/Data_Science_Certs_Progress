def arithmetic_arranger(problems):
    pt1 = len(problems)
    if pt1 >= 5:
        print("Error: Too many problems.")
        quit()
    mylist_0 = []
    mylist_1 = []
    mylist_2 = []
    operands = []
    int1 = []
    operand1 = []
    int2 = []
    sum_list = []
    SUMnow = False
    for list in problems:
      new_list = list.split()
      new_str0 = (new_list[0])
      print(new_str0)
      new_str1 = (new_list[1])
      print(new_str1)
      new_str2 = (new_list[2])
      print(new_str2)
      mylist_0 += [new_str0]
      operands += [new_str1]
      mylist_2 += [new_str2]
      if SUMnow == True:
        sum = eval(f'{new_str0}{new_str1}{new_str2}')
        sum_list += [sum]
        print(sum)
    for a in range(len(mylist_0)): # a is = 0 1 2 3 range
      while a > len(mylist_0): # number of characters/bytes in list
        int1 = 

    


   



    return(mylist_0, operands, mylist_2, sum_list)
            


print(arithmetic_arranger(["32 + 698", "1 - 3801", "45 + 43", "123 + 49",]))

