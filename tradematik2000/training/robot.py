import numpy as np

class robot:
    def __init__(self):
        return

    def take_action(self, wallet, current_price):
        action = self.decide_action()
        
        asset = "BTC"

        if action == 1:
            amount = self.decide_amount(wallet,'USD')
            if amount > 0 :
                asset_amount_to_be_purchased = round(amount/current_price[asset],10)
                print(f"Robot has decided to buy {asset_amount_to_be_purchased} amount of {asset} with {amount} USD")
                decision = [1,asset_amount_to_be_purchased, -amount]
            else:
                print(f"Robot has decided buy but the funds are not sufficient")
                decision = [0,0,0]
            return decision
            
        elif action == 0:
            print(f"Robot has decided not to take any action")
            decision = [0,0,0]
            return decision

        elif action == -1:
            amount = self.decide_amount(wallet,'BTC')
            if amount > 0 :
                asset_amount_to_be_sold = round(amount/current_price[asset],10)
                print(f"Robot has decided to sell {asset_amount_to_be_sold} amount of {asset} for {amount} USD")
                decision = [-1,-asset_amount_to_be_sold,amount]
            
            else:
                print(f"Robot has decided sell but the funds are not sufficient")
                decision = [0,0,0]
            return decision



        
    def decide_action(self):
        action_space = [-1,0,1]
        selected_action = np.random.randint(-1,2)
        return selected_action


    def decide_amount(self,wallet,name):
        minimum_amount = 0.001
        maximum_amount = wallet.asset_amount(name)

        if maximum_amount>0:
            selected_amount = np.random.uniform(minimum_amount,maximum_amount)
            return selected_amount
        else:
            return 0