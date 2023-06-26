model = {
    'iphone': {
        'iphone 1': {'Name': 'iPhone 1', 'Ram': '128 MB', 'Storage': '4 GB'}
    }
}
model['iphone'].update('iphone 2')
print(model['iphone'])