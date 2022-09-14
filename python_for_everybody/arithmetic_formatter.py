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
    new_mylist0 = ''
    new_mylist12 = ''
    new_mylines = ''
    new_mysum = ''
    error_boo = False
    error = ''

    pt1 = len(problems)
    if pt1 >= 6:
      return 'Error: Too many problems.'

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
        if ((a.isnumeric()) == False):
            return 'Error: Numbers must only contain digits a.'

    for b in mylist_2:
        if ((b.isnumeric()) == False):
            return 'Error: Numbers must only contain digits b.'


    for d, e in zip(lleng_int, llenf_int):
      if d >= 5 or e >= 5:
        return 'Error: Numbers cannot be more than four digits.'

    # test for correct operands
    for it in operands:
      val = ((op_plus == it) or (op_minus == it))
      if val == False:
        return """Error: Operator must be '+' or '-'."""
    

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

    for a,b in zip(whitespace_c_sum, mylist_0):
        n_list = a+b+whitespace_problems
        new_mylist0 += n_list
    for a,b,c in zip(operands, whitespace_f_sum, mylist_2):
        m_list = a+b+c+whitespace_problems
        new_mylist12 += m_list
    for a in lines_sum:
        l_list = a+whitespace_problems
        new_mylines += l_list
    for a,b in zip(sum_string, whitespace_sum_sum):
        s_list = b+a+whitespace_problems
        new_mysum += s_list
    


    new_mylist0 = new_mylist0.rstrip()
    new_mylist12 = new_mylist12.rstrip()
    new_mylines = new_mylines.rstrip()
    new_mysum = new_mysum.rstrip()
  
    problems_list2 = new_mylist0+carriage_return+new_mylist12+carriage_return+new_mylines+carriage_return+new_mysum
    problems_list1 = new_mylist0+carriage_return+new_mylist12+carriage_return+new_mylines

    if SUMnow:
        arranged_problems = problems_list2
    else:
        arranged_problems = problems_list1

    return arranged_problems
            


print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'], True))

