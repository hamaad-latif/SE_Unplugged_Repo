import csv
import random
def generator(list):
    random_val = list[random.randrange(list.__len__())]
    return random_val

# Function to generate the random data
def generateRandomData(range):
    dict = {
        'Gender': ['F', 'M'],
        'Class': [3,4,5],
        'Age': [7,8,9,10,11,12,13,14],
        'Results_Before':['P', 'F'],
        'Results_After': ['P', 'F'],
    }
# Creating CSV file    
    with open('random_dataset.csv', 'a', newline='') as csv_file:
        for i in range(range):
            Age = generator(dict['Age'])
            Gender = generator(dict['Gender'])
            Results_Before = generator(dict['Results_Before'])
            Results_After = generator(dict['Results_After'])
            Class = generator(dict['Class'])
            if Results_Before == "F" and Results_After == "P":
                Positive_Outcomes = "T"
            else: Positive_Outcomes = "F"
            csvWriter = csv.writer(csv_file, delimiter=',')
            csvWriter.writerow([Age,Gender,Results_Before, Results_After, Class, Positive_Outcomes])


if __name__ == '__main__':
    generateRandomData(5000)
