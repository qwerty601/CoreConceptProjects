# Expense Tracker
l=[]
while True:
    print("------MENU------")
    print("Press 1 --> Add Expenses")
    print("Press 2 --> View all Expenses")
    print("Press 3 --> View Total expenses")
    print("Press 4 --> Exit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        d=input("Enter the date of Expense: ")
        i=input("Enter the product name you bought: ")
        c=input("Enter the category of the product (like clothing, electronics, etc.): ")
        p=float(input("Enter the price of product you bought: "))
        l.append({"Date": d,"item": i,"Category": c,"Price": p})
    elif(choice==2):
        if(len(l)==0):
            print("Jao pehle kharcha karo!")
        else:
            count=1
            for eachkharcha in l:
                print(f"Kharcha no.- {count}")
                for key, value in eachkharcha.items():
                    print(f"{key}: {value}")
                count+=1
    elif(choice==3):
        total_expense=0
        for eachkharcha in l:
            total_expense+=eachkharcha["Price"]
        print(f"Your Total Expense is: {total_expense}")
    elif(choice==4):
        print("Thank You for using our Expense Tracker App.")
        break
