# CONSTANTS, value per 1 unit
TOKEN_TO_GOLD = 1.3     # 1 Token = 1.3 Gold
CREDIT_TO_GOLD = 0.8    # 1 Credit = 0.8 Gold
MONEY_TO_GOLD = 85      # $1 = 85 Gold


class BundleBase:
    def __init__(self, cost, token, credit):
        self.cost = cost
        self.token = token
        self.credit = credit
        self.gold_value = 0  # The value is in Gold currency

    def calculate_value(self):
        self.gold_value = 0    # Reset
        if self.token > 0:
            self.gold_value += self.token * TOKEN_TO_GOLD
        if self.credit > 0:
            self.gold_value += self.credit * CREDIT_TO_GOLD

    def calculate_bundle_worth(self):
        return round(self.gold_value, 2)


class PayMoneyBundle(BundleBase):
    def __init__(self, cost, token, credit, gold):
        super().__init__(cost, token, credit)
        self.gold = gold
        self.calculate_value()

    def calculate_value(self):
        self.gold_value = 0  # Reset
        super().calculate_value()
        if self.gold > 0:
            self.gold_value += self.gold

    def percentage_value(self):
        percentage = ((self.calculate_bundle_worth() / MONEY_TO_GOLD) / self.cost) * 100
        return str(round(percentage, 2))

class PayGoldBundle(BundleBase):
    def __init__(self, cost, token, credit):
        super().__init__(cost, token, credit)
        self.calculate_value()      # Run here during __init__ since no calculate_value() method

    def percentage_value(self):
        percentage = (self.calculate_bundle_worth() / self.cost) * 100
        return str(round(percentage, 2))


if __name__ == '__main__':

    # Should prolly be a LOOP and an ELSE here
    selection = input("Pay with:\t")
    if selection == "m":    #Pay with money
        print("Format: [USD_COST, TOKEN, CREDIT, GOLD]")
        user_input = input("Enter values:\t")
        input_list = user_input.split()
        input_numbers = [int(i) for i in input_list]

        bundle = PayMoneyBundle(input_numbers[0], input_numbers[1], input_numbers[2], input_numbers[3])
        print(f"\nBundle's GOLD value:\t\t\t{bundle.gold_value:.2f}".rstrip('0').rstrip('.') + f" GOLD -- > You paid ${bundle.cost}")
        print(f"Bundle TOTAL GOLD Value %:\t\t{bundle.percentage_value()}%")
    elif selection == "g":
        print("Format: [GOLD_COST, TOKEN, CREDIT]")
        user_input = input("Enter values:\t")
        input_list = user_input.split()
        input_numbers = [int(i) for i in input_list]

        bundle = PayGoldBundle(input_numbers[0], input_numbers[1], input_numbers[2])
        print(f"\nBundle's GOLD value:\t\t\t{bundle.gold_value:.2f}".rstrip('0').rstrip('.') + f" GOLD -- > You paid {bundle.cost} GOLD")
        print(f"Bundle TOTAL GOLD Value %:\t\t{bundle.percentage_value()}%")





