import pandas as pd

def get_naive_aov(data_path):
    orders = pd.read_csv(data_path)
    num_orders = orders.shape[0]
    total_amount = orders['order_amount'].sum()
    naive_aov = total_amount / num_orders
    return naive_aov

def get_appi(data_path):
    orders = pd.read_csv(data_path)
    total_num_items = orders['total_items'].sum()
    total_amount = orders['order_amount'].sum()
    appi = total_amount / total_num_items
    return appi

if __name__ == '__main__':
    data_path = 'data/2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv'
    naive_aov = get_naive_aov(data_path)
    appi = get_appi(data_path)
    print(f'naive AOV is {naive_aov}')
    print(f'average price per item is {appi}')


