from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        # Retrieve form data and convert to our custom data structure.
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        pred_df = data.get_data_as_data_frame()

        # Initialize the prediction pipeline and perform prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        prediction = results[0]
    except Exception as e:
        # In case of error, log the exception and provide a default message.
        prediction = f"An error occurred: {str(e)}"

    # Render the result page with prediction value
    return render_template('result.html', results=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0")