

# 🎓 Student Performance Indicator
<div align="center">
  <h2>Project Output</h2>
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
    <figure style="margin: 10px;">
      <img src="https://github.com/SamyakAnand/Student-Performance-Indicator/blob/main/Images/index.png?raw=true" alt="Index Page" width="300" style="border:2px solid #eee; border-radius:10px;">
      <figcaption style="text-align: center; margin-top: 5px; font-weight: bold;">Index Page</figcaption>
    </figure>
    <figure style="margin: 10px;">
      <img src="https://github.com/SamyakAnand/Student-Performance-Indicator/blob/main/Images/home.png?raw=true" alt="Prediction Page" width="300" style="border:2px solid #eee; border-radius:10px;">
      <figcaption style="text-align: center; margin-top: 5px; font-weight: bold;">Prediction Page</figcaption>
    </figure>
    <figure style="margin: 10px;">
      <img src="https://github.com/SamyakAnand/Student-Performance-Indicator/blob/main/Images/result.png?raw=true" alt="Result Page" width="300" style="border:2px solid #eee; border-radius:10px;">
      <figcaption style="text-align: center; margin-top: 5px; font-weight: bold;">Result Page</figcaption>
    </figure>
  </div>
</div>


## 🔍 Problem Statement

This project aims to understand how a student's academic performance (measured through test scores) is influenced by factors such as gender, ethnicity, parental education level, lunch type, and participation in a test preparation course.

---

## 📥 Data Collection

* 📊 **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)
* 🔢 **Shape**: 1000 rows × 8 columns
* 📁 Features include:

  * Gender
  * Race/Ethnicity
  * Parental Level of Education
  * Lunch
  * Test Preparation Course
  * Math Score (Target)
  * Reading Score
  * Writing Score

---

## 🧹 Data Preprocessing

* ✅ Checked for missing values
* ✅ Removed duplicates
* ✅ Ensured proper data types
* ✅ Verified unique values in categorical columns
* ✅ Scaled and encoded features using `ColumnTransformer`

---

## ⚙️ Project Workflow

1. **Data Ingestion**: Load, clean, split into train/test, and save.
2. **Data Transformation**: Build preprocessing pipeline with imputation, encoding, and scaling.
3. **Model Training**: Train and evaluate regression models (best: Linear Regression).
4. **Prediction Pipeline**: Load model and transformer, accept user input, and make predictions.
5. **Deployment**: Flask-based UI for score prediction hosted with Docker.

---

## 🔬 Usage

This project is suitable for:

* Exploratory Data Analysis (EDA)
* Predictive Modeling
* Educational Insights & Strategy Development

---

## 📜 License

Refer to the original dataset page on Kaggle for licensing information.

---

## 📚 Citation

If using this dataset or project, cite the Kaggle source and original dataset contributors.

---

## 🙏 Acknowledgments

Thanks to Kaggle and the original dataset contributors for providing this valuable educational data.


