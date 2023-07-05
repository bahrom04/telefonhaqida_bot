from aiogram import types, filters
from config import dp
from Data_base import user
from iPhone.iphone_phone import iphone_models
from Samsung.samsung_phone import samsung_s_models
from keyboard import keyboards

iphones = iphone_models()
samsung_s_model = samsung_s_models()
ID = '1107759940'

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if str(message.from_user.id) in user.user_number():
        print('This is old user')
    else:
        member_id = message.from_user.id
        member_name = message.from_user.full_name
        data = [member_name,member_id]
        try:
            user.add(data)
            print('New member added to the database')
        except:
            print('Member already exists in the database')

    await message.reply(text='Choose Phone Characteristics', reply_markup=keyboards.kb)


# Define a list of iPhone versions
# Loop through the iPhone versions and generate the handler code
# for version in keyboards.iphone:
#     lover_v = version.lower()
#     handler_code = f"""
# @dp.message_handler(regexp='^{version}$')
# async def iphone(message: types.Message):
#     media = types.MediaGroup()
#     media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
#     await message.answer_media_group(media=media)
# """
#     # Execute the generated handler code
#     exec(handler_code)

for version in keyboards.iphone_3g:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_4:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_5:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_6:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_7:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_8:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_x:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_xs:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_11:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_12:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_13:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.iphone_14:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=iphones['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)


for version in keyboards.samsung_s:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def samsung(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/{lover_v}.jpg'), caption=samsung_s_model['samsung s']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.samsung_a:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def samsung(message: types.Message):
    # media = types.MediaGroup()
    # media.attach_photo(photo=types.InputFile('./Samsung/{lover_v}.jpg'), caption=samsung_s_models['samsung a']['{lover_v}'])
    # await message.answer_media_group(media=media)
      await message.answer(text='hi')
"""
    # Execute the generated handler code
    exec(handler_code)

for version in keyboards.redmi_note:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def samsung(message: types.Message):
    # media = types.MediaGroup()
    # media.attach_photo(photo=types.InputFile('./Samsung/{lover_v}.jpg'), caption=eng_model['samsung']['{lover_v}'])
    # await message.answer_media_group(media=media)
      await message.answer(text='hi')
"""
    # Execute the generated handler code
    exec(handler_code)

@dp.message_handler(filters.Text(contains='iPhone📱'))
async def send_kb(message: types.Message):
    await message.answer(text='Choose iPhone📱 Model', reply_markup=keyboards.kb_iphone)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 3G📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 3G Model', reply_markup=keyboards.kb_iphone_3g)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 4📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 4 Model', reply_markup=keyboards.kb_iphone_4)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 5📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 5 Model', reply_markup=keyboards.kb_iphone_5)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 6📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 6 Model', reply_markup=keyboards.kb_iphone_6)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 7📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 7 Model', reply_markup=keyboards.kb_iphone_7)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 8📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 8 Model', reply_markup=keyboards.kb_iphone_8)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone X📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone X Model', reply_markup=keyboards.kb_iphone_x)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone XS📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone XS Model', reply_markup=keyboards.kb_iphone_xs)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 11📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 11 Model', reply_markup=keyboards.kb_iphone_11)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 12📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 12 Model', reply_markup=keyboards.kb_iphone_12)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 13📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 13 Model', reply_markup=keyboards.kb_iphone_13)
    await message.delete()

@dp.message_handler(filters.Text(contains='iPhone 14📱'))
async def send_kb_3g(message: types.Message):
    await message.answer(text='Choose iPhone 14 Model', reply_markup=keyboards.kb_iphone_14)
    await message.delete()

@dp.message_handler(filters.Text(contains='Samsung📱'))
async def send_samsung(message: types.Message):
    await message.answer(text='Choose Samsung S📱 Model', reply_markup=keyboards.kb_samsung)
    await message.delete()

@dp.message_handler(filters.Text(contains='Samsung S📱'))
async def send_samsung(message: types.Message):
    await message.answer(text='Choose Samsung A📱 Model', reply_markup=keyboards.kb_samsung_s)
    await message.delete()

@dp.message_handler(filters.Text(contains='Samsung A📱'))
async def send_samsung(message: types.Message):
    await message.answer(text='Choose Samsung A📱 Model', reply_markup=keyboards.kb_samsung_a)
    await message.delete()

@dp.message_handler(filters.Text(contains='Redmi Note📱'))
async def send_samsung(message: types.Message):
    await message.answer(text='Choose Redmi Note📱 Model', reply_markup=keyboards.kb_redmi_note)
    await message.delete()

@dp.message_handler(filters.Text(contains='Go Back'))
async def send_iphone(message: types.Message):
    await message.answer(text='Choose Phone Brand', reply_markup=keyboards.kb)
    await message.delete()

@dp.message_handler(filters.Text(contains='Go Back🍎'))
async def send_iphone(message: types.Message):
    await message.answer(text='Choose Phone Brand', reply_markup=keyboards.kb_iphone)
    await message.delete()
