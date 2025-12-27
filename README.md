# Iris Flower Classification using K-Nearest Neighbors (KNN)

This is my first machine learning project.
In this project, I implemented the K-Nearest Neighbors (KNN) algorithm
from scratch to classify iris flowers into different species.

---

## Project Objective

The main objective of this project is to understand how the KNN algorithm works by:
- Implementing KNN manually without using machine learning libraries
- Evaluating model accuracy
- Analyzing the effect of different values of K on performance

---

## Dataset

- Name: Iris Dataset
- Total samples: 150
- Features:
  - Sepal length
  - Sepal width
  - Petal length
  - Petal width
- Target variable:
  - Species (Setosa, Versicolor, Virginica)

The dataset is stored in the file `iris.csv`.

---

## Algorithm Used

### K-Nearest Neighbors (KNN)

Steps followed in the algorithm:
1. Calculate the distance between a test point and all training points
2. Select the K nearest neighbors
3. Perform majority voting among the neighbors
4. Predict the class label

The entire algorithm is implemented from scratch using Python.

---

## Exploratory Data Analysis (EDA)

- Examined the dataset structure and checked for missing values
- Visualized relationships between features using pair plots
- Observed that petal features provide better separation between species compared to sepal features

---

## Model Evaluation

- The dataset is split into training and testing sets
- Model accuracy is calculated for different values of K
- Multiple experiments are performed to reduce the effect of randomness from a single data split

---

## Results

- The KNN model achieved high accuracy on the Iris dataset
- A balanced value of K produced stable and reliable predictions

---

## Tools and Libraries Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## Learning Outcome

Through this project, I learned:
- How the KNN algorithm works internally
- The importance of choosing an appropriate value of K
- Distance calculation and majority voting
- How to structure and document a machine learning project.

