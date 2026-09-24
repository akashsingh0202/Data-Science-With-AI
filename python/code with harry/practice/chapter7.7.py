n=int(input("Enter a number : "))
# i=0
# for i in range (n):
#     for j in range(n):
#         print("*", end="")
#     print()


for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("\n")