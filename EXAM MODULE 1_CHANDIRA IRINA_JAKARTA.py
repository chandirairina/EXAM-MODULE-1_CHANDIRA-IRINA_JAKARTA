#NOMOR 1 FIX
def Hashtag(string):
    #untuk kondisi empty string, input maupun result pasti bakal sama aja
    if string=="":
        return False
    else:
    #splitting the string 
        splitted=string.split()
    #membuat list yang berisi kata2 dari string dengan huruf depan kapital semua
        capitalized=[]

    #membuat kata2 dari string supaya huruf depannya kapital semua    
        for i in splitted:
            capitalized.append(i.capitalize())

    #string kosong buat nampung gabungan kata2 yang udah kapital depannya
        stringbaru=""
    #menggabungkan string yang huruf depan dari setiap katanya udah huruf kapital semua
        for j in capitalized:
            stringbaru+=j

    #supaya depannya ada hashtagnya
        stringbaru="#"+stringbaru
    
    #kalau final result lebih dari 140 chars, return False
        if len(stringbaru)>140:
            return False
        else:
            return stringbaru

#normal case, random capitalized words
tes=Hashtag(" Hello there how are you doing")
print(tes)

#case banyak spasi
tesdua=Hashtag(" Hello    World")
print(tesdua)

#case of empty string
tes2=Hashtag("")
print(tes2)

# #case of string longer than 140 words
# tes3=Hashtag("Sebelumnya Perkenalkan Saya Angel Team Operational Purwadhika Jakarta ingin menginformasikan kelas kita yg sementara full online sampai situasi kondusif, untuk kelas perdana kita akan di mulai, ")
# print(tes3)

#NOMOR 2 FIX
def create_phone_number(number):
    nolsembilan=[1,2,3,4,5,6,7,8,9,0]
#panjang string harus 10
    if len(number)==10:
#empty string buat nampung angka dalam bentuk string
        phone=""
        for i in number:
#harus between 0-9
            if type(i)==int and i in nolsembilan:
#supaya "phone" berisi angka dalam bentuk string
                phone+=str(i)
            else:
                # print("not integer or not between 0-9")
                return False
                break

#bikin format phone numbernya
        phoneno="("+phone[0:3]+")"+" "+phone[3:6]+"-"+phone[6:]
        return phoneno
    else:
        # print("should be 10 integers between 0-9")
        return False
        
#normal case
testno2_1=create_phone_number([1,2,3,4,5,6,7,8,9,0])
print(testno2_1)

# #case of more than 10 nums
# testno2_2=create_phone_number([1,2,3,4,5,6,7,8,9,0,1])
# print(testno2_2)

# #case of not all integers
# testno2_3=create_phone_number([1,"string",3,4,5,6,7,8,9,0])
# print(testno2_3)

#NOMOR 3 FIX
def sort_odd_even(num):

#case of an empty string, return empty string
    if num==[]:
        return num
    else:
#misahin dulu ganjil dan genap menjadi 2 list berbeda untuk mempermudah sorting
        ganjil=[]
        genap=[]
        for data in num:
            if data%2==0:
                genap.append(data)
            else:
                ganjil.append(data)

#bubble sort ganjil
        for angka in range(len(ganjil)-1):
            for angka1 in range(len(ganjil)-angka-1):
                if ganjil[angka1]>ganjil[angka1+1]:
                    ganjil[angka1],ganjil[angka1+1]=ganjil[angka1+1],ganjil[angka1]

#bubble sort genap
        for angka2 in range(len(genap)-1):
            for angka3 in range(len(genap)-angka2-1):
                if genap[angka3]<genap[angka3+1]:
                    genap[angka3],genap[angka3+1]=genap[angka3+1],genap[angka3]

#membuat empty list untuk nampung hasil susunan angka ganjil genap supaya ssuai keinginan
        lstbaru=[]

#membuat indexing utk ganjil dan genap
        idxgjl=0
        idxgnp=0
     
        for nums in num:
#masukin angka dari list "genap" yang udah sorted di tempat angka awal ("num") yang tadinya genap, 
            if nums%2==0:
                lstbaru.append(genap[idxgnp])
#indexnya dimajuin terus setiap udah masuk 1
                idxgnp+=1
#masukin angka ganjil yang sudah sorted di angka yang tadinya di tempat angka awal ("num") yang juga emang ganjil
            else:
                lstbaru.append(ganjil[idxgjl])
#indexnya dimajuin terus setiap udah masuk 1
                idxgjl+=1

        return lstbaru

#normal case
test1=sort_odd_even([5,3,2,8,1,4])
print(test1)

# #test other cases
# testing=sort_odd_even([1,2,3,4,5,6,7,8,9,10,11,12])
# print(testing)

# #case of an empty list
# test2=sort_odd_even([])
# print(test2)