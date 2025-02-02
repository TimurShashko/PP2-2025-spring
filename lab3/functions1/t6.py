def rev(s):
    s_list=[]
    s_list=s.split()
    s_list.reverse()
    return ' '.join(s_list)

print(rev("We are here"))
print("")