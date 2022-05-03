#Author:Deanna Brown
#Date Created:April 9,2022
#Course: ITT103
#Purpose:The purpose of this program is to calculate and print the commision of a sales person

Class=input("input Class(1-3) or zero to end program: ")
if Class =="0"or Class ==" 0" or Class =="0 ":
    quit()

salesperson_number=input("input sales person number:")
sales_amount=input("input sales_amount: ")
if salesperson_number==""  or sales_amount=="" or Class=="":
    print("please make sure u have entered a value for each section ")
else:
    sales_amount=int(sales_amount)
    salesperson_number=int(salesperson_number)
    Class=int(Class)
    if Class ==1:
        if sales_amount <= 1000:
            print('commission =',sales_amount*0.06)
        elif  sales_amount > 1000 and  sales_amount< 2000:
            print('commission =',sales_amount*0.07)
        elif sales_amount >= 2000:
            print('commission =',sales_amount*0.1) 
    if Class ==2:
        if sales_amount <= 1000:
            print('commission =',sales_amount*0.04)
        else:
            print('commission =',sales_amount*0.06)

    if Class ==3:
        print('commission =',sales_amount*0.045)
    
    if Class >3 or Class<0:
        print('invalid Class,Choose between Class 1-3')

    

 
    

   

