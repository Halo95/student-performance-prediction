# Student Performance Prediction – Machine Learning Portfolio Project

This is a simple, beginner-friendly machine learning project built for a data science portfolio. The goal is to predict whether a student is likely to pass based on study-related habits such as study time, attendance, previous scores, and sleep hours.

## Project Goal

The model answers this question:

> Can we predict whether a student will pass using basic academic and lifestyle information?

This project is easy to explain because it uses common, understandable features and a simple classification model.

## Dataset

This project uses a small synthetic dataset created inside the notebook/script. The dataset contains the following columns:

- `study_hours`: Number of hours studied per week
- `attendance_rate`: Class attendance percentage
- `previous_score`: Previous exam score
- `sleep_hours`: Average sleep hours per night
- `practice_tests`: Number of practice tests completed
- `passed`: Target variable; 1 means passed, 0 means failed

## Machine Learning Approach

This is a supervised classification problem.

The model used is **Logistic Regression**, which is a simple and explainable machine learning algorithm commonly used for binary classification problems.

## Project Structure

```text
student-performance-ml/
│
├── README.md
├── requirements.txt
├── student_performance_model.py
├── student_performance_notebook.ipynb
└── .gitignore
```

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/student-performance-ml.git
cd student-performance-ml
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the model:

```bash
python student_performance_model.py
```

## Example Output

The script trains a Logistic Regression model and prints:

- Model accuracy
- Classification report
- Confusion matrix
- Example prediction for a new student

## Sample Business / Education Insight

The model can help schools or academic advisors identify students who may need extra support before exams. For example, students with low study hours, poor attendance, and low previous scores may be flagged for academic intervention.

## Skills Demonstrated

- Data generation and preparation
- Exploratory understanding of features
- Train-test split
- Machine learning classification
- Model evaluation using accuracy, precision, recall, and F1-score
- Making predictions with a trained model
- Communicating results clearly

## Future Improvements

- Use a real student performance dataset
- Add visualizations
- Compare multiple models such as Decision Tree and Random Forest
- Deploy the model with Streamlit
- Add model explainability using feature importance

## Author

Created by Brian Quartey as part of a data science portfolio after completing the ALX Data Science program.
