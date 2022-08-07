from telegram import ReplyKeyboardRemove
from sqlalchemy import and_
from sqlalchemy.sql import select, insert
from modules.helpers.states import STATE_WAIT_CONTACT
from modules.configs.text import ru
from modules.keyboard.main import MainKb, RegKb




def start_registration(update_messsage, context, state_checker):
    from_info = update_messsage.message.from_user
    tg_id = from_info.id


    # find_members = 