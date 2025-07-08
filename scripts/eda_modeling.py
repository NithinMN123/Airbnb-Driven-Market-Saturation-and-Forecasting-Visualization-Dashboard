# Import necessary libraries for data analysis, visualization, and modeling
import pandas as pd  # For reading and manipulating data
import seaborn as sns  # For enhanced visualization (especially statistical plots)
import matplotlib.pyplot as plt  # Core plotting library
from sklearn.linear_model import LinearRegression  # For performing basic regression modeling
import statsmodels.api as sm  # For statistical modeling and detailed regression summaries

# Load the cleaned Airbnb dataset
df = pd.read_csv('../data/AB_NYC_2019_cleaned.csv')  
# This dataset has been preprocessed in the ETL step to remove nulls and outliers.
# Loading it here means we’re ready to analyze patterns and build models.

# --- Exploratory Data Analysis (EDA) ---

# Create a boxplot to visualize how price varies across boroughs
sns.boxplot(
    x='neighbourhood_group',         # Boroughs like Manhattan, Brooklyn, etc.
    y='price',                       # Target variable we're studying
    data=df[df['price'] < 500]       # Filter out extreme outliers above $500 for clearer visualization
)
plt.title('Price Distribution by Borough')  
plt.savefig('../data/price_distribution.png')  
# This visual shows which boroughs have higher median prices and how varied prices are within each group.
# Useful for spotting high-value or volatile pricing areas.

# --- Linear Regression Modeling ---

# Select features (independent variables) to predict price
X = df[['number_of_reviews', 'availability_365']]  
# Hypothesis: listings with more reviews or year-round availability might charge different prices

# Select target variable (dependent variable)
y = df['price']  

# Fit a linear regression model using scikit-learn
model = LinearRegression().fit(X, y)  
print("Linear Regression Coefficients:", model.coef_)  
# This prints how strongly each feature (reviews, availability) affects price.
# A positive coefficient means the feature increases the price; negative means it lowers it.

# Add a constant term for intercept (required by statsmodels)
X_sm = sm.add_constant(X)  

# Build and fit the OLS (Ordinary Least Squares) model
model_sm = sm.OLS(y, X_sm).fit()  

# Print detailed statistical summary
print(model_sm.summary())  
# This gives in-depth metrics like:
# - R-squared (how well the model explains price variation)
# - p-values (statistical significance of each feature)
# - confidence intervals, standard errors
# - F-statistic (overall model fit)

# 👉 Use Case:
# Urban analysts or stakeholders can use this model to understand what drives pricing
# and if availability or popularity significantly impact cost.
