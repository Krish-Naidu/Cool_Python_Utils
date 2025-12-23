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
    print(user_input)
else:
    print("is not in the database.")