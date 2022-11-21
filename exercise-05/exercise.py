import random as r

def random_list_sum():
    rand_list = []
    for i in range(15):
        rand_list.append(r.randint(-100,100))
    print(rand_list)
    print(sum(rand_list))

random_list_sum()

