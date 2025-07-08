import pandas as pd  # Importing pandas for data manipulation and cleaning

# Load raw Airbnb listing data from the source CSV
df = pd.read_csv('../data/AB_NYC_2019.csv')
# This is the raw dataset containing listing details like price, location, reviews, etc.
# It may have missing or inconsistent data that needs cleaning before analysis.

# Drop rows that are missing critical values
df = df.dropna(subset=['name', 'host_name', 'last_review', 'reviews_per_month'])
# We remove entries that lack important descriptive or review data.
# These missing values could distort insights on pricing or popularity.

# Remove listings with non-positive price values
df = df[df['price'] > 0]
# Listings with zero or negative prices are not realistic and would skew price analysis.

# Create a new feature: price per minimum night
df['price_per_min_night'] = df['price'] / df['minimum_nights']
# Helps normalize price across listings with different stay requirements.
# This metric is useful for comparing pricing fairness and market competitiveness.

# Extract the month from the last review date
df['month'] = pd.to_datetime(df['last_review']).dt.month
# This enables time-series analysis and helps identify seasonal patterns in bookings.

# Save the cleaned and enriched dataset to a new file
df.to_csv('../data/AB_NYC_2019_cleaned.csv', index=False)
# This becomes the standardized dataset used across all EDA, modeling, and dashboarding.

print("ETL completed.")
# Confirms that the data cleaning and feature engineering steps were successful.
