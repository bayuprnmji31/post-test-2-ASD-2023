''''
NAMA = BAYU PURNAMA AJI
NIM  = 2209116050
POST_TEST 2 ASD
'''


def fibonacciSearch(arr, x):
    """
    Fungsi Fibonacci Search yang mengembalikan indeks dari elemen x pada array arr,
    atau -1 jika x tidak ada di arr.
    """
    n = len(arr)
    fib2 = 0  # fibonacci(n-2)
    fib1 = 1  # fibonacci(n-1)
    fib = fib2 + fib1  # fibonacci
  
    # Cari nilai dari fibonacci(n) yang terbesar yang lebih kecil atau sama dengan n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
  
    # Indeks awal untuk pencarian
    offset = -1 #mempengaruhi posisi index wibi pada kolom 1
  
    # Melakukan pencarian
    while fib > 1:
        i = min(offset+fib2, n-1)
  
        # Jika x lebih besar daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kanan
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
  
        # Jika x lebih kecil daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kiri
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
  
        # Jika x ditemukan, kembalikan indeks i
        else:
            return i
  
    # Jika elemen tidak ditemukan, kembalikan -1
    if fib1 and arr[offset+1] == x:
        return offset+1
  
    # Jika elemen tidak ditemukan, kembalikan -1
    return -1


# fungsi data ini adalah sebagai mendatar list di dalam list agar list index 3  sejajar dengan list index 1 dan 2
def datar(arr):
    flat_arr = []
    for item in arr:
        if isinstance(item, list):
            flat_arr.extend(datar(item))
        else:
            flat_arr.append(item)
    return flat_arr

nama= ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Mencari posisi index data Arsel, Avivah, dan Daiva dengan searching jump search
index_arsel  = fibonacciSearch(nama, "Arsel")
index_avivah = fibonacciSearch(nama, "Avivah")
index_daiva  = fibonacciSearch(datar(nama), "Daiva")

# Mencari posisi index wahyu pada kolom o dan wibi pada kolom 1 dengan searching jump search
index_wahyu  = fibonacciSearch(nama[3],"wahyu")
index_wibi   = fibonacciSearch(nama[3],"Wibi")

# output posisi index arsel, avivah, dan daiva berdasarkan urutan
print("1. Arsel di Index {}, Avivah di Index {}, Daiva di Index {}".format(index_arsel, index_avivah, index_daiva))

# output posisi index wahyu pada kolom 0
print("2. Wahyu berada di index {} pada kolom 0".format(index_wahyu+4))

# output posisi index wibi pada kolom 1
print("3. Wibi berada di index {} pada kolom 1".format(index_wibi+2))