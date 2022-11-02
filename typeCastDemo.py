#type cast = convert the data type of a value to another data type

x = 1 #int
y = 2.0 #float
z = '3' #str

x = str(x)
y = float(y)  #use float(), str(), int(), etc. to "typecast" variable to another type.
z = int(z)

x = str(type(x))

print('x is a ' + x)
print(y)
print(z)