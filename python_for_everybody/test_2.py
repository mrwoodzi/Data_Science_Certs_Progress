def arithmetic_arranger(problems):
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

print(arithmetic_arranger(["999 + 560", "1 - 3801", "55 + 66", "123 + 49"]))

#            