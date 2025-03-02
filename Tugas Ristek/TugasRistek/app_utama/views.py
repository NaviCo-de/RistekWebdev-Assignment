#Views app_utama
from django.shortcuts import render, redirect
from .utils import read_json, write_json
from datetime import datetime

def home(request):
    return render(request, 'home.html')
def list_data(request):
    data = read_json()

    term = request.GET.get('search','').lower()

    if term:
        filtered_data = []
        for item in data:
            if term in item['judul_tryout'].lower():
                filtered_data.append(item)
        
        data = filtered_data

    return render(request, 'list.html', {'data':data})

def add_data(request):
    if request.method == 'POST':
        #Ngambil data dari form html
        judul_tryout = request.POST.get('judul_tryout')
        kategori = request.POST.get('kategori')
        tanggal_dibuat = datetime.now().strftime("%d/%m/%Y")

        data = read_json()
        new_id = len(data) + 1

        upload_data = {
            'id': new_id,
            "judul_tryout": judul_tryout,
            "kategori": kategori,
            "tanggal_dibuat": tanggal_dibuat
        }

        data.append(upload_data)

        write_json(data)

        return redirect('tryout')
    return render(request, 'add_data.html')

def edit_data(request, id):
    data = read_json()

    entry = next((item for item in data if item['id'] == id), None)

    if request.method == 'POST':
        entry['judul_tryout'] = request.POST.get('judul_tryout')
        entry['kategori'] = request.POST.get('kategori')
        entry['tanggal_dibuat'] = datetime.now().strftime("%d/%m/%Y")

        write_json(data)

        return redirect('tryout')
    return render(request, 'edit.html', {'entry':entry})

def delete_data(request, id):
    data = read_json()

    data = [item for item in data if item['id'] != id]

    for index, item in enumerate(data, start=1):
        item['id'] = index
    
    write_json(data)

    return redirect('tryout')
