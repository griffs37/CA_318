def is_subsequence(sub, string):
    #return True # if sub is a subsequence of str otherwise False
    i = 0
    j = 0
    matchedList = []
    subLen = len(sub)
    stringLen = len(string)

    while (i < subLen) and (j < stringLen):
        if sub[i] == string[j]:
            matchedList.append(string[j])
            i += 1
        j += 1

    # print(matchedList)
    joined = "".join(matchedList)
    # print(joined)
    
    if joined == sub:
        return True
    else:
        return False