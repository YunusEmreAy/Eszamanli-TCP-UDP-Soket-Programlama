# Eşzamanlı TCP & UDP Soket Programlama
## Çok Kanallı Mesaj Odası Uygulaması

Bu proje, Python kullanarak soket programlama ile geliştirilen bir TCP ve UDP tabanlı mesaj odası uygulamasını içermektedir. Uygulama, hem TCP hem de UDP protokolleri üzerinden eşzamanlı bağlantıları destekler ve istemciler arasında mesaj alışverişi sağlar.

## İçerik

- **21100011016_Server.py**: Sunucu tarafı kodu. TCP ve UDP bağlantılarını işleyen eşzamanlı bir sunucu uygulaması.
- **21100011016_ClientTCP.py**: TCP istemci uygulaması. Sunucuya bağlanır ve mesaj alışverişini sağlar.
- **21100011016_ClientUDP.py**: UDP istemci uygulaması. Sunucuya bağlanır ve mesaj alışverişini sağlar.

## Projede Yapılan Çalışmalar

1. **Sunucu (Server)**
   - TCP ve UDP mesajlarını dinler.
   - Her yeni istemci bağlantısı için bir iş parçacığı başlatır.
   - Kullanıcı adı doğrulaması yapar ve aynı kullanıcı adının birden fazla istemci tarafından kullanılmasına izin vermez.
   - İstemcilerden gelen mesajları tüm bağlı istemcilere iletir.
   - Bir kullanıcı bağlantıyı sonlandırdığında diğer istemcilere bilgi verir.

2. **TCP İstemci (ClientTCP)**
   - TCP protokolünü kullanarak sunucuya bağlanır.
   - Mesaj alışverişi sağlar ve "exit" komutu ile bağlantıyı sonlandırır.

3. **UDP İstemci (ClientUDP)**
   - UDP protokolünü kullanarak sunucuya bağlanır.
   - Mesaj alışverişi sağlar ve "exit" komutu ile bağlantıyı sonlandırır.

## Kullanım

1. **Sunucuyu Başlatın**: `21100011016_Server.py` dosyasını çalıştırarak sunucuyu başlatın.
2. **İstemcileri Çalıştırın**:
   - **TCP İstemci**: `21100011016_ClientTCP.py` dosyasını çalıştırarak TCP istemciyi başlatın.
   - **UDP İstemci**: `21100011016_ClientUDP.py` dosyasını çalıştırarak UDP istemciyi başlatın.
3. **Mesajlaşma**: İstemciler kullanıcı adı ile bağlanıp mesaj göndererek sohbet edebilirler. "exit" komutu ile bağlantı sonlandırılabilir.

## Teknik Detaylar

- **Sunucu**: 127.0.0.1 IP adresini kullanır. TCP portu 12345 ve UDP portu 12346 olarak ayarlanmıştır.
- **Buffer Size**: 1024 byte.
- **Dil**: Python 3 (socket, threading, select modülleri kullanılmıştır).

## Proje Detayları

- **Sunucu**, eşzamanlı ve çok kanallı yapıda çalışır. Her bir istemci için yeni bir iş parçacığı oluşturur.
- **TCP ve UDP istemciler**, aynı anda sunucuya bağlanabilir ve mesajlaşabilir.
- **Kullanıcı Adı Kontrolü**: Aynı kullanıcı adı ile birden fazla istemcinin bağlanmasına izin verilmez.
- **Sunucu Konsolunda Mesajlar**: Gönderilen her mesaj sunucu konsolunda mesajı gönderen kullanıcı adı ve protokol bilgisi ile birlikte görüntülenir.

---

Bu uygulama, soket programlama becerilerini geliştirmek ve çoklu bağlantılarla çalışmayı öğrenmek amacıyla hazırlanmıştır.

