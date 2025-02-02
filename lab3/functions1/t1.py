def gr_to_ounces(grams):
    return 28.3495231 * grams 

grams = float(input("Enter grams to convert: "))
result  = gr_to_ounces(grams)
print(result)