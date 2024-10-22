from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dummy prediction function for each model
def predict(model, inputs):
    if model == "Nearest Neighbor":
        return "Benign" if random.random() > 0.5 else "Malignant"
    elif model == "Naïve Bayes":
        return "Malignant" if random.random() > 0.5 else "Benign"
    elif model == "Decision Tree":
        return "Malignant" if random.random() > 0.5 else "Benign"
    else:
        return "Unknown Model"

@app.route('/', methods=['GET', 'POST'])
def index():
    predictions = []
    if request.method == 'POST':
        # Retrieve form inputs
        clump_thickness = request.form['clump_thickness']
        uniformity_cell_size = request.form['uniformity_cell_size']
        uniformity_cell_shape = request.form['uniformity_cell_shape']
        marginal_adhesion = request.form['marginal_adhesion']
        single_epithelial_cell_size = request.form['single_epithelial_cell_size']
        bland_chromatin = request.form['bland_chromatin']
        normal_nucleoli = request.form['normal_nucleoli']
        selected_models = request.form.getlist('model')

        # Format the inputs
        inputs = f"Clump Thickness: {clump_thickness}, Uniformity Cell Size: {uniformity_cell_size}, Uniformity Cell Shape: {uniformity_cell_shape}, Marginal Adhesion: {marginal_adhesion}, Single Epithelial Cell Size: {single_epithelial_cell_size}, Bland Chromatin: {bland_chromatin}, Normal Nucleoli: {normal_nucleoli}"

        # Make predictions for each selected model
        for model in selected_models:
            prediction = predict(model, inputs)
            predictions.append(f"Model: {model} - Prediction: {prediction}")
        
        return render_template('index.html', prediction=predictions, model=selected_models, inputs=inputs)

    return render_template('index.html', prediction=predictions)

if __name__ == '__main__':
    app.run(debug=True)