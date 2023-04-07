import statistics
import pandas as pd
import plotly.express as px 
import csv 
import plotly.graph_objects as go 
import numpy as np 

# initialising the csv
df = pd.read_csv("savings_data.csv")

# displaying a scatter plot to find the nature of the data 
fig = px.scatter(df, y="quant_saved", color="female")
fig.show()

# finding mean, median and mode of the big data 
avg = statistics.mean(df["quant_saved"])
med = statistics.median(df["quant_saved"])
mod = statistics.mode(df['quant_saved'])
print(avg, med, mod)
# stating the findings in the data 
# mean median and mode are too far apart while mode is zero 

# finding if the people who saved are wealthy or not 
with open("savings_data.csv", newline="") as f:
    reader = csv.reader(f)
    savings_data = list(reader)

savings_data.pop(0)

total_entries = len(savings_data)
total_people_wealthy = 0 
male_saved = 0 

wealthy = []
not_wealthy = []
male = []
female = []

for data in savings_data:
    if int(data[3]) == 1:
        total_people_wealthy += 1
        wealthy.append(float(data[0]))
    else:
        not_wealthy.append(float(data[0]))

    if int(data[1]) == 0:
        male_saved += 1
        male.append(float(data[0]))
    else:
        female.append(float(data[0]))

print(male_saved)
print(total_people_wealthy)
print(f"wealthy people savings mean: {statistics.mean(wealthy)}")
print(f"wealthy people savings median: {statistics.median(wealthy)}")
print(f"wealthy people savings mode: {statistics.mode(wealthy)}")

print("\n\n")
print(f"not wealthy people savings mean: {statistics.mean(not_wealthy)}")
print(f"not wealthy people savings median: {statistics.median(not_wealthy)}")
print(f"not wealthy people savings mode: {statistics.mode(not_wealthy)}")

print("\n\n")
print(f"male people savings mean: {statistics.mean(male)}")
print(f"male people savings median: {statistics.median(male)}")
print(f"male people savings mode: {statistics.mode(male)}")

print("\n\n")

print(f"female people savings mean: {statistics.mean(female)}")
print(f"female people savings median: {statistics.median(female)}")
print(f"female people savings mode: {statistics.mode(female)}")

# state findings 
# the mean median and mode are still very far apart from each other 

figure = go.Figure(go.Bar(x = ["wealthy", "not wealthy"], y = [total_people_wealthy, (total_entries - total_people_wealthy)]))
figure.show()

malefig = go.Figure(go.Bar(x = ["male, female"], y = [male_saved, (total_entries - male_saved)]))
malefig.show()

# find the standard deviation 
standard_deviation = statistics.stdev(df["quant_saved"])
print( "standard deviation of population data: " ,standard_deviation)

# finding correlation between wealthy and not wealthy 
wealthy_ppl = []
savings = []

for data in savings_data:
    if float(data[3]) == 1:
        savings.append(float(data[0]))
        wealthy_ppl.append(float(data[3]))

correlation = np.corrcoef(wealthy_ppl, savings)
print(f"correlation between wealth and savings is: {correlation[0, 1]}")

# finding correlation between females and savings 
fem_savings = []
females = []

for data in savings_data:
    if float(data[1]) != 0:
        fem_savings.append(data[0])
        females.append(data[1])

corr = np.corrcoef(females, fem_savings)
print(f"correlation between females and savings is: {corr[0, 1]}")

# the data is not related closely at all
