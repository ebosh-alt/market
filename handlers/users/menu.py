import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InputFile
from data.config import bot, OFFER
from service.GetMessage import get_mes
from service.keyboards import Keyboards

router = Router()
logger = logging.getLogger(__name__)


@router.message(Command("start"))
async def start(message: Message | CallbackQuery):
    id = message.from_user.id
    await bot.send_document(document=OFFER,
                            chat_id=id,
                            caption=get_mes("start_registration"),
                            reply_markup=Keyboards.start_registration_kb)


@router.callback_query(F.data == "menu")
async def menu(message: CallbackQuery, state: FSMContext):
    await state.clear()
    id = message.from_user.id
    await bot.send_message(chat_id=id,
                           text=get_mes("menu"),
                           reply_markup=Keyboards.menu_kb)


menu_rt = router
