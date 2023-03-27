Dekoratörler diğer fonksiyonların işlevselliğini değiştiren fonksiyonlardır. Kodu kısaltırlar ve daha anlaşılır hale getirirler.Bir dekoratör aslında fonksiyon çağıran bir fonksiyondan başka bir şey değildir. Kendisinden önce, @ işareti ile geldiği fonksiyonu çalıştırmadan önce kendi içinde wrapped edilmiş işleri yapar ve sonra kendisinden sonra gelen fonksiyonu çağırarak onun görevini yerine getirmesini sağlar.

def Decorator_F(Bir_fonk): def Durum_F(): print("Dürüm Fonksiyonu işleri") return Bir_fonk() return Durum_F

@Decorator_F def Bir_fonksiyon(): print("Bir fonksiyonum çalıştı")

Bir_fonksiyon()

Yukarıdaki dekoratör örneğinin çıktısı aşağıdaki gibidir: Dürüm Fonksiyonu işleri fonksiyonum olan 'Bir_fonksiyon' çağırılmadan önce Bir fonksiyonum çalıştı

Pytest’teki en yaygın kullanılan dekoratörler şunlardır: @pytest.fixture: Test fonksiyonlarına veya sınıflarına bir bağımlılık eklemek veya belirli bir bağımlılığı her test için bir kere çağırmak için kullanılır.

@pytest.mark.parametrize: Test fonksiyonlarına veya sınıflarına farklı giriş değerleri sağlamak için kullanılır. Bu, bir testi, birden fazla giriş değeriyle çalıştırmak için kullanışlıdır.

@pytest.mark.skip: Belirli bir testi atlamak için kullanılır.

@pytest.mark.xfail: Belirli bir testin başarısız olması bekleniyorsa ve başarısızlık raporlanmasına izin verilmemesi gerekiyorsa kullanılır.

@pytest.mark.timeout: Belirli bir testin maksimum süresini belirlemek için kullanılır.
