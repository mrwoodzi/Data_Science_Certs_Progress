def sum67(nums):
    answer = 0
    dontAddNow = False
    for i in nums:
        if i == 6:
            dontAddNow = True
        if dontAddNow:
            if i == 7:
                dontAddNow = False
        else:
            print(i)
            answer += i

    return answer

mylist = [1, 1, 6, 7, 2]
print(sum67(mylist))
