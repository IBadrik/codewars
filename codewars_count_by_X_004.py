def count_by(x, n):
    i = 1
    a_list = []
    while i <= n:
        result_num = i * x
        a_list.append(result_num)
        i += 1
    return a_list

# In this kata I need to create a function with two arguments
# that will return an array of the first n multiples of x