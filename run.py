a=open("file1.txt","r")
b=open("file2.txt","r")
data_b=b.read()
data_a=a.read()
a.close()
b.close()
a=open("file1.txt","w")
b=open("file2.txt","w")
a.write(data_b)
b.write(data_a)
a.close()
b.close()
print( data_a )
print( data_b )