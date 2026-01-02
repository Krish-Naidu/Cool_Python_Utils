class ShoppingItem:
    def __init__(self, name):
        self.name = name
        self.purchased = False


class ShoppingList:
    def __init__(self):
        self.items = []
    
    def add_item(self, name):
        item = ShoppingItem(name)
        self.items.append(item)
    
    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return
    
    def mark_purchased(self, name):
        for item in self.items:
            if item.name == name:
                item.purchased = True
                return
    
    def display(self):
        for item in self.items:
            print(item.name)

    def get_purchased_items(self) -> list:
        all_items = self.items
        for shopping_item in all_items:        
            if shopping_item.purchased == True:
                print(shopping_item.name)

# Main program
my_list = ShoppingList()
running = True

while running:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Mark purchased")
    print("4. Show list")
    print("5. view purchased items")
    print("6. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        name = input("Item name: ")
        my_list.add_item(name)
    
    elif choice == "2":
        name = input("Item name: ")
        my_list.remove_item(name)
    
    elif choice == "3":
        name = input("Item name: ")
        my_list.mark_purchased(name)
    
    elif choice == "4":
        my_list.display()

    elif choice == "5":
        my_list.get_purchased_items()

    
    elif choice == "6":
        running = False
