def is_common_subsequence(sub, first, second):
    #return True # if sub is a common subsequence the two other strings
    i = 0
    j = 0
    matchedList = []
    subLen = len(sub)
    firstLen = len(first)

    while (i < subLen) and (j < firstLen):
        if sub[i] == first[j]:
            matchedList.append(first[j])
            i += 1
        j += 1

    # print(matchedList)
    joined = "".join(matchedList)
    # print(joined)
    
    if joined == sub:
        trueorfalse = True
    else:
        trueorfalse = False
    
    i = 0
    j = 0
    matchedList2 = []
    subLen = len(sub)
    secondLen = len(second)

    while (i < subLen) and (j < secondLen):
        if sub[i] == second[j]:
            matchedList2.append(second[j])
            i += 1
        j += 1

    # print(matchedList2)
    joined = "".join(matchedList2)
    # print(joined)
    
    if joined == sub:
        trueorfalse2 = True
    else:
        trueorfalse2 = False

    if trueorfalse == trueorfalse2:
        return True
    else:
        return False

# print(is_common_subsequence("cat", "topcat", "acetyau"))