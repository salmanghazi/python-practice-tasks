# Transfer
This module allows a user to transfer an amount from one account to another
### Call Text
```
tradingSession.transfer(exchange, from_account, to_account, from_account_type,to_account_type, asset, amount, [symbols])
```
### Parameters
The function transfer() takes 8 parameters that are required for the exchange to execute transfer between accounts
The parameters are structured as following:
#### exchange
The exchange at which the transfer is to be performed
#### from_account
The account from which the amount is to be trasferred
#### to_account
The account to which the amount is to be trasferred
#### from_account_type
The account type from which the amount is being transferred
#### to_account_type
The account type to which the amount is being transferred
#### asset
The asset which is the price of the symbol (it's mainly 'quote' asset here)
#### amount
The amount which is to be transferred between two accounts
#### symbol
The symbol which is being traded at this point
### Success Combinations
| exchange | from_account | to_account | from_account_type | to_account_type | asset | amount | symbols |
|----------|--------------|------------|-------------------|-----------------|-------|--------|---------|
| binance  | lalm         | lalm       | spot              | spot            | usdt  | 0.01   | ethusdt |
| binance  | lalm         | lal1       | spot              | isolated_margin | usdt  | 0.01   | ethusdt |
| binance  | lalm         | lal2       | spot              | cross-margin    | usdt  | 0.01   | ethusdt |
| binance  | lal1         | lalm       | spot              | cross-margin    | usdt  | 0.01   | ethusdt |
| binance  | lal1         | lal1       | swap              | spot            | usdt  | 0.1    | ethusdt |
| binance  | lal1         | lal2       | spot              | isolated_margin | usdt  | 0.01   | ethusdt |
| binance  | lal2         | lalm       | spot              | cross-margin    | usdt  | 0.01   | ethusdt |
| binance  | lal2         | lal1       | spot              | cross-margin    | usdt  | 0.01   | ethusdt |
| binance  | lal2         | lal2       | swap              | spot            | usdt  | 0.1    | ethusdt |
|----------|--------------|------------|-------------------|-----------------|-------|--------|---------|
| huobi    | lalm         | lalm       | spot              | spot            | usdt  | 0.01   | ethusdt |
| huobi    | lalm         | lal1       | cross_margin      | isolated_margin | usdt  | 0.01   | ethusdt |
| huobi    | lalm         | lal2       | spot              | cross_margin    | usdt  | 0.01   | ethusdt |
| huobi    | lal1         | lalm       | isolated_margin   | spot            | usdt  | 0.1    | ethusdt |
| huobi    | lal1         | lal1       | spot              | spot            | usdt  | 0.01   | ethusdt |
| huobi    | lal1         | lal2       | cross_margin      | isolated_margin | usdt  | 0.01   | ethusdt |
| huobi    | lal2         | lalm       | spot              | cross_margin    | usdt  | 0.01   | ethusdt |
| huobi    | lal2         | lal1       | isolated_margin   | spot            | usdt  | 0.1    | ethusdt |
| huobi    | lal2         | lal2       | spot              | spot            | usdt  | 0.01   | ethusdt |
### NOTES:
1. Transfer API hasn't been implemented for Okex exchange yet.
2. Future account type is not working for transfer API.

# Order 
There are three API calls that fall into this category, namely, submit order, cancel order, and cancel all order.
## Submit Order
submitOrder(), as the name suggests, is used to submit an order or even multiple orders to an exchange with respect to the parameters we pass through the wrapper functions.
### Call Text
```
tradingSession.submitOrder(orders)
```
### Parameters
The function submitOrder() takes a single parameter, which is a list of 'Orders' that need to be bought or sold.
Each order in that list has following necessary parameters:
#### order_type
limit, market, stop_limit, stop_loss, post
#### quantity
This is the quantity of the trade
#### side
Sell, Buy
#### account_type
This is the account type on which the trade is being executed
### Success Combinations
| exchange | order_type | quantity | side | account_type    |
|----------|------------|----------|------|-----------------|
| huobi    | limit      | 0.001    | buy  | spot            |
| huobi    | market     | 0.001    | buy  | isolated_margin |
| huobi    | post       | 0.002    | buy  | cross_margin    |
| huobi    | stop_limit | 0.001    | buy  | spot            |
| huobi    | limit      | 0.001    | sell | isolated_margin |
| huobi    | market     | 0.001    | sell | cross_margin    |
| huobi    | post       | 0.002    | sell | spot            |
| huobi    | stop_limit | 0.001    | sell | spot            |
|----------|------------|----------|------|-----------------|
| binance  | limit      | 0.001    | buy  | swap            |
| binance  | market     | 0.001    | buy  | isolated_margin |
| binance  | stop_loss  | 0.002    | buy  | cross_margin    |
| binance  | stop_limit | 0.001    | buy  | spot            |
| binance  | limit      | 0.001    | sell | isolated_margin |
| binance  | market     | 0.001    | sell | cross_margin    |
| binance  | stop_loss  | 0.002    | sell | swap            |
| binance  | stop_limit | 0.001    | sell | spot            |
|----------|------------|----------|------|-----------------|
| okex     | limit      | 0.001    | buy  | spot            |
| okex     | market     | 0.001    | buy  | cross_margin    |
| okex     | post       | 0.002    | buy  | cross_margin    |
| okex     | limit      | 0.001    | sell | cross_margin    |
| okex     | market     | 0.001    | sell | spot            |
| okex     | post       | 0.002    | sell | spot            |
## Cancel Order
cancelOrder() is a function used to cancel a single order which is passed in the form of a list to the function parameters.
### Call Text
```
tradingSession.cancelOrder([single_accepted_order])
```
### Parameter
Only parameter is an accepted order which has its own parameters that are already covered above.
## Cancel All Orders
cancelAllOrders() is a function used to cancel all active orders in the exchange. 
### Call Text
```
tradingSession.cancelAllOrders(exchange)
```
### Parameter
It only takes a single parameter, which is the 'Exchange' name. It cancels all the active orders of the mentioned exchange.

# Loan
This module allows a user to take a certain amount as loan from an account
### Call Text
```
tradingSession.loan(exchange, from_account_type, asset, amount, [symbols])
```
### Parameters
The function loan() takes 5 parameters that are required for the loan to be taken
The parameters are structured as following:
#### exchange
The exchange at which the loan is to be taken
#### from_account_type
The account type from which the amount is being taken as loan
#### asset
The asset which is the price of the symbol (it's mainly 'quote' asset here)
#### amount
The amount which is to be borrowed
#### symbol
The symbol which is being traded at this point
### Success Combinations
| exchange | from_account_type | asset | amount | symbols |
|----------|-------------------|-------|--------|---------|
| binance  | swap              | usdt  | 0.001  | ethusdt |
| binance  | isolated_margin   | usdt  | 0.1    | ethusdt |
| binance  | cross_margin      | usdt  | 1.0    | ethusdt |
| binance  | swap              | usdt  | 0.0001 | ethusdt |
| binance  | isolated_margin   | usdt  | 0.001  | ethusdt |
| binance  | cross_margin      | usdt  | 0.1    | ethusdt |
| binance  | swap              | usdt  | 0.001  | ethusdt |
| binance  | isolated_margin   | usdt  | 1.0    | ethusdt |
| binance  | cross_margin      | usdt  | 1.0    | ethusdt |
|----------|-------------------|-------|--------|---------|
| exchange | from_account_type | asset | amount | symbols |
|----------|-------------------|-------|--------|---------|
| huobi    | cross_margin      | usdt  | 0.001  | ethusdt |
| huobi    | isolated_margin   | usdt  | 0.1    | ethusdt |
| huobi    | cross_margin      | usdt  | 1.0    | ethusdt |
| huobi    | cross_margin      | usdt  | 0.0001 | ethusdt |
| huobi    | isolated_margin   | usdt  | 0.001  | ethusdt |
| huobi    | cross_margin      | usdt  | 0.1    | ethusdt |
### NOTES:
1. Loan API hasn't been implemented for Okex exchange yet.
2. Loan can be taken from isolated margin and cross margin account types only for Huobi Exchange.
3. Loan can be taken from isolated margin, swap, future and cross margin account types only for Binance Exchange.
4. Future account type is not working for loan API.

# Repay
This module allows a user to REPAY borrowed amount from an account
### Call Text
```
tradingSession.repay(exchange, from_account_type, asset, amount, [symbols])
```
### Parameters
The function repay() takes 5 parameters that are required to repay the borrowed amount
The parameters are structured as following:
#### exchange
The exchange at which the the loan is being repaid
#### from_account_type
The account type from which the loan is being repaid
#### asset
The asset which is the price of the symbol (it's mainly 'quote' asset here)
#### amount
The amount which is to be repaid back
#### symbol
The symbol which is being traded at this point
### Success Combinations
| exchange | from_account_type | asset | amount | symbols |
|----------|-------------------|-------|--------|---------|
| binance  | swap              | usdt  | 0.001  | ethusdt |
| binance  | isolated_margin   | usdt  | 0.1    | ethusdt |
| binance  | cross_margin      | usdt  | 1.0    | ethusdt |
| binance  | swap              | usdt  | 0.0001 | ethusdt |
| binance  | isolated_margin   | usdt  | 0.001  | ethusdt |
| binance  | cross_margin      | usdt  | 0.1    | ethusdt |
| binance  | swap              | usdt  | 0.001  | ethusdt |
| binance  | isolated_margin   | usdt  | 1.0    | ethusdt |
|----------|-------------------|-------|--------|---------|
| exchange | from_account_type | asset | amount |
|----------|-------------------|-------|--------|
| huobi    | cross_margin      | usdt  | 0.001  |
| huobi    | isolated_margin   | usdt  | 0.1    |
| huobi    | cross_margin      | usdt  | 1.0    |
| huobi    | isolated_margin   | usdt  | 0.0001 |
### NOTES:
1. Repay API hasn't been implemented for Okex exchange yet.
2. The account types allowed for Loan API will be allowed for Repay API as well.
3. 'Symbol' parameter is included in the API call for Binance but not for Huobi exchange.

# Withdraw
withdraw() is used to withdraw cash from your account to an address
### Call Text
```
tradingSession.repay(exchange, from_account_type, asset, amount, [symbols])
```
### Parameters
The function withdraw() takes multiple parameters which are structured as following:
#### exchange
The exchange for which the amount is to be withdrawn
#### from_account_type
The account type from which we are withdrawing
#### address
The address to which we are withdrawing
#### currency
Currency symbol, i.e USDT
#### amount
Amount to be withdrawn 
#### fee
The withdrawal fee.
#### symbol 
The symbol which is being traded at this point
### Success Combinations
| exchange | account_type    | address                                    | asset | amount | fee  | symbols |
|----------|-----------------|--------------------------------------------|-------|--------|------|---------|
| huobi    | spot            | 0xB4a232995c29dAcB010e7885ac01d050A6F78b0B | usdt  | 5.0    | 2.35 | ethusdt |
| huobi    | cross_margin    | 0xB4a232995c29dAcB010e7885ac01d050A6F78b0B | usdt  | 5.0    | 2.35 | ethusdt |
| huobi    | isolated_margin | 0xB4a232995c29dAcB010e7885ac01d050A6F78b0B | usdt  | 5.0    | 2.35 | ethusdt |
|----------|-----------------|--------------------------------------------|-------|--------|------|---------|
| exchange | account_type    | address                                    | asset | amount | symbols |
|----------|-----------------|--------------------------------------------|-------|--------|---------|
| binance  | cross_margin    | 0xB4a232995c29dAcB010e7885ac01d050A6F78b0B | usdt  | 5.0    | ethusdt |
| binance  | isolated_margin | 0xB4a232995c29dAcB010e7885ac01d050A6F78b0B | usdt  | 5.0    | ethusdt |
| binance  | swap            | 0xB4a232995c29dAcB010e7885ac01d050A6F78b0B | usdt  | 5.0    | ethusdt |
| binance  | spot            | 0xB4a232995c29dAcB010e7885ac01d050A6F78b0B | usdt  | 5.0    | ethusdt |
### NOTES:
1. Withdraw API hasn't been implemented for Okex exchange yet.
2. The 'Fee' parameter is ignored for Binance, the withdrawal fee is deducted from the amount itself.
3. Fee of the relevant exchange changes frequently
