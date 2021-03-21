from training.assets import asset, wallet
from training.robot import robot
from training.data import read_data
from training.settings import TRAINING_DATA_PATH



def game():

    print('Simulation has initialized')
    time = 0
    my_wallet = wallet()
    assets_in_scope = ['USD','BTC']

    for a in assets_in_scope:
        my_wallet.add_new_asset(asset(a,0,0))

    my_wallet.show_assets()

    training_df = read_data(TRAINING_DATA_PATH)
    n_data = len(training_df)

    print(f"Size of the data set: {n_data}")

    for i in range(0,n_data):
        
        print(training_df['open'][i])



    


