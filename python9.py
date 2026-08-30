classes = ["Math", "Physics", "Biology", "Tech"]
classes2 = ["EduTech", "Electro"]

# append is to add a value to the list
classes.append("Art")

# You can also insert to what ever spesific place to the list
classes.insert(0, "Art")

# You can also extend the list 
classes.extend(classes2,)

# You can also remove from list 
classes.remove(classes[1])

# You can also sort your list in ascending order
classes.sort()

# You can also sort your list in descending order
classes.sort(reverse=True)

print(classes)
