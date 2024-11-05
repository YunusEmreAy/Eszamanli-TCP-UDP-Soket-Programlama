import socket  # Soket programlama için gerekli modül
import threading  # Çoklu iş parçacığı için gerekli modül
import select

# Sunucu Bilgileri
Sunucu_IP_Adresi = '127.0.0.1'  # Sunucu IP adresi
TCP_Baglanti_Portu = 12345  # TCP bağlantı portu
UDP_Baglanti_Portu = 12346  # UDP bağlantı portu
BUFFER_SIZE = 1024  # Soketten okunacak veri miktarı (byte)

# Kullanıcı listesi
TCP_Baglantilari = list()  # Bağlı TCP istemciler listesi
UDP_Baglantilari = list()  # Bağlı UDP istemciler listesi
Kullanici_Adlari = list()  # Kullanıcı adları listesi


def broadcast(Kullanici_Adi, Mesaj):
    print("--> {}: {}".format(Kullanici_Adi,Mesaj))  # Sunucu konsolunda mesajı göster
    for TCP in TCP_Baglantilari:
        TCP.send("{}: {}".format(Kullanici_Adi, Mesaj).encode()) # Mesajı tüm TCP istemcilere gönder
    for UDP in UDP_Baglantilari:
        UDP_Soketi_Olustur.sendto("{}: {}".format(Kullanici_Adi, Mesaj).encode('utf-8'), UDP) # Mesajı tüm UDP istemcilere gönder

def TCP_Connect(conn, addr):

    Kullanıcı_Adı = conn.recv(BUFFER_SIZE).decode()
    if Kullanıcı_Adı in Kullanici_Adlari:
        conn.send("Bu kullanıcı adı zaten alınmış, lütfen farklı bir kullanıcı adı deneyiniz.".encode('utf-8'))
        conn.close()
        return

    conn.send("Baglanti Basarili".encode('utf-8'))
    TCP_Baglantilari.append(conn)
    Kullanici_Adlari.append(Kullanıcı_Adı)
    broadcast("Server", "{} [TCP] ile bağlanmıştır hoşgeldiniz.".format(Kullanıcı_Adı))
    conn.send("\n--> Hoşgeldin {}, TCP ile bağlısın.".format(Kullanıcı_Adı).encode('utf-8'))

    try:
        while True:
            message = conn.recv(BUFFER_SIZE)
            message = message.decode()

            if message == "TCP_Baglanti_Sonlandir":
                broadcast("Server", "{} [TCP] sohbet odasından ayrıldı.".format(Kullanıcı_Adı))
                conn.send("Hoşcakal {}, TCP ile bağlantın sonlandırıldı.".format(Kullanıcı_Adı).encode('utf-8'))
                Kullanici_Adlari.remove(Kullanıcı_Adı)
                TCP_Baglantilari.remove(conn)

                break
            broadcast(Kullanıcı_Adı+"[TCP]",message)
    except ConnectionResetError:
        Kullanici_Adlari.remove(Kullanıcı_Adı)
        TCP_Baglantilari.remove(conn)
        broadcast("Server", "{} [TCP] sohbet odasından ayrıldı.".format(Kullanıcı_Adı))


###################################################################################################################################################

TCP_Soketi_Olustur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP soketi oluştur
TCP_Soketi_Olustur.bind((Sunucu_IP_Adresi, TCP_Baglanti_Portu))  # TCP soketini belirtilen IP ve porta bağla
TCP_Soketi_Olustur.listen(5)  # Bağlantıları dinlemeye başla

UDP_Soketi_Olustur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP soketi oluştur
UDP_Soketi_Olustur.bind((Sunucu_IP_Adresi, UDP_Baglanti_Portu))  # UDP soketini belirtilen IP ve porta bağla
print("Sunucu başlatıldı ve bağlantılar dinleniyor...")
while True:
    Yeni_TCP_istegi_Var_Mi, _, _ = select.select([TCP_Soketi_Olustur], [], [], 1)
    if Yeni_TCP_istegi_Var_Mi:
        conn, addr = TCP_Soketi_Olustur.accept() # Yeni bağlantı kabul et
        threading.Thread(target=TCP_Connect, args=(conn, addr)).start() # Her yeni bağlantı için yeni bir iş parçacığı başlat
        
        
    Yeni_UDP_istegi_Var_mi, _, _ = select.select([UDP_Soketi_Olustur], [], [], 1)
    if Yeni_UDP_istegi_Var_mi:
        mesaj, addr = UDP_Soketi_Olustur.recvfrom(BUFFER_SIZE)
        mesaj = mesaj.decode()
        if mesaj.split(":")[0] == "Yeni_UDP_istegi":
            if mesaj.split(":")[1] in Kullanici_Adlari:
                UDP_Soketi_Olustur.sendto("Bu kullanıcı adı zaten alınmış, lütfen farklı bir kullanıcı adı deneyiniz.".encode('utf-8'), addr)
            else:
                UDP_Soketi_Olustur.sendto("Baglanti Basarili".encode('utf-8'), addr)

                Kullanici_Adlari.append(mesaj.split(":")[1])
                UDP_Baglantilari.append(addr)

                broadcast("Server", "{} [UDP] ile bağlanmıştır hoşgeldiniz.".format(mesaj.split(":")[1]))
                UDP_Soketi_Olustur.sendto("Hoşgeldin {}, UDP ile bağlısın.".format(mesaj.split(":")[1]).encode('utf-8'), addr)

        elif mesaj.split(":")[0] == "UDP_Baglanti_Sonlandir":

            broadcast(mesaj.split(":")[1] + "[UDP]", "Görüşürüz")
            broadcast("Server", "{} [UDP] sohbet odasından ayrıldı.".format(mesaj.split(":")[1]))
            UDP_Soketi_Olustur.sendto("Hoşcakal {}, UDP ile bağlantın sonlandırıldı.".format(mesaj.split(":")[1]).encode('utf-8'),addr)

            Kullanici_Adlari.remove(mesaj.split(":")[1])
            UDP_Baglantilari.remove(addr)

        else:
            broadcast(mesaj.split(":")[0]+"[UDP]", mesaj.split(":")[1])
