from aiogram import types

from loader import dp

from data.oxfordLookup import getDefinitions
from googletrans import Translator as GTranslator
gtranslator = GTranslator()
dest = ''

@dp.message_handler()
async def tarjimon(message: types.Message, gtranslator=gtranslator):
    lang = gtranslator.detect(message.text).lang
    if lang == 'en':
        dest = 'uz'
    else:
        dest = 'en'
    if message.text.lower() == "olma":
        result = "apple"
    elif message.text.lower() == "nok":
        result = "pear"
    else:
        result = gtranslator.translate(message.text.lower(), dest=dest).text
    lookup = getDefinitions(result)
    await message.answer(result)
    if dest == "en":
        await message.answer_voice(lookup['audio'])
