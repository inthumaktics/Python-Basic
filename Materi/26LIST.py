#=====LIST=====

#1. Kumpulan data angka
data_angka = [1,2,3,4,20]
print(data_angka)

#2. Kumpulan data string
data_string = ["Erika", "Ellinor", "Plummy"]
print(data_string)

#3. Kumpulan data boolean 
data_boolean = [True, False, True, True, False]
print(data_boolean)

#4. Kumpulan data campuran
data_campuran = [1, "apa lo", 2, "Responsi anjai", 3,"Astaghfirullah!", True]
print(data_campuran)

#5. ALTERNATIF MEMBUAT LIST
data_range = range(0,20,3)
print(data_range)
data_list = list(data_range)
print(data_list)

#6. List dengan for loop, List comprehension
list_for = [i**5 for i in range(0,20)]
print(list_for)

#7. List dengan for if
list_for_if = [i for i in range(0, 20) if i != 5]
print(list_for_if)

list_for_if = [i for i in range(0, 20) if i%2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0, 20) if i%2 != 0]
print(list_for_if)
