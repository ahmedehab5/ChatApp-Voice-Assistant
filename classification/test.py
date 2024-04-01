import classification as clf
import csv

no_of_rows = 0
no_of_success = 0
with open('./dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        no_of_rows += 1
        predicted_command = clf.classify(row['order'])
        if predicted_command ==row['command']:
            no_of_success += 1
        else:
            print(row['command'], ' -> ',predicted_command)


print(no_of_success/no_of_rows*100, '%')

