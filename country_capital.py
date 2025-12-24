countries = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "Australia": "Canberra",
    "Canada": "Ottawa",
    "Egypt": "Cairo",
    "Italy": "Rome",
    "United Kingdom": "London"
}

user_input = input("Enter a country name: ")

if user_input in countries:
    capital = countries[user_input]
    print(capital)
else:
    print("is not in the database.")