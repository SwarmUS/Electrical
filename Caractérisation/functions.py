import csv

def load_csv(filename):
    with open(filename, newline='') as csvfile:
        x= []
        y= []
        reader = csv.reader(csvfile)
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
        return x,y


