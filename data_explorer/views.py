from django.shortcuts import render, redirect
import pandas as pd
from .forms import DatasetUploadForm
from .models import Dataset

def upload_dataset(request):
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_data', dataset_id=form.instance.id)
    else:
        form = DatasetUploadForm()
    return render(request, 'upload.html', {'form': form})

def view_data(request, dataset_id):
    dataset = Dataset.objects.get(id=dataset_id)
    data = pd.read_csv(dataset.file.path)
    stats = data.describe().to_html(classes="min-w-full text-center divide-y divide-gray-200")
    return render(request, 'data.html', {'stats': stats})
