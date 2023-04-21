# import json
import csv

# with open("name.json",'r') as filehandle:
#     dict = json.load(filehandle)
# print(dict)
# person_dict = {"name": "Bob",
# "languages": ["English", "French"],
# "married": True,
# "age": 32}
#
# with open("name.jason",'w') as filehandle:
#     json.dump(person_dict,filehandle)
# print(dict)
# csv.register_dialect('all',
#                      delimiter='|',
#                      skipinitialspace=True,
#                      quoting=csv.QUOTE_ALL)
# with open("name.csv",'r') as csvhandle:
#     contents = csv.DictReader(csvhandle)
#     for line in contents:
#         print (line)
with open("name1.csv",'w') as file:
    handle = csv.writer(file)
    handle.writerow(["SID",'sname','contribution'])
    handle.writerow([1,"raki","how to get"])
    handle.writerow([2, "rogh", "how to live"])
    handle.writerow([2, "rama", "how to survive"])
