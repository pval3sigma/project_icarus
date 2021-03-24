class wallet:
    def __init__(self):
        self.holdings = dict()

    def add_new_asset(self, name):
        self.holdings[name] = 0
        print(f'Asset for {name} is created with 0 amount')


    def update_asset(self,asset,amount):
        self.holdings[asset] = self.holdings[asset] + amount
        print(f'Value of {asset} has changed to {self.holdings[asset]}')

    def total_assets(self,current_price_dict):
        total_asset_val = 0
        for asset in self.holdings.keys():
            total_asset_val += self.holdings[asset] * current_price_dict[asset]
        return total_asset_val
     
    def asset_amount(self,name):
        asset_amount = self.holdings[name]
        return asset_amount

    def show_assets(self):
        print(self.holdings)