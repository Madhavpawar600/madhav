from sys import getsizeof
com=[x*5 for x in range(1000)]
gen=(x*5 for x in range(1000))
print(getsizeof(com))
print(getsizeof(gen))
