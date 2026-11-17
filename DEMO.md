# Canlı demo · 6 dakika

| Süre | Ekranda göster | Anlatım |
|---|---|---|
| 0:00–0:45 | `belge.txt` | “Hazır modellerle yazılım kulübünün belgesinden cevap veren yerel bir asistan geliştirdim. Belge toplantı, aidat ve kayıt bilgisi içeriyor.” |
| 0:45–1:30 | `embedding_arama.py` içinde arama ve kaynak seçimi | “MiniLM soruyu ve paragrafları vektörlere çeviriyor. Python, benzerlik puanına göre ilk iki paragrafı Gemma'ya veriyor.” |
| 1:30–3:00 | Aidat sorusunun önce ve sonra çıktısı | “İki çalıştırmada da aynı soru ve aynı model var. İkinci istekte belgeden alınan pasajlar da var.” İkinci cevaptaki tutarı ve etiketi terminaldeki kaynakla doğrula. |
| 3:00–4:00 | “Toplantı hangi sınıfta yapılıyor?” | İlgili paragrafı ve B204 cevabını göster. |
| 4:00–5:00 | “Kulüp başkanının adı nedir?” | Belgeyi kontrol et ve modelin kaynak yetersizliğine nasıl cevap verdiğini göster. Beklenen cevap “Bu bilgi verilen kaynaklarda bulunmuyor.” |
| 5:00–6:00 | Makale özeti ve kapanış | “Makale arama kalitesi ile cevabın kaynağa sadakatini ayrı değerlendiriyor. Aidat örneğinde ikisini de terminalden kontrol edebiliyoruz.” |

İlk model indirmelerini ve karşılaştırma çalıştırmasını sunumdan önce tamamla. Sunumda aynı terminal çıktısını hazır tut. Aidat sorusunu `--karsilastir` ile, diğer örnekleri normal modda çalıştır.
