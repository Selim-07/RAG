# RAG öncesi ve sonrası · Üyelik aidatı

**Soru:** Üyelik için ne kadar ödemem gerekiyor?  
**Model:** `gemma3:4b`  
**Belgedeki doğru bilgi:** Kulüp aidatı aylık 60 TL'dir.

## İlk gözlem · Gemma'ya doğrudan soruldu

> Üyelik ücreti, türüne bağlı olarak değişir.  
> **Yıllık üyelik:** 1.500 TL  
> **Aylık üyelik:** 60 TL  
> Üyelik türüne göre daha fazla ayrıntı ve ek bilgiler için lütfen [buraya tıklayın](https://www.turkastro.com/uyelik).

Model bu çalıştırmada kulüp belgesini görmedi. 60 TL tutarı belgeyle örtüşüyor. Yıllık ücret ve bağlantı kulüp belgesinde geçmiyor.

## Eş koşullarda karşılaştırma

README'deki `--karsilastir` komutuyla iki gerçek yanıtı `karsilastirma-ciktisi.txt` dosyasına kaydet. Bu komut önceki doğrudan sorgudan farklı olarak iki isteğe de aynı kaynak kullanma talimatını verir.

Çıktıları üç gözlemle değerlendir:

1. Arama, aidat bilgisini içeren paragrafı buldu mu?
2. Kaynaklı cevap aylık 60 TL dedi mi?
3. Cevabın sonundaki etiket gerçekten aidat paragrafına mı gidiyor?

Kaynaklı çıktı için beklenen örnek “Kulüp aidatı aylık 60 TL'dir. [S2]”. Pasaj sırasına göre etiket değişebilir. Teslimde terminalin ürettiği gerçek yanıtı kullan.
