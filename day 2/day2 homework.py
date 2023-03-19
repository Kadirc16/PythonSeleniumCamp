""" ÖDEV TANIMI:

Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

Bu öğrenci kayıt sistemine;

Aldığı isim soy isim ile listeye öğrenci ekleyen -
Aldığı isim soy isim ile eşleşen değeri listeden kaldıran -
Listeye birden fazla öğrenci eklemeyi mümkün kılan -
Listedeki tüm öğrencileri tek tek ekrana yazdıran -
Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir. """

students = ["Kadir Celep","Tarık Tekelioğlu","Recep Ballıoğlu"]

print(students)

def addStudent ():
    name = input("eklenecek öğrencinin adını girin:")
    surname = input("eklenecek öğrencinin soyadını girin:")
    students.append(name+" "+surname)
    print("öğrenci listeye eklendi.")
    print(students)

addStudent()

print("**************")
def removeStudent ():
    name = input("silinecek öğrencinin adını girin :")
    surname = input("silinecek öğrencinin soyadını girin :")
    students.remove(name+ " " + surname)
    print("kişi listeden silindi")
    print(students)

removeStudent()

print("**************")

def addsStudents():
  number = int ( input("kaç kişi ekleyeceksiniz :"))
  for i in range(number):
     ekleKisi = input("yeni eklenecek kişinin adı soyadı :")
     students.append(ekleKisi)
     i+=1
     print("öğrenciler listeye eklendi.")
   
  print(students)

print("****************")

addsStudents()

def studentList():
  for student in range (len(students)) :
    print(students[student])
    student +=1
  print("öğrenciler listelendi")

studentList()

print("****************")

def studentFindNumber():
   student = input ("numarasıni istediğiniz öğrencinin adı soyadı :")
   i=0
   while  i < len(students):
      if students[i] == student:
        print("öğrenci numarası :")
        print(i)
        break
      i +=1

studentFindNumber()
