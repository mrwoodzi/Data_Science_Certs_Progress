if new_string != (op[0]) or (op[-1]):
              print(op[0])
              print(len(new_string))
              print(len(newlist_0))
              print(string)
              print(newlist_0)
              print(newlist_1)
              print(new_string)
              print("Error: Operator must be '+' or '-'.")
              quit()
            if new_int != int:
                print("Error: Numbers must only contain digits.")
                quit()
            if new_int_2 != int:
                print("Error: Numbers must only contain digits.")
                quit()

                print(newlist_1)
    plus = '+'
    minus = '-'
    if newlist_1 != plus or minus:
      print("Error: Operator must be '+' or '-'.")
      quit()


    for b in problems:
        SUMnow = False
        string = b
        new_list = string.split() # turns string into individual lists
        newlist_0 = new_list[0]
        newlist_1 = new_list[1]
        newlist_2 = new_list[2]
        new_int = int(newlist_0)
        new_int_2 = int(newlist_2)
        new_string = str(newlist_1)
        op = ['+', '-']
        whitespace = ""
        whitespace_2 = "  "
        whitespace_3 = ""
        lines = ""
        nll = len(newlist_0) 
        print(nll) # Just checking the len
        nll2 = len(newlist_2)
        print(nll2) # Just checking the len
        sum = eval(f'{newlist_0}{newlist_1}{newlist_2}')
        sum_string = str(sum)
        len_sum = len(sum_string)
        if (nll <=2 and nll2 <= 2) and (nll == 2 and nll2 == 2) and len_sum == 2:
            lines = "----"
            whitespace = "  "
            whitespace_2 = " "
            whitespace_3 = "  "
        elif (nll == 3 or nll2 == 3) and (nll == 3 and nll2 == 2) and len_sum == 3:
            lines = "-----"
            whitespace = "  "
            whitespace_2 = "  "
            whitespace_3 = "  "
        elif (nll == 3 or nll2 == 3) and (nll == 2 and nll2 == 3):
            lines = "-----"
            whitespace = "   "
            whitespace_2 = " "
            whitespace_3 = "  "
        elif (nll == 4 or nll2 == 4) and (nll == 4 and nll2 == 1):
            lines = "------"
            whitespace = "  "
            whitespace_2 = "    "
            whitespace_3 = "  "
        elif (nll == 4 or nll2 == 4) and (nll == 1 and nll2 == 4):
            lines = "------"
            whitespace = "     "
            whitespace_2 = " "
            whitespace_3 = "  "
        lll = (len(lines))

        if lll == 4:
            print(lll)
        if lll == 5:
            print(lll)
        if lll == 6:
             print(lll)
             
        print(f"{whitespace}{newlist_0}\n{newlist_1}{whitespace_2}{newlist_2}\n{lines}")
        print(f'{whitespace_3}{sum}') # This puts the problem vertically # whitespace now

              newlist_0 = new_list[0]
      newlist_1 = new_list[1]
      newlist_2 = new_list[2]
#      mylist += new_list[0] +  + new_list[1] +  + new_list[2]
      operands += ' ' + newlist_1
      nll += ' ' + newlist_0
      nll2 += ' ' + newlist_2
    for a in range(len(mylist_0)): # a is = 0 1 2 3 range

    while loopadd < lenalllist:
      loopadd = loopadd + 1
      print(loopadd)


    alllist += [new_str0] + [new_str1] + [new_str2] + [sum]

    while loopadd < mllen:
      loopadd = loopadd + 1
      print(loopadd)
      for g, f in zip(mylist_0, mylist_2):
        print(g, f)
        len_g = len(g)
        print(len_g)
        len_f = len(f)
        print(len_f)
        if len_g or len_f == 4:
          lines = '------'

