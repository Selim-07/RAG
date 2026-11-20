# Demo örnekleri

Bu örnekler repodaki üç paragraflık `belge.txt` için hazırlanmıştır. Her çalıştırmada bulunan kaynaklar ve cevap terminalde gösterilir.

## 1. Kaynaksız ve kaynaklı cevap

```powershell
.\.venv\Scripts\python.exe .\embedding_arama.py --karsilastir --soru "Üyelik için ne kadar ödemem gerekiyor?"
```

Kayıtlı denemede kaynak verilmeyen istek bilgi yetersizliği belirtmiştir. Kaynaklı cevap aylık 60 TL bilgisini `[S2]` etiketiyle vermiştir. Tam çıktı ve değerlendirme [KARSILASTIRMA.md](KARSILASTIRMA.md) dosyasındadır.

## 2. Belgede bulunan başka bir bilgi

```powershell
.\.venv\Scripts\python.exe .\embedding_arama.py --soru "Toplantı hangi sınıfta yapılıyor?"
```

Belgede toplantı yeri B204 olarak belirtilmiştir. Kontrol edilecek noktalar, toplantı paragrafının seçilmesi ve cevabın B204 bilgisini destekleyen kaynak etiketiyle vermesidir. Bu örnek için repoda kayıtlı bir çalıştırma çıktısı yoktur.

## 3. Belgede bulunmayan bilgi

```powershell
.\.venv\Scripts\python.exe .\embedding_arama.py --soru "Kulüp başkanının adı nedir?"
```

Belgede başkan adı bulunmaz. Talimata göre beklenen cevap:

> Bu bilgi verilen kaynaklarda bulunmuyor.

Bu, beklenen davranıştır; modelin her çalıştırmada buna uyacağı garanti değildir. Bu örnek için repoda kayıtlı bir çalıştırma çıktısı yoktur. Arama benzerlik eşiği kullanmadığından bu soruda da pasaj gönderilir.

## Demo değerlendirmesi

Arama başarısı ve cevap üretimi ayrı kontrol edilir: önce gerekli bilginin seçilen kaynaklarda bulunup bulunmadığına, ardından cevabın bu kaynaklarla uyumuna bakılır. Bir kaynak etiketi bulunması tek başına cevabın doğru olduğunu göstermez.
