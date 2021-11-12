# name of student: Alwin Wezenbeek
# number of student: 99060433
# purpose of program: learning while loops
# function of program: to calculate the change
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #what you need to pay
paid = int(float(input('Paid amount: ')) * 100) #what you paid
change = paid - toPay #what you paid minus what you have to pay

if change > 0: # if the change is higher than 0
  coinValue = 0.50 #value of the coin = 0.50 cents
  coinValue = 1.00 #value of the coin = 1.00 euro
  coinValue = 2.00 #value of the coin = 2.00 euro
  coinValue = 5.00 #value of the coin = 5.00 euro
  
  while change > 0 and coinValue > 0: #when change and coinvalue is more than 0
    nrCoins = change // coinValue # change and coinvalue equals nrcoins

    if nrCoins > 0: # if nrcoins is higher than 0
      print ('return maximal ', int(nrCoins), ' coins of ', float(coinValue), ' cents!' ) #asks the user to return the amount of coins
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #asks the user how many coins they returned
      change -= nrCoinsReturned * coinValue #CoinsReturned multiplied by CoinValue equals the change

# comment on code below: counting down the value of the coin when returning
    if coinValue == 5.00:
      coinValue = 2.00
    elif coinValue == 2.00:
      coinValue = 1.00
    elif coinValue == 1.00:
      coinValue = 0.50
    elif coinValue == 0.50:
      coinValue = 0
    else:
      coinValue = 0

if change > 0: # if change is higher than 0 it prints the change that is not yet returned
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')