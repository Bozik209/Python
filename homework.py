def onedigit(num):
    if num==1:
        print('one')
    if num==2:
        print('two')
    if num==3:
        print('three')
    if num==4:
        print('four')
    if num==5:
        print('five')
    if num==6:
        print('six')
    if num==7:
        print('seven')
    if num==8:
        print('eight')
    if num==9:
        print('nine')
def twodigit(num):
    sumOfnum=int(num/10)+(num%10)
    print(num ,"is 2 digit number, sum is", sumOfnum)
def threedigit(num):
    sum1=int(num%10)
    sum2=int(num/10)%10
    sum3=int((num/10)/10)%10
    sumOfnum=sum1*sum2*sum3
    print(num ,"is 3 digit number, mul is", sumOfnum)

num=int(input("Enter number: "))

if num<10:
    onedigit(num)

if num>10 and num<100:
    twodigit(num)

if num>100 and num<1000:
    threedigit(num)

if num>1000:
    print("Number has more than 3 digits")
