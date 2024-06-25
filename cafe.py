item_list = ['tea','coffee','hot chocolate','cake',]
stock_dict= {'tea':15, 'coffee': 10,'hot chocolate':20,'cake':17}
price_dict={'tea':3.50, 'coffee':3.00,'hot chocolate':4.00,'cake':17.00}

total =0 
for i in item_list:
    total += stock_dict[i]*price_dict[i]
print(total)