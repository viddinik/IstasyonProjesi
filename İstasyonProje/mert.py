import time

# Duraklar
duraklar = [
    "Hacıosman",
    "Darüşşafaka",
    "Atatürk Oto Sanayi",
    "İTÜ-Ayazağa",
    "Seyrantepe",
    "Sanayi Mahallesi",
    "4.Levent",
    "Levent",
    "Gayrettepe",
    "Şişli-Mecidiyeköy",
    "Osmanbey",
    "Taksim",
    "Şişhane",
    "Haliç",
    "Vezneciler İstanbul Üniversitesi",
    "Yenikapı",
]

sureler = [
    10,  # Hacıosman - Darüşşafaka
    20,  # Darüşşafaka - Atatürk Oto Sanayi
    48,  # Atatürk Oto Sanayi - İTÜ-Ayazağa
    120,  # İTÜ-Ayazağa - Seyrantepe
    140,  # Seyrantepe - Sanayi Mahallesi
    230,  # Sanayi Mahallesi - 4.Levent
    103,  # 4.Levent - Levent
    170,  # Levent - Gayrettepe
    161,  # Gayrettepe - Şişli-Mecidiyeköy
    128,  # Şişli-Mecidiyeköy - Osmanbey
    133,  # Osmanbey - Taksim
    100,  # Taksim - Şişhane
    260,  # Şişhane - Haliç
    322,  # Haliç - Vezneciler İstanbul Üniversitesi
    173,  # Vezneciler İstanbul Üniversitesi - Yenikapı
]

# Trenin hareketi
for i in range(len(duraklar) - 1):
    kalkis_durak = duraklar[i]
    varis_durak = duraklar[i + 1]
    yolculuk_suresi = sureler[i]

    # Tren kalkıyor
    print(f" Tren {kalkis_durak} istasyonundan kalkıyor. Bir sonraki durak {varis_durak}, Yolculuk süresi: {yolculuk_suresi} saniye ")
    
    for kalan_sure in range(yolculuk_suresi, 0, -1):
        print(f" Kalan süre: {kalan_sure} saniye ", end="\r")
        time.sleep(1)

    # Tren gelinen durağı söylüyor
    print(f" Tren {varis_durak} istasyonuna geldi. Kapılar 15 saniye boyunca açık.")
    time.sleep(10)

    # Kapılar kapanıyor
    print(f" Kapılar kapanıyor..")

    # Tren ayrılırken geriye doğru sayım
    for geriye_sayim in range(5, 0, -1):
        print(f" Kapılar kapanmasına {geriye_sayim} saniye kaldı. ", end="\r")
        time.sleep(1)

    # Bir sonraki durağa doğru hareket
    print(f" Tren {varis_durak} istasyonundan ayrılıyor... Yolculuk devam ediyor.")

    # 3 saniye bekleme
    time.sleep(3)

# Son durağa ulaşıldığında
print(f" Tren {duraklar[-1]} istasyonuna ulaştı. Yolculuk tamamlandı.")
