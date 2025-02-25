def all_true(tpl):
    return all(tpl)

if __name__ == "__main__":
    my_tuple = (1, True, "non-empty", 5) 
    print(all_true(my_tuple))  

    my_tuple2 = (1, 0, 2)      
    print(all_true(my_tuple2)) 
