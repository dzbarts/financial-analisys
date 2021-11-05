import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Portfolio import *
import matplotlib


# total cost
cost = 0

for i in range(length_of_flatten_port):
    cost += stock[i].Close[-1] * weight_of_stocks[i]
cost = round(float(cost), 2)

# column of dividends
dividends = []

for i in range(length_of_flatten_port):
    dividends.append(flatten_portfolio[i].info['dividendRate'])

# assets Pandas DataFrame
assets = []

for i in range(length_of_stock):
    assets.append(stock[i].tail(1))

assets = pd.concat(assets)
assets.index = flatten_port
assets = assets.round(2)
assets['Dividends (per year)'] = dividends
assets.insert(0, 'Number', weight_of_stocks)

major_holders = []
for i in range(length_of_flatten_port):
    major_holders.append(pd.DataFrame(np.array(flatten_portfolio[i].major_holders),
                                      columns=[flatten_port[i], 'stock']).set_index('stock').T)

assets = assets.join(pd.concat(major_holders))
assets.insert(0, 'Stocks', flatten_port)
assets.pop('Adj Close')

# pie plot of assets
def plot_p():
    plt.style.use('dark_background')

    fig_p, ax1 = plt.subplots()
    ax1.pie(weight_of_stocks, labels=flatten_port)
    fig_p.set_facecolor('#19232D')
    return fig_p
    # plt.show()


# stock growth Pandas DataFrame
list_of_stock_growth_percentages = []
list_of_stock_growth = []
for i in range(length_of_flatten_port):
    list_of_stock_growth_percentages.append(round((stock[i].Close[-1] /
                                                   stock[i].Close[-2] - 1) * 100, 2))
    list_of_stock_growth.append(round((stock[i].Close[-1] - stock[i].Close[-2]), 2))

stock_growth = pd.DataFrame({'Stock growth, %': list_of_stock_growth_percentages,
                             'Stock growth, RUB': list_of_stock_growth},
                            index=flatten_port)

stock_growth.insert(0, 'Stocks', flatten_port)


# plot of time series
def plot_common(period):
    fig_c, ax1 = plt.subplots()
    for i in range(length_of_stock):
        ax1.plot(stock[i].Close[-period:])

    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    fig_c.set_facecolor('#19232D')
    return fig_c
    # plt.show()