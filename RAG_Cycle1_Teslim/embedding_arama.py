import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

from sentence_transformers import SentenceTransformer


belge_yolu = Path(__file__).with_name("belge.txt")
metin = belge_yolu.read_text(encoding="utf-8")
pasajlar = metin.strip().split("\n\n")

top_k = 2
parser = argparse.ArgumentParser(description="Yazılım kulübü belge asistanı")
parser.add_argument("--soru", help="Soruyu terminalden etkileşimsiz al.")
parser.add_argument("--karsilastir", action="store_true", help="Aynı soruyu belgesiz de çalıştır.")
ayarlar = parser.parse_args()
soru = ayarlar.soru if ayarlar.soru is not None else input("Sorunu yaz: ")

# 1. Soruyla ilgili pasajları bul.
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    device="cpu",
)
soru_vektoru = model.encode([soru])
from hashlib import sha256

import numpy as np

vektor_dosyasi = belge_yolu.with_name("belge_vektorleri.npz")
belge_izi = sha256(metin.encode("utf-8")).hexdigest()

pasaj_vektorleri = None

if vektor_dosyasi.exists():
    with np.load(vektor_dosyasi) as kayit:
        if kayit["belge_izi"].item() == belge_izi:
            pasaj_vektorleri = kayit["vektorler"]
            print("Belge vektörleri diskten yüklendi.")

if pasaj_vektorleri is None:
    pasaj_vektorleri = model.encode(pasajlar)
    np.savez(
        vektor_dosyasi,
        belge_izi=belge_izi,
        vektorler=pasaj_vektorleri,
    )
    print("Belge vektörleri hesaplandı ve diske kaydedildi.")
puanlar = model.similarity(soru_vektoru, pasaj_vektorleri)[0].tolist()
sonuclar = list(zip(puanlar, pasajlar))
sonuclar.sort(key=lambda sonuc: sonuc[0], reverse=True)

# 2. İlk iki pasajı kaynak olarak ekle.
kaynaklar = []
for kaynak_no, (puan, pasaj) in enumerate(sonuclar[:top_k], start=1):
    kaynaklar.append(f"[S{kaynak_no}] {pasaj}")

baglam = "\n\n".join(kaynaklar)
prompt_sablonu = (
    "Soruyu Türkçe yanıtla. Kaynaklarda sorulan bilgiyi ara.\n"
    "Bilgiyi bulursan kısa bir cevap yaz ve cevabı destekleyen "
    "kaynağın etiketini olduğu gibi sona ekle.\n"
    "Bilgiyi bulamazsan şu cümleyi tek başına yaz: "
    "Bu bilgi verilen kaynaklarda bulunmuyor.\n\n"
    "Örnek:\n"
    "Kaynak: [S1] Kütüphane saat 18.00'de kapanır.\n"
    "Soru: Kütüphane kaça kadar açık?\n"
    "Cevap: Kütüphane saat 18.00'e kadar açık. [S1]\n"
    "Soru: Kütüphane müdürünün adı ne?\n"
    "Cevap: Bu bilgi verilen kaynaklarda bulunmuyor.\n\n"
    "Kaynaklar:\n{baglam}\n\n"
    "Soru: {soru}\n"
    "Cevap:"
)

# 3. Hazırlanan metni yerel cevap modeline gönder.
def ollama_cevapla(prompt):
    istek_verisi = {
        "model": "gemma3:4b",
        "prompt": prompt,
        "stream": False,
    }
    if ayarlar.karsilastir:
        istek_verisi["options"] = {"temperature": 0}
    istek = Request(
        "http://127.0.0.1:11434/api/generate",
        data=json.dumps(istek_verisi).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(istek, timeout=120) as yanit:
        sonuc = json.load(yanit)
    return sonuc["response"].strip()


if ayarlar.karsilastir:
    print(f"\nSoru\n{soru}")
    print("\nRAG öncesi | Belgeden pasaj verilmedi", flush=True)
    print(ollama_cevapla(prompt_sablonu.format(baglam="", soru=soru)))

print(f"\nModele verilen kaynaklar\n\n{baglam}")
print("\nCevap hazırlanıyor...", flush=True)
cevap = ollama_cevapla(prompt_sablonu.format(baglam=baglam, soru=soru))
print(f"\n{'RAG sonrası | Cevap' if ayarlar.karsilastir else 'Cevap'}\n{cevap}")
