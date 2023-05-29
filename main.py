from numpy import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt

type_of_newsday = list()
random_for_type = list()
random_for_Demand = list()
Demand = list()


# generate types of days.
def Day_Type(Days):
    for i in range(Days):
        r1 = random.random()
        type_ = 0
        if r1 < .18:
            type_ = 1
        elif r1 < 0.60:
            type_ = 2
        elif r1 < 0.92:
            type_ = 3
        else:
            type_ = 4
        type_of_newsday.append(type_)
        random_for_type.append(r1 * 100)


# generation of demands of excellent days depends on
# its probability distribution.
def get_excellent_Demand():
    r = random.random()
    if r < 0.07:
        D = 50
    elif r < 0.15:
        D = 60
    elif r < 0.27:
        D = 70
    elif r < 0.4:
        D = 80
    elif r < 0.62:
        D = 90
    elif r < 0.85:
        D = 100
    elif r < 0.93:
        D = 110
    else:
        D = 120
    Demand.append(D)
    random_for_Demand.append(r * 100)


# generation of demands of good days depends on
# its probability distribution.
def get_good_Demand():
    r = random.random()
    if r < 0.06:
        D = 40
    elif r < 0.15:
        D = 50
    elif r < 0.31:
        D = 60
    elif r < 0.5:
        D = 70
    elif r < 0.78:
        D = 80
    elif r < 0.9:
        D = 90
    elif r < 0.97:
        D = 100
    else:
        D = 110
    Demand.append(D)
    random_for_Demand.append(r * 100)


# generation of demands of fair days depends on
# its probability distribution.
def get_fair_Demand():
    r = random.random()
    if r < 0.15:
        D = 40
    elif r < 0.37:
        D = 50
    elif r < 0.56:
        D = 60
    elif r < 0.83:
        D = 70
    elif r < 0.93:
        D = 80
    elif r < 0.98:
        D = 90
    else:
        D = 100
    Demand.append(D)
    random_for_Demand.append(r * 100)


# generation of demands of poor days depends on
# its probability distribution.
def get_poor_Demand():
    r = random.random()
    if r < 0.42:
        D = 40
    elif r < 0.7:
        D = 50
    elif r < 0.84:
        D = 60
    elif r < 0.94:
        D = 70
    elif r < 0.99:
        D = 80
    else:
        D = 90
    Demand.append(D)
    random_for_Demand.append(r * 100)


def calculate(Days, bundle):
    type_of_newsday.clear()
    random_for_Demand.clear()
    random_for_type.clear()
    Demand.clear()
    revenue = list()
    lost_profit = list()
    salvage = list()
    daily_profit = list()
    scrape_price = 15
    selling_price = 70
    buying_price = 50
    Day_Type(Days)
    # calculations needed to solve our problem:-
    # --------------------------------------------------------------------------------------
    # Profit = revenue from sales − cost of newspapers − lost profit from excess
    # demand + salvage from sale of scrap papers
    # cost of newspapers = maximum *buying price. -> 60*50
    # --------------------------------------------------------------------------------------
    # Revenue = demand*selling (70).
    # lost profit =(demand-maximum (60)) *(selling (70) -buying (50)).
    # Salvage = (maximum- demand) * scrape price (15).

    # generation of demand depends on the type of day.

    for i in range(Days):
        if type_of_newsday[i] == 1:
            get_excellent_Demand()
        if type_of_newsday[i] == 2:
            get_good_Demand()
        if type_of_newsday[i] == 3:
            get_fair_Demand()
        if type_of_newsday[i] == 4:
            get_poor_Demand()
    max_purchase = 120

    mx = -1
    max_profit = 0
    optimal = -1
    temp_bundle = bundle
    best_profit = list()
    while temp_bundle <= max_purchase:
        t = PrettyTable(
            ['Day', 'Random digits for type of newsday ', 'Type of Newsday ', 'Random digit for demand', 'Demand ',
             'Revenue from sales ($)', 'Lost profit from excess demand ', 'Salvage from sale of scrap ',
             'Daily profit '])
        daily_profit.clear()
        lost_profit.clear()
        salvage.clear()
        revenue.clear()
        for i in range(Days):
            # calculate the revenue.
            # temp bundle (bundle->120)

            revenue_ = min(Demand[i], temp_bundle) * selling_price
            revenue.append(revenue_)
            # calculate the lost profit.
            pro = selling_price - buying_price
            lost_profit_ = max(0, (Demand[i] - temp_bundle) * pro)
            lost_profit.append(lost_profit_)
            # calculate the salvage value.
            salvage_ = max(0, (temp_bundle - Demand[i]) * scrape_price)
            salvage.append(salvage_)
            # calculate the cost of newspaper needed in daily profit function.
            cost_of_newspaper = temp_bundle * buying_price
            # calculate the daily profit.
            daily_profit_ = revenue[i] - cost_of_newspaper - lost_profit[i] + salvage[i]
            daily_profit.append(daily_profit_)

            t.add_row([i + 1, random_for_type[i], type_of_newsday[i], random_for_Demand[i], Demand[i],
                       revenue[i], lost_profit[i], salvage[i], daily_profit[i]])
        num_of_win = sum(i > 0 for i in daily_profit)
        if num_of_win > mx:
            mx = num_of_win
            optimal = temp_bundle
            best_profit = daily_profit
            for i in range(Days):
                max_profit = max(daily_profit[i], max_profit)

        temp_bundle += bundle
        print(t)
        print('\n')

    print("\nMax Profit we can get is: ", max_profit, " when demand is: ", optimal)
    print('the optimal number of papers to purchase:', optimal)
    plt.hist(best_profit)
    plt.show()


# Days = int(input())
Days, Trails, bundle = map(int,
                           input("Enter number of Days, Trails, and bundle you want(separated by a space):").split())
# inputs must be separated by a space not enter
for i in range(Trails):
    print("For Trail: ", i + 1)
    calculate(Days, bundle)
