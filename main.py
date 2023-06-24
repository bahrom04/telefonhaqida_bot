from aiogram import executor, types, filters
from config import dp,Dispatcher
from eng import model
from keyboards import kb, kb_samsung, kb_iphone

# Importing models dictionary in uzbek language
eng_model = model()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Get phones characteristic⚙️\nChoose Phone Brand📱", reply_markup=kb)


@dp.message_handler(filters.Text(contains='iPhone📱'))
async def send_kb(message: types.Message):
    await message.answer(text='Choose iPhone📱 Model', reply_markup=kb_iphone)
    await message.delete()

@dp.message_handler(filters.Text(contains='Samsung📱'))
async def send_samsung(message: types.Message):
    await message.answer(text='Choose Samsung📱 Model', reply_markup=kb_samsung)
    await message.delete()

@dp.message_handler(filters.Text(contains='Go Back'))
async def send_iphone(message: types.Message):
    await message.answer(text='Choose Phone Brand', reply_markup=kb)
    await message.delete()

@dp.message_handler(regexp='(^iPhone 1[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 1.jpg'), caption=eng_model['iphone']['iphone 1'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 3G[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 3g.jpg'), caption=eng_model['iphone']['iphone 3G'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 4[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 4.jpg'), caption=eng_model['iphone']['iphone 4'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 5[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 5.jpg'), caption=eng_model['iphone']['iphone 5'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 6[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 6.jpg'), caption=eng_model['iphone']['iphone 6'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 7[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 7.jpg'), caption=eng_model['iphone']['iphone 7'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 8[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 8.jpeg'), caption=eng_model['iphone']['iphone 8'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone X[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone x.jpg'), caption=eng_model['iphone']['iphone X'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone XS[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone xs.jpg'), caption=eng_model['iphone']['iphone XS'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 11[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 11.jpg'), caption=eng_model['iphone']['iphone 11'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 12[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 12.jpg'), caption=eng_model['iphone']['iphone 12'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 13[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 13.jpg'), caption=eng_model['iphone']['iphone 13'])
    await message.answer_media_group(media=media)

@dp.message_handler(regexp='(^iPhone 14[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/iphone 14.jpg'), caption=eng_model['iphone']['iphone 14'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S1[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 1.jpg'), caption=eng_model['samsung']['samsung s1'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S2[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 2.jpg'), caption=eng_model['samsung']['samsung s2'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S3[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 3.jpg'), caption=eng_model['samsung']['samsung s3'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S4[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 4.jpg'), caption=eng_model['samsung']['samsung s4'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S5[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 5.jpg'), caption=eng_model['samsung']['samsung s5'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S6[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 6.jpg'), caption=eng_model['samsung']['samsung s6'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S7[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 7.jpg'), caption=eng_model['samsung']['samsung s7'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S8[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 8.jpg'), caption=eng_model['samsung']['samsung s8'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S9[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 9.jpg'), caption=eng_model['samsung']['samsung s9'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S10[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 10.jpg'), caption=eng_model['samsung']['samsung s10'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S20[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 20.jpg'), caption=eng_model['samsung']['samsung s20'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S21[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 21.jpg'), caption=eng_model['samsung']['samsung s21'])
    await message.answer_media_group(media=media)


@dp.message_handler(regexp='(^Samsung S22[s]?$)')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/samsung s 22.jpg'), caption=eng_model['samsung']['samsung s22'])
    await message.answer_media_group(media=media)

# def register_handler_commands(dp: Dispatcher):
#     dp.register_message_handler(send_welcome, commands=['start'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)