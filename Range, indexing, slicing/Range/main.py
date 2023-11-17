#buatlah sebuah list angka
#didalam variable num_list
#dengan isian [2, 4, 6, 8, 10, ...., 180]

num_list = list(range(2, 181))


# tampilkan item angka 18 dari num_list
print(num_list[16])  #positive indexing

# tampilkan item angka 172 dari num_list
print(num_list[-9]) #negative indexing

#tampilkan kumpulan angka
#seperti berikut
#[10, 20, 30, 40, 50, 60, 70, 80, 100]

print(num_list[8:101:10])
