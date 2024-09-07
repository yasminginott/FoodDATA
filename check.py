import pandas as pd

# Load the dataframes
df_branded_food = pd.read_csv('foodDATA_filtered/branded_food_filtered.csv')
df_food = pd.read_csv('foodDATA_filtered/food_filtered.csv')
df_food_nutrient = pd.read_csv('foodDATA_filtered/food_nutrient_filtered.csv')
df_nutrient = pd.read_csv('foodDATA_filtered/nutrient_filtered.csv')

# Merge 'description' from df_food into df_branded_food based on 'fdc_id'
df_merged = pd.merge(df_branded_food[['fdc_id', 'ingredients']], df_food[['fdc_id', 'description']], on='fdc_id', how='inner')

# Merge 'nutrient name' from df_nutrient into df_food_nutrient based on 'nutrient_id'
df_food_nutrient = pd.merge(df_food_nutrient[['fdc_id', 'nutrient_id', 'amount']], 
                            df_nutrient[['id', 'name']], 
                            left_on='nutrient_id', right_on='id', how='inner')

# Pivot the data so each nutrient becomes a column
df_nutrient_pivot = df_food_nutrient.pivot_table(index='fdc_id', columns='name', values='amount').reset_index()

# Merge everything into a final dataframe
df_final = pd.merge(df_merged, df_nutrient_pivot, on='fdc_id', how='inner')

# Save the full dataframe to CSV
df_final.to_csv('final_full_output.csv', index=False)

print("Full table saved as 'final_full_output.csv'")

# ---- Validation and Checks ----

# 1. Display first 5 rows for visual inspection
print("First 5 rows of the final dataframe:")
print(df_final.head())

# 2. Check specific 'fdc_id' for correctness
fdc_id_to_check = 1105904  # Change this ID to a specific product you'd like to check
print(f"Data for fdc_id {fdc_id_to_check}:")
print(df_final[df_final['fdc_id'] == fdc_id_to_check])

# 3. Check for missing values (NaN)
print("Checking for missing values in the final dataframe:")
print(df_final.isnull().sum())

# 4. Compare number of rows before and after merge
print("Number of rows in df_branded_food:", len(df_branded_food))
print("Number of rows in df_final:", len(df_final))

# 5. Check specific nutrient value for a specific product
nutrient_to_check = 'Protein'  # Change this to a nutrient you'd like to inspect
print(f"Value of {nutrient_to_check} for fdc_id {fdc_id_to_check}:")
print(df_final[df_final['fdc_id'] == fdc_id_to_check][nutrient_to_check])

# 6. Save a small sample for external review
df_final_sample = df_final.head(20)
df_final_sample.to_csv('final_sample_output.csv', index=False)
print("Sample saved as 'final_sample_output.csv'")

# 7. Check for rows with unexpected 0 or NaN values in important columns
print("Checking for rows with 0 or NaN in important columns like 'Protein' and 'Energy':")
print(df_final[(df_final['Protein'] == 0) | (df_final['Protein'].isna())])
print(df_final[(df_final['Energy'] == 0) | (df_final['Energy'].isna())])
