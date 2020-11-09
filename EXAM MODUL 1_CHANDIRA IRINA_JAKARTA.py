#NOMOR 1
def Hashtag(string):
    if type(string)==str:
        #untuk kondisi empty string, input maupun result akan sama
        if string=="":
            return False
        else:
        #splitting the string 
            splitted=string.split()
        #membuat list yang berisi kata2 dari string dengan huruf depan kapital semua
            capitalized=[]

        #membuat kata2 dari string agar huruf depannya semuanya kapital    
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
#bikin format phone numbernya
        phoneno="("+phone[0:3]+")"+" "+phone[3:6]+"-"+phone[6:]
        return phoneno
        
#NOMOR 3 FIX
def sort_odd_even(num):

#case of an empty string, return empty string
    if num==[]:
        return num
    else:
#memisahkan ganjil dan genap menjadi 2 list berbeda untuk mempermudah sorting
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
#masukan angka dari list "genap" yang udah sorted di tempat angka awal ("num") yang tadinya genap
            if nums%2==0:
                lstbaru.append(genap[idxgnp])
#indexnya dimajuin terus setiap udah masuk 1
                idxgnp+=1
#masukan angka ganjil yang sudah sorted di angka yang tadinya di tempat angka awal ("num") yang juga emang ganjil
            else:
                lstbaru.append(ganjil[idxgjl])
#indexnya dimajukan setiap sudah masuk 1
                idxgjl+=1
                
        return lstbaru