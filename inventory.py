
#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        output = "\n"
        output += "________________________________________________"
        output += f"\nCountry: {self.country}\n"
        output += f"Code: {self.code}\n"
        output += f"Product: {self.product}\n"
        output += f"Cost: {self.cost}\n"
        output += f"Quantity: {self.quantity}\n"
        output += "________________________________________________"
        output += "\n"
        return output

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt", "r", encoding="utf-8") as f:
            next(f)  # skip the header line 
            for line in f:  # loop through every remaining line                
                country, code, product, cost, quantity = line.split(",")
                cost = float(cost)
                quantity = int(quantity)
                shoe_list.append(Shoe(country,code,product,cost, quantity))
        
    except FileNotFoundError:
        print("File not found")
        
def capture_shoes():    
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    print("SHOE CAPTURE\n")
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")
    shoe_list.append(Shoe(country, code, product, cost, quantity))

def view_all():    
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    sorted_stock = sorted(shoe_list, key=lambda Shoe: Shoe.quantity) # sort by quantity
    print("\nShoe stock with lowest quantity:")
    shoe = sorted_stock[0] # shoe with lowest stock 
    print(shoe)
    update_stock = input("Would you like to update the quantity? (Y/N): ")
    if update_stock == "Y":
        amount = int(input("Quantity to add: "))
        shoe.quantity += amount
        with open("inventory.txt", "w", encoding="utf-8") as f: # Updating file
            f.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code = input("Enter shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)

def value_per_item():    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoe in shoe_list:
        print(f"Shoe: {shoe.product}")
        print(f"Value: {shoe.cost * shoe.quantity}\n")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    sorted_stock = sorted(shoe_list, key=lambda Shoe: Shoe.quantity, reverse=True) # sort by quantity highest to lowest
    print("Product with highest quantity (ON SALE!)")
    print(sorted_stock[0])
    

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    print("\n==================== SHOE INVENTORY MENU ====================")
    print("1. Read shoe data from file")
    print("2. Capture a new shoe")
    print("3. View all shoes")
    print("4. Re-stock (lowest quantity shoe)")
    print("5. Search for a shoe by code")
    print("6. View value per item")
    print("7. View highest quantity shoe (ON SALE)")
    print("8. Exit")
    print("===============================================================")

    choice = input("Please select an option (1-8): ")

    if choice == "1":
        read_shoes_data()
        print("Shoe data loaded from file.")

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        view_all()

    elif choice == "4":
        re_stock()

    elif choice == "5":
        search_shoe()

    elif choice == "6":
        value_per_item()

    elif choice == "7":
        highest_qty()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid selection. Please choose a number between 1 and 8.")