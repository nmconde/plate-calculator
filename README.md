# Plate Calculator

## Description
Simple application to calculate the optimal loading of plates on a barbell used for weightlifting. 

## Usage
```python
import sys
improt math

# User Inputs
testweight = 165; # The total desired weight (including the weight of the bar)
barweight = 45; # The weight of the bar
weights = [2.5,5,10,25,45,35]; # THe plate weights available
```

```python
# Expected Output
Weights Per Side of the Barbell:
('Input Weight ', 165)
('Adjusted Weight ', 165.0)
(45, ' lbs:', 1.0, ' plates')
(35, ' lbs:', 0.0, ' plates')
(25, ' lbs:', 0.0, ' plates')
(10, ' lbs:', 1.0, ' plates')
(5, ' lbs:', 1.0, ' plates')
(2.5, ' lbs:', 0, ' plates')
```

## Roadmap
* Basic Functionality. Output the desired number of plates 
* Android Application. Rewrite from Python to Java for Android Application in Android Studio
* Training Weights. Allow user to input training weight and desired percentages for different sets
* Optimal Loading Between Sets. Develop optimization to allow for ease of loading between sets of different weights
