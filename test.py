import csv
import NER.tagger as tagger

def concat_entites(entities):
    #join entities with space between them
    return ' '.join(entities)

# read csv file in dictionary format
no_of_rows = 0
no_of_success = 0
with open('dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if row['name'] != '':
            no_of_rows += 1
            ner = concat_entites(tagger.NER(row['text'])[0])
            if ner ==row['name']:
                no_of_success += 1
            elif ner[1:] == row['name']:
                no_of_success += 1
            else:
                print(row['name'], ' -> ',ner)


print(no_of_success/no_of_rows*100, '%')