import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
austin = pd.read_csv('C:/INFS 6351/listings_austin.csv')

plt.figure(figsize=(12, 8))
fig1 = sns.boxplot(x = 'neighbourhood', y = 'price', hue = 'room_type', data = austin, palette = "Set3", linewidth = 1.5, fliersize = 4)
fig1.set_xlabel('Zipcode')
fig1.set_ylabel('Price')
fig1.set_title('Relationship of Zip code and Airbnb prices in Austin')
plt.show()
