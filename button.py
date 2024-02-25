from aiogram.utils.keyboard import InlineKeyboardButton ,InlineKeyboardBuilder


button_fw = InlineKeyboardButton(text="➡️",callback_data="fw")
button_rnd = InlineKeyboardButton(text="🎲",callback_data="rnd")
button_bw = InlineKeyboardButton(text="⬅️",callback_data="bw")

kbd = InlineKeyboardBuilder([[button_fw, button_rnd, button_bw]])


