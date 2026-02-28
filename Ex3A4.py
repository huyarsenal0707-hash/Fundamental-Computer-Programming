cities_list = []
for i in range(5):
    city = input(f"Enter city {i+1}: ")
    cities_list.append(city)
print("The cities you entered are: ")
for city in cities_list:
    print(city)
    