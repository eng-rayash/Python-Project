student = {"name":"sara","age":20 ,"major": "IT"}

print(student["name"])
student["age"] = 21
student["city"] = "sanaa"
print(student.get("phone","N/A"))
del student["major"]

for key , Value in student.items():
    print(key, Value)

print(student.keys())
print(student.values())