# Secret Notes

Secret Notes, XOR şifreleme yöntemi kullanarak metinleri şifreleyen ve şifre çözen basit bir Tkinter uygulamasıdır.

## Özellikler
- XOR algoritması ile şifreleme ve deşifreleme
- Kullanıcı dostu grafik arayüz
- Dosya işlemleri: Şifreli metinleri kaydetme ve açma

## Kurulum ve Kullanım
1. Python 3.x ve Tkinter yüklü olduğundan emin olun.
2. Projeyi bilgisayarınıza klonlayın veya indirin.
3. `python your_script.py` komutuyla uygulamayı başlatın.
4. Arayüzde başlık, metin ve master key girip "Save & Encrypt" butonuyla şifreli dosya oluşturun.
5. "Decrypt" butonuyla şifreli dosyayı açıp içeriğini görüntüleyin.

## Kod Açıklaması
- **xor_encrypt_decrypt**: Veriyi ve anahtarı (key) alır, string ise önce bytes’a çevirir, ardından XOR işlemi uygulayarak şifreleme/deşifreleme yapar.
- **Save_Encrypt**: Gerekli alanların dolu olduğunu kontrol eder, dosya kaydetme diyaloguyla dosya yolunu alır, metni şifreler ve dosyaya yazar.
- **Decrypt**: Master key’nin girildiğini kontrol eder, dosya açma diyaloguyla şifreli dosyayı seçer, dosyayı bytes olarak okur, şifreyi çözer ve sonucu arayüzde gösterir.

## Hata Yönetimi
- Eksik veri girildiğinde ve hatalı master key kullanıldığında kullanıcıya hata mesajları gösterilir.
