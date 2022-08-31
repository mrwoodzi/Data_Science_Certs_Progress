
from string import whitespace


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
    sum_string = []
    sum_len_list = []
    secondhalflist = []
    alllist = []
    secondhalfstring = ''
    lines_sum = []
    lines_sum_split = []
    whitespace_op = ''
    whitespace_problems = '    '
    whitespace = ' '
    whitespace_c = '' # first print line whitespaces
    whitespace_c_sum = []
    whitespace_f = '' # sum between operand and number in second print line
    whitespace_f_sum = []
    whitespace_sum_sum = ''# sum line white spaces
    lleng = []
    llenf = []
    lenlist = []
    lleng_int = []
    llenf_int = []
    lenlist_lines = []
    problems_list1 = '\n'
    problems_list2 = '\n'
    problems_list3 = '\n'
    problems_list4 = '\n'
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
      #print(operands)
      #print(it)
      val = ((op_plus == it) or (op_minus == it))
      if val == False:
        #print(val)
        #print(f'{op_plus}')
        #print(f'{op_minus}')
        #print(f'{new_str1}')
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
    #print(mylist_0)
    #print(operands)
    #print(mylist_2)
    #print(mystring_0)
    #print(mystring_2)

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
      sum_s = str(sum)
      #print(sum_s)
      len_sum = len(sum_s)
      #print(len_sum)
      sum_string += sum_s.split()
      sum_len_list += [len_sum]
      secondhalflist += [new_str1] + [new_str2]
      secondhalfstring += new_str1 + new_str2
      alllist += [new_str0] + [new_str1] + [new_str2] + [sum]
    lenalllist = len(alllist)
    mllen = len(mylist_0[0]) #This looks at the first
    mylen0 = len(mylist_0)
    #sum_string = ''.join(map(str, sum_list)) # turns sum_list into printable string
    #print(sum_string)
    #for i in sum_string:
    #  print(i)
    #print(sum_len_list)



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
        #print(lines)
        
    print(lines_sum)
    for i in lines_sum:
      #print(i)
      len_lines = len(i)
      #print(len_lines)
      lenlist_lines += [(f'{len_lines}')]
    
    #print(lenlist_lines)
    for a, b, c in zip(lleng_int, llenf_int, lenlist_lines): #compile whitespace_c_list
      print(a, b, c)
      if c == 3:
        print(c)
        whitespace_c = '\t\t'
        whitespace_f = '\t'
        whitespace_c_sum += [(f'{whitespace_c}')]
        whitespace_f_sum += [(f'{whitespace_f}')]
      elif c == 4:
        print(c)
        if a == 1 and b == 2:
          whitespace_c = '\t\t\t'
          whitespace_f = '\t'
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
        elif a == 2 and b == 1:
          whitespace_c = '\t\t'
          whitespace_f = '\t'
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
        elif a == 2 and b == 2:
          whitespace_c = '\t\t'
          whitespace_f = '\t'
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
      elif c == 5:
        if a == 1 and b == 3:     
          whitespace_c = '\t\t\t\t'
          whitespace_f = '\t'
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
        elif a == 2 and b == 3:
          whitespace_c = '\t\t\t'
          whitespace_f = '\t'
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
        elif a == 3 and b == 3:
          whitespace_c = '\t\t'
          whitespace_f = '\t'
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
        elif a == 3 and b == 1:
          whitespace_c = '\t\t'
          whitespace_f = '\t\t\t'
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
        elif a == 3 and b == 2:
          whitespace_c = '\t\t'
          whitespace_f = '\t\t'
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]
        elif a == 3 and b == 3:
          whitespace_c = '\t\t'
          whitespace_f = '\t'
          whitespace_c_sum += [(f'{whitespace_c}')]
          whitespace_f_sum += [(f'{whitespace_f}')]


    print(whitespace_c_sum)
    print(whitespace_f_sum)
    #print(lines_sum_split)
    for d, o, g, s, u, in zip(mylist_0, operands, mylist_2, sum_list, lines_sum):
      print( d, o, g, s, u)
      problem1 =(f'{d}')
      problem2 = (f'{o}{g}')
      problem3 = u
      problem4 = (f'{whitespace_sum_sum}{s}')
      #print(problem1)
      #print(problem2)
      #print(problem3)
      #print(problem4)
      problems_list1 += (f'{problem1}{whitespace_problems}') #each problems list has '\n' at the end at top
      problems_list2 += (f'{problem2}{whitespace_problems}')
      problems_list3 += (f'{problem3}{whitespace_problems}')
      problems_list4 += (f'{problem4}{whitespace_problems}')
    #print(mystring_0)
    #print(mylist_2)
    #print(mystring_2)
    if SUMnow:
      arranged_problems = problems_list1 + problems_list2 + problems_list3 + problems_list4
    else:  
      arranged_problems = problems_list1 + problems_list2 + problems_list3
    #print(problem)
    

    return arranged_problems
            


print(arithmetic_arranger(["8 + 1", "10 - 38", "999 + 999", "523 - 49"], True))


