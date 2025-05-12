print("enter the data")

d1 = int(input("enter the data d1 : "))
d2 = int(input("enter the data d2 : "))
d3 = int(input("enter the data d3 : "))
d4 = int(input("enter the data d4 : "))

p1 = d1 ^ d2 ^ d4
p2 = d1 ^ d3 ^ d4
p3 = d2 ^ d3 ^ d4 

encoded = [p1,p2,d1,p3,d2,d3,d4]
print("encoded data is : ", encoded)

print("enter the recived data")

recieved = []
for i in range(7):
    print("enter the data at postion : ", i+1)
    recieved.append(int(input()))
    print("received data is : ", recieved)

c1 = recieved[0] ^ recieved[2] ^ recieved[4] ^ recieved[6]
c2 = recieved[1] ^ recieved[2] ^ recieved[5] ^ recieved[6]
c3 = recieved[3] ^ recieved[4] ^ recieved[5] ^ recieved[6]

error = c1*1 + c2*2 + c3*4

if error == 0:
    print("no error detected")
else:
    print("errot detecte at psotion : ", error)
    recieved[error-1]^=1
    print("corrected data id : ",recieved)

original = [recieved[2], recieved[4], recieved[5],recieved[6]]
print("original data is : ", original)