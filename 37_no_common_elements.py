# WAP to Elements Present in One List but Not Another

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common = []
for i in list1:
    if i not in list2 :
        common.append(i)

#   ->  If you find no common elements from both list. 

'''
for j in list2:
    if j not in list1:
        common.append(j)
'''

print(common)