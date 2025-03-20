my_list = []
appendable = (10, 20, 30, 40)
for i in appendable:
    my_list.append(i)
my_list.insert(1,15)
new_list = [50, 60, 70]
my_list.extend(new_list)
my_list.pop()
my_list.sort()
print(my_list.index(30))
