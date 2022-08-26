
def arithmetic_arranger(problems, SUMnow):
    op_plus = '+'
    op_minus = '-'
    op_plus_print = ("'+'")
    op_minus_print = ("'-'")
    mylist_0 = []
    mystring_0 = ''
    mylist_2 = []
    mystring_2 = ''
    operands = []
    myoperands = ''
    sum_list = []
    sum_string = ''
    secondhalflist = []
    alllist = []
    secondhalfstring = ''
    lines = ''
    whitespace_c = ' '
    whitespace_f = ' '
    whitespace_op = ' '
    whitespace_sum = ' '
    whitespace_problems = '    '
    lleng = []
    llenf = []
    lenlist = []
    lleng_int = []
    llenf_int = []
    lenlist_int = []
    problems_list1 = ' \n'
    problems_list2 = ' \n'
    problems_list3 = ' \n'
    problems_list4 = ' \n'
    carriagereturn = '\n'
    pt1 = len(problems)
    #print(pt1)
    if pt1 >= 5:
        print("Error: Too many problems.")
        quit()
    for it in problems:
      new_list = it.split()
      #print(new_list)
      #print(new_list[0])
      new_str0 = (new_list[0])
      #print(new_str0)
      new_str1 = (new_list[1])
      #print(new_str1)
      new_str2 = (new_list[2])
      mylist_0 += [new_str0]
      mystring_0 += new_str0 + ''
      operands += [new_str1]
      myoperands += new_str1 + ''
      mylist_2 += [new_str2]
      mystring_2 += new_str2 + ''
      contains_digit1 = any(map(str.isnumeric, new_list[0])) # tests wether the string contains something that isn't an int
      if (contains_digit1 == False):
        #print(contains_digit1)
        print('Error: Numbers must only contain digits.')
        quit()
      contains_digit2 = any(map(str.isnumeric, new_list[2]))
      if (contains_digit2 == False):
        #print(contains_digit2)
        print('Error: Numbers must only contain digits.')
        quit()
      if int(len(new_str0)) >= 5 or int(len(new_str2)) >= 5:
        print('Error: Numbers cannot be more than four digits.')
        quit()

    for it in operands:
      print(operands)
      print(it)
      val = ((op_plus == it) or (op_minus == it))
      if val == False:
        print(val)
        print(f'{op_plus}')
        print(f'{op_minus}')
        print(f'{new_str1}')
        print(f'Error: Operator must be {op_plus_print} or {op_minus_print}.')
        quit()
    
    for g, f in zip(mylist_0, mylist_2):
      #print(g, f)
      len_g = len(g)
      len_gstring = str(len_g)
      #print(len_g)
      len_f = len(f)
      len_fstring = str(len_f)
      #print(len_f)
      lenlist += len_gstring + len_fstring
      lleng += len_gstring
      llenf += len_fstring
      #print(lenlist)
    lleng_int = [eval(i) for i in lleng] # gives me the len of the top part of the problem
    llenf_int = [eval(i) for i in llenf] # this is bottom part of problem
    lenlist_int = [eval(i) for i in lenlist] #this is the then of the entire list
    print(mylist_0)
    print(operands)
    print(mylist_2)
    print(mystring_0)
    print(mystring_2)

    for list in problems:   #This rearranges the list into multiple string and int lists to play around with
      new_list = list.split()
      #print(new_list)
      new_str0 = (new_list[0])
      #print(new_str0)
      new_str1 = (new_list[1])
      #print(new_str1)
      new_str2 = (new_list[2])
      sum = eval(f'{new_str0}{new_str1}{new_str2}')
      sum_list += [sum]
      secondhalflist += [new_str1] + [new_str2]
      secondhalfstring += new_str1 + new_str2
      alllist += [new_str0] + [new_str1] + [new_str2] + [sum]
    lenalllist = len(alllist)
    mllen = len(mylist_0[0]) #This looks at the first
    mylen0 = len(mylist_0)
    sum_string = ''.join(map(str, sum_list)) # turns sum_list into printable string


    # compiling the 4 lists
    for c, b, d, o, g, s in zip(lleng_int, llenf_int, mylist_0, operands, mylist_2, sum_list): # 
      #print(c, b, o, d, g)
      if c == 1 and b == 1:
        lines = '---'
      elif (c == 2 or b == 1) and (c == 1 or b == 2):
        #print(c, b)
        lines = '----'
        lenlines2 = len(lines)
        #print(lenlines2)
      elif (c == 3 or b <= 3) and (c <= 3 or b == 3):
        #print(c, b)
        lines = '-----'
        lenlines3 = len(lines)
        #print(lenlines3)
      elif (c == 4 or b <= 4) and (c <= 4 or b == 4):
        #print(c, b)
        lines = '------'
        lenlines4 = len(lines)
        #print(lenlines4)
      
      problem1 = (f'{whitespace_c}{d}{whitespace_problems}')
      problem2 = (f'{o}{whitespace_f}{g}{whitespace_problems}')
      problem3 = (f'{lines}{whitespace_problems}')
      problem4 = (f'{whitespace_sum}{s}{whitespace_problems}')
      #print(problem1)
      #print(problem2)
      #print(problem3)
      #print(problem4)
      problems_list1 += (f'{problem1}')
      problems_list2 += (f'{problem2}')
      problems_list3 += (f'{problem3}')
      problems_list4 += (f'{problem4}')
    #print(mystring_0)
    #print(mylist_2)
    #print(mystring_2)
    if SUMnow:
      arranged_problems = problems_list1 + problems_list2 + problems_list3 + problems_list4
    else:  
      arranged_problems = problems_list1 + problems_list2 + problems_list3
    #print(problem)
    

    return arranged_problems
            


print(arithmetic_arranger(["32 + 698", "1 - 3801", "45 + 43", "123 + 49"], True))

