'''item="fried rice"
price=40
rating=4.5
is_veg=True
print(type(item))
print(type(price))
print(type(rating))
print(type(is_veg))


menu=["Dosa","Idli","Samosa"]
print(type(menu))


print(menu[2])
print(menu[1])
menu.append("Vada")
menu[1]="puri"
menu[2]="Egg puff"
print(menu)
menu.remove("Dosa")
print(menu)

#print(item)
#print(price)
#print(item,"cost=",price)

working_days=("Monday","Tuesday","Wednesday","Thursday","Friday")

print(working_days[2])
'''


prices = {
    "Dosa": 40,
    "Idli": 30,
    "Idli": 35,
    "Samosa": 15
}
prices["Vada"]=25
#prices["Idli"]=35
prices.pop("Samosa")
print(prices)


#print(prices["Dosa"])
#print(prices["Samosa"])
