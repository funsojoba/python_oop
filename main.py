from data import data
import colored
import greyscale
from assets import art


class Printer:
    """
    Printer class
    """
    def __init__(self):
        self.total_ink = data.resources['ink']
        self.total_paper = data.resources['paper']
        self.total_profit = data.resources['profit']

        self.greyscale_price = data.FORMAT['greyscale']['price']
        self.greyscale_ink = data.FORMAT['greyscale']['materials']['ink']
        self.coloured_price = data.FORMAT['coloured']['price']
        self.coloured_ink = data.FORMAT['coloured']['materials']['ink']

    def get_report(self):
        return f'''
        Paper  : {self.total_paper}pc
        Ink    : {self.total_ink}ml
        Profit : #{self.total_profit}
        '''

    def take_money(self):
        """
        This method takes money from user in some specific currency type
        Biyar - #5
        Faiba - #10
        Muri - #20
        Wazobia - #50
        """

        try:
            biyar = int(input("How many Biyar? "))
            faiba = int(input("How many Faiba? "))
            muri = int(input("How many Muri? "))
            waso = int(input("How many Wasobia? "))

            biya_amount = biyar * 5
            faiba_amount = faiba * 10
            muri_amount = muri * 20
            waso_amount = waso * 50
        except (TypeError, ValueError):
            return "Invalid input"

        return sum([biya_amount, faiba_amount, muri_amount, waso_amount])

    def print_paper(self, quantity, ink, price):
        total_ink = ink * quantity
        total_price = price * quantity
        self.total_ink -= total_ink
        self.total_paper -= quantity
        self.total_profit += total_price

    def check_ink(self, quantity, ink):
        return quantity * ink <= self.total_ink

    def check_paper(self, quantity):
        return quantity <= self.total_paper

    def total_cost(self, quantity, price_per_page):
        return quantity * price_per_page

    def check_money(self, quantity, price):
        total_cost = price.price * quantity
        inputted_money = self.take_money()
        try:
            if inputted_money > total_cost:
                difference = inputted_money - total_cost
                print(f"Here is #{difference} Naira in change.")
                self.print_paper(quantity, price.ink, price.price)
                print("Here's your project")
            elif inputted_money == total_cost:
                self.print_paper(quantity, price.ink, price.price)
                print("Here's your project")
            else:
                print("Sorry that’s not enough money. Money refunded")
        except TypeError:
            print("seems there's an error, please try again")


printer = Printer()


def printing_machine():
    """
    This function receives the user's option and makes printing decision based on the user's choice
    :return:
    """
    print(art.logo)

    while True:
        option = input("What format would you like? (coloured or grayscale) ")
        if option.lower() in ['colored', 'coloured']:
            try:
                quantity = int(input("How many copies: "))
                if printer.check_ink(quantity, colored.ink):
                    if printer.check_paper(quantity):
                        print('Your price is #',printer.total_cost(quantity, colored.price))
                        printer.check_money(quantity, colored)
                    else:
                        print("Sorry there is not enough paper.")
                else:
                    print("Sorry there is not enough ink.")
            except ValueError:
                print("seems there's an error, please try again")
        elif option.lower() in ['greyscale', 'grayscale']:
            try:
                quantity = int(input("How many copies: "))
                if printer.check_ink(quantity, colored.ink):
                    if printer.check_paper(quantity):
                        print('Your price is #', printer.total_cost(quantity, greyscale.price))
                        printer.check_money(quantity, greyscale)
                    else:
                        print("Sorry there is not enough paper.")
                else:
                    print("Sorry there is not enough ink.")
            except ValueError:
                print("Seems there's an error, please try again")
        elif option.lower() == 'report':
            print(printer.get_report())
        elif option.lower() == 'off':
            print("Thank you for using our service")
            break
        else:
            print("Please input the correct values")
            continue


printing_machine()



