n = int(input("enter the number of student's:"))
lst = []
for i in range(n):
    scr = float(input("eneter the student's programming score:"))
    lst.append(scr)

average_lst = sum(lst) / n
max_lst = max(lst)
min_lst = min(lst)

print("score's average:" , average_lst)
print("the highest score:" , max_lst)
print("lowest score:" , min_lst)
