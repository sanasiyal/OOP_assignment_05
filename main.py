class ATM:
   
 
    def __init__(self,balance = 5000 , pin = 1234) :
        self.balance = balance
        self.pin = pin

    def check_pin(self , input_pin):
        return self.pin == input_pin    

atm = ATM()
             
        #    pin checking

user_pin = int(input("Enter your pin"))
if atm.check_pin(user_pin):
 

  while True:
    print("ATM Menu")  
    print("1. Check balance") 
    print("2. Deposit amount") 
    print("3. Withdraw amount") 
    print("4. Exit") 
    # print("valid pin")

    user_choice = input("Enter your choice in number(1 to 4):  ")

    if user_choice == "1":

     print(f"your current balance is {atm.balance}")


        #   for deposit
    if user_choice == "2":
      dep_amount = int(input("Enter your deposit amount"))

      if dep_amount < 0:
       print("invalid deposite amount")
       exit()

      atm.balance += dep_amount
      print("deposite successfull!")
      print(f"your cenrrent balance is {atm.balance}")


            #   for withdraw
   
    if user_choice == "3":
      withdraw_amount = int(input("Enter your withdraw amount"))

      if withdraw_amount > atm.balance:
       print("invalid withdraw amount")
       exit()


      if atm.balance >= withdraw_amount:
        atm.balance -= withdraw_amount
        print("withdraw successfull")
        print(f"your current balance is {atm.balance}")

    # else:
    #   print("insufficient balane")

    if user_choice == "4": 
       print("Thank you!")

       break

else:
      print("invalid pin") 
   
  

   

    












































# else:
#     print("invalid pin") 

# check_balance = atm.balance

# print(check_balance)


# dep_amount = int(input("Enter your deposite amount"))
# # if user_pin == atm.check_pin():
#    atm.balance += dep_amount
#    print("your amount is added")

# if user_pin != atm.pin:
#     print("you can't be able for deposite")

# else:
#     print("error")

# withdraw_amount = int(input("enter you r withdraw amount"))
# if user_pin == atm.check_pin() and atm.balance >= withdraw_amount:
#     print("your withdrwa is done")

# else:
#     print("insufficient balane")
#     exit()                



      