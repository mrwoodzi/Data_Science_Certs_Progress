def arithmetic_arranger(problems, SUMnow=None):
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
    sum_string = []
    sum_len_list = []
    secondhalflist = []
    secondhalfstring = ''
    lines_sum = []
    whitespace_problems = '    '
    whitespace_c = '' # first print line whitespaces
    whitespace_c_sum = []
    whitespace_f = '' # sum between operand and number in second print line
    whitespace_f_sum = []
    whitespace_sum_sum = [] # sum line white spaces
    lleng = []
    llenf = []
    lenlist = []
    lleng_int = []
    llenf_int = []
    lenlist_lines = []
    problems_list1 = ''
    problems_list2 = ''
    problems_list3 = ''
    problems_list4 = ''
    carriage_return = '\n'

    pt1 = len(problems)
    if pt1 >= 6:
        print("'Error: Too many problems.'")
        quit()

    # compiles list of numbers for first line print, second line print and operands
    for it in problems:
      new_list = it.split()
      new_str0 = (new_list[0])
      new_str1 = (new_list[1])
      new_str2 = (new_list[2])
      mylist_0 += [new_str0]
      mystring_0 += new_str0 + ''
      operands += [new_str1]
      myoperands += new_str1 + ''
      mylist_2 += [new_str2]
      mystring_2 += new_str2 + ''
      # tests wether the string contains something that isn't an int

    # compiles the the len of first line list and second line list
    for g, f in zip(mylist_0, mylist_2):
      len_g = len(g)
      len_gstring = str(len_g)
      len_f = len(f)
      len_fstring = str(len_f)
      lenlist += len_gstring + len_fstring
      lleng += len_gstring
      llenf += len_fstring
    lleng_int = [eval(i) for i in lleng] # gives me the len of the top part of the problem
    llenf_int = [eval(i) for i in llenf] # this is bottom part of problem

    for a in mylist_0:
      a_int = int(a)
      if type(a_int) != int:
        print("'Error: Numbers must only contain digits a.'")
        quit()
    for b in mylist_2:
      b_int = int(b)
      if type(b_int) != int:
        print("'Error: Numbers must only contain digits b.'")
        quit()
    for d, e in zip(lleng_int, llenf_int):
      if d >= 5 or e >= 5:
        print("'Error: Numbers cannot be more than four digits.'")
        quit()

    # test for correct operands
    for it in operands:
      val = ((op_plus == it) or (op_minus == it))
      if val == False:
        print(f"'Error: Operator must be {op_plus_print} or {op_minus_print}.'")
        quit()
    

    #This rearranges the list into multiple string and int lists to play around with
    for list in problems:  
      new_list = list.split()
      new_str0 = (new_list[0])
      new_str1 = (new_list[1])
      new_str2 = (new_list[2])
      sum = eval(f'{new_str0}{new_str1}{new_str2}')
      sum_list += [sum]
      sum_s = str(sum)
      len_sum = len(sum_s)
      sum_string += sum_s.split()
      sum_len_list += [len_sum]
      secondhalflist += [new_str1] + [new_str2]
      secondhalfstring += new_str1 + new_str2


    # compiling the list of lines:
    for c, b in zip(lleng_int, llenf_int):
      #print(c, b)
      if (c == 1 and b == 1):
        lines = '---'
        lines_sum += [(f'{lines}')]
        #print(lines)
      elif (c == 2 and b <= 2) or ( c <= 2 and b == 2):
        lines = '----'
        lines_sum += [(f'{lines}')]
        #print(lines)
      elif (c == 3 and b <= 3) or ( c <= 3 and b == 3):
        lines = '-----'
        lines_sum += [(f'{lines}')]
        #print(lines)
      elif (c == 4 and b <= 4) or ( c <= 4 and b == 4):
        lines = '------'
        lines_sum += [(f'{lines}')]

    # compiles the len of the lines into a list
    for i in lines_sum:
      len_lines = len(i)
      lenlist_lines += [(f'{len_lines}')]

    # this compiles the whitespace into 3 whitespace lists
    for a, b, c, d in zip(lleng_int, llenf_int, lenlist_lines, sum_len_list): #compiles all whitespace
      if c == '3':
        whitespace_c = '  '
        whitespace_f = ' '
        whitespace_c_sum += [(f'{whitespace_c}')]
        whitespace_f_sum += [(f'{whitespace_f}')]
        if d == 1:
          whitespace_sum = '  '
          whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif d == 2:
          whitespace_sum = ' '
          whitespace_sum_sum += [(f'{whitespace_sum}')]
      elif c == '4':
        if a == 1 and b == 2:
          whitespace_c = '   '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]  
        elif a == 2 and b == 1:
          whitespace_c = '  '
          whitespace_f = '  '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 2 and b == 2:
          whitespace_c = '  '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
      elif c == '5':
        if a == 1 and b == 3:     
          whitespace_c = '    '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 2 and b == 3:
          whitespace_c = '   '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 3 and b == 3:
          whitespace_c = '  '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 3 and b == 1:
          whitespace_c = '  '
          whitespace_f = '   '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 3 and b == 2:
          whitespace_c = '  '
          whitespace_f = '  '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 3 and b == 3:
          whitespace_c = '  '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
      if c  == '6':
        if a == 4 and b == 1:
          whitespace_c = '  '
          whitespace_f = '    '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '     '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 6:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 4 and b == 2:
          whitespace_c = '  '
          whitespace_f = '   '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '     '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 6:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 4 and b == 3:
          whitespace_c = '  '
          whitespace_f = '  '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '     '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 6:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 4 and b == 4:
          whitespace_c = '  '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '     '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 6:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 1 and b == 4:
          whitespace_c = '     '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '     '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 6:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 2 and b == 4:
          whitespace_c = '    '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '     '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 6:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]
        elif a == 3 and b == 4:
          whitespace_c = '   '
          whitespace_f = ' '
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
          if d == 1:
            whitespace_sum = '     '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 2:
            whitespace_sum = '    '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 3:
            whitespace_sum = '   '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 4:
            whitespace_sum = '  '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 5:
            whitespace_sum = ' '
            whitespace_sum_sum += [(f'{whitespace_sum}')]
          elif d == 6:
            whitespace_sum = ''
            whitespace_sum_sum += [(f'{whitespace_sum}')]


    for c, f, d, o, g, s, u, z in zip(whitespace_c_sum, whitespace_f_sum, mylist_0, operands, mylist_2, sum_list, lines_sum, whitespace_sum_sum):
      problem1 =(f'{c}{d}')
      problem2 = (f'{o}{f}{g}')
      problem3 = u
      problem4 = (f'{z}{s}')
      problems_list1 += (f'{problem1}{whitespace_problems}') #each problems list has '\n' at the end at top
      problems_list2 += (f'{problem2}{whitespace_problems}')
      problems_list3 += (f'{problem3}{whitespace_problems}')
      problems_list4 += (f'{problem4}{whitespace_problems}')
    

    if SUMnow:
      arranged_problems = (f'{problems_list1}{carriage_return}{problems_list2}{carriage_return}{problems_list3}{carriage_return}{problems_list4}')
    else:  
      arranged_problems = (f'{problems_list1}{carriage_return}{problems_list2}{carriage_return}{problems_list3}')
    

    return arranged_problems
            


print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True))