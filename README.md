# Yerel RAG Belge Asistanı

Bu Python uygulaması, bir metin belgesine dayanarak Türkçe soruları yanıtlar. MiniLM, soruyu ve `belge.txt` içindeki paragrafları vektörlere dönüştürür. Program en benzer iki paragrafı Ollama üzerinden yerel çalışan Gemma 3 4B modeline gönderir. Yanıttaki `[S1]` veya `[S2]` etiketi, kullanılan paragrafı gösterir.

## Windows’ta kurulum ve çalıştırma

Python 3.12 ve Ollama kurulu olmalı. Ollama’yı açın ve proje klasöründe bir PowerShell terminalinde şu komutları çalıştırın:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
ollama pull gemma3:4b
.\.venv\Scripts\python.exe .\embedding_arama.py
```

İlk çalıştırmada MiniLM indirilir. Kendi belgenizi kullanmak için `belge.txt` dosyasının içeriğini değiştirin ve paragrafları boş satırla ayırın. Uygulama belge değiştiğinde kayıtlı vektörleri yeniler.

## RAG öncesi ve sonrası

Aşağıdaki komut aynı soruyu aynı model ve talimatla iki kez çalıştırır. İlk istekte belge pasajı verilmez. İkinci isteğe aramanın bulduğu iki pasaj eklenir. Her iki yanıt ve kullanılan pasajlar terminalde görünür ve `karsilastirma-ciktisi.txt` dosyasına kaydedilir.

```powershell
$env:PYTHONIOENCODING = "utf-8"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
.\.venv\Scripts\python.exe .\embedding_arama.py --karsilastir --soru "Toplantılar nerede yapılıyor?" | Tee-Object -FilePath .\karsilastirma-ciktisi.txt
```

Kaynaklı yanıtı değerlendirirken cevaptaki bilgiyi ve kaynak etiketini terminalde gösterilen pasajlarla karşılaştırın. Kendi belgenizi kullanıyorsanız komuttaki soruyu belgenize göre değiştirin.
