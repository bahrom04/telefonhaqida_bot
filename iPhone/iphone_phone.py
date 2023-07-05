def iphone_models():
    iphones = {
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
            'iphone 7 plus': '''Model: iPhone 7 Plus
RAM: 3GB
Storage: 32GB, 128GB, 256GB
Camera: Dual 12 MP (wide-angle and telephoto)
Front Camera: 7 MP
Battery: 2900mAh
Price (2016): $769, $869, $969
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
            'iphone 8 plus': '''Model: iPhone 8 Plus
RAM: 3GB
Storage: 64GB, 256GB
Camera: Dual 12 MP (wide-angle and telephoto)
Front Camera: 7 MP
Battery: 2691mAh
Price (2017): $799, $949
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
            'iphone xs max': '''Model: iPhone XS Max
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

            'iphone 12 pro': '''Model: iPhone 12 Pro
Ram: 6GB
Storage: 128, 256, 512GB
Kamera: 12, 12, 12 MP, LiDAR scanner, 4k video recording
Front-Kamera: 12 MP, 4k video recording
Battery: 2815 mah
Price(2020): $999, $1099, $1299
CPU: Apple A14 Bionic
Country: USA''',

            'iphone 12 pro max': '''Model: iPhone 12 Pro Max
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
            'iphone 13 mini': '''Model: iPhone 13 Mini
RAM: 4GB
Storage: 128GB, 256GB, 512GB
Camera: Triple 12 MP (wide, ultra-wide, telephoto) with LiDAR scanner, 4K video recording
Front Camera: 12 MP with 4K video recording
Battery: 3095mAh
Price (2020): $1099, $1199, $1399
CPU: Apple A15 Bionic
Country: USA''',

            'iphone 13 plus': '''Model: iPhone 13 Plus
RAM: 4GB
Storage: 128GB, 256GB, 512GB
Camera: Triple 12 MP (wide, ultra-wide, telephoto) with LiDAR scanner, 4K video recording
Front Camera: 12 MP with 4K video recording
Battery: To be announced
Price (2020): To be announced
CPU: Apple A15 Bionic
Country: USA''',

            'iphone 13 pro max': '''
Model: iPhone 13 Pro Max
RAM: 4GB
Storage: 128GB, 256GB, 512GB
Camera: Triple 12 MP (wide, ultra-wide, telephoto) with LiDAR scanner, 4K video recording
Front Camera: 12 MP with 4K video recording
Battery: To be announced
Price (2020): To be announced
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
Country: USA''',

            'iPhone 14 plus': ''' 
- Model: iPhone 14 Plus
- Ram: [RAM capacity not available]
- Storage: [Storage capacity options not available]
- Camera: [Camera specifications not available]
- Front Camera: [Front camera specifications not available]
- Battery: [Battery capacity not available]
- Price: [Price information not available]
- CPU: [CPU information not available]
- Country: [Country information not available]''',

            'iPhone 14 pro': ''' 
- Model: iPhone 14 Pro
- Ram: [RAM capacity not available]
- Storage: [Storage capacity options not available]
- Camera: [Camera specifications not available]
- Front Camera: [Front camera specifications not available]
- Battery: [Battery capacity not available]
- Price: [Price information not available]
- CPU: [CPU information not available]
- Country: [Country information not available]''',

            'iPhone 14 pro max': ''' 
- Model: iPhone 14 Pro Max
- Ram: [RAM capacity not available]
- Storage: [Storage capacity options not available]
- Camera: [Camera specifications not available]
- Front Camera: [Front camera specifications not available]
- Battery: [Battery capacity not available]
- Price: [Price information not available]
- CPU: [CPU information not available]
- Country: [Country information not available]
'''
        }
    }
    return iphones
