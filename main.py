# CONSTANTS, value per $1
TOKEN_VALUE = 42.85714
CREDIT_VALUE = 75
GOLD_VALUE = 60


class BundleBase:
    def __init__(self, price, token, credit):
        self.price = price
        self.token = token
        self.credit = credit
        self.value = 0

    def calculate_value(self):
        if self.token > 0:
            self.value += self.token / TOKEN_VALUE
        if self.credit > 0:
            self.value += self.credit / CREDIT_VALUE

    def get_value(self):
        return str(round(self.value, 2))


class PayMoneyBundle(BundleBase):
    def __init__(self, price, token, credit, gold):
        super().__init__(price, token, credit)
        self.gold = gold

    def calculate_value(self):
        super().calculate_value()
        if self.gold > 0:
            self.value += self.gold / GOLD_VALUE

    def percentage_value(self):
        percentage = (self.value / self.price) * 100
        return str(round(percentage, 2))


class PayGoldBundle(BundleBase):
    def __init__(self, price, token, credit):
        super().__init__(price, token, credit)

    def percentage_value(self):
        gold_value = self.price / GOLD_VALUE
        currencies_value = self.value

        percentage = (currencies_value / gold_value) * 100
        return str(round(percentage, 2))


if __name__ == '__main__':

    selection = input("Pay with:\t")
    if selection == "d":
        print("Format: [USD, TOKEN, CREDIT, GOLD]")
        user_input = input("Enter values:\t")
        input_list = user_input.split()
        input_numbers = [int(i) for i in input_list]

        bundle = PayMoneyBundle(input_numbers[0], input_numbers[1], input_numbers[2], input_numbers[3])
        bundle.calculate_value()
        print(f"Bundle value percentage:    {bundle.percentage_value()}%")
        print(f"Bundle is worth:    ${bundle.get_value()}")
    else:
        print("Format: [GOLD, TOKEN, CREDIT]")
        user_input = input("Enter values:\t")
        input_list = user_input.split()
        input_numbers = [int(i) for i in input_list]

        bundle = PayGoldBundle(input_numbers[0], input_numbers[1], input_numbers[2])
        bundle.calculate_value()
        print(f"Bundle value percentage:    {bundle.percentage_value()}%")
        print(f"Gold spent is worth:    ${str(round(input_numbers[0]/140, 2))}")
        print(f"Bundle is worth:    ${bundle.get_value()}")





