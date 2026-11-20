# Yerel RAG Belge Asistanı

Bu Python uygulaması, bir metin belgesine dayanarak Türkçe soruları yanıtlar. Hazır MiniLM embedding modeli soruyu ve belge paragraflarını vektörlere dönüştürür. Program, benzerlik sıralamasındaki ilk iki paragrafın metnini soruyla birlikte Ollama üzerinden yerel çalışan Gemma 3 4B modeline gönderir.

Modeller bu projede yeniden eğitilmez. Embedding modeli aramayı, Gemma ise kaynaklardan cevap oluşturmayı sağlar.

## Windows’ta kurulum ve çalıştırma

Python 3.12, Ollama ve modelleri indirmek için internet bağlantısı gerekir. Repoyu indirin veya klonlayın, Ollama’yı açın ve proje klasöründe bir PowerShell terminalinde şu komutları çalıştırın:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
ollama pull gemma3:4b
.\.venv\Scripts\python.exe .\embedding_arama.py
```

İlk çalıştırmada MiniLM modeli de indirilir. Modeller indirildikten sonra soru cevaplama yerel olarak çalışır. Ollama'nın yerel servisi çalışır durumda olmalıdır.

## Nasıl çalışır?

1. `belge.txt` okunur ve boş satırlarla ayrılmış paragraflara bölünür.
2. Belgenin SHA-256 özeti, kayıtlı vektörlerin ait olduğu içerikle karşılaştırılır.
3. İçerik aynıysa belge vektörleri diskten yüklenir; değişmişse yeniden hesaplanır.
4. Sorunun vektörü hesaplanır ve paragraflar benzerlik puanına göre sıralanır.
5. İlk iki paragrafın metni, soru ve cevaplama talimatıyla birlikte Gemma’ya gönderilir.
6. Kaynaklar ve üretilen cevap terminalde gösterilir.

Modelden cevaba `[S1]` veya `[S2]` kaynak etiketi eklemesi istenir. Bu etiketler o soruda gönderilen pasajların sırasını gösterir; doğruluğun otomatik olarak doğrulandığı anlamına gelmez.

## Kendi belgenizi kullanma

`belge.txt` dosyasının içeriğini değiştirin ve paragrafları boş satırla ayırın. Ardından programı yeniden çalıştırın. İçerik değişikliği algılandığında `belge_vektorleri.npz` yenilenir. Bu dosya otomatik oluşturulur ve repoya eklenmesi gerekmez.

Soruyu doğrudan komutla da verebilirsiniz:

```powershell
.\.venv\Scripts\python.exe .\embedding_arama.py --soru "Toplantılar nerede yapılıyor?"
```

## Kaynaksız ve kaynaklı cevap karşılaştırması

Aşağıdaki komut aynı soruyu aynı model, aynı talimat şablonu ve `temperature=0` ayarıyla iki kez çalıştırır. İlk isteğe belgeden pasaj eklenmez; ikinci isteğe aramanın bulduğu iki pasaj eklenir. Terminal çıktısı aynı zamanda `karsilastirma-ciktisi.txt` dosyasına kaydedilir.

```powershell
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
.\.venv\Scripts\python.exe .\embedding_arama.py --karsilastir --soru "Üyelik için ne kadar ödemem gerekiyor?" | Tee-Object -FilePath .\karsilastirma-ciktisi.txt
```

Kayıtlı denemenin değerlendirmesi [KARSILASTIRMA.md](KARSILASTIRMA.md), demo örnekleri [DEMO.md](DEMO.md) dosyasındadır. Kendi belgenizi kullanıyorsanız soruları da belgenize göre değiştirin.

## Mevcut sınırlar

- Örnek belge toplantı, aidat ve kayıt bilgilerini içeren üç kısa paragraftan oluşur; büyük belgelerde başarı ölçülmüş değildir.
- Parçalama boş satırlara dayanır. Uzun paragraflar için otomatik boyut sınırlaması veya örtüşme uygulanmaz.
- Aramada benzerlik eşiği yoktur. Soru ilgisiz olsa da mevcut paragraflardan en benzer ikisi seçilir.
- Modelden kaynaklarda cevap yoksa bunu belirtmesi istenir; bu davranış ve kaynak etiketleri garanti değildir.
- Benzerlik puanı, cevabın doğru olma olasılığını göstermez.
- Kayıtlı karşılaştırma tek bir örnektir; genel doğruluk oranı sunmaz.
- Vektör önbelleği belge içeriğine göre yenilenir. Embedding modeli veya parçalama yöntemi kodda değiştirilirse eski `belge_vektorleri.npz` dosyası silinerek yeniden oluşturulmalıdır.
