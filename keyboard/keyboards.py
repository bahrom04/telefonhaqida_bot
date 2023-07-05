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
iphone = ['iPhone 1', 'iPhone 3G📱', 'iPhone 4📱', 'iPhone 5📱', 'iPhone 6📱', 'iPhone 7📱', 'iPhone 8📱',
          'iPhone X📱', 'iPhone XS📱', 'iPhone 11📱', 'iPhone 12📱', 'iPhone 13📱', 'iPhone 14📱', 'iPhone 15📱']
kb_iphone = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_iphone = [types.reply_keyboard.KeyboardButton(text=x) for x in iphone]
# Go Back Button
go_back = types.reply_keyboard.KeyboardButton(text='Go Back')
go_back_iphone = types.reply_keyboard.KeyboardButton(text='Go Back🍎')
kb_iphone.add(*button_list_iphone, go_back)

iphone_3g = ['iPhone 3G', 'iPhone 3GS']
kb_iphone_3g = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_3g = [types.reply_keyboard.KeyboardButton(text='iPhone 3G'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 3GS'),
                         ]
kb_iphone_3g.add(*buttonslist_iphone_3g, go_back_iphone)

iphone_4 = ['iPhone 4', 'iPhone 4S']
kb_iphone_4 = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_4 = [types.reply_keyboard.KeyboardButton(text='iPhone 4'),
                        types.reply_keyboard.KeyboardButton(text='iPhone 4S'),
                        ]
kb_iphone_4.add(*buttonslist_iphone_4, go_back_iphone)

iphone_5 = ['iPhone 5', 'iPhone 5S']
kb_iphone_5 = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_5 = [types.reply_keyboard.KeyboardButton(text='iPhone 5'),
                        types.reply_keyboard.KeyboardButton(text='iPhone 5S'),
                        ]
kb_iphone_5.add(*buttonslist_iphone_5, go_back_iphone)

iphone_6 = ['iPhone 6', 'iPhone 6S']
kb_iphone_6 = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_6 = [types.reply_keyboard.KeyboardButton(text='iPhone 6'),
                        types.reply_keyboard.KeyboardButton(text='iPhone 6S'),
                        ]
kb_iphone_6.add(*buttonslist_iphone_6, go_back_iphone)

iphone_7 = ['iPhone 7', 'iPhone 7 Plus']
kb_iphone_7 = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_7 = [types.reply_keyboard.KeyboardButton(text='iPhone 7'),
                        types.reply_keyboard.KeyboardButton(text='iPhone 7 Plus'),
                        ]
kb_iphone_7.add(*buttonslist_iphone_7, go_back_iphone)

iphone_8 = ['iPhone 8', 'iPhone 8 Plus']
kb_iphone_8 = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_8 = [types.reply_keyboard.KeyboardButton(text='iPhone 8'),
                        types.reply_keyboard.KeyboardButton(text='iPhone 8 Plus'),
                        ]
kb_iphone_8.add(*buttonslist_iphone_8, go_back_iphone)

iphone_x = ['iPhone X']
kb_iphone_x = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_x = [types.reply_keyboard.KeyboardButton(text='iPhone X'),
                        ]
kb_iphone_x.add(*buttonslist_iphone_x, go_back_iphone)

iphone_xs = ['iPhone XR', 'iPhone XS', 'iPhone XS Max']
kb_iphone_xs = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_xs = [types.reply_keyboard.KeyboardButton(text='iPhone XR'),
                         types.reply_keyboard.KeyboardButton(text='iPhone XS'),
                         types.reply_keyboard.KeyboardButton(text='iPhone XS Max'),
                         ]
kb_iphone_xs.add(*buttonslist_iphone_xs, go_back_iphone)

iphone_11 = ['iPhone 11', 'iPhone 11 Pro', 'iPhone 11 Pro Max']
kb_iphone_11 = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_11 = [types.reply_keyboard.KeyboardButton(text='iPhone 11'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 11 Pro'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 11 Pro Max')
                         ]
kb_iphone_11.add(*buttonslist_iphone_11, go_back_iphone)

iphone_12 = ['iPhone 12 Mini','iPhone 12', 'iPhone 12 Pro', 'iPhone 12 Pro Max']
kb_iphone_12 = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_12 = [types.reply_keyboard.KeyboardButton(text='iPhone 12 Mini'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 12'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 12 Pro'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 12 Pro Max'),
                         ]
kb_iphone_12.add(*buttonslist_iphone_12, go_back_iphone)

iphone_13 = ['iPhone 13 Mini','iPhone 13', 'iPhone 13 Pro', 'iPhone 13 Pro Max']
kb_iphone_13 = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_13 = [types.reply_keyboard.KeyboardButton(text='iPhone 13 Mini'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 13'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 13 Pro'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 13 Pro Max')
                         ]
kb_iphone_13.add(*buttonslist_iphone_13, go_back_iphone)


iphone_14 = ['iPhone 14', 'iPhone 14 Plus', 'iPhone 14 Pro', 'iPhone 14 Pro Max']
kb_iphone_14 = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
buttonslist_iphone_14 = [types.reply_keyboard.KeyboardButton(text='iPhone 14'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 14 Plus'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 14 Pro'),
                         types.reply_keyboard.KeyboardButton(text='iPhone 14 Pro Max')
                         ]
kb_iphone_14.add(*buttonslist_iphone_14, go_back_iphone)

# Keyboards for Samsung
samsung_s = ['Samsung S1', 'Samsung S2', 'Samsung S3', 'Samsung S4', 'Samsung S5', 'Samsung S6', 'Samsung S7',
             'Samsung S8',
             'Samsung S9', 'Samsung S10', 'Samsung S20', 'Samsung S21']
kb_samsung_s = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_samsung = [types.reply_keyboard.KeyboardButton(text=x) for x in samsung_s]
kb_samsung_s.add(*button_list_samsung, go_back)

samsung_a = ['Samsung Alpha', 'Samsung A3(2014)', 'Samsung A5(2014)', 'Samsung A5(2017)', 'Samsung A6s',
             'Samsung A7(2018)', 'Samsung A8(2018)', 'Samsung A8+(2018)', 'Samsung A8s', 'Samsung A6(2018)',
             'Samsung A6+(2018)', 'Samsung A8 Star', 'Samsung A9(2019)', 'Samsung A10', 'Samsung A10s', 'Samsung A10e',
             'Samsung A20', 'Samsung A20e', 'Samsung A30', 'Samsung A50', 'Samsung A60', 'Samsung A70',
             'Samsung A80', 'Samsung A2 Core', 'Samsung A40s']
kb_samsung_a = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_samsung_a = [types.reply_keyboard.KeyboardButton(text=x) for x in samsung_a]
kb_samsung_a.add(*button_list_samsung_a, go_back)

redmi_note = ['Redmi 1', 'Samsung S2', 'Samsung S3', 'Samsung S4', 'Samsung S5', 'Samsung S6', 'Samsung S7',
              'Samsung S8',
              'Samsung S9', 'Samsung S10', 'Samsung S20', 'Samsung S21']
kb_redmi_note = types.reply_keyboard.ReplyKeyboardMarkup(resize_keyboard=True)
button_list_redmi_note = [types.reply_keyboard.KeyboardButton(text=x) for x in redmi_note]
kb_redmi_note.add(*button_list_redmi_note, go_back)
