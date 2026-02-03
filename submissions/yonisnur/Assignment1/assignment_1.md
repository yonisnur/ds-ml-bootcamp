1\. Definition of Machine Learning

Machine Learning is a subfield of artificial intelligence that focuses
on developing algorithms and models that can learn from data and make
predictions or decisions based on that data. Instead of following fixed
rules, machine learning systems improve their performance as they are
exposed to more information.

Real-life example: A common real-world application of machine learning
is email spam detection. By analyzing past emails labeled as "spam" or
"not spam," a machine learning model learns patterns such as repeated
keywords, sender behavior, and message structure. Once trained, the
model can automatically classify new incoming emails, helping users
filter unwanted messages efficiently.

------------------------------------------------------------------------

2\. Supervised Learning vs. Unsupervised Learning

2.1 Supervised Learning

Supervised learning uses labeled datasets, where each input is
associated with a known output. The objective is to learn the
relationship between input features and output labels so that the model
can accurately predict outcomes for new, unseen data.

Example: Email classification is a typical supervised learning task. The
model is trained on emails that are already labeled as spam or not spam.
After training, it can predict whether a new email belongs to either
category.

2.2 Unsupervised Learning

Unsupervised learning works with unlabeled data. Its goal is to identify
hidden patterns, structures, or relationships within the dataset without
predefined output labels.

Example: Customer segmentation is an example of unsupervised learning.
By analyzing customer purchasing behavior, the algorithm can group
customers with similar habits together, which can help businesses design
targeted marketing strategies.

Illustrative analogy -- Sorting books without labels: Imagine organizing
a box of books with no categories provided. By observing similarities,
you may group mystery novels together, place textbooks in another pile,
and separate comic books based on their visual style. This process
resembles how unsupervised learning discovers structure in raw data.

Summary comparison: Overall, supervised learning is best suited for
prediction tasks with known outcomes, while unsupervised learning is
useful for discovering patterns and trends in unstructured data.

------------------------------------------------------------------------

3\. Overfitting: Causes and Prevention

Overfitting occurs when a machine learning model learns the training
data too closely, including noise and irrelevant details, which reduces
its ability to generalize to new data.

3.1 Causes of Overfitting

The training dataset is too small and does not represent all possible
input variations.

The dataset contains noisy or irrelevant features.

The model is trained for too many iterations on the same data.

The model is overly complex relative to the amount of available data.

3.2 Example of Overfitting

Consider a model trained to identify dogs in images. If most training
images show dogs outdoors in parks, the model may incorrectly associate
grass with the presence of a dog. As a result, it may fail to recognize
dogs indoors, demonstrating poor generalization.

3.3 Prevention Methods

Overfitting can be reduced by using larger and more diverse datasets,
simplifying the model, applying regularization techniques, and
validating performance using unseen data.

------------------------------------------------------------------------

4\. Training Data and Test Data Splitting

In machine learning, datasets are typically divided into training data
and test data. The training set is used to teach the model patterns and
relationships, while the test set is used to evaluate how well the model
performs on new, unseen data.

A common split ratio is 70--80% for training and 20--30% for testing.
This separation is necessary to assess the model's ability to generalize
beyond the data it was trained on and to detect issues such as
overfitting.

------------------------------------------------------------------------

5\. Case Study: Machine Learning in Healthcare

Title

Automatically Explaining Machine Learning Prediction Results: A
Demonstration on Type 2 Diabetes Risk Prediction

Summary

This study applied machine learning techniques to predict the risk of
Type 2 Diabetes using electronic medical record data. In addition to
achieving high prediction accuracy, the research emphasized
explainability, allowing clinicians to understand why specific
predictions were made.

Key Findings

The proposed method successfully explained predictions for a large
proportion of correctly classified patients.

Explainable predictions increased transparency, making the model more
suitable for clinical use.

The study demonstrated that machine learning can support early diagnosis
by extracting meaningful patterns from complex medical data.

------------------------------------------------------------------------

References

GeeksforGeeks. (n.d.). *Real-life applications of machine learning*.
Retrieved from
<https://www.geeksforgeeks.org/machine-learning/real-life-applications-of-machine-learning/>

GeeksforGeeks. (n.d.). *Difference between supervised and unsupervised
learning*. Retrieved from
<https://www.geeksforgeeks.org/machine-learning/difference-between-supervised-and-unsupervised-learning/>

Amazon Web Services (AWS). (n.d.). *What is overfitting?* Retrieved from
<https://aws.amazon.com/what-is/overfitting/>

Lundberg, S. M., & Lee, S. I. (2017). *Automatically explaining machine
learning prediction results: A demonstration on type 2 diabetes risk
prediction*. arXiv preprint arXiv:1705.07874. Retrieved from
<https://arxiv.org/abs/1705.07874>
