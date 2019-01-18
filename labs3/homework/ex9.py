def get_even_list(l):
    even_list=[]
    for num in l:
        if num % 2==0:
            even_list.append(num)
    return(even_list)

even_list = get_even_list([1, 4, 5, -1, 10])
print(even_list)