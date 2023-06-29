from aiogram import executor, types, filters
from config import dp,Dispatcher
from eng import model
from keyboards import kb, kb_samsung, kb_iphone, iphone, samsung

eng_model = model()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Get phones characteristic⚙️\nChoose Phone Brand📱", reply_markup=kb)


# Define a list of iPhone versions
# Loop through the iPhone versions and generate the handler code
for version in iphone:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def iphone(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./iPhone/{lover_v}.jpg'), caption=eng_model['iphone']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)


for version in samsung:
    lover_v = version.lower()
    handler_code = f"""
@dp.message_handler(regexp='^{version}$')
async def samsung(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(photo=types.InputFile('./Samsung/{lover_v}.jpg'), caption=eng_model['samsung']['{lover_v}'])
    await message.answer_media_group(media=media)
"""
    # Execute the generated handler code
    exec(handler_code)

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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)