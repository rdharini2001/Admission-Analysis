import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
#The chance of getting admitted into a university depends on the following parameters:
#1.GRE SCORE
#2.TOEFL SCORE
#3.University Ranking
#4.SOP
#5.LOR
#6.CGPA
#7.Research
#8.Chance of Admit
#Let's now analyze how each of these parametes affets admissions
data = pd.read_csv("../input/us-graduate-schools-admission-parameters/US_graduate_schools_admission_parameters_dataset.csv")
data.head()
#Let's start with exploring the dataset
data.shape
data.describe()
#Now let's see how GRE score affects admission
print(data.columns)
import seaborn as sns
sns.distplot(a = data['GRE Score'] , kde = False)
#Analysis of SOP vs Chance of Admit
sns.barplot(x=data['SOP'],y=data['Chance of Admit '])
#Now let's see the influence of Research on Chance of Admit
sns.swarmplot(x = data['Research'],y = data['Chance of Admit '])
sns.heatmap(data = data)
sns.barplot(x=data['University Rating'],y=data['Chance of Admit '])
sns.barplot(x=data['Research'],y=data['Chance of Admit '])
sns.kdeplot(data = data['LOR '],shade = True)
sns.distplot(a = data['CGPA'] , kde = False)
