my_list= [*range(5)] 

print(my_list)


take_2nd_power = lambda x: x**2
check_if_even = lambda x: True if take_2nd_power(x) % 2 == 0 else False


for x in my_list:
    if check_if_even(x):
        print(take_2nd_power(x))
    else:
        continue
