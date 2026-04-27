from django.shortcuts import render
from django.http import JsonResponse
import json

ARABICA_ROBUSTA = [
    {"kategori": "Bentuk", "arabica": "Pipih, Lonjong, garis tengah melengkung", "robusta": "Bulat, kecil, garis tengah lurus"},
    {"kategori": "Warna", "arabica": "Cokelat terang hingga sedang", "robusta": "Cokelat gelap hingga sangat gelap"},
    {"kategori": "Rasa", "arabica": "Asam tinggi, manis, kompleks, fruity, floral", "robusta": "Pahit, bodi tebal, earthy, kacang"},
    {"kategori": "Ketinggian", "arabica": "1000–2100 mdpl", "robusta": "< 800 mdpl"},
    {"kategori": "Aroma", "arabica": "Harum, kaya", "robusta": "Kurang harum, kuat"},
    {"kategori": "Kafein", "arabica": "Rendah (1.1%–1.4%)", "robusta": "Tinggi (1.7%–4.0%)"},
]

GERAI_KOPI = [
    {"tahun": 2022, "jumlah": 8.5},
    {"tahun": 2023, "jumlah": 10.0},
    {"tahun": 2024, "jumlah": 10.8},
    {"tahun": 2025, "jumlah": 11.5},
]

EKSPOR_IMPOR = [
    {"tahun": 2023, "ekspor_vol": 279937, "ekspor_val": 929009, "impor_vol": 40899, "impor_val": 116996},
    {"tahun": 2024, "ekspor_vol": 316721, "ekspor_val": 1638116, "impor_vol": 52293, "impor_val": 186733},
]

TOP_NEGARA = [
    {"negara": "USA", "volume": 44307, "nilai": 307426},
    {"negara": "Egypt", "volume": 31479, "nilai": 142516},
    {"negara": "Malaysia", "volume": 31084, "nilai": 130476},
    {"negara": "Belgium", "volume": 21298, "nilai": 115717},
    {"negara": "Russia", "volume": 21201, "nilai": 104711},
]

PROVINSI_DATA = [
    {"provinsi": "Aceh", "luas": 113099, "produksi": 74131, "produktivitas": 0.66},
    {"provinsi": "Sumatera Utara", "luas": 99064, "produksi": 91695, "produktivitas": 0.93},
    {"provinsi": "Sumatera Barat", "luas": 23884, "produksi": 15316, "produktivitas": 0.64},
    {"provinsi": "Riau", "luas": 4912, "produksi": 1834, "produktivitas": 0.37},
    {"provinsi": "Jambi", "luas": 32029, "produksi": 23227, "produktivitas": 0.73},
    {"provinsi": "Sumatera Selatan", "luas": 267435, "produksi": 219586, "produktivitas": 0.82},
    {"provinsi": "Bengkulu", "luas": 90500, "produksi": 55634, "produktivitas": 0.61},
    {"provinsi": "Lampung", "luas": 152609, "produksi": 120379, "produktivitas": 0.79},
    {"provinsi": "Bangka Belitung", "luas": 398, "produksi": 110, "produktivitas": 0.28},
    {"provinsi": "Kepulauan Riau", "luas": 18, "produksi": 1, "produktivitas": 0.06},
    {"provinsi": "Jawa Barat", "luas": 55958, "produksi": 26479, "produktivitas": 0.47},
    {"provinsi": "Jawa Tengah", "luas": 48933, "produksi": 26802, "produktivitas": 0.55},
    {"provinsi": "DI Yogyakarta", "luas": 1874, "produksi": 1877, "produktivitas": 1.00},
    {"provinsi": "Jawa Timur", "luas": 96311, "produksi": 54128, "produktivitas": 0.56},
    {"provinsi": "Banten", "luas": 6418, "produksi": 2019, "produktivitas": 0.31},
    {"provinsi": "Bali", "luas": 33749, "produksi": 14711, "produktivitas": 0.44},
    {"provinsi": "Nusa Tenggara Barat", "luas": 14081, "produksi": 6423, "produktivitas": 0.46},
    {"provinsi": "Nusa Tenggara Timur", "luas": 74269, "produksi": 24377, "produktivitas": 0.33},
    {"provinsi": "Kalimantan Barat", "luas": 7455, "produksi": 2975, "produktivitas": 0.40},
    {"provinsi": "Kalimantan Tengah", "luas": 2151, "produksi": 238, "produktivitas": 0.11},
    {"provinsi": "Kalimantan Selatan", "luas": 2436, "produksi": 886, "produktivitas": 0.36},
    {"provinsi": "Kalimantan Timur", "luas": 1294, "produksi": 124, "produktivitas": 0.10},
    {"provinsi": "Kalimantan Utara", "luas": 859, "produksi": 107, "produktivitas": 0.12},
    {"provinsi": "Sulawesi Utara", "luas": 7666, "produksi": 3724, "produktivitas": 0.49},
    {"provinsi": "Sulawesi Tengah", "luas": 11793, "produksi": 3133, "produktivitas": 0.27},
    {"provinsi": "Sulawesi Selatan", "luas": 80229, "produksi": 31785, "produktivitas": 0.40},
    {"provinsi": "Sulawesi Tenggara", "luas": 9433, "produksi": 2609, "produktivitas": 0.28},
    {"provinsi": "Gorontalo", "luas": 1405, "produksi": 126, "produktivitas": 0.09},
    {"provinsi": "Sulawesi Barat", "luas": 16978, "produksi": 4750, "produktivitas": 0.28},
    {"provinsi": "Maluku", "luas": 1386, "produksi": 486, "produktivitas": 0.35},
    {"provinsi": "Maluku Utara", "luas": 390, "produksi": 16, "produktivitas": 0.04},
    {"provinsi": "Papua Barat", "luas": 191, "produksi": 6, "produktivitas": 0.03},
    {"provinsi": "Papua Barat Daya", "luas": 87, "produksi": 3, "produktivitas": 0.03},
    {"provinsi": "Papua", "luas": 368, "produksi": 93, "produktivitas": 0.25},
    {"provinsi": "Papua Tengah", "luas": 5770, "produksi": 1178, "produktivitas": 0.20},
    {"provinsi": "Papua Pegunungan", "luas": 10050, "produksi": 3273, "produktivitas": 0.33},
]


def index(request):
    context = {
        "arabica_robusta": json.dumps(ARABICA_ROBUSTA),
        "gerai_kopi": json.dumps(GERAI_KOPI),
        "ekspor_impor": json.dumps(EKSPOR_IMPOR),
        "top_negara": json.dumps(TOP_NEGARA),
        "provinsi_data": json.dumps(PROVINSI_DATA),
    }
    return render(request, "story/index.html", context)


def map_data(request):
    return JsonResponse({"data": PROVINSI_DATA})
