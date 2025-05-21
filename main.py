class BundleBase:
    # Values per (1) card
    # Some of these values are approximations -- they are NOT end all be all
    CREDITS_TO_CARD = 9615  # ORIGINAL_VALUE 9950, but lowered due to FREE 200 Tokens from caches
    TOKENS_TO_CARD = 6000
    GOLD_TO_CARD = 7500     # Assuming a 1.25 Gold to Token ratio from Token Tuesday
    MONEY_TO_CARD = 92      # In USD; assuming 1 $Dollar to Gold ratio

    def __init__(self, cost, credit=0, token=0):
        self.cost = cost
        self.credit = credit
        self.token = token
        self.credit_percentage = 0
        self.token_percentage = 0
        self.cost_percentage = 0
        self.value_percentage = 0

    @property
    def show_value(self):
        return self.value_percentage

class PayMoneyBundle(BundleBase):
    def __init__(self, cost, credit, token, gold=0):
        super().__init__(cost, credit, token)
        self.gold = gold
        self.gold_percentage = 0
        self.calculate_and_store_value()

    def calculate_and_store_value(self):
        value_num = 0

        if self.credit:
            self.credit_percentage = (self.credit / self.CREDITS_TO_CARD) * 100
            value_num += self.credit_percentage
        if self.token:
            self.token_percentage = (self.token / self.TOKENS_TO_CARD) * 100
            value_num += self.token_percentage
        if self.gold:
            self.gold_percentage = (self.gold / self.GOLD_TO_CARD) * 100
            value_num += self.gold_percentage

        self.cost_percentage = (self.cost / self.MONEY_TO_CARD) * 100
        self.value_percentage = value_num / self.cost_percentage * 100

class PayGoldBundle(BundleBase):
    def __init__(self, cost, credit, token):
        super().__init__(cost, credit, token)
        self.calculate_and_store_value()

    def calculate_and_store_value(self):
        value_num = 0

        if self.credit:
            self.credit_percentage = (self.credit / self.CREDITS_TO_CARD) * 100
            value_num += self.credit_percentage
        if self.token:
            self.token_percentage = (self.token / self.TOKENS_TO_CARD) * 100
            value_num += self.token_percentage

        self.cost_percentage = (self.cost / self.GOLD_TO_CARD) * 100
        self.value_percentage = value_num / self.cost_percentage * 100


if __name__ == '__main__':

    # Should prolly be a LOOP and an ELSE here
    selection = input("Pay with:\t")
    if selection == "m":    #Pay with money
        print("Format: [USD_COST, CREDIT, TOKEN, GOLD]")
        user_input = input("Enter values:\t")
        input_list = user_input.split()
        input_numbers = [int(i) for i in input_list]

        bundle = PayMoneyBundle(input_numbers[0], input_numbers[1], input_numbers[2], input_numbers[3])
        print(f"Bundle TOTAL Value %:\t\t{bundle.show_value:.2f}%".rstrip('0').rstrip('.'))
    elif selection == "g":
        print("Format: [GOLD_COST, CREDIT, TOKEN]")
        user_input = input("Enter values:\t")
        input_list = user_input.split()
        input_numbers = [int(i) for i in input_list]

        bundle = PayGoldBundle(input_numbers[0], input_numbers[1], input_numbers[2])
        print(f"Bundle TOTAL Value %:\t\t{bundle.show_value:.2f}%".rstrip('0').rstrip('.'))





