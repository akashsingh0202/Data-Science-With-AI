import  numpy as np ,time
# l=range(10000000)
# start=time.time()
# result=[i**2 for i in l]
# end=time.time()
# print(end-start)


ar1=np.arange(10000000)
start=time.time()
result=ar1**2
end=time.time()
print(end-start)