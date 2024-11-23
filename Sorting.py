#Fitri Handayani_F55123017

#========Kode Program========

import random
import time

# Merge Sort 
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Bubble Sort 
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Generate array random
X = [random.randint(1, 100) for _ in range(10)]

# Time Complexity Merge Sort
start_time = time.perf_counter()
merge_sorted = X.copy()
merge_sort(merge_sorted)
end_time = time.perf_counter()
merge_time = end_time - start_time

# Time Complexity Bubble Sort
start_time = time.perf_counter()
bubble_sorted = X.copy()
bubble_sort(bubble_sorted)
end_time = time.perf_counter()
bubble_time = end_time - start_time

# Output
print(f"Array asli: {X}")
print(f"Merge Sort: {merge_sorted} (Waktu: {merge_time:.6f} detik)")
print(f"Bubble Sort: {bubble_sorted} (Waktu: {bubble_time:.6f} detik)")



#========Pseudocode========
# FUNGSI merge_sort(array)
#     JIKA panjang(array) > 1
#         mid = panjang(array) // 2
#         left = elemen array dari indeks 0 hingga mid - 1
#         right = elemen array dari indeks mid hingga akhir

#         PANGGIL merge_sort(left)
#         PANGGIL merge_sort(right)

#         i = 0, j = 0, k = 0

#         SELAMA i < panjang(left) DAN j < panjang(right)
#             JIKA left[i] < right[j]
#                 array[k] = left[i]
#                 i = i + 1
#             LAIN
#                 array[k] = right[j]
#                 j = j + 1
#             k = k + 1

#         SELAMA i < panjang(left)
#             array[k] = left[i]
#             i = i + 1
#             k = k + 1

#         SELAMA j < panjang(right)
#             array[k] = right[j]
#             j = j + 1
#             k = k + 1

# FUNGSI bubble_sort(array)
#     n = panjang(array)
#     UNTUK i dari 0 hingga n - 1
#         UNTUK j dari 0 hingga n - i - 2
#             JIKA array[j] > array[j + 1]
#                 TUKAR array[j] dengan array[j + 1]

# Buat array acak X dengan 10 elemen, setiap elemen bernilai antara 1 hingga 50

#     // Hitung waktu untuk Merge Sort
#     salin array X ke merge_sorted
#     mulai_waktu = waktu saat ini
#     PANGGIL merge_sort(merge_sorted)
#     waktu_merge = waktu saat ini - mulai_waktu

#     // Hitung waktu untuk Bubble Sort
#     salin array X ke bubble_sorted
#     mulai_waktu = waktu saat ini
#     PANGGIL bubble_sort(bubble_sorted)
#     waktu_bubble = waktu saat ini - mulai_waktu

#     // Cetak hasil
#     CETAK "Array asli:", X
#     CETAK "Merge Sort:", merge_sorted, "(Waktu:", waktu_merge, "detik)"
#     CETAK "Bubble Sort:", bubble_sorted, "(Waktu:", waktu_bubble, "detik)"


#=====Analisis======
# 1. Merge Sort
#   a. Big O (Worst Case)
        # Di sini, n adalah jumlah elemen dalam array. Meskipun Merge Sort adalah algoritma divide-and-conquer, waktu eksekusinya tetap (n log n) dalam kasus terburuk, karena array dibagi menjadi dua bagian berulang kali (logaritmik) dan setiap elemen harus dibandingkan (linear).
    # b. Big Theta 
        # Merupakan kompleksitas yang lebih tepat karena dalam setiap kondisi (termasuk best case, average case, dan worst case), waktu eksekusi Merge Sort tetap (n log n).

#2. Bubble Sort
    # a. Big O (Worst Case)
        # Dalam kasus terburuk, setiap elemen dalam array dibandingkan dengan elemen lainnya, yang membutuhkan waktu sebesar n^2. Hal ini terjadi ketika array terbalik atau hampir terbalik.
    #b. Big Theta
        # Bubble Sort memiliki waktu eksekusi O(n^2) di semua kondisi, baik pada worst, average, dan best case (tergantung implementasi, jika tidak ada optimasi).

#3. Kesimpulan
    # Merge Sort lebih efisien daripada Bubble Sort dalam hal kompleksitas waktu, terutama untuk array yang lebih besar, karena Merge Sort memiliki waktu eksekusi O(n log n) dibandingkan dengan O(n^2) dari Bubble Sort.