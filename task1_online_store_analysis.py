import pandas as pd
df = pd.read_csv('online_store_data.csv')

rows = df.shape[0]
print(f"Ukupan broj redova: {rows}")

most_sold = df.sort_values(by='quantity_sold', ascending=False).iloc[0]
print("\nNajprodavaniji proizvod u trgovini:")
print(most_sold[['product_name', 'quantity_sold']])

smartphones = df[df['category'] == 'Smartphones']
top_5_phones = smartphones.sort_values(by='quantity_sold', ascending=False).head(5)
print("\nTop 5 najprodavanijih mobilnih telefona:")
print(top_5_phones[['product_name', 'quantity_sold']])

laptops = df[(df['category'] == 'Laptops') & (df['price'].notnull()) & (df['price'] > 0)]
max_price = laptops['price'].max()
min_price = laptops['price'].min()

print(f"\nNajskuplji laptop: {max_price}")
print(f"Najjeftiniji laptop: {min_price}")
