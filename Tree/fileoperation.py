from os.path import getsize

# f=open('data.txt','w')
# f.write('This line:1')
# f.close()

f=open('data.txt','r')
print(f.read())
f.close()

f=open('data.txt','a')
f.write("\n An this line:12")
f.close()

f=open('data.txt','r')
for line in f:
    print(line.strip())
f.close()

f=open('data.txt','r')
for i in range(getsize('data.txt')):
    f.seek(i)
    print(f"Byte: {i} : \t {f.read(1)}")
f.close()

