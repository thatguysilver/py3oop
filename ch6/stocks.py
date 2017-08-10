import datetime
def middle(stock, date):
    symbol, current, high, low = stock

    return (((high + low) / 2), date)

mid_value, date = middle(('FB', 75.00, 75.03, 74.90), 
        datetime.date(2014, 10, 31)
