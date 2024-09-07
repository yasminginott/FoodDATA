import pandas as pd

# df = pd.read_csv('foodDATA/nutrient.csv')
# relevant_nutrients = [2047, 2048, 1008, 1062, 1258, 1004, 1085, 1063, 2000, 1093, 1079, 1003]
# filtered_df = df[df['id'].isin(relevant_nutrients)]
# filtered_df.to_csv('filtered_nutrient.csv', index=False)

import pandas as pd

# Read the original food nutrient table
df_food_nutrient = pd.read_csv('foodDATA/food_nutrient.csv')

# List of relevant nutrient IDs for Nutri-Score
relevant_nutrients = [2047, 2048, 1008, 1062, 1258, 1004, 1085, 1063, 2000, 1093, 1079, 1003]

# Filter the dataset for relevant nutrients based on 'nutrient_id'
df_food_nutrient_filtered = df_food_nutrient[df_food_nutrient['nutrient_id'].isin(relevant_nutrients)]

# Select only the necessary columns
df_food_nutrient_filtered = df_food_nutrient_filtered[['id', 'fdc_id', 'nutrient_id', 'amount']]

# Save the filtered dataset to a new file
df_food_nutrient_filtered.to_csv('food_nutrient_filtered.csv', index=False)

print("Filtered table saved as 'food_nutrient_filtered.csv'")


# df_food = pd.read_csv('foodDATA/food.csv')
# df_food_filtered = df_food[['fdc_id', 'description', 'food_category_id']]
# df_food_filtered.to_csv('food_filtered.csv', index=False)
# print("Filtered table saved as 'food_filtered.csv'")

# df_branded_food = pd.read_csv('foodDATA/branded_food.csv')
# df_branded_food = df_branded_food[['fdc_id',"brand_owner","brand_name","ingredients","short_description"]]
# df_branded_food.to_csv('branded_food_filtered.csv', index=False)
# print("Filtered table saved as 'branded_food_filtered.csv'")