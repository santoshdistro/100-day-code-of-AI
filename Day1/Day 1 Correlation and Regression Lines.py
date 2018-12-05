import math
physics = '15 12 8 8 7 7 7 6 5 3'
history = '10 25 17 11 13 17 20 13 9 15'
X = list(map(int,physics.split()))            ## no need to use list()...
Y = list(map(int,history.split()))         ## ..while using Python2.x
sig_X = sum(X)                            ## -- ΣX
sig_Y = sum(Y)                            ## -- ΣY
numer1 = sum([a*b for a,b in zip(X, Y)])  ## -- ΣXY
numer2 = (sig_X*sig_Y)/len(X)             ## -- ΣX*ΣY/n
numer = int(numer1) - int(numer2)
denom1 = sum([i**2 for i in X])
denom2 = (sig_X**2)/len(X)
denom3 = sum([j**2 for j in Y])
denom4 = (sig_Y**2)/len(Y)
group1 = denom1 - denom2
group2 = denom3 - denom4
denom = math.sqrt(group1*group2)
kp_coeff = numer/denom
print("%.03f" % kp_coeff )