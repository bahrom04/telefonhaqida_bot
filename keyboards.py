from aiogram import types

kb = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist = [types.reply_keyboard.KeyboardButton(text='iPhone📱'),
               types.reply_keyboard.KeyboardButton(text='Samsung📱')]
kb.add(*buttonslist)

# Keyboards for iPhone
kb_iphone = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
b1_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 1')
b3_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 3G')
b4_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 4')
b5_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 5')
b6_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 6')
b7_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 7')
b8_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 8')
b10_iphone = types.reply_keyboard.KeyboardButton(text='iPhone X')
b10s_iphone = types.reply_keyboard.KeyboardButton(text='iPhone XS')
b11_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 11')
b12_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 12')
b13_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 13')
b14_iphone = types.reply_keyboard.KeyboardButton(text='iPhone 14')
go_back = types.reply_keyboard.KeyboardButton(text='Go Back')
# Adding buttons to rows
kb_iphone.add(b1_iphone, b3_iphone, b4_iphone)
kb_iphone.row(b5_iphone, b6_iphone, b7_iphone)
kb_iphone.row(b8_iphone, b10_iphone, b10s_iphone)
kb_iphone.row(b11_iphone, b12_iphone, b13_iphone)
kb_iphone.row(b14_iphone, go_back)


kb_samsung = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
b1_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S1')
b2_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S2')
b3_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S3')
b4_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S4')
b5_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S5')
b6_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S6')
b7_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S7')
b8_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S8')
b9_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S9')
b10_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S10')
b20_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S20')
b21_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S21')
b22_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S22')
b23_samsung = types.reply_keyboard.KeyboardButton(text='Samsung S23')


kb_samsung.add(b1_samsung, b2_samsung, b3_samsung)
kb_samsung.row(b4_samsung, b5_samsung, b6_samsung)
kb_samsung.row(b7_samsung, b8_samsung, b9_samsung)
kb_samsung.row(b10_samsung, b20_samsung, b21_samsung)
kb_samsung.row(go_back)