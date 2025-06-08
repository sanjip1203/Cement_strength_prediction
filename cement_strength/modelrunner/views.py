import numpy as np
import pickle
from django.shortcuts import render
from django.http import JsonResponse

# Load model and scaler once
with open('modelrunner/models/best_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('modelrunner/models/minmax_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

def predict_csMPa(request):
    if request.method == 'POST':
        try:
            # Get input values from POST
            cement = float(request.POST.get('cement'))
            slag = float(request.POST.get('slag'))
            flyash = float(request.POST.get('flyash'))
            water = float(request.POST.get('water'))
            superplasticizer = float(request.POST.get('superplasticizer'))
            coarseaggregate = float(request.POST.get('coarseaggregate'))
            fineaggregate = float(request.POST.get('fineaggregate'))
            age = float(request.POST.get('age'))

            # Prepare input array
            input_data = np.array([[cement, slag, flyash, water, superplasticizer, coarseaggregate, fineaggregate, age]])

            # Scale the input
            input_scaled = scaler.transform(input_data)

            # Predict
            prediction = model.predict(input_scaled)[0]

            return render(request, 'predict.html', {'prediction': prediction})

        except Exception as e:
            return render(request, 'predict.html', {'error': str(e)})

    return render(request, 'predict.html')
