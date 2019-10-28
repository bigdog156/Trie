data = open("mean.txt",'r+')

data.seek(0,2)
string = "yeu thich\n" 
data.write(string)
lenStr = len(string)
x = data.tell() - lenStr
print(x)
data.seek(x)
load = data.readline()
print(load)
# tem = data.readline()
# print(tem)