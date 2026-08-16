# #normal way
# l=[]
# for i in range(1,6):
#     l.append(i)
# print(l)

#in conprehension way
# num = [i for i in range(1, 6)]
# print(num)

even = [i for i in range(1, 11) if i % 2 == 0]
print(even)