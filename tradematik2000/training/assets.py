class asset:
    def __init__(self, name, amount, current_price):
        self.name = name
        self.amount = amount
        self.current_price = current_price
        self.value = amount * current_price


    def update(self,action,amount):
        return


class wallet:
    def __init__(self):
        self.holdings = dict()

    def add_new_asset(self, asset):
        self.holdings[asset.name] = [asset.amount, asset.current_price, asset.value]

    
    def show_assets(self):
        print(self.holdings)