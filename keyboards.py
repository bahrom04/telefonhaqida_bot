from aiogram import types

kb = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist = [types.reply_keyboard.KeyboardButton(text='iPhone📱'),
               types.reply_keyboard.KeyboardButton(text='Samsung📱')]
kb.add(*buttonslist)

# Keyboards for iPhone
iphone = ['iPhone 1', 'iPhone 3G', 'iPhone 4', 'iPhone 5', 'iPhone 6', 'iPhone 7', 'iPhone 8',
          'iPhone X', 'iPhone XS', 'iPhone 11', 'iPhone 12', 'iPhone 13', 'iPhone 14', 'Go Back']
kb_iphone = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_iphone = [types.reply_keyboard.KeyboardButton(text=x) for x in iphone]
kb_iphone.add(*button_list_iphone)

# Keyboards for Samsung
samsung = ['Samsung S1', 'Samsung S2', 'Samsung S3', 'Samsung S4', 'Samsung S5', 'Samsung S6', 'Samsung S7', 'Samsung S8',
          'Samsung S9', 'Samsung S10', 'Samsung S20', 'Samsung S21', 'Go Back']
kb_samsung = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_samsung = [types.reply_keyboard.KeyboardButton(text=x) for x in samsung]
kb_samsung.add(*button_list_samsung)