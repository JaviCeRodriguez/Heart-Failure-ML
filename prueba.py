# Imports
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_bar(data: dict, index: list) -> None:
    df_pathologies = pd.DataFrame(data, index=index)
    ax = df_pathologies.plot(kind='pie', rot=0, figsize=(20, 5), subplots=True, autopct='%1.1f%%', colors=['green', 'red'])


def pathologies_cases(data, feature: str, event: int) -> list:
    data_feature = data[data["DEATH_EVENT"]==event][feature]
    idx = pd.Index(data_feature)
    return list(idx.value_counts())


# Obtengo los datos y muestro las primeras 10 filas
dataset = './heart_failure_clinical_records_dataset.csv'
heart_data = pd.read_csv(dataset)
heart_data.head(10)

pathologies_feat = ["anaemia", "diabetes", "high_blood_pressure", "smoking"]


p_surv = {f: pathologies_cases(data=heart_data, feature=f, event=0) for f in pathologies_feat}
p_dead = {f: pathologies_cases(data=heart_data, feature=f, event=1) for f in pathologies_feat}

plot_bar(data=p_surv, index=['Survivors', 'Deaths'])
plt.show()