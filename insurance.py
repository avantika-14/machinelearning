txt="Welcome to Insurance Company"
x=txt.center(120)
print(x)

p={101:234,102:345,103:456,104:567,105:789}
d={101:{"Reuben D'cruz":"car insurance"},102:["Akanksha Singh",["ife insurance","car insurance","property insurance"]],
   103:["Arvika Deewan","property insurance"],104:["Avinash Sharma","life insurance"],105:["Valerie Rodriguez","property insurance"],}

def view_policies():
    #admin
    #customer
    a=True
    while a:
        n=int(input("1.To view life insurance policy\n2.To view car insurance policy\n3.To view property insurance policy\n4.To exit\n"))
        if n==1:
            print("Life insurance is a contract between an insurance policy holder and an insurer or assurer, where the insurer promises to pay a designated beneficiary a sum of money upon the death of an insured person. Depending on the contract, other events such as terminal illness or critical illness can also trigger payment.")
        if n==2:
            print("Car insurance's primary use is to provide financial protection against physical damage or bodily injury resulting from traffic collisions and against liability that could also arise from incidents in the car.")
        if n==3:
            print("Property insurance provides protection against most risks to property, such as fire, theft and some weather damage. This includes specialized forms of insurance such as fire insurance, flood insurance, earthquake insurance, home insurance, or boiler insurance.")
        if n==4:
            a==False
            break
        else:
            print("please enter a valid choice")

def view_customer():
    #admin
    print(d)

def create_customer():
    #admin
    print("the customer ids are",d.keys())
    m=int(input("enter the customer id:"))
    h=input("enter the customer name:")
    s=input("enter the insurance(s):")
    d[m]=[h,s]
    print(d)

def delete_customer():
    #admin
    b=int(input("enter the customer number you wish to delete:"))
    if b in d:
        del(d[b])
        print("the customer is deleted",d)
    else:
        print("please enter a valid choice")

def view_policy():
    #customer
    c=int(input("enter your customer id:"))
    if c in p:
        e=int(input("enter your password:"))
        if p[c]==e:
            print(d[c])
        else:
            print("enter a valid password")
    else:
        print("enter a valid customer id")    

x=True                
while(x):
    ch1=int(input("1.Enter as administrator\n2.Enter as member\n3.Exit\n"))
    if(ch1==1):
        u=input("enter the password:")
        b="1234"
        if u==b:
            y=True
            while(y):
                ch=int(input("1.To check the policy\n2.To see cutomer details\n3.To create new customer\n4.To delete customer\n5.Back to main menu\n"))
                print()
                if(ch==1):
                    view_policies()
                    print()
                elif(ch==2):
                    view_customer()
                    print()
                elif(ch==3):
                    create_customer()
                    print()
                elif(ch==4):
                    delete_customer()
                    print()
                elif(ch==5):
                    y=False
                    break
                else:
                    print("Please enter a valid choice")
                    print()
        else:
            print("please enter a valid password")
            
        
    if(ch1==2):
        y=True
        while(y):
            ch=int(input("1.To view policy\n2.To view your policy\n3.Back to main menu\n"))
            print()
            if(ch==1):
                view_policies()
                print()
            elif(ch==2):
                view_policy()
                print()
            elif(ch==3):
                y=False
                break
            else:
                print("Please enter a valid choice")
                print()
    
    if(ch1==3):
        x=False
    else:
        print("Please enter a valid choice")
