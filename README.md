# Student Performance Prediction – Machine Learning Portfolio Project

## Overview

This project demonstrates a complete machine learning workflow using Logistic Regression to predict whether a student is likely to pass based on academic and lifestyle factors.

The project was developed as part of my data science portfolio after completing the ALX Data Science Program. It showcases skills in data preparation, machine learning model development, evaluation, and documentation.

---

## Project Goal

The objective of this project is to answer the following question:

> Can we predict whether a student will pass using basic academic and lifestyle information?

This project uses a simple and explainable machine learning model, making it easy to understand and communicate to both technical and non-technical audiences.

---

## Dataset

This project uses a synthetic dataset generated within the notebook and Python script for educational and demonstration purposes.

The dataset contains the following features:

| Feature         | Description                          |
| --------------- | ------------------------------------ |
| study_hours     | Number of hours studied per week     |
| attendance_rate | Class attendance percentage          |
| previous_score  | Previous examination score           |
| sleep_hours     | Average hours of sleep per night     |
| practice_tests  | Number of practice tests completed   |
| passed          | Target variable (1 = Pass, 0 = Fail) |

---

## Machine Learning Approach

This is a supervised machine learning classification problem.

### Model Used

* Logistic Regression

Logistic Regression was selected because it is:

* Easy to understand
* Computationally efficient
* Highly interpretable
* Widely used for binary classification problems

---

## Project Structure

```text
student-performance-prediction/
│
├── README.md
├── requirements.txt
├── student_performance_model.py
├── student_performance_notebook.ipynb
└── .gitignore
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Jupyter Notebook
* Google Colab

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Halo95/student-performance-prediction.git
cd student-performance-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Model

```bash
python student_performance_model.py
```

---

## Results

The Logistic Regression model achieved:

**Accuracy: 90%**

### Classification Metrics

* Precision: Strong predictive performance
* Recall: High detection rate of passing students
* F1-Score: Balanced model performance

### Confusion Matrix

```text
[[29, 1],
 [ 3, 7]]
```

Interpretation:

* 29 students correctly identified as not passing
* 7 students correctly identified as passing
* 1 false positive prediction
* 3 false negative predictions

The results demonstrate that the model performs effectively on the evaluation dataset.

---

## Example Output

The model generates:

* Accuracy Score
* Classification Report
* Confusion Matrix
* Predictions for new student records

---

## Educational Impact

This model can help educational institutions identify students who may require additional academic support before final examinations.

Potential applications include:

* Early intervention programs
* Academic performance monitoring
* Student support systems
* Educational analytics

---

## Skills Demonstrated

This project demonstrates proficiency in:

* Data Generation and Preparation
* Feature Engineering
* Data Analysis
* Train-Test Splitting
* Machine Learning Classification
* Logistic Regression
* Model Evaluation
* Performance Metrics Analysis
* Python Programming
* Technical Documentation
* Git and GitHub Version Control

---

## Future Improvements

Potential enhancements include:

* Using a real-world student performance dataset
* Adding data visualizations and exploratory data analysis (EDA)
* Comparing multiple machine learning models

  * Decision Tree
  * Random Forest
  * XGBoost
* Hyperparameter tuning
* Model explainability using SHAP
* Deploying the model as a web application using Streamlit

---

## Author

**Brian Quartey**

* ALX Data Science Graduate
* Aspiring Data Scientist
* Preparing for Graduate Studies in Data Science and Analytics

GitHub: https://github.com/Halo95

---

## License

This project is intended for educational and portfolio purposes.
