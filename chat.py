class Chat:

    START_TEXT = """Esenlikler Sayğılar , Bu  videola  Altyazını Birleştiren , Bir Telegram Botur.

<b>Başlamak için bana Bir URL/ Telegram dosyası gönder</b>

/help daha fazla ayrıntı için..

♨️ : @DTO_Bots
    """

    HELP_USER = "??"

    HELP_TEXT ="""<b>Yardım Menüsüne Hoş Geldiniz</b>

1.) Bir Video dosyası veya url gönderin.
2.) Bir altyazı dosyası gönderin (ass veya srt)
3.) İstediğiniz mux'in türünü seçin!

Dosyaya özel ad vermek için url'yi | ile ayrılmış olarak gönderin.
<i>url|özel_adı.mp4</i>

♨️ : @DTO_Bots
"""

    NO_AUTH_USER = """ Esenlikler , Bu botu kullanma yetkiniz yok.\nBot Yiyesile iletişime geçin!
♨️ @DTO_Bots
"""
    DOWNLOAD_SUCCESS = """Dosya başarıyla indirildi!✅

Geçen süre : {} saniye."""
    FILE_SIZE_ERROR = "HATA: Dosya Boyutu URL'den Çıkarılamıyor!"
    MAX_FILE_SIZE = "Dosya boyutu 2Gb'den büyük. Hangi telegramin koyduğu sınır!"
    LONG_CUS_FILENAME = """Sağladığınız dosya adı 60 karakterden uzun.
Lütfen daha kısa bir ad Seçin."""
    UNSUPPORTED_FORMAT = """HATA : Dosya biçimi {} Desteklenmiyor!"""
    CHOOSE_CMD = """Altyazı dosyası başarıyla indirildi.✅\nİstediğiniz mux'i seçin!\n
/softremove 
/softmux 
/hardmux 
"""
