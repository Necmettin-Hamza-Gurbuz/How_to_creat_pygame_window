import pygame 

#pygame modülünün içindeki tüm fonksiyonları aktif etmek için alttaki kod kullanılır

pygame.init()

# Pencerenizin genişlik ve uzunluğunu ayarlayın
genislik_yukseklik=(400 , 360)

#Pencereyi yaratın
pencere = pygame.display.set_mode(genislik_yukseklik)

#Pencerenin Yanıt Vermesini sağlayın
durum = True
while durum:
    for etkinlik in pygame.event.get():
        print(etkinlik)
        #Pencerenin kapanmasını sağlayın
        if etkinlik.type==pygame.QUIT:
            durum = False
