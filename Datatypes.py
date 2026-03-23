#list 
a=["apple","banana","cherry"]
b=["melon","kiwi"]
print(a[-2:-1])
a.append("mango")
print(a)
a.insert(3,"grapes")
print(a)
a.extend(b)
print(a)

b=["Hindi", "English","Marathi", "Bengali", "Tamil", "Telegu"]
b.remove("Marathi")
print(b)
group=["Messi","Kylian","Neymar","Ronaldo","Mbappe"]
group.pop(3)
print(group)
group.reverse()
print(group)
num=[1,6,3,4,5]
n=sorted(num)
print(n)
print(n.index(3))
print(10 in n)
print(sum(n))

# enumerate returns the index and the value of the item in the list
for i,item in enumerate(n,start=1):
    print(i,item)


# join method is used to join the items in the list with a separator
mylist=["apple","banana","cherry"]
mystring="-".join(mylist)
print(mystring)
my_list=mystring.split('-')
print(my_list)

#Tuples
list_1=(2,5,23,5,1,89)
print(list_1)
print(list_1[2])

#Sets
my_set={"Messi","Ronaldo","Neymar","Mbappe","Ronaldo"}
print(my_set)

new1_set={"C","C#","Python","Java"}
new2_set={"Python","Rust","C++","C#"}
# intersection returns the common elements in both sets
print(new1_set.intersection(new2_set))
#difference returns the elements that are in the first set but not in the second set
print(new1_set.difference(new2_set))
#union returns all the elements in both sets without duplicates
print(new1_set.union(new2_set))

#empty list
empty_list=[]
empty_list=list()

#tuple
empty_tuple=()
empty_tuple=tuple()

#empty set
empty_set=set()

#Dictionary
my_dict={"name":"Raju","age":23,"cast":"hindu"}
print(my_dict)
print(my_dict["name"])
