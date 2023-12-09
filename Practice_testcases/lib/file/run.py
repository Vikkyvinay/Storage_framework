
import json
total_amount=0
with open("sample.json") as file1:
    out=json.load(file1)
out1=[]
out2=[]
for i,j in out.items():
    for a in j:
        for x,y in a.items():
            if x == "price":
                total_amount += y
                out1.append(y)
            elif x == "product_name":
                out2.append(y)
out2.insert(0,"total amount price")
out1.insert(0,total_amount)
import csv
with open("test.csv", "w",newline='') as file2:
    writer = csv.writer(file2)
    writer.writerow(out2)
    writer.writerow(out1)




class Product:
    pass
class ElectronicItem(Product):
    pass
class Laptop(ElectronicItem):
    pass
