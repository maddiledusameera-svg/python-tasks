'''n=int(input())
for i in range(1,n+1):
    for j in range(1,(2*n)+1):
        print("*",end=" ")
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,(2*n)+1):
        if i==1 or i==n or j==1 or j==2*n :
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print()'''

'''print("*")
print("*")
print("*","3",sep="?")'''



'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if  i==n or j==1 or j==i or i==1:
            print('*',end=' ')
        else:
            print(" ",end=' ')
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print("*",end=' ')
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        if i==1 or i==n or j==n+1 or j==i+1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()'''

'''n=int(input())
for i in range (1,n+1):
    for j in range(n+1,i+1,-1):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(n+1,i+1,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        if i==n or k==1 or k==i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=' ')
    for k in range(n+1,i,-1):
        print("*",end=' ')
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=' ')
    for k in range(n+1,i,-1):
        if (i==1 or k==i+1 or k==n+1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=' ')
    for k in range(1,2*i):
        print("*",end=" ")
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=' ')
    for k in range(1,2*i):
        if i==n or k==1 or k==(2*i)-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=' ')
    for k in range((2*n)-i,i-1,-1):
        print("*",end=' ')
    print()'''
#upsiden down half diamond

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=' ')
    for k in range((2*n)-i,i-1,-1):
        if i==1 or k==(2*n)-i or k==i :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or i==(n//2)+1 or j==(n//2)+1 or j==1 or j==n or i==j or i+j==n+1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==(n//2)+1 and j==(n//2)+1 or i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n=int(input())
spaces=(n//2)
stars=1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(" ",end=' ')
    for k in range(1,stars+1):
        if i==1 or i==n or k==1 or k==stars :
            print("*",end=' ')
        else:
            print(" ",end=' ')
       
    print()
    if i<(n//2)+1:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2'''


'''n=int(input())
spaces=(n//2)
stars=1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(" ",end=' ')
    for k in range(1,stars+1):
        if i==1 or i==n or k==1 or k==stars or i==(n//2)+1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
       
    print()
    if i<(n//2)+1:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2'''

'''n=int(input())
spaces=(n//2)
stars=1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(" ",end=' ')
    for k in range(1,stars+1):
        if i==1 or i==n or k==1 or k==stars or i==(n//2)+1 or k==(stars//2)+1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
       
    print()
    if i<(n//2)+1:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2'''

'''n=int(input())
spaces=(n//2)
stars=1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(" ",end=' ')
    for k in range(1,stars+1):
        if i==1 or i==n or k==1 or k==stars or i==(n//2)+1 and k==(n//2)+1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
       
    print()
    if i<(n//2)+1:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2'''

'''n=int(input())
stars=n
spaces=0
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(" ",end=" ")
    for k in range(1,stars+1):
        print("*",end=" ")
    print()
    if i<(n//2)+1:
        stars-=2
        spaces+=1
    else:
        stars+=2
        spaces-=1


n=int(input())
stars=n
spaces=0
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(" ",end=" ")
    for k in range(1,stars+1):
        if  k==1 or k==stars:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()
    if i<(n//2)+1:
        stars-=2
        spaces+=1
    else:
        stars+=2
        spaces-=1'''

#number patterns
'''n=int(input())
for i in range(n,0,-1):
    for j in range(1,n+1):
       print(i,end=" ")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
       print(i,end=" ")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
       print(j,end=" ")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
       print(j,end=" ")
    print()'''

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=' ')
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(j,end=' ')
    print()'''

'''n=int(input())
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end=' ')
    print()


n=int(input())
spaces=n-1
for i in range(n,0,-1):
    for j in range(1,spaces+1):
        print(" ",end=" ")
    for k in range(i,n+1):
        print(k,end=' ')
    print()
    spaces -= 1'''

'''n=int(input())
spaces=n-1
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(" ",end=' ')
    for k in range(i,0,-1):
        print(k,end=' ')
    print()
    spaces-=1

n=int(input())
spaces=0
for i in range(1,n+1):
    for j in range(1,spaces+1):
        print(' ',end=' ')
    for k in range(n,i-1,-1):
        print(k,end=' ')
    print()
    spaces+=1'''


n=int(input())
spaces=n-1
for i in range(n,0,-1):
    for j in range(1,spaces+1):
        print(" ",end=' ')
    for k in range(n,i-1,-1):
        print(k,end=' ')
    print()
    spaces-=1
