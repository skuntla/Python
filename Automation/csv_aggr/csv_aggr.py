import csv

def calculate_trade_total(filename):
    try:
        trade_totals = {}
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                try:
                    trade_id, symbol, quantity, price, date = row
                    quantity = int(quantity)
                    price = float(price)
                    total_value = quantity * price
                    trade_totals[int(trade_id)] = total_value
                except (ValueError, IndexError):
                    print(f"Error processing row: {row}")

        return trade_totals
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    filename = "sample_data.csv"
    trade_totals = calculate_trade_total(filename)
    if trade_totals:
        print(trade_totals)
