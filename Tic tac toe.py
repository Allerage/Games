#!/usr/bin/env python
# coding: utf-8

      
        
    

    
    


# In[7]:


n=["-","-","-","-","-","-","-","-","-"]
win_sit=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,5,7]]
def display_board(n):
    for i in range(0,len(n),3):
        print(n[i]+"|"+n[i+1]+"|"+n[i+2])
display_board(n) 
choice=[]
k=input("Choose X or 0")
if k=='X':
    choice.append("X")
    choice.append("0")
else:
    choice.append("0")
    choice.append("X")
    
flag=1
count=0
i=0
game_status=True
x_choose=[]
y_choose=[]
winner=""
while game_status:
    
    
    if(choice[i]=='X'):
        print("X Turn")
        xp=int(input("Enter the postion from 1 to 9"))
        x_choose.append(xp)
        print(x_choose)
        n[xp-1]='X'
        count+=1
        display_board(n)
        i+=1
        x_choose.sort()
        if(x_choose in win_sit ):
            print("-")
            game_status=False
            winner="X"
            flag=1
            
    else:
        print("0 Turns")
        zp=int(input("enter the postion from 1 to 9"))
        y_choose.append(zp)
        n[zp-1]="0"
        count+=1
        display_board(n)
        i-=1
        y_choose.sort()
        if(y_choose in win_sit ):
            print("-")
            game_status=False
            winner="Y"
            break
            
print(winner)            
        
    
   


# # 

# In[6]:


win_sit=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,5,7]]
n=[7,5,1]
n.sort()
print(n)
print(n.sort() in win_sit)


# In[ ]:




