# Load modules
# import codecademylib
# from matplotlib import pyplot as plt
import pandas as pd
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('D:\Repository\page_visits.csv')


# Why do citizens visit our website?
# Calculate survey results
survey_results = df.groupby('website_goal')\
  	.first_name.count()

# Make a pie chart
plt.pie(survey_results.values,
        labels=survey_results.index,
        autopct='%d%%'
       )
plt.title('Why do citizens visit our website?')
plt.axis('equal')
plt.show()

# Page Visits over Time
by_day = df.groupby('visit_date').first_name.count()

plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.plot(by_day.values,
        marker='o', markersize=8, linewidth=3)
plt.ylabel("Number of Visits")
ax.set_xticks(range(len(by_day))[::8])
ax.set_xticklabels(by_day.index[::8], rotation=45)
plt.show()


# plt.hist(df.age, range=(10, 65), bins=(65 - 10)/5, edgecolor='white')
plt.hist(df.age, range=(10, 65), bins=10, edgecolor='white')

plt.xlabel('Visitor Age')
plt.ylabel('Number of Visitors')
plt.title('Histogram of Visitor Age')
plt.show()



'''
# Paste code here:
import pandas as pd

# Load data
df = pd.read_csv('D:\Repository\page_visits.csv')

# Display data
print(df.head())

# Display survey results
print(
  df.groupby('website_goal')\
  	.first_name.count()\
  	.reset_index()\
  	.rename(columns={'first_name': 'number_of_citizens'})
)
'''
