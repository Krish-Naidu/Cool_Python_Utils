def get_capital():
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
    
    capital = countries.get(user_input)
    print(capital)
