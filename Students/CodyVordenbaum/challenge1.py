from __future__ import division #for regular division of integers equaling numbers with decimal points
import random # random function for coin tosses
import matplotlib.pyplot as plt # function to plot the histogram data

def coinflip(probability): # start of the program
    "Function for coin flips"
flip = random.randint(0,1)
if (flip == 0):
    print("Tails")
    prob = "1-p"
    print("Probability: %s" % prob)
else:
    print("Heads")
    p = 0.5
    print("Probability: %f" % p)

print("\nTossing the coin 1,000 times:")

Heads = 0
Tails = 0
tosses = 1
while tosses <=1000: # while loop to run through the tosses fast
    flip = random.randint(0,1)
    if (flip == 0):
        Tails += 1
        tosses += 1
    else:
        Heads += 1
        tosses += 1

em_tails = (Tails/1000.0) # calculating emperical data
em_heads = (Heads/1000.0)
print("Heads Emperical Data: %f" % em_heads) # displaying the calulations
print("Tails Emperical Data: %f" % em_tails)


print("\nGeometric Random Variable Coin FLips:")
flips = 0 # resetting variables
histoTrials = 0
record = []
toss = 0
while histoTrials <= 10000: # running 10,000 times
    while (flips ==0):
        flips = random.randint(0,1)
        toss += 1
        if (flips == 1):
            break
    record.append(toss) #adding the number of tosses to a list
    histoTrials += 1
    flips = 0 # resetting variables for the correct measurements
    toss = 0

plt.hist(record, bins='auto') # plotting the data with the auto feature
plt.title("Histogram of Coin Flips until Heads Appears")
plt.show()
