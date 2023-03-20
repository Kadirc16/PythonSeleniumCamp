""" HTML

 HTML, Hypertext Markup Language'ın kısaltmasıdır ve web sayfalarının yapısını ve içeriğini belirlemek için kullanılan bir işaretleme 
 dilidir. HTML, bir web tarayıcısı tarafından yorumlanan belirli bir kodlama kullanarak, metin, görüntüler, videolar ve diğer içerik
 türlerini bir arada sunmak için kullanılır. HTML, birçok farklı etiket ve öğe içerir ve bu etiketler sayesinde bir web sayfasının 
 tasarımını ve işlevselliğini kontrol etmek mümkündür. HTML, web geliştirme ve tasarımın temel taşıdır ve temel bileşenlerinden 
 biridir. Genel bilinen kanının aksine HTML bir programlama dili değildir. Daha açık anlatmak gerekirse, Chrome, Firefox, Yandex gibi
 tarayıcıların okuyup anlamlandırdığı dil HTML dilidir. Web tasarımcılarına sayfalar ve uygulamalar için yapı profilleri, bağlantılar
 blok alıntılar, paragraflar ve başlıklar oluşturmalarında yardımcıdır. Bu konuda basit kod yapıları olan etiketler ve nitelikler web
 sayfaları şekillendirilebilir. HTML için aslında bir web sitesinin iskeleti denilebilir. HTML kodları, bir web sayfasının yapısını 
 oluşturan parçacıklardır. Kullanılan kod ne olursa olsun tümü "<" ile başlar ve ">" ile bitmek zorundadır. CSS ve Javascript ile 
 beraber kullanıldığında HTML vasıtasıyla görsel ve dinamik web siteleri yaratılabilir. 

 HTML Locators

 HTML Locators, web sayfalarında bulunan belirli ögeleri(elementler) bulmak ve onlarla etkileşime geçmek için kullanılan yöntemlerdir.
 Bu öğeler, HTML kodunda belirli etiketler aracılığıyla tanımlanır ve her bir öğe, benzersiz bir kimlik (ID) veya belirli bir özellik
 seti (class, name, tagname vb.) kullanarak bulunabilir. HTML Locators, Selenium veya benzeri bir test otomasyon aracı kullanarak 
 web sayfası testlerinde veya web scraping gibi birçok farklı senaryoda kullanılır. HTML Locators, web sayfasındaki ögelerin hızlı 
 ve doğru bir şeekilde bulunmasını sağlar ve böylece test senaryolarının yazılmasını ve uygulanmasını kolaylaştırır. Locators, 
 Selenium IDE'ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur. Doğru elementin tanımlanması, 
 otomasyon oluşturmanın ön koşuludur. Site üzerindeki bir elemente örneğin giriş butonuna selenium ile tıklama işlemi yaptırmak 
 istediğimizde bu işlemi locator'lar aracılığıyla yaparız. Seleninum ile geliştirmek istediğimiz test otomasyonlarında locator'ları 
 kullanarak ilgili alanlara veri gönderebilir, tıklama işlemi yaptırabilir, var olan içeriği temizleyebiliriz. 

 Selenium Aksiyonları

 Selenium, web sayfaları üzerinde farklı aksiyonları gerçekleştirmek için kullanılan bir test otomasyon aracıdır. Bu aksiyonlar,
 web sayfalarındaki öğeleri bulmak ve üzerlerinde etkileşimde bulunmak için kullanılır. İşte Selenium'da kullanılan bazı aksiyonlar
 ve detaylı açıklamaları:
 1) send_keys() => Bu aksiyon, bir metin kutusuna yazı yazmak veya bir düğmeye klavyeden bir tuş göndermek için kullanılır. Örneğin,
                     bir metin kutusuna "Merhaba Dünya" yazmak için aşağıdaki kod kullanılabilir:
                     element = driver.find_element_by_id("myTextbox")
                     element.send_keys("Merhaba Dünya")

2) click() => Bu aksiyon, bir öğeye(düğme, bağlantı vb.) tıklamak için kullanılır. Örneğin, bir düğmeye tıklamak için:
                 element = driver.find_element_by_id("myTextbox")
                 element.click()

3) clear() => Bu aksiyon, bir metin kutusundaki mevcut metni silmek için kullanılır. Örneğin, bir metin kutusundaki mevcut
                 metni silmek için aşağıdaki kod kullanılabilir:
                 elemnent = driver.find_element_by_id("myTextbox")
                 element.clear()

 4) submit() =>  Bu aksiyon, bir formu göndermek için kullanılır. Bu aksiyon, formdaki "submit" düğmesine tıklamadan veya Enter
                  tuşuna basmadan önce kullanılabilir. Örneğin bir formu göndermek için:
                  element = driver.find_element_by_id("myForm")
                  element.submit()

5) select_by_visible_text() => Bu aksiyon, bir açılır kutudan seçenek seçmek için kullanılır. Bu aksiyon, seçenekleri açılır kutudan
                                  görülebilen metinleri kullanarak seçer. Örneğin, bir açılır kutudan "Ankara" seçmek için aşağıdaki
                                  kod kullanılabilir: 
                                  from selenium.webdriver.supportui import Select
                                  element = driver.find_element_by_id("myDropdown")
                                  select = Select(element)
                                  select.select_by_visible_text("Ankara")

 6) find_element_by => Web sitesindeki bir ögeyi bulmak için kullanılır.  
7) get() => Bu aksiyon, URL'ye gitmek için kullanılır.
 8) maximize_window() => Tarayıcı penceresini tam ekran yapmak için kullanılır.         
 9) scroll () => Sayfayı aşağı yukarı kaydırmak için kullanılır.           """