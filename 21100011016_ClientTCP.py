import socket  # Soket programlama için gerekli modül
import threading  # Çoklu iş parçacığı için gerekli modül

# Sunucu Bilgileri
Sunucu_IP_Adresi = '127.0.0.1'  # Sunucu IP adresi
TCP_Baglanti_Portu = 12345  # TCP bağlantı portu
BUFFER_SIZE = 1024  # Soketten okunacak veri miktarı (byte)

def main():
    print("***Lütfen Baglantiyi Sonlandirmak icin \"exit\" tuslayiniz***")
    while True:
        Kullanici_Adi = input("Kullanıcı adınızı girin: ")  # Kullanıcı adı al
        TCP_Soketi_Olustur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP soketi oluştur
        TCP_Soketi_Olustur.connect((Sunucu_IP_Adresi, TCP_Baglanti_Portu))  # Sunucuya bağlan
        TCP_Soketi_Olustur.send(Kullanici_Adi.encode())  # Kullanıcı adını sunucuya gönder

        Sunucudan_Gelen_Mesaj = TCP_Soketi_Olustur.recv(BUFFER_SIZE).decode()
        if Sunucudan_Gelen_Mesaj == "Bu kullanıcı adı zaten alınmış, lütfen farklı bir kullanıcı adı deneyiniz.":
            print(Sunucudan_Gelen_Mesaj)
        elif Sunucudan_Gelen_Mesaj == "Baglanti Basarili":
            break

    threading.Thread(target=Sunucudan_Mesaj_Al, args=(TCP_Soketi_Olustur,)).start() # Mesajları almak için iş parçacığı başlat

    while True:
        Gonderilecek_Mesaj = input()  # Sunucuya Gonderilecek Mesaj
        if Gonderilecek_Mesaj.lower() == 'exit':
            TCP_Soketi_Olustur.send("TCP_Baglanti_Sonlandir".encode())  # Mesajı sunucuya gönder
            break
        TCP_Soketi_Olustur.send(Gonderilecek_Mesaj.encode())  # Mesajı sunucuya gönder

def Sunucudan_Mesaj_Al(sock): # Sunucudan gelen mesajları al
    while True:
        Sunucudan_Gelen_Mesaj = sock.recv(BUFFER_SIZE).decode()
        print("--> "+Sunucudan_Gelen_Mesaj)

main()
