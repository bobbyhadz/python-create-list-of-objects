# Create a list of objects in Python

class Employee():
    def __init__(self, id):
        self.id = id


list_of_objects = []

for i in range(5):
    list_of_objects.append(Employee(i))

print(list_of_objects)

for obj in list_of_objects:
    print(obj.id)  # 👉️ 0, 1, 2, 3, 4