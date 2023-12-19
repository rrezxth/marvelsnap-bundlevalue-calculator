# CONSTANTS, value per $1
TOKEN_VALUE = 100
CREDIT_VALUE = 175
GOLD_VALUE = 140


class PayMoneyBundle:
    def __init__(self, price, token, credit, gold):
        self.price = price
        self.token = token
        self.credit = credit
        self.gold = gold
        self.value = 0

    def calculate_value(self):
        if self.token > 0:
            self.value += self.token / TOKEN_VALUE
        if self.credit > 0:
            self.value += self.credit / CREDIT_VALUE
        if self.gold > 0:
            self.value += self.gold / GOLD_VALUE

    def get_value(self):
        return str(round(self.value, 2))

    def percentage_value(self):
        percentage = (self.value / self.price) * 100
        return str(round(percentage, 2))


class PayGoldBundle:
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

    def percentage_value(self):
        gold_value = self.price / GOLD_VALUE
        token_value = self.token / TOKEN_VALUE
        credit_value = self.credit / CREDIT_VALUE

        currencies_value = token_value + credit_value

        percentage = (currencies_value / gold_value) * 100
        return str(round(percentage, 2))


if __name__ == '__main__':
    user_input = input("Enter values:\t")
    input_list = user_input.split()
    input_numbers = [int(i) for i in input_list]

    # bundle = PayMoneyBundle(input_numbers[0], input_numbers[1], input_numbers[2], input_numbers[3])
    # bundle.calculate_value()
    # print(f"Bundle value percentage:    {bundle.percentage_value()}%")
    # print(f"Bundle is worth:    ${bundle.get_value()}")

    bundle = PayGoldBundle(input_numbers[0], input_numbers[1], input_numbers[2])
    bundle.calculate_value()
    print(f"Bundle value percentage:    {bundle.percentage_value()}%")
    print(f"Bundle is worth:    ${bundle.get_value()}")
