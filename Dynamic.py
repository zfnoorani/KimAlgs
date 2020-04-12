

def prob6_25(array,size):
    mySet= set()
    count = 0
    shouldIbreak=False
    for i in range (0,len(array)):
        count += array[i]
    if(count%3==1):
        return False
    #count=count/3
    Matrix = [[[False]*size for x in range(count)] for y in range(count)] 
    #print(Matrix)
    for j in range(0,size):
        val=array[j]
        for k in range(0,count):
            for l in range(0,count):
                Matrix[val][0][0]=True
                Matrix[0][val][0]=True
                Matrix[0][0][0]==True
                if j>0:
                    if Matrix[k][l][j-1]==True:
                        Matrix[k][l][j]=True
                    if Matrix[l][k][j-1]==True:
                        Matrix[l][k][j]=True
                    if Matrix[k][l][j]==False:
                        if Matrix[k-val][l][j-1]==True:
                            Matrix[l][k][j]=True
                    if Matrix[k][l][j]==False:
                        if Matrix[k][l-val][j-1]==True:
                            Matrix[l][k][j]=True
                    if Matrix[l][k][j]==True and l+k==count/3:
                        addition=l,k
                        mySet.add(addition)
                        shouldIbreak=True
                        break
            if shouldIbreak==True:
                    shouldIbreak=False
                    break
        
                


    if len(mySet)>=3:
        return True 
    else: return False

                        

    
    #print(Matrix[20][20][5])

#8,2,10,4,6 - [Tested] We do have a partition
#2,2,3,5    -  [Tested] No partition 
#1,2,3,4,4,5,8 - [Tested] We do have a partition 
arr = [1,2,3,4,4,5,8] 
n = len(arr) 
if prob6_25(arr,n)==True:
    print "We have a 3-Part Partition"
else:
    print "We do not have a 3 part Partition"
  
