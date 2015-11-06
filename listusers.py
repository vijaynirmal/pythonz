user_name = ['Vijay','Karthick','Justin']
pin_codes = ['07054','600090','600041']
pair1 = [user_name[0] , pin_codes[0]] 
pair2 = [user_name[1],pin_codes[1]] 
pair3 = [user_name[2],pin_codes[2]]
pairs = [pair1,pair2,pair3]
x = input("Enter the User Name ")
y = input("Enter the PIN code ")
if [x,y] in pairs : print ("Access Granted")
else : print("Access Denied")
