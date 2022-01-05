import os

telegram = {
    "token":  os.getenv(
        "TOKEN", "5022309092:AAGV8O3dFD5R-rhFwyETUobJarMHtnDzq4w"
    )
}

google = {
    "service_urls": [
        'translate.google.com',
        'translate.google.co.kr',
        'translate.google.co.uk',
        'translate.google.es',
        'translate.google.pt',
        'translate.google.de',
        'translate.google.fr',
        'translate.google.ua',
        'translate.google.cn',
        'translate.google.md',
        'translate.google.ru',
        'translate.google.ro'
    ]
}
