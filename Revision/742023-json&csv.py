# import json
# with open("person.json",'r') as filehandle:   # file to be saved on pycharm location
#
#     dict1 =json.load(filehandle)
# print(dict1)
#
# person_dict1 = {"name":"Bob",
# "Languages":["English","French"],
# "married":True,
# "age":32
# }
#
# with open("per2.json",'w') as filehandle:
#     json.dump(person_dict1,filehandle)
# print(dict)


import csv
# with open("sam.csv",'r') as csvhandle:
#     contents = csv.reader(csvhandle, delimiter="|")   #delimitter should be given in case no comma, it will consider comma as default
#     # contents = csv.reader(csvhandle,)
#     contents = csv.reader(csvhandle, dialect="all")
#     for line in contents:
#         print(line)

csv.register_dialect('all',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

# with open("sam.csv",'r') as csvhandle:
#     contents = csv.reader(csvhandle, dialect="all")
#     for line in contents:
#         print(line)
#
# with open("sam.csv", 'r') as csvhandle:
#     contents = csv.DictReader(csvhandle, dialect="all")
#     for line in contents:
#         print(line)

with open("books1.csv",'w',newline="") as file:
    handle =csv.writer(file)
    handle.writerow(["SID","Stuname", "Contibution"])
    handle.writerow([1,"ravi","how to win"])
    handle.writerow([2,"Ram", "How to lead"])
    handle.writerow([3,"Raj", "Run for success"])

# Lines=[["SID","Stuname", "Contibution"]
# [1,"ravi","how to win"]
# [2,"Ram", "How to lead"]
# [3,"Raj", "Run for success"]]
# with open(book2.csv,'w') as file:


