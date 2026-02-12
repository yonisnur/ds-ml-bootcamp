**A Study on Car Rental Data for Machine Learning Applications**

**1. Title and Collection Method**

**Title**

**Car Rental Usage and Pricing Dataset: A Real-World Data Collection for
Machine Learning**

**Collection Method**

This dataset focuses on **car rental usage and pricing patterns** and
was collected using a **Car Rental Data Collection Form**, similar to a
survey questionnaire. The data was gathered manually from individuals
involved in car rental services or customers renting vehicles.

The collected information includes:

- rental duration in hours

- type of car

- seating capacity

- car condition

- transmission type

- rental price

The dataset was stored in **CSV format**, making it suitable for
analysis and machine learning tasks.\
Importantly, this dataset was **self-collected** and not obtained from
pre-existing repositories such as Kaggle or UCI, ensuring originality
and real-world relevance.

------------------------------------------------------------------------

**2. Description of Features and Label**

**Input Variables (Features -- X)**

The dataset contains the following input variables that describe the
characteristics of each car rental record:

  -------------------------------------------------------------------
  **Feature Name**   **Description**                    **Data Type**
  ------------------ ---------------------------------- -------------
  Rental Duration    Number of hours the car is rented  Numerical
  (Hours)                                               

  Type of Car        Category of the car (SUV, VAN,     Categorical
                     Mini car, etc.)                    

  Seating Capacity   Number of passengers the car can   Numerical
                     carry                              

  Car Condition      Physical condition of the car (New Categorical
                     or Old)                            

  Transmission Type  Type of transmission (Automatic or Categorical
                     Manual)                            
  -------------------------------------------------------------------

**Output Variable (Label -- y)**

  -----------------------------------------
  **Label**   **Description**   **Data
                                Type**
  ----------- ----------------- -----------
  Rental      Cost of renting   Numerical
  Price       the car           

  -----------------------------------------

Since the output variable is a continuous numerical value, the dataset
is mainly suitable for **regression problems**.

------------------------------------------------------------------------

**3. Dataset Structure**

The dataset has a simple but effective structure that reflects
real-world car rental data.

- **Number of rows (samples):** More than 50 records

- **Number of columns:** 6 variables (timestamp excluded)

- **File format:** CSV

**Sample of the Dataset**

Table 1 presents a small sample of **5 rows** extracted from the dataset
to illustrate its structure.

**Table 1: Sample Records from the Car Rental Dataset**

  --------------------------------------------------------------------------------
  **Rental         **Type   **Seating    **Car         **Transmission   **Rental
  Duration         of Car** Capacity**   Condition**   Type**           Price**
  (Hours)**                                                             
  ---------------- -------- ------------ ------------- ---------------- ----------
  8                SUV      4            New           Automatic        10

  5                VAN      4            Old           Automatic        50

  5                Mini car 4            Old           Manual           12

  4                Mini car 2            New           Automatic        5

  1                SUV      2            New           Automatic        5000
  --------------------------------------------------------------------------------

This sample shows that the dataset contains both **numerical** and
**categorical** variables, which is common in real-world data and
important for data preprocessing practice.

------------------------------------------------------------------------

**4. Data Quality Issues**

Because the dataset represents real-world data, several data quality
issues are present:

1.  **Outliers**

    - Extremely high values such as a rental price of 5000 compared to
      other records may negatively affect model performance.

2.  **Inconsistent Data Entry**

    - Categorical values may be written differently (e.g., "Mini car"
      vs. "Mini Car").

3.  **Categorical Features**

    - Features such as car type, car condition, and transmission type
      require **encoding** before applying machine learning algorithms.

4.  **Different Feature Scales**

    - Rental duration, seating capacity, and rental price are on
      different scales, which may require **feature scaling**.

5.  **Possible Missing Values**

    - Since data was collected using a form, some entries may be
      incomplete or missing.

These issues will need to be addressed during the **data preprocessing
stage**.

------------------------------------------------------------------------

**5. Use Case in Machine Learning**

The dataset can be used in several machine learning applications:

**5.1 Regression**

- **Objective:** Predict the rental price of a car

- **Possible Models:** Linear Regression, Decision Tree Regression,
  Random Forest Regression

- **Application:** Helping car rental companies set fair and competitive
  prices.

**5.2 Classification**

- Rental prices can be categorized into classes such as:

  - Low

  - Medium

  - High

- This transforms the problem into a **classification task**.

**5.3 Clustering**

- Cars or rental records can be grouped based on:

  - rental duration

  - car type

  - rental price

- This can support **customer segmentation** and business insights.

------------------------------------------------------------------------

**6. Conclusion**

This car rental dataset provides a practical example of **real-world
data collection**. Although it contains quality issues such as outliers,
categorical variables, and possible missing values, it is highly
suitable for learning essential concepts in **Data Foundations for
Machine Learning**.

The dataset prepares learners for key preprocessing tasks such as data
cleaning, encoding, scaling, and feature engineering, making it an
excellent foundation for further machine learning modeling and analysis.
