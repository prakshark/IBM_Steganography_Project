import cv2
import os
import string

img=cv2.imread("flower.jpg")
msg=input("Enter Secret Message: ")
password=input("Enter a Passcode: ")

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)

n=0;
m=0;
z=0;

for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+10
    m=m+n
    z=(z+m)%3

cv2.imwrite("EncryptedImg.jpg",img)
os.startfile("EncryptedImg.jpg")
message=""
n=0
m=0
z=0

pas=input("Enter Passcode for decryption: ")
if(password==pas):
    for i in range(len(msg)):
        message=message+c[img[n,m,z]]
        n=n+10
        m=m+n
        z=(z+m)%3
    print("Decrypted Message: ",message)
else:
    print("You are not Authenticated")
