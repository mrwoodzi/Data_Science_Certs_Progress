def sum67(nums):
    newlist1 = []
    middle = []
    newlist2 = []
    list1 = 0
    list2 = 0
    s = 0
    skip = False
    for i in range(len(nums)): 
        list1 = nums[i]
        if list1 < 6 and skip == False:
            newlist1.append(list1)
            newlist = nums[i]
            print(newlist)
            print(newlist1)
        elif list1 == 6 and skip == False:
            skip = True
            print('True, continue')
            pass
        elif skip == True and list1 != 7:
            pass
        elif list1 == 7 and skip == True:
            skip = False
            print(newlist)
            pass
        elif skip == False and list1 != 6:
            newlist1.append(list1)
            newlist = nums[i]
            print(newlist)
            print(newlist1)
    for s in range(len(newlist1)):
        new_s = newlist1[s]
        print(s, new_s)
        new_sum += new_s
        print(new_sum)



            

            

print(sum67([1, 2, 2, 6, 99, 99, 7, 9, 10, 11]))
