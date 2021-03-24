from training.assets import wallet
from training.robot import robot
from training.data import read_data
from training.settings import TRAINING_DATA_PATH



def game():

    print('Simulation has initialized')
    my_wallet = wallet()
    tradematik = robot()
    assets_in_scope = ['USD','BTC']
    price_dict = dict()

    for a in assets_in_scope:
        my_wallet.add_new_asset(a)
        price_dict[a] = 1

    my_wallet.update_asset('USD',1000)
    my_wallet.show_assets()
    
    training_df = read_data(TRAINING_DATA_PATH)
    n_data = len(training_df)

    print(f"Size of the data set: {n_data}")

    total_portfolio_value = dict()
    total_portfolio_value[0] = 1000

    for i in range(1,1000):

        print(f'\nStep {i} is started')
        current_price = training_df['open'][i]
        print(f"Current price of bitcoin is {current_price}")
        
        price_dict['BTC'] = current_price
        total_portfolio_value[i] = my_wallet.total_assets(price_dict)
        print(f"Total portfolio value is now: {total_portfolio_value[i]}")
        reward = total_portfolio_value[i] - total_portfolio_value[i-1]
        print(f"Reward: {reward}")
        decision = tradematik.take_action(my_wallet,price_dict)

        
        my_wallet.update_asset('USD',decision[2])
        my_wallet.update_asset('BTC',decision[1])
        my_wallet.show_assets()

        

        


    


