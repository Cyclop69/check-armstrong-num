def armstrong(a):
  list=[]
  while a>=10:
    list.append(a%10)
    a=a//10
  if a<9:
    list.append(a)
  b=0
  for i in list:
    b=b+i**3
  return b
   

b=int(input("enter the num:"))
j=armstrong(b)
if j==b:
  print("the given num is armstrong")
if j!=b:
  print("the given num is not armstrong")

  
  
  







