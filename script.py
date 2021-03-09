import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

merged_visits_cart = pd.merge(visits, cart, how='left')
null_cart_time = merged_visits_cart[merged_visits_cart.cart_time.isnull()]
null_cart_time.info()
percent_visited_no_cart = float(len(null_cart_time)) / float(len(merged_visits_cart))

merged_cart_checkout = pd.merge(cart, checkout, how='left')
null_checkout_time = merged_cart_checkout[merged_cart_checkout.checkout_time.isnull()]
percent_cart_no_checkout = float(len(null_checkout_time)) / float(len(merged_cart_checkout))

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head())

merged_checkout_purchase = pd.merge(checkout, purchase, how='left')
null_purchase_time = merged_checkout_purchase[merged_checkout_purchase.purchase_time.isnull()]
percent_checkout_no_purchase = float(len(null_purchase_time)) / float(len(merged_checkout_purchase))
print(percent_checkout_no_purchase)
print(percent_cart_no_checkout)
print(percent_visited_no_cart)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())




