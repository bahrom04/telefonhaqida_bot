def model():
    models = {
        'iphone': {
            'iphone 1': '''Model: iPhone 1
Ram: 128MB
Storage: 4, 8, 16 GB
Kamera: 2 MP
Front-Kamera: None
Battery: 1400 mah
Price(2007): $499, $599
CPU: ARM11
Country: USA''',

        'iphone 3g': '''Model: iPhone 3G
Ram: 128MB
Storage: 8, 16 GB
Kamera: 2 MP
Front-Kamera: None
Battery: 1150 mah
Price(2008): $199, 299
CPU: ARM11
Country: USA''',

        'iphone 3gs': '''Model: iPhone 3GS
Ram: 256MB
Storage: 8, 16, 32 GB
Kamera: 3.15 MP
Front-Kamera: None
Battery: 1220 mah
Price(2009): $199, 299
CPU: ARM Cortex-A8
Country: USA''',

        'iphone 4': '''Model: iPhone 4
Ram: 512MB
Storage: 8, 16, 32 GB
Kamera: 5 MP
Front-Kamera: VGA
Battery: 1420 mah
Price(2010): $199, 299
CPU: Apple A4
Country: USA''',

        'iphone 4s': '''Model: iPhone 4s
Ram: 512MB
Storage: 8, 16, 32, 64 GB
Kamera: 8 MP
Front-Kamera: VGA
Battery: 1432 mah
Price(2011): $199, 299, 399
CPU: Apple A5
Country: USA''',

        'iphone 5': '''Model: iPhone 5
Ram: 1GB
Storage: 16, 32, 64 GB
Kamera: 8 MP
Front-Kamera: 1.2 MP
Battery: 1440 mah
Price(2012): $199, 299, 399
CPU: Apple A6
Country: USA''',

        'iphone 5s': '''Model: iPhone 5s
Ram: 1GB
Storage: 16, 32, 64 GB
Kamera: 8 MP
Front-Kamera: 1.2 MP
Battery: 1560 mah
Price(2013): $199, 299, 399
CPU: Apple A7
Country: USA''',

        'iphone 6': '''Model: iPhone 6
Ram: 1GB
Storage: 16, 64, 128 GB
Kamera: 8 MP
Front-Kamera: 1.2 MP
Battery: 1810 mah
Price(2014): $199, 299, 399
CPU: Apple A8
Country: USA''',

        'iphone 6s': '''Model: iPhone 6s
Ram: 2GB
Storage: 16, 32, 64, 128 GB
Kamera: 12 MP
Front-Kamera: 5 MP
Battery: 1715 mah
Price(2015): $199, 299, 399
CPU: Apple A9
Country: USA''',

        'iphone 7': '''Model: iPhone 7
Ram: 2GB
Storage: 32, 128, 256 GB
Kamera: 12 MP
Front-Kamera: 7 MP
Battery: 1960 mah
Price(2016): $649, $749, $849
CPU: Apple A10 Fusion
Country: USA''',

        'iphone 8': '''Model: iPhone 8
Ram: 2GB
Storage: 64, 256 GB
Kamera: 12 MP
Front-Kamera: 7 MP
Battery: 1821 mah
Price(2017): $699, $849
CPU: Apple A11 Bionic
Country: USA''',

        'iphone x': '''Model: iPhone X
Ram: 3GB
Storage: 64, 256 GB
Kamera: 12 MP
Front-Kamera: 7 MP
Battery: 2716 mah
Price(2017): $999, $1149
CPU: Apple A11 Bionic
Country: USA''',

        'iphone xr': '''Model: iPhone XR
Ram: 3GB
Storage: 64, 128, 256 GB
Kamera: 12 MP
Front-Kamera: 7 MP
Battery: 2942 mah
Price(2018): $749, $799, $899
CPU: Apple A12 Bionic
Country: USA''',

        'iphone xs': '''Model: iPhone XS
Ram: 4GB
Storage: 64, 256, 512 GB
Kamera: 12 MP
Front-Kamera: 7 MP
Battery: 2658 mah
Price(2018): $999, $1149, $1349
CPU: Apple A12 Bionic
Country: USA''',

        'iphone 11': '''Model: iPhone 11
Ram: 4GB
Storage: 64, 128, 256 GB
Kamera: 12,12, 12 MP
Front-Kamera: 12 MP, 4k video recording
Battery: 3110 mah
Price(2019): $699, $749, $849
CPU: Apple A13 Bionic
Country: USA''',

        'iphone 11 Pro': '''Model: iPhone 11 Pro
Ram: 4GB
Storage: 64, 256, 512GB
Kamera: 12, 12, 12 MP
Front-Kamera: 12 MP, 4k video recording
Battery: 3190 mah
Price(2019): $999, $1149, $1349
CPU: Apple A13 Bionic
Country: USA''',

        'iphone 11 Pro Max': '''Model: iPhone 11 Pro Max
Ram: 4GB
Storage: 64, 256, 512 GB
Kamera: 12, 12, 12 MP
Front-Kamera: 12 MP, 4k video recording
Battery: 3969 mah
Price(2019): $1099, $1249, $1449
CPU: Apple A13 Bionic
Country: USA''',

        'iphone SE 2nd Gen': '''Model: iPhone SE 2nd Gen
Ram: 3GB
Storage: 64, 128, 256 GB
Kamera: 12 MP
Front-Kamera: 7 MP
Battery: 1821 mah
Price(2020): $399, $449, $549
CPU: Apple A13 Bionic
Country: USA''',

        'iphone 12': '''Model: iPhone 12
Ram: 4GB
Storage: 64, 128, 256, 512GB
Kamera: 12, 12, 12 MP, 4k video recording
Front-Kamera: 12 MP, 4k video recording
Battery: 2815 mah
Price(2020): $699, $749, $849, $1349
CPU: Apple A14 Bionic
Country: USA''',

        'iphone 12 mini': '''Model: iPhone 12 Mini
Ram: 4GB
Storage: 64, 128, 256 GB
Kamera: 12, 12, 12 MP, 4k video recording
Front-Kamera: 12 MP, 4k video recording
Battery: 2227 mah
Price(2020): $699, $749, $849
CPU: Apple A14 Bionic
Country: USA''',

        'iphone 12 Pro': '''Model: iPhone 12 Pro
Ram: 6GB
Storage: 128, 256, 512GB
Kamera: 12, 12, 12 MP, LiDAR scanner, 4k video recording
Front-Kamera: 12 MP, 4k video recording
Battery: 2815 mah
Price(2020): $999, $1099, $1299
CPU: Apple A14 Bionic
Country: USA''',

        'iphone 12 Pro Max': '''Model: iPhone 12 Pro Max
Ram: 6GB
Storage: 128, 256, 512GB
Kamera: 12, 12, 12 MP, LiDAR scanner, 4k video recording
Front-Kamera: 12 MP, 4k video recording
Battery: 3687 mah
Price(2020): $1099, $1199, $1399
CPU: Apple A14 Bionic
Country: USA''',

        'iphone 13': '''Model: iPhone 13
Ram: 4GB
Storage: 128, 256, 512GB
Kamera: 12, 12, 12 MP, LiDAR scanner, 4k video recording
Front-Kamera: 12 MP, 4k video recording
Battery: 3095 mah
Price(2020): $1099, $1199, $1399
CPU: Apple A15 Bionic
Country: USA''',

        'iphone 14': '''Model: iPhone 14
Ram: 6GB
Storage: 128, 256, 512GB
Kamera: 12, 12, 12 MP, LiDAR scanner, 4k video recording
Front-Kamera: 12 MP, 4k video recording
Battery: 3279 mah
Price(2020): $799
CPU: Apple A15 Bionic
Country: USA'''
        },
        'samsung': {
            'samsung s1': '''Model: Samsung s1
Ram: 128MB
Storage: 4, 8, 16 GB
Kamera: 2 MP
Front-Kamera: None
Battery: 1400 mah
Price(2007): $499, $599
CPU: ARM11
Country: USA''',
    'samsung s2': '''Model: Samsung s2
Ram: 512MB
Storage: 8, 16, 32 GB
Kamera: 5 MP
Front-Kamera: 0.3 MP
Battery: 1500 mah
Price(2011): $199, $299
CPU: ARM Cortex-A9
Country: Global''',
    'samsung s3': '''Model: Samsung galaxy s3
Ram: 1GB
Storage: 16, 32, 64 GB
Kamera: 8 MP
Front-Kamera: 1.9 MP
Battery: 2100 mah
Price(2012): $199, $299
CPU: Samsung Exynos 4412
Country: Global''',
    'samsung s4': '''Model: Samsung galaxy s4
Ram: 2GB
Storage: 16, 32, 64 GB
Kamera: 13 MP
Front-Kamera: 2 MP
Battery: 2600 mah
Price(2013): $199, $299
CPU: Samsung Exynos 5 Octa 5410
Country: Global''',
    'samsung s5': '''Model: Samsung galaxy s5
Ram: 2GB
Storage: 16, 32, 64 GB
Kamera: 16 MP
Front-Kamera: 2 MP
Battery: 2800 mah
Price(2014): $199, $299
CPU: Samsung Exynos 5 Octa 5433
Country: Global''',
    'samsung s6': '''Model: Samsung galaxy s6
Ram: 3GB
Storage: 32, 64, 128 GB
Kamera: 16 MP
Front-Kamera: 5 MP
Battery: 2550 mah
Price(2015): $199, $299
CPU: Samsung Exynos 7420
Country: Global''',
    'samsung s7': '''Model: Samsung galaxy s7
Ram: 4GB
Storage: 32, 64 GB
Kamera: 12 MP
Front-Kamera: 5 MP
Battery: 3000 mah
Price(2016): $199, $299
CPU: Samsung Exynos 8890
Country: Global''',
    'samsung s8': '''Model: Samsung galaxy s8
Ram: 4GB
Storage: 64, 128 GB
Kamera: 12 MP
Front-Kamera: 8 MP
Battery: 3000 mah
Price(2017): $199, $299
CPU: Samsung Exynos 8895
Country: Global''',
    'samsung s9': '''Model: Samsung galaxy s9
Ram: 4GB
Storage: 64, 128, 256 GB
Kamera: 12 MP
Front-Kamera: 8 MP
Battery: 3000 mah
Price(2018): $199, $299
CPU: Samsung Exynos 9810
Country: Global''',
    'samsung s10': '''Model: Samsung galaxy s10
Ram: 8GB
Storage: 128, 512 GB
Kamera: 12 MP, 12 MP, 16 MP
Front-Kamera: 10 MP
Battery: 3400 mah
Price(2019): $749, $899
CPU: Samsung Exynos 9820
Country: Global''',
    'samsung s20': '''Model: Samsung galaxy s20
Ram: 8GB
Storage: 128, 512 GB
Kamera: 12 MP, 64 MP, 12 MP
Front-Kamera: 10 MP
Battery: 4000 mah
Price(2020): $999, $1199
CPU: Samsung Exynos 990
Country: Global''',
    'samsung s21': '''Model: Samsung galaxy s21
Ram: 8GB
Storage: 128, 256 GB
Kamera: 12 MP, 64 MP, 12 MP
Front-Kamera: 10 MP
Battery: 4000 mah
Price(2021): $799, $849
CPU: Samsung Exynos 2100
Country: Global'''
        }
    }
    return models