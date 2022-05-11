# %%
import pandas as pd

# %%
#Import data

data = pd.read_excel('/Users/dannyfung/Downloads/2019 Winter Data Science Intern Challenge Data Set.xlsx')
print(data.head())
data.shape

# %%
#Naive AOV

mean_amount = sum(data['order_amount']) / data.shape[0]
print(mean_amount)

# %%
#Create new per unit cost field (order_amount / total_items)

data['order_amount_per_item'] = data['order_amount'] / data['total_items']
data.head()

# %%
#orders with total_items > 1

print(data.loc[data['total_items']> 1.0].shape)

# %%
#Verify that the per unit price (order_amount_per_item) is consistent for every shop 

shop_ids = set(data['shop_id'])
#print(shop_ids)

for id in shop_ids:
    check = {}
    sub_data = data.loc[data['shop_id']==id]
    if len(set(sub_data['order_amount_per_item'])) != 1:
        check[id] = list(set(sub_data['order_amount_per_item']))
    else:
        pass

print(len(check) == 0)

# %%
#Possible AOV #1 - sum of order amounts / sum of total items sold

new_mean = sum(data['order_amount'])/sum(data['total_items'])
print('$',round(new_mean,2))

# %%
#Possible AOV #2 - sum of per unit cost per order / sum of total number of orders

new_mean1 = sum(data['order_amount_per_item'])/data.shape[0]
print('$',round(new_mean1,2))

# %%
'''The naive AOV calculation works if the total_items per order always 1. However, since there are over 3000 orders with more than 1 item, the order_amount for these orders will be larger 
and results in the anomalous $3145.13 AOV. 

Instead, we can calculate a more reasonable AOV by taking the ratio of the sum of the order_amount column and the sum of the total_items column. This calculation comes out to be $357.92 and 
provides the average price per item sold per order.

Alternatively, another AOV calculation was taking the ratio of the sum of the order_amount_per_item column and total number of orders. The value comes out to be $387.74 and represents the average
shoe price of all shoe purchases made in the 100 sneaker shops over the 30 day window. This number will fluctuate depending on which store gets more orders and does not depend on the number of 
units purchased per order.'''


