# class BaseKb:
#     @staticmethod
#     def after_reg_kb(update_message):
#         if update_message.callback_query:
#             tg_id = update_message.callback_query.message.chat.id
#         else:
#             tg_id = update_message.message.chat.id
#         find_members = query_and_execute(select(members).where(members.c.tg_id == tg_id)).first()
#         if find_members:
#             if find_members.role == 'ADMIN':
#                 return MainKb.admin_repl
#             else:
#                 if find_members.status == 'RBC':
#                     return MainKb.reg_repl
#                 else:
#                     return MainKb.guest_repl
#         else:
#             return MainKb.no_reg_repl


from sqlalchemy import select, or_, and_
# from modules.database.main import query_and_execute
# from modules.database.main import create_array_from_select
# from modules.database.tables.schemes import members, resources
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove
from modules.configs.text import ru


class MainKb:
    reg_keyboard = [
        [
            KeyboardButton(text=ru['report']),
            KeyboardButton(text=ru['download_picture'])
        ],
        [
            KeyboardButton(text=ru['callback'])
        ]
    ]

    reg_repl = ReplyKeyboardMarkup(reg_keyboard, resize_keyboard=True)