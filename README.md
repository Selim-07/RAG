# Yazılım kulübü belge asistanı

AR-GE LLM & Derin Öğrenme, Cycle 1 · RAG prototipi

Asistan, yazılım kulübüyle ilgili soruları `belge.txt` üzerinden cevaplar. MiniLM aramada kullanılacak vektörleri üretir. Python, en benzer iki pasajı seçer. Ollama üzerinde yerel çalışan Gemma 3 4B, seçilen pasajlardan Türkçe cevap üretir ve kullandığı pasajın etiketini ekler.

## Kurulum ve çalıştırma

Python 3.12 ve Ollama kurulu olmalı. Proje klasöründe PowerShell açıp aşağıdaki komutları çalıştırın. İlk kurulumda Gemma ve MiniLM modellerini indirmek için internet gerekir.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
ollama pull gemma3:4b
.\.venv\Scripts\python.exe .\embedding_arama.py
```

Ollama uygulamasını açık tutun. Program Ollama'ya `127.0.0.1:11434` üzerinden bağlanır. Çalışan bir Ollama uygulamanız ya da sunucunuz yoksa ayrı terminalde `ollama serve` çalıştırabilirsiniz.

## Önce ve sonra karşılaştırması

```powershell
.\.venv\Scripts\python.exe .\embedding_arama.py --karsilastir --soru "Üyelik için ne kadar ödemem gerekiyor?" | Tee-Object -FilePath .\karsilastirma-ciktisi.txt
```

Program aynı soruyu, modeli, cevap talimatını ve model ayarını kullanır. İlk çağrıda belge pasajları boştur. İkinci çağrıda en benzer iki pasaj eklenir ve terminalde gösterilir. Beklenen sonuç aylık **60 TL** ve aidat paragrafına işaret eden bir etikettir. Etiket arama sırasına göre değişebilir.

Gemma yanıtı çalıştırma sırasında üretir. `karsilastirma-ciktisi.txt` dosyasındaki gerçek çıktıyı ve gösterilen kaynakları kontrol ettikten sonra teslim için kaydedin.

## Teslim dosyaları

- `makale_ozeti.pdf` — Wu ve arkadaşlarının RAG incelemesinin bir sayfalık özeti
- `DEMO.md` — Altı dakikalık canlı demo akışı
- `KARSILASTIRMA.md` — Daha önce gözlemlenen kaynaksız çıktı ve değerlendirme notları
