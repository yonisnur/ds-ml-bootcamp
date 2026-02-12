# Reflection on Data Preparation and Feature Engineering

This reflection explains the key decisions made during data cleaning, preprocessing, and feature engineering, and the rationale behind each choice.

## Handling Missing Values
For **numerical features**, I used the **median** instead of the mean or mode. The median is robust to outliers and skewed distributions, which were present in variables such as price-related fields. Using the mean could have shifted values unrealistically due to extreme observations.  
For **categorical features**, I used the **mode**, as it preserves the most common category and is appropriate for nominal data where numerical averaging is not meaningful.

## Outlier Detection and Treatment
I applied the **Interquartile Range (IQR) method** to detect outliers. The IQR approach is effective because it does not assume a normal distribution and is resistant to extreme values.  
Instead of removing outliers, I used **IQR capping (winsorization)** to limit extreme values within acceptable bounds. This decision helped retain all observations while reducing the disproportionate influence of extreme values on the model, which is especially important given the limited dataset size.

## Feature Engineering
Several features were engineered to improve model performance and interpretability:
- **Log-transformed price (`LogPrice`)**: This was created to reduce right skewness in the target variable and stabilize variance, making relationships more linear.
- **Derived numerical features** (e.g., ratios or aggregated measures): These capture more meaningful patterns than raw variables alone and help the model learn underlying relationships.
- **Categorical encoding**: Categorical variables were converted into dummy (0/1) variables so that they could be used effectively by machine learning algorithms.

Each engineered feature was selected based on domain relevance and its potential contribution to predictive power, while avoiding unnecessary complexity.

## Feature Scaling
I applied **feature scaling only to input features (X)** and not to the target variable. Continuous numerical features were standardized to ensure that variables measured on different scales contributed equally to the model.  
Binary dummy variables (0/1) were left unscaled because scaling them would reduce interpretability and offers no practical benefit.

## Conclusion
Overall, the preprocessing decisions prioritized **robustness, interpretability, and data integrity**. Using median imputation, IQR capping, and thoughtful feature engineering ensured that the dataset was well-prepared for modeling while minimizing bias and information loss.
