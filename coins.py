# name of student: Alwin Wezenbeek
# number of student: 99060433
# purpose of program: learning while loops
# function of program: to calculate the change
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #what you need to pay
paid = int(float(input('Paid amount: ')) * 100) #what you paid
change = paid - toPay #what you paid minus what you have to pay

if change > 0: # if the change is higher than 0
  coinValue = 500 #value of the coin
  
  while change > 0 and coinValue > 0: #when change and coinvalue is more than 0
    nrCoins = change // coinValue # change and coinvalue equals nrcoins

    if nrCoins > 0: # if nrcoins is higher than 0
      print ('return maximal ', int(nrCoins), ' coins of ', float(coinValue), ' cents!' ) #asks the user to return the amount of coins
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #asks the user how many coins they returned
      change -= nrCoinsReturned * coinValue #CoinsReturned multiplied by CoinValue equals the change

# comment on code below: counting down the value of the coin when returning
    if coinValue == 500:
      coinValue = 300
      Returned500coinValue = nrCoinsReturned #remembers the amount of coins you returned
    elif coinValue == 300:
      coinValue = 200
      Returned300coinValue = nrCoinsReturned
    elif coinValue == 200:
      coinValue = 100
      Returned200coinValue = nrCoinsReturned
    elif coinValue == 100:
      coinValue = 50
      Returned100coinValue = nrCoinsReturned
    elif coinValue == 50:
      coinValue = 20
      Returned50coinValue = nrCoinsReturned
    elif coinValue == 20:
      coinValue = 10
      Returned20coinValue = nrCoinsReturned
    elif coinValue == 5:
      coinValue = 0
      Returned10coinValue = nrCoinsReturned
    else:
      coinValue = 0
      Returned5coinValue = nrCoinsReturned

if change > 0: # if change is higher than 0 it prints the change that is not yet returned
  print('Change not returned: ', str(change) + ' cents')
else: #prints the change of specific coins returned
  print('change of 500 returned:' + str(Returned500coinValue))
  print('change of 300 returned:' + str(Returned300coinValue))
  print('change of 200 returned:' + str(Returned200coinValue))
  print('change of 100 returned:' + str(Returned100coinValue))
  print('change of 50 returned:' + str(Returned50coinValue))
  print('change of 20 returned:' + str(Returned20coinValue))
  print('change of 10 returned:' + str(Returned10coinValue))
  print('change of 5 returned:' + str(Returned5coinValue))