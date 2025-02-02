def unic(list):
    new_list=[]
    for i in range (0,len(list)):
        is_here=False
        for j in range(0,len(new_list)):
            if list[i]==new_list[j]:
                is_here=True
        if (not is_here):
            new_list.append(list[i])
    return new_list

list=["a", "a", "b", "b", "b", "c"]
print(unic(list))
print("")