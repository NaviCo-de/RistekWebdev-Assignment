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
            "tanggal_dibuat": tanggal_dibuat,
            "list_pertanyaan": []
        }

        data.append(upload_data)

        write_json(data)

        return redirect('tryout')
    return render(request, 'add_data.html')

def detail_data(request, id, judul_tryout):
    data = read_json()

    item = next((item for item in data if item['id']==id), None)
    
    return render(request, 'detail_data.html', {'item':item})

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

def add_question(request, id, judul_tryout):
    if request.method == 'POST':
        get_question = request.POST.get('pertanyaan')
        get_jawaban_salah = request.POST.get('jawaban_salah')
        get_jawaban_benar = request.POST.get('jawaban_benar')

        data = read_json()
        for item in data:
            if item["id"] == id:
                tryout = item
                break
        nomor = len(tryout["list_pertanyaan"]) + 1

        data_pertanyaan = {
            "nomor_pertanyaan" : nomor,
            "pertanyaan": get_question,
            "jawaban_benar": get_jawaban_benar,
            "jawaban_salah": get_jawaban_salah
        }

        tryout["list_pertanyaan"].append(data_pertanyaan)

        write_json(data)
        return redirect('detail_data', judul_tryout=judul_tryout, id = id)
        
    return render(request, 'add_question.html')

def edit_question(request, id, judul_tryout, nomor_pertanyaan):
    data = read_json()

    if request.method == 'POST':
        for item in data:
            if item["id"] == id:
                tryout = item
                break
        for pertanyaan in tryout["list_pertanyaan"]:
            if pertanyaan["nomor_pertanyaan"] == nomor_pertanyaan:
                entry = pertanyaan

        entry["pertanyaan"] = request.POST.get('pertanyaan_baru')
        entry["jawaban_benar"] = request.POST.get('jawaban_benar_baru')
        entry["jawaban_salah"] = request.POST.get('jawaban_salah_baru')

        write_json(data)

        return redirect('detail_data', judul_tryout=judul_tryout, id = id)
    return render(request, 'edit_question.html')

def delete_question(request, id, judul_tryout, nomor_pertanyaan):
    data = read_json()
    
    for item in data:
        if item["id"] == id:
            tryout = item
            
        tryout["list_pertanyaan"] = [pertanyaan for pertanyaan in tryout["list_pertanyaan"] if pertanyaan["nomor_pertanyaan"] != nomor_pertanyaan]

        for nomor, questions in enumerate(tryout["list_pertanyaan"], start=1):
            questions['nomor_pertanyaan'] = nomor
    
        write_json(data)
        break

    return redirect('detail_data', judul_tryout=judul_tryout, id = id)

