from aiogram import types

kb = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist = [types.reply_keyboard.KeyboardButton(text='iPhone📱'),
               types.reply_keyboard.KeyboardButton(text='Samsung📱'),
               types.reply_keyboard.KeyboardButton(text='Redmi Note📱'),
               ]
kb.add(*buttonslist)

kb_samsung = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_samsung = [types.reply_keyboard.KeyboardButton(text='Samsung S📱'),
                       types.reply_keyboard.KeyboardButton(text='Samsung A📱'),
               ]
kb_samsung.add(*buttonslist_samsung)

# Keyboards for iPhone
iphone = ['iPhone 1', 'iPhone 3G', 'iPhone 4', 'iPhone 5', 'iPhone 6', 'iPhone 7', 'iPhone 8',
          'iPhone X', 'iPhone XS', 'iPhone 11', 'iPhone 12', 'iPhone 13', 'iPhone 14','iPhone 15']
kb_iphone = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_iphone = [types.reply_keyboard.KeyboardButton(text=x) for x in iphone]
go_back = types.reply_keyboard.KeyboardButton(text='Go Back')
kb_iphone.add(*button_list_iphone, go_back)

# Keyboards for Samsung
samsung_s = ['Samsung S1', 'Samsung S2', 'Samsung S3', 'Samsung S4', 'Samsung S5', 'Samsung S6', 'Samsung S7', 'Samsung S8',
          'Samsung S9', 'Samsung S10', 'Samsung S20', 'Samsung S21']
kb_samsung_s = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_samsung = [types.reply_keyboard.KeyboardButton(text=x) for x in samsung_s]
kb_samsung_s.add(*button_list_samsung, go_back)

samsung_a = ['Samsung A1', 'Samsung S2']
kb_samsung_a = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_samsung_a = [types.reply_keyboard.KeyboardButton(text=x) for x in samsung_a]
kb_samsung_a.add(*button_list_samsung_a, go_back)

redmi_note = ['Redmi 1', 'Samsung S2', 'Samsung S3', 'Samsung S4', 'Samsung S5', 'Samsung S6', 'Samsung S7', 'Samsung S8',
          'Samsung S9', 'Samsung S10', 'Samsung S20', 'Samsung S21']
kb_redmi_note = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_redmi_note = [types.reply_keyboard.KeyboardButton(text=x) for x in redmi_note]
kb_redmi_note.add(*button_list_redmi_note, go_back)