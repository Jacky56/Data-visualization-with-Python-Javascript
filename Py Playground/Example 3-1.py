import json
import csv
path1 = "../data/nobel_winners_cleaned.json"
with open(path1,"r") as f:
    data = json.load(f)

nobel_winners =[
    {'cataegory' : 'A',
     'name' : 'A name',
     'nationality' : 'A nation',
     'sex' : 'A gender',
     'year' : 1},
    {'cataegory' : 'B',
     'name' : 'B name',
     'nationality' : 'B nation',
     'sex' : 'B gender',
     'year' : 2},
    {'cataegory' : 'C',
     'name' : 'C name',
     'nationality' : 'C nation',
     'sex' : 'C gender',
     'year' : 3}
    ]

path = "../data/nobel_winners.csv"

    
cols = nobel_winners[0].keys()

cols = sorted(cols) #optional

##with open(path,"w") as f: #normal way 
##    f.write(','.join(cols) +"\n")
##
##    for sample in nobel_winners:
##        row = [str(sample[col]) for col in cols]
##        f.write(','.join(row) +"\n")


with open(path,'w' , newline= '') as f:#superior way with csv library
    writer = csv.DictWriter(f, fieldnames = cols)
    writer.writeheader()
    for w in nobel_winners:
        writer.writerow(w)

with open(path,) as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)

