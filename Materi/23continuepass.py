#CONTINUE AND PASS

#PASS -->> berfungsi sebagai dummy, tidak akan dieksekusi

number = 0

while number < 5:
    number +=1

    if number ==3:
        pass

    print(number)

#CONTINUE 

number = 0
print(f"number is now -->> {number}") 

while number < 5 :
    number += 1
    print(f"number is now -->> {number}") #aksi 1

    if number == 3:
        print("Terserahmu!")
        continue #akan membuat loop meloncat ke step selanjutnya
    print("GA NGURUS NJIR!") #aksi 2

print("End!!!")