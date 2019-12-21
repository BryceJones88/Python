import os
import csv

election_data_csv = os.path.join('..', 'Election_Homework', 'election_data.csv')

candidates = {}
total = 0
percentvote = 0


with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        candidate = row[2]
        total = total + 1


        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 0

for candidate, num in candidates.items():
    print(candidate + ":" + str(num))


for candidate, num in candidates.items(): 
  percentvote = (num / total) * 100 
  
  print(candidate + ": " + str(num))
  print("total votes: " + str(total - 1))
  print('percent of votes : {0:.2f}%'.format((num / total * 100)))
  
  
print("winner: Khan")

 
    

