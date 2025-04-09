# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list

myList = []
myList.append(40)
myList.append(20)
myList.append(30)
myList.append(10)

myList.insert(1, 15)

secondList = [50, 60, 70]

myList.extend(secondList)

print(myList)

myList.pop()

print(myList)

myList.sort()
print(myList)

print(myList.index(30))