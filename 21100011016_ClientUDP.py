import socket  # Soket programlama için gerekli modül
import threading

# Sunucu Bilgileri
Sunucu_IP_Adresi = '127.0.0.1'  # Sunucu IP adresi
UDP_Baglanti_Portu = 12346  # UDP bağlantı portu
BUFFER_SIZE = 1024  # Soketten okunacak veri miktarı (byte)

def Sunucudan_Mesaj_Al(sock): # Sunucudan gelen mesajları al
    while True:
        Sunucudan_Gelen_Mesaj, _ = UDP_Soketi_Olustur.recvfrom(BUFFER_SIZE)
        print("--> "+Sunucudan_Gelen_Mesaj.decode())

print("***Lütfen Baglantiyi Sonlandirmak icin \"exit\" tuslayiniz***")
UDP_Soketi_Olustur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP soketi oluştur

while True:
    Kullanici_Adi = input("Kullanıcı adınızı girin: ")  # Kullanıcı adı al
    UDP_Soketi_Olustur.sendto("Yeni_UDP_istegi:{}".format(Kullanici_Adi).encode(), (Sunucu_IP_Adresi, UDP_Baglanti_Portu))  # Kullanıcı adını sunucuya gönder

    Sunucudan_Gelen_Mesaj, _ = UDP_Soketi_Olustur.recvfrom(BUFFER_SIZE)
    if Sunucudan_Gelen_Mesaj.decode() == "Bu kullanıcı adı zaten alınmış, lütfen farklı bir kullanıcı adı deneyiniz.":
        print(Sunucudan_Gelen_Mesaj.decode())
    elif Sunucudan_Gelen_Mesaj.decode() == "Baglanti Basarili":
        break

threading.Thread(target=Sunucudan_Mesaj_Al, args=(UDP_Soketi_Olustur,)).start()

while True:
    Gonderilecek_Mesaj = input()  # Kullanıcıdan mesaj al
    if Gonderilecek_Mesaj.lower() == 'exit':
        UDP_Soketi_Olustur.sendto("UDP_Baglanti_Sonlandir:{}".format(Kullanici_Adi).encode(), (Sunucu_IP_Adresi, UDP_Baglanti_Portu))  # Çıkış mesajını sunucuya gönder
        break
    UDP_Soketi_Olustur.sendto("{}:{}".format(Kullanici_Adi,Gonderilecek_Mesaj).encode(), (Sunucu_IP_Adresi, UDP_Baglanti_Portu))  # Mesajı sunucuya gönder


