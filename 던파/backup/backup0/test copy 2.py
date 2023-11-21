import json
from dataclasses import dataclass

@dataclass
class Student:
    def __init__(self='', name='', roll_no='', address='', json_string=None):

        if(json_string != None):
            self.__dict__ = json.loads(json_string)
        else:
            self.name = name
            self.roll_no = roll_no
            self.address = address
   
    def to_json(self):
        '''
        convert the instance of this class to json
        '''
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)
   
class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin
          
address = Address("Bulandshahr", "Adarsh Nagar", "203001")
student1 = Student("Raju1", 53, address)
student2 = Student("Raju2", 53, address)

map = {
    # "name": "interpolator",
    "qhfl1" : student1,
    "qhfl2" : student2,
}
# Encoding
student_json = student1.to_json()
print(student_json)
print(type(student_json))
  
# Decoding
student = Student(json_string=student_json)
print(student)
print(type(student))

print(student1)
print(type(student1))

# map["qhfl2"].roll_no = 100
# list = []
# for key, value in map.items():
#     list.append(value.to_json())

# with open('ff.json', 'w') as f:
#     json.dump(list, f)

# with open('ff.json', 'r') as f:
#     list2 = json.load(f)

# # clear list
# list = []
# for i in list2:
#     student = json.loads(i)
#     print(student)
#     print(type(student))
#     list.append(student)
#     # list.append(json.loads(i))

# # print map
# print(list[1])

# # json string to Student
# # student = json.loads(list[1])
# # print(student)
