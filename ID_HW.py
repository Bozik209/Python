def funcname(idUser,check):
        i=0
        sumnum=0
        temp=0
        while i<9:
                temp=int(int(idUser[i])*int(check[i]))
                if temp/2!=0:
                        temp=temp%10+int(temp/10)
                sumnum+=temp
                temp=0
                i+=1

        if sumnum%10==0:
                print("Your ID is valid")
        else:
                print("Your ID is FAKE!!")      
                



idUser=list(input("Enter youer ID:"))
if len(idUser)==8:
        idUser.insert(0,0)
        
check= [1,2,1,2,1,2,1,2,1]
funcname(idUser,check)
