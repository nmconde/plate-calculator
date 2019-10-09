import sys
import math
# Add your script below this line

# User Inputs
testweight = 165;
barweight = 45;
weights = [2.5,5,10,25,45,35];

# Processed Variables
processed_weights = sorted(weights,reverse=True);
num_weights = len(weights);
halfweight1 = (testweight-barweight)/2;
halfweight2 = math.floor(halfweight1/(min(processed_weights)));
runweight = halfweight2*(min(processed_weights));
adjustedweight = (runweight*2)+barweight;

alloptions = [];

for y in range(0,len(processed_weights)):
    weightarray = [0]*y;
    localweight = runweight;
    for x in range(y,len(processed_weights)):
        if localweight > 0:
            plates = math.floor(localweight/processed_weights[x])
            weightarray.append(plates);
            localweight -= plates*processed_weights[x];
            endarray = len(processed_weights)-x-1;
    if endarray > 0:
        for x in range (0,endarray):
            weightarray.append(0)
    alloptions.append(weightarray)

min_range = float("inf");
for x in range(0,len(alloptions)):
    if len(alloptions[x]) < min_range:
        min_range = sum(alloptions[x]);
        final_num = alloptions[x];
        

print("Weights Per Side of the Barbell:")
print("Input Weight ",testweight)
print("Adjusted Weight ",adjustedweight)
for x in range(0,len(processed_weights)):
    print(processed_weights[x], ' lbs:', final_num[x], ' plates')