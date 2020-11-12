import pandas as pd
import operator
import numpy as np


def read_file(file):
    data = pd.read_csv(file, delimiter=";")
    return data


diseases = read_file("disease.csv")
symptoms = read_file("symptom.csv")

disease_prob = []

count = diseases['количество пациентов'].values[-1]
for i in diseases['количество пациентов'].values[:-1]:
    disease_prob.append(i / count)

our_symptoms = [np.random.randint(0, 2) for i in range(len(symptoms) - 1)]
our_probs = [1] * (len(diseases['Болезнь']) - 1)
for i in range(len(diseases['Болезнь']) - 1):
    our_probs[i] *= disease_prob[i]
    for j in range(len(symptoms) - 1):
        if our_symptoms[j] == 1:
            our_probs[i] *= float(symptoms.iloc[j][i + 1].replace(',', '.'))

index, value = max(enumerate(our_probs), key=operator.itemgetter(1))
print(diseases['Болезнь'].values[index])
