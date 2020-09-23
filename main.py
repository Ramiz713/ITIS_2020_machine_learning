import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_file(file):
    table = pd.read_csv(file, delimiter=",")
    return table

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height + 1, '%d' % int(height), ha='center', va='bottom')

def draw(survived_means, dead_means, groups):
    n_groups = 6
    index = np.arange(n_groups)
    bar_width = 0.35

    survived_rect = plt.bar(index, survived_means, bar_width, color='r', label='Survived')
    dead_rect = plt.bar(index + bar_width, dead_means, bar_width, color='black', label='Dead')
    autolabel(survived_rect)
    autolabel(dead_rect)

    plt.xlabel('Groups of person')
    plt.ylabel('Number of persons')
    plt.title('Statistics of survivors and deaths')
    plt.xticks(index + bar_width / 2, groups)
    plt.legend()

    plt.tight_layout()
    plt.show()

data = read_file("train.csv")
passengers = pd.DataFrame(data, columns=['Survived', 'Age'])

fig, ax = plt.subplots()
bins = [0, 2, 4, 13, 20, 110]
age_categories = ['Infant', 'Toddler', 'Kid', 'Teen', 'Adult']
passengers['AgeGroup'] = pd.cut(passengers['Age'], bins=bins, labels=age_categories, right=False)
passengers['AgeGroup'] = passengers['AgeGroup'].cat.add_categories('Unknown').fillna('Unknown')
survived_means = list()
dead_means = list()
age_categories.append('Unknown')
for label in age_categories:
    survived_frame = passengers.loc[(passengers['AgeGroup'] == label) & (passengers['Survived'] == 1)]
    survived_means.append(survived_frame.shape[0])
    dead_frame = passengers.loc[(passengers['AgeGroup'] == label) & (passengers['Survived'] == 0)]
    dead_means.append(dead_frame.shape[0])
draw(survived_means, dead_means, age_categories)
