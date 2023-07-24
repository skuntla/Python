import csv
import random
from datetime import datetime, timedelta

def generate_sample_data():
    # Generate 100 sample entries
    sample_data = []
    for i in range(1, 101):
        trade_id = i
        symbol = random.choice(['AAPL', 'GOOG', 'MSFT', 'AMZN', 'TSLA'])
        quantity = random.randint(10, 1000)
        price = round(random.uniform(100.0, 3000.0), 2)
        date = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime('%Y-%m-%d')
        sample_data.append([trade_id, symbol, quantity, price, date])

    return sample_data

def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['TradeID', 'Symbol', 'Quantity', 'Price', 'Date'])
        writer.writerows(data)

if __name__ == "__main__":
    sample_data = generate_sample_data()
    write_to_csv('sample_data.csv', sample_data)
