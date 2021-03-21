import pandas as pd


def read_data(path):
    financial_data = pd.read_csv(path)
    return financial_data