pt1 = len(problems)
    if pt1 >= 5:
        print("Error: Too many problems.")
        quit()
    for a in problems:
        string = a
        new_list = string.split() # turns string into individual lists
        newlist_0 = new_list[0]
        newlist_1 = new_list[1]
        newlist_2 = new_list[2]
        new_int = int(newlist_0)
        new_int_2 = int(newlist_2)
        new_string = str(newlist_1)
        op = ['+', '-']
        whitespace = ""
        whitespace_2 = "  "
        whitespace_3 = ""
        lines = ""
        nll = len(newlist_0) 
        print(nll) # Just checking the len
        nll2 = len(newlist_2)
        print(nll2) # Just checking the len
        sum = eval(f'{newlist_0}{newlist_1}{newlist_2}')
        sum_string = str(sum)
        len_sum = len(sum_string)
        if (nll <=2 and nll2 <= 2) and (nll == 2 and nll2 == 2) and len_sum == 2:
            lines = "----"
            whitespace = "  "
            whitespace_2 = " "
            whitespace_3 = "  "
        elif (nll == 3 or nll2 == 3) and (nll == 3 and nll2 == 2) and len_sum == 3:
            lines = "-----"
            whitespace = "  "
            whitespace_2 = "  "
            whitespace_3 = "  "
        elif (nll == 3 or nll2 == 3) and (nll == 2 and nll2 == 3):
            lines = "-----"
            whitespace = "   "
            whitespace_2 = " "
            whitespace_3 = "  "
        elif (nll == 4 or nll2 == 4) and (nll == 4 and nll2 == 1):
            lines = "------"
            whitespace = "  "
            whitespace_2 = "    "
            whitespace_3 = "  "
        elif (nll == 4 or nll2 == 4) and (nll == 1 and nll2 == 4):
            lines = "------"
            whitespace = "     "
            whitespace_2 = " "
            whitespace_3 = "  "
        lll = (len(lines))

        if lll == 4:
            print(lll)
        if lll == 5:
            print(lll)
        if lll == 6:
             print(lll)
             
        print(f"{whitespace}{newlist_0}\n{newlist_1}{whitespace_2}{newlist_2}\n{lines}")
        print(f'{whitespace_3}{sum}') # This puts the problem vertically # whitespace now
         
        continue
        return sum

    while loopadd < mllen:
      loopadd = loopadd + 1
      print(loopadd)

          if lleng[0] == 2:
      print('you did it')

      (f'{whitespace_c}{d}{whitespace_problems}\n{o}{whitespace_op}{g}{whitespace_problems}\n{lines}\n')
      {d}{whitespace_problems}{carriagereturn}{o}{whitespace_op}{g}{whitespace_problems}{carriagereturn}{lines}{carriagereturn}

          reorderedlist = mylist_0 + secondhalflist
    reorderedstring = mystring_0 + secondhalfstring + sum_string
    #print(reorderedlist)
    for inter in reorderedlist: # I need to iterate over each value and op in list
        n = inter
        #print(n)
        nl = n.split() # turns string into individual lists ['32']
        nl_0 = nl[0] # turns list into 32 printed
        #print(nl_0)

    print(alllist)
    print(mllen)
    print(lleng_int)
    print(llenf_int)
    print(lenlist_int)
    print(lleng)
    print(llenf)
    print(lenlist)
    print(mylist_2)

        for a, b in zip(mylist_0, mylist_2):
      if a or b != int:
       print('Error: Numbers must only contain digits.')
       quit()

whitespace = ' '
      if c == 1 and b == 1:
        lines = '---'
        lenlines = len(lines)
        sum_s = str(s)
        #print(sum_s)
        sumlen_s = len(sum_s)
        #print(sumlen_s)
        whitespace_c_sum = ''
        whitespace_f_sum = ''
        whitespace_sum_sum =  ''
      elif c == 2 and b == 2:
        lines = '----'
        lenlines = len(lines)
        sum_s = str(s)
        #print(sum_s)
        sumlen_s = len(sum_s)
        #print(sumlen_s)
        whitespace_c_sum = ''
        whitespace_f_sum = ''
        whitespace_sum_sum = ''
      elif c == 3 and b == 3:
        lines = '-----'
        lenlines = len(lines)
        sum_s = str(s)
        #print(sum_s)
        sumlen_s = len(sum_s)
        #print(sumlen_s)
        whitespace_c_sum = ''
        whitespace_f_sum = ''
        whitespace_sum_sum = whitespace
      elif c == 4 and b == 4:
        lines = '------'
        lenlines = len(lines)
        sum_s = str(s)
        #print(sum_s)
        sumlen_s = len(sum_s)
        #print(sumlen_s)
        whitespace_c_sum = '  '
        whitespace_f_sum = ' '           
        whitespace_sum_sum = ' '
      elif (c == 2 and b == 1) or (c == 1 and b == 2):
        #print(c, b)
        lines = '----'
        lenlines = len(lines)
        if c == 2 and b == 1:
          whitespace_c_sum = '  '
          whitespace_f_sum = '  '           
          whitespace_sum_sum = '  '
        #print(lenlines2)
        elif b == 2 and c == 1:
          whitespace_c_sum = '   '
          whitespace_f_sum = ' '           
          whitespace_sum_sum = '  '
        #print(lenlines2)
      elif (c == 3 or b <= 3) and (c <= 3 or b == 3):
        #print(c, b)
        lines = '-----'
        lenlines = len(lines)
        whitespace_c_sum =  '  '
        whitespace_f_sum = ' '           
        whitespace_sum_sum = ' '
        whitespace_f = ' '
        #print(lenlines3)
      elif (c == 4 or b <= 4) and (c <= 4 or b == 4):
        #print(c, b)
        lines = '------'
        lenlines = len(lines)
        whitespace_c_sum = '  '
        whitespace_f_sum = ' '           
        whitespace_sum_sum = ' '
        #print(lenlines4)

    sum_string = ''.join(map(str, sum_list)) # turns sum_list into printable string