# list []
# Indexable
# Mutable
# Maintains insertion order
# allows duplicate  values

# set {} = Union , Intersection, Difference
# not INdexable - Hashing
# Mutable
# Doesnt maintain insertion order
# Doesnt allow duplication

# x={"tiger", "lion", "cat", "dog", "eagle", "crow"}
# y={"bear", "dear", "cat", "cow","sparrow"}
# z={"hiran","billi","kutta","sher","or nhi pta","billi"}
# n= set()

# # a=set{z}
# # print(z)

# # print(x.union(y))
# # print(x.difference(y))
# # print(x.intersection(y))

# # for i in z:
# #     j=i.lower()
# #     print(i)

# #
# for i in z:
#     n.add(i.upper())
# print(n)

x={1,2,3,4,5,6,5}
y={5,6,7,8}

# x.remove(2)  #stop performing-exceptional
# x.discard()   # not stop perfroming and ignorrer
# x.pop()  #remove first value
# print(x)

#update function -- update set and store value & union fun only display value after adding
# x.update(y)
# print(x)


#issubset - give output in true and false
print(y.issubset(x))











#symmetric difference & Disjoint

