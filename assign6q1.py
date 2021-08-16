# .  QUESTION
#  Using Python for data analysis.
#   Download the files needed to complete this assignment from here
# . (https://drive.google.com/file/d/1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV/view)
# This data set contains data from Stack overflow Developer Survey.
# Use the Python libraries to analyze the date and answer the following questions.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data1 = pd.read_csv("survey_results_public.csv")
data1.head()
data2 = pd.read_csv("survey_results_schema.csv")
data2.head()
data1.columns