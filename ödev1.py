"""Aldığı isim soy isim ile listeye öğrenci ekleyen +
Aldığı isim soy isim ile eşleşen değeri listeden kaldıran + 
Listeye birden fazla öğrenci eklemeyi mümkün kılan 
Listedeki tüm öğrencileri tek tek ekrana yazdıran +
Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan +
Listeden birden fazla öğrenci silmeyi mümkün kılan(döngü kullanınız) +
"""
   
liste = ["Ahmet Ali","Kerem Ali","Zeynep Ali"]
               
def ogrenci_kayit_ve_var_olan_ogrenci_silme():
    giriş = input(str("Lütfen İsim Soyisim giriniz:"))
    liste.append(giriş)
    if giriş in liste:
        liste.remove(giriş)
        print(f"Var olan öğrenci tekrardan eklenmeye çalışıldığı için silinmiştir.\n {liste}")
            
def çoklu_ogrenci_ekleme():
    ögrenci_sayisi=int(input("Eklemek istediğiniz öğrenci sayısını giriniz: "))
    a=0
    while a < ögrenci_sayisi:
        giriş2 =input(f"Eklemek istediğiniz {a+1}. öğrencinin ismi ve soyismi: ")
        liste.append(giriş2)
        a = a + 1
        print("Öğrenciler başarıyla eklenmiştir.")

def öğrenci_bilgileri_öğrenme():
    for student in enumerate(liste):
        print(student)
        

def çoklu_öğrenci_silme():
    if len(liste) == 5:
        while len(liste) == 3:
            liste.pop()
            print(liste)
islem = int(input("Lütfen sayı yapmak istediğiniz işlemle ilgili sayı giriniz:")) 
while islem < 5:                
    if islem == 0:
        ogrenci_kayit_ve_var_olan_ogrenci_silme()
        break
    elif islem == 1:
        çoklu_ogrenci_ekleme()
        break
    elif islem == 2:
        öğrenci_bilgileri_öğrenme()
        break
    elif islem == 3 :
        çoklu_öğrenci_silme()
        break
else:
    print("Yanlış işlem seçtiniz.Lütfen tekrar başlatın.")
    



            

         
