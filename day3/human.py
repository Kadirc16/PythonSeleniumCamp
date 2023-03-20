#self => this in java
class Human : 
     #built-in --> classlar içinde hazır bir fonksiyon... init --> initialize
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi.") #Constructor yapıcı blok

    def __str__(self):   
        return f"STR Fonksiyonundan dönen değer : {self.name}"

    def talk (self,sentence):
        name= "Ercan" # self keyword u olmazsa fonksiyon içindekini çıkartır.
        print(f"{self.name} : {sentence}") #self dediğimizde bu classın içindeki alanı işaret ettiğimizi anlıyor. yazmazsak (not defined) kendi bloğunda arar.
    def walk(self):
        print(f"{self.name} is walking")
#Pyhtonda tanımlandığı nesnenin kendisini ifade eder.bir class içinde tanımlanan her fonksiyonun için ilk parametresinde self bulunması gerekiyor. ( self yerine başka isimde verilebilir. yaygın olanı self old. için self communitye uygundur). Pyhton ilk alanı self den sonraki ilk parametreyi görecektir.