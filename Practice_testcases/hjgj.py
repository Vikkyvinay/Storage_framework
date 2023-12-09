"""

a=[[1,2,3,4][9,8,7,6][4,3,2,1][4,5,6,7][6,7,8,9]]

import re
a="192.168.0.134,547.876.876.987"

inp = "(\d+).(\d+).(\d+).(\d+)"
out = re.search(a,inp)
if out:

a=[1,2,5,8,0,56]
for i in a:


list1 = [[1, 2, 3, 4], [4, 3, 2, 1], [9], [1, 2, 7, 9]]
for i in range(len(list1)):
    list1 [i] [-1] = 5
print(list1)


list1 = [[1,2,3,4],[4,3,2,1],[1,5,9,9],[9],[1,2,7,9]]
for i in list1:
    num = int("".join(map(str, i)))
    num += 1
    new_list = list(map(int, str(num)))
    print(new_list)


n = int(input("Enter number: "))
out = True
if n <= 1:
    print("Not a prime number")
else:
    for i in range(2,n):
        if (n%i) == 0:
            out = False
            break
    if out:
        print("Prime number")
    else:
        print("Not a prime number")


for i in range(5, 0, -1):
    print(str(i)*i)


n=20
count = 0
for a in range(n):
    b = n - a
    count += 1
    print([a,b], count)



str1 = "abababcdbab"
str2 = "ab"

count = str1.count(str2)
print(count)

count = 0
for i in range(len(str1) - len(str2)+1):
    if str1[i:i + len(str2)] == str2:
        count += 1
print(count)


data={12:100,13:500,14:800}
a=0
out={}
for i in data.values():
    if i>a:
        a=i
for j,k in data.items():
    if k==a:
        out[j] = k
print(out)


import pytest

@pytest.mark.parametrize("n, out",[(1,11),(2,22),(3,33)])
def test_multi(n, out):
    assert 11*n == out

def test_add(2,3):
    assert


r=["sdp","sdb","sdk","sde","sdh"]
e=["sda","sdb","sdc","sde","sdh"]
for i in r:
    if i in e:
        c=1
    else:
        c=2
    if c==1:
        print(f"the drive{i} in both")
    else:
        print(f"the drive{i}not in e")

# create a one class and calculate number of objects

class product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        product.count += 1


inp = product("TV", 2000)
inp2 = product("phone", 2000)

obj1 = product.count

print("items order: ", obj1)


import os

file = os.rename("fwversion_currentdateandtime.txt", "new_file1.txt")
# print(file.read())
# for i in file:
#     print(i)
# file.write("append the next content")
# file.close()


class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def Dog2(self):
        return f"{self.name}"
# Local attributes
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
# Accessing class attributes
print(f"Rodger is a {Rodger.attr1}")
print(f"Tommy is also a {Tommy.attr1}")
# Accessing Instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
# Accessing Local attributes
print(Rodger.Dog2())
print(Tommy.Dog2())


# 1.  Take two list and convert to a dictionary?

l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
dict = {}
for i in range(len(l1)):
    dict[l1[i]] = l2[i]

print(dict)

# 2.  write a python program to generate 3 files in a folder every 1hr
#     but next every hour 1 file got missed print that file name?

import os

folder = "newfolder"

file_path = os.path.join(folder, "new_file.txt")
try:
    os.mkdir(folder)
    with open(file_path,"w") as file:
        print(f"file{file_path}")
except Exception as e:
    print(f"an error occcured:{e}")

# 3.   write a program for open a file read the content?

import os

folder = "newfolder"
file_path = os.path.join(folder, "new_file.txt")

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


# 4.  write a program to open a file, in that file there is number of alphabets and
#     integers if when ever you can read the if integer apper exit from the file?


"""
# Python Program to find no.of occurances of each character in string with out inbuilt
str1 = "this is python"

freq = {}
for char in str1:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)
# for char, count in freq.items():
#     print(char, count)

# Remove all white spaces from above string
str1 = "This is python"
# out = str1.replace(" ", "")
# print(out)

out1 = ""
for i in str1:
    if i != " ":
        out1 += i
print(out1)


# Convert all even index to upper and odd index to lower characters in below string
str1 = "python"
out = ""
for i in range(len(str1)):
    if i % 2 == 0:
        out += str1[i].upper()
    else:
        out += str1[i].lower()
print(out)

# Arrange above list to ascending order without using creating another list
list1 = [1, 10, 2, 11, 4]
out = list1.




