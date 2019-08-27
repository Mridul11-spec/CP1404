print ("Electricity bill estimator")
c = float(input('Enter cents per kwh: '))
d = float(input('Enter daily use in kwh: '))
e = float(input('Enter number of billing days: '))
a = d * e * c /100
print('Estimated bill: ', a)
