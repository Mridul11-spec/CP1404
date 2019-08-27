print("Electricity bill Estimator 2.0")
t = int(input('Which tariff? 11 or 31: '))
while t != 11 and t != 31:
    print ("invalid input")
    t = int(input('Which tariff? 11 or 31: '))
d = float(input('Enter daily use in kwh: '))
e = float(input('Enter number of billing days: '))
total = d * e
if t == 11:
    total2 = total * 0.244618
    output = round(total2,2)
    print('Estimated bill:$ ', output)

else:
    total2 = total * 0.136928
    output = round(total2, 2)
    print('Estimated bill: $',output)