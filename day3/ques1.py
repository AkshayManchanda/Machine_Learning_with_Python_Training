usa = ['atlanta','new york','chicago','baltimore']
uk = ['london','bristol','cambridge']
india = ['mumbai','delhi','banglore']

'''
#(a)
i=input("Enter city name: ")
if i in usa:
    print('city is in USA')
elif i in uk:
    print('city is in UK')
elif i in india:
    print('city is in INDIA')
else:
    print('idk the country of the city entered!!')
'''
   
#(b)
i=input("Enter 1st city name: ")
j=input("Enter 2nd city name: ")
if (i in usa and j in usa) or (i in uk and j in uk) or (i in india and j in india):
    print("Both are in same country!")
else:
    print("Both are in different countries!")