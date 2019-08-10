x,p=list(map(int,input().split(' ')))
per = 0
fr = 0
while x>0:
  per=(p*x)/100
  x=int(x-per)
  fr+=1
 print(fr)
 
