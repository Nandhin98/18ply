  n=int(input())
 l=[]
 c=0
 k="kabali"
 a=sorted(k)
 for i in range(n):
  	s=input()
	 l.append(s)
 for i in l:
  	if sorted(i)==a:
  		c=c+1
 print(c)
