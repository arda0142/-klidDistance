import math

def oklidMesafesi(nokta1, nokta2):
    """
    2D uzaydaki iki nokta arasındaki Öklid mesafesini hesaplar.
    :param nokta1: İlk noktayı temsil eden demet (x1, y1).
    :param nokta2: İkinci noktayı temsil eden demet (x2, y2).
    :return: Öklid mesafesi (float).
    """
    return math.sqrt((nokta2[0] - nokta1[0])**2 + (nokta2[1] - nokta1[1])**2)

# Noktalar listesini tanımla
noktalar = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Mesafeler listesini başlat
mesafeler = []

# Tüm nokta çiftleri arasındaki mesafeleri hesapla
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# Minimum mesafeyi bul ve yazdır
min_mesafe = min(mesafeler)
print("Minimum Öklid mesafesi:", min_mesafe)
