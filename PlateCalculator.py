import sys
import math
import csv
# Add your script below this line

"""
Function Name: Plate Calculator
Function Application: Takes the testweight, barweight, and assorted weights and finds optimal barbell loading
"""

def platecalculator(testweight,barweight,weights):
    processed_weights = sorted(weights,reverse=True);
    num_weights = len(weights);
    halfweight1 = (testweight-barweight)/2;
    halfweight2 = round(halfweight1/(min(processed_weights)));
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
    return adjustedweight, processed_weights, final_num;            

"""
Function Name: Percentages Calculator
Function Application: Takes the testweight, barweight, assorted weights and percentages and outputs the plate calculator per percentage
"""

def percentagecalculator(testweight,barweight,weights,percentages):
    maxweight = platecalculator(testweight,barweight,weights)[0];
    csv_data = []
    plates_row = ["Percentage","Weight","Adjusted"]
    for z in range(0,len(processed_weights)):
        plates_row.append([processed_weights[z]])
    for x in range(0,len(percentages)):
        PerAdjusted, ProcessedWeights, PerFinalNum = platecalculator((testweight*(percentages[x]/100)),barweight,weights);
        percentagerow = [percentages[x],testweight*(percentages[x]/100),PerAdjusted];
        for j in range(0,len(processed_weights)):
            percentagerow.append(PerFinalNum[j])
        csv_data.append(percentagerow)
    return maxweight, csv_data, plates_row;

# User Inputs
name = ["Carey"]
exercises = ["Bench","Squat"];
exercise_weight = [81.8*0.9,110.3*0.9];
barweight = 45;
weights = [2.5,5,10,25,45,35];
percentages = [75,85,95,75]

with open('531_weights.csv','w') as f:
    writer = csv.writer(f, lineterminator = '\n')
    writer.writerow(["Plate Calculator:",name])
    for x in (0,len(exercises)-1):
        adjustedweight, processed_weights, final_num = platecalculator(exercise_weight[x],barweight,weights)
        maxweight, csv_data, plates_row = percentagecalculator(exercise_weight[x],barweight,weights,percentages)
        writer.writerow([])
        writer.writerow([exercises[x]])
        writer.writerow(["Training Max:",exercise_weight[x]])
        writer.writerow(["Adjusted Max:",maxweight])
        writer.writerow(plates_row)
        writer.writerows(csv_data)
