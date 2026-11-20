# Kaynaksız ve kaynaklı cevap karşılaştırması

## Deney düzeni

- **Soru:** Üyelik için ne kadar ödemem gerekiyor?
- **Cevap modeli:** `gemma3:4b`
- **Belgedeki bilgi:** Kulüp aidatı aylık 60 TL'dir.
- **Ayar:** Her iki istekte `temperature=0`.
- **Karşılaştırma:** Aynı soru ve talimat şablonu kullanılır. İlk isteğin kaynak alanı boştur; ikinci isteğe bulunan iki pasaj eklenir.

Tam kayıt [karsilastirma-ciktisi.txt](karsilastirma-ciktisi.txt) dosyasındadır. Tekrarlama komutu [README.md](README.md) içindedir.

## Kayıtlı sonuçlar

### Belgeden pasaj verilmeyen cevap

> Bu bilgi verilen kaynaklarda bulunmuyor.

Bu istekte de yalnızca kaynaklara dayanma talimatı vardır. Dolayısıyla sonuç, modelin genel bilgisini ölçen serbest bir sohbet denemesi değildir.

### Kaynaklı istekte gönderilen pasajlar

> [S1] Yeni üyeler kayıt formunu doldurduktan sonra ilk toplantıya katılabilir.
>
> [S2] Kulüp aidatı aylık 60 TL'dir. Ödemeler her ayın ilk haftasında alınır.

### Kaynaklı cevap

> Üyelik için aylık 60 TL ödemeniz gerekiyor. [S2]

## Değerlendirme

Bu denemede arama, aidat bilgisini içeren paragrafı ilk iki sonuç arasına almıştır. Üretilen cevap aylık 60 TL bilgisini korumuş ve bunu destekleyen `[S2]` kaynağını göstermiştir.

Bu kayıt, kaynak eklemenin bu sorudaki etkisini gösterir. Tek bir deneme, sistemin her soruda doğru cevap verdiğini veya bilgi eksikliğini her zaman doğru belirlediğini kanıtlamaz. Farklı ifadeler, belgede cevabı olmayan sorular ve belge güncellemeleri ayrıca test edilmelidir.
