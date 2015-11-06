x = ['Vijay Nirmal',28,'M','30/11/1986']
y = ['Karthick',28,'M','15/12/1986']
z = [x,y]
print ("Vijay's details are " + str(z[0]))
print ("Vijay is a ", str(x[-2]))
print ("Hello"[1])

year = input("Enter the Year ")
month = int(input("Enter the Month "))
day = int(input("Enter the day "))

monthlist = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
endings = ['st','nd','rd'] + 17*['th'] + ['st','nd','rd'] +7*['th'] + ['st']

formatted_month = monthlist[month - 1]
formatted_day = day -1
new_day = str(day) + endings[formatted_day]

print ("The formatted date is " + new_day + " " + formatted_month + " " + year)
