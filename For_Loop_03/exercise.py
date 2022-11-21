list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

        
for i,j,k in zip(list1, tuple1, set1):    
    print(i,j,k)        
        
        
for key, value in dict1.items():
    if value == "land":
        print (key, "lives in", value )        
    else:
        continue
        



