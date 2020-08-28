def operations():
    global output
    ol=input().split()
    operation=ol[0]
    updater=set(map(int,input().split()))
    if operation=="intersection_update":
        s.intersection_update(updater)
    elif operation=="update":
        s.update(updater)
    elif operation=="symmetric_difference_update":
        s.symmetric_difference_update(updater)
    elif operation=="difference_update":
        s.difference_update(updater)
    output=sum(s)                
input()
s=set(map(int,input().split()))
n=int(input())
for i in range(n):
    operations()
print(output)    
