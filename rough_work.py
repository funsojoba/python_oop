# The entry point of you application
from assets import art
from data import data


class Printer:
    def __init__(self):
        self.total_ink = data.resources['ink']
        self.total_paper = data.resources['paper']
        self.total_profit = data.resources['profit']

    def get_report(self):
        print(f'''
        Paper   : {self.total_paper}
        Ink     : {self.total_ink}
        Profit  : {self.total_profit}
        ''')

    def take_money(self):
        try:
            biyar = int(input("How many Biyar? "))
            faiba = int(input("How many Faiba? "))
            muri = int(input("How many Muri? "))
            waso = int(input("How many Wasobia? "))

            biya_amount = biyar * 5
            faiba_amount = faiba * 10
            muri_amount = muri * 20
            waso_amount = waso * 50
        except TypeError:
            return "Invalid input"
        except ValueError:
            return "Invalid input"

        return sum([biya_amount, faiba_amount, muri_amount, waso_amount])

    def check_ink(self, quantity, ink):
        return quantity * ink > self.total_ink

    def check_paper(self, quantity, paper):
        return quantity * paper > self.total_paper

    def calc_price(self, quantity, color_cost):
        return quantity * color_cost

    def check_money(self, quantity, ink, color_cost):
        self.quantity = quantity
        self.ink = ink
        self.color_cost = color_cost

        calculated_price = self.calc_price(self.quantity, self.color_cost)
        take_money = self.take_money()

        difference = take_money - calculated_price

        if take_money > calculated_price:
            print(f"take your change #{difference}")
            self.print_paper(self.quantity, self.ink, self.color_cost)
            self.get_report()
        elif take_money == calculated_price:
            self.print_paper(self.quantity, self.ink, self.color_cost)
            print("Printed . . .")
            self.get_report()
        else:
            print("You don't have enough to print")

    def print_paper(self, quantity, ink, price):
        self.quantity = quantity
        self.ink = ink
        self.price = price

        total_ink = self.ink * self.quantity
        total_price = self.price * self.quantity
        self.total_ink -= total_ink
        self.total_paper -= self.quantity
        self.total_profit += total_price

    def print_printer(self):
        print("Printing . . .")


class ColoredPrinter(Printer):
    def __init__(self):
        super().__init__()
        self.price = data.FORMAT['coloured']['price']
        self.ink = data.FORMAT['coloured']['materials']['ink']

    def print_coloured(self):
        quantity = int(input("How many copies: "))
        print(f"#{self.calc_price(quantity, self.price)}")
        self.check_money(quantity, self.ink, self.price)


class GreyScale(Printer):
    def __init__(self):
        super().__init__()
        self.price = data.FORMAT['greyscale']['price']
        self.ink = data.FORMAT['greyscale']['materials']['ink']

    def print_greyscale(self):
        quantity = int(input("How many copies: "))
        print(f"#{self.calc_price(quantity, self.price)}")
        self.check_money(quantity, self.ink, self.price)


color = ColoredPrinter()
greyscale = GreyScale()
printer = Printer()
# color.print_coloured()


def main():
    while True:
        question = input("What format would you like? ( coloured or grayscale ): ")
        if question.lower() in ['greyscale', 'grayscale']:
            greyscale.print_greyscale()
        elif question.lower() in ['colored', 'coloured']:
            color.print_coloured()
        elif question.lower() == 'report':
            # printer.get_report()
            color.get_report()
        elif question.lower() == 'off':
            print("Thank you for using our service")
            break
        else:
            print("Please input the right option")
            continue

main()

# printer.check_money(10, 5, 25)
# print(printer.get_report())
# printer.check_money(10, 7, 35)
