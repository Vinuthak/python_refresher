friends = ["Bob","Rolf"]
def add_friend():
    friend_name = input("Enter your friend name: ")
    f = friends + [friend_name]
    friends.append(friend_name)
    print(f)
    print(friends)
add_friend()
print(friends) #global variable
#print(f) error as it is local variable.