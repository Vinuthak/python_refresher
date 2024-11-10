friends = {"Bob","Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local_friends = friends.difference(abroad) #(friends)-(abroad)
print(local_friends)
local_friends = abroad.difference(friends) #(abroad)-(friends) => empty set => set()
print(local_friends)

#Lets say we have local and abroad set of friends and we need to find total friends,then use union
loc = {"Rolf"}
abrd = {"Bob", "Anne"}
frnz = abrd.union(loc)
print(frnz)

arts = {"Me","Praveen","Umesh"}
science = {"Me","Praveen","Sandy"}
both = arts.intersection(science)
print(both)