import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
TOKEN = "8060637949:AAHQfS_vx3MIrjyCQoUt65H4ojEeaXAB5HQ"

# ---------------- папки ----------------
submenus = {
    "Jp_1": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\JP-JP",   
    "Es_2": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\ES-ES",
    "Pl_3": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\PL-PL",
    "It_4": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\IT-IT",
    "Ca_5": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\CA-EN",
    "Uk_6": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\UK-EN",   
    "Tru_7": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\TR-EU",
    "Ro_8": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\RO-RO",
    "RuE_9": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\RU-EU",
    "PlE_10": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\PL-EU",
    "De_11": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\DE-DE",
    "Cz_12": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\CZ-CZ",
    "UzR_13": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\UZ-RU",
#-----Папки для чаржа----
    "ChEU-RU_1": r"C:\Users\Administrator\Desktop\Mybot\LandsFx\ChargeEU-RU"
}
#----------------Текст оферов когда нажимаешь на кнопку офферов форекс-------------
button_texts = {
    "Jp_1": "GEO: JP-JP\nCR 12%\nFunnels: Quantum-elite. Finance-app.\nSource: Native\nPrice: 1450$+11%",
    "Es_2": "GEO: ES-ES\nCR 11%\nFunnels: SuperFunnels\nSource: Native\nPrice: 1350$",
    "Pl_3": "GEO: PL-PL\nCR 10%\nFunnels: FastFunnels\nSource: Native\nPrice: 1250$",
    "It_4": "GEO: IT-IT\nCR 9%\nFunnels: ITFunnels\nSource: Native\nPrice: 1100$",
    "Ca_5": "GEO: CA-EN\nCR 8%\nFunnels: CanadaFunnels\nSource: Native\nPrice: 1400$",
    "Uk_6": "GEO: UK-EN\nCR 12%\nFunnels: UKFunnels\nSource: Native\nPrice: 1450$",
    "Tru_7": "GEO: TR-EU\nCR 10%\nFunnels: TRFunnels\nSource: Native\nPrice: 1200$",
    "Ro_8": "GEO: RO-RO\nCR 9%\nFunnels: ROFunnels\nSource: Native\nPrice: 1100$",
    "RuE_9": "GEO: RU-EU\nCR 13%\nFunnels: RUEFunnels\nSource: Native\nPrice: 1500$",
    "PlE_10": "GEO: PL-EU\nCR 10%\nFunnels: PLEFunnels\nSource: Native\nPrice: 1250$",
    "De_11": "GEO: DE-DE\nCR 11%\nFunnels: DEFunnels\nSource: Native\nPrice: 1300$",
    "Cz_12": "GEO: CZ-CZ\nCR 9%\nFunnels: CZFunnels\nSource: Native\nPrice: 1100$",
    "UzR_13": "GEO: UZ-RU\nCR 12%\nFunnels: UZFunnels\nSource: Native\nPrice: 1450$",
#----------------Текст оферов когда нажимаешь на кнопку офферов Чарж-------------
    "ChEU-RU_1": "GEO: Charge EU-RU\nCR 6%\nFunnels: Юрка\nSource: GG,FB\nPrice: 100$",
#---Текст  кнопок Invalids------
   "inv_1": """текст""",
    "inv_2": """текст""",
    "inv_3": """текст""",
    "inv_4": """текст """
#-----Текст прайс,ордер, наша команда---
    "text1": """Текст"""  
    "text2": """Текст"""
    "text3": """текст"""
    "text4": """текст"""
}

# ---------------- Главное меню ----------------
def main_menu():
    keyboard = [
        [InlineKeyboardButton("Наша Команда", callback_data='text1'),
         InlineKeyboardButton("Order", callback_data='text2')],
        [InlineKeyboardButton("Price Forex", callback_data='text3'),
         InlineKeyboardButton("GEO Fx", callback_data='menu_forex')],
        [InlineKeyboardButton("Price Charge", callback_data='text4'),
         InlineKeyboardButton("GEO ChB", callback_data='menu_charge')],
        [InlineKeyboardButton("Invalids", callback_data='menu_invalid')]
    ]
    return InlineKeyboardMarkup(keyboard)

# ---------------- Подменю ----------------
def forex_menu(): #-кнопки меню форекс
    keyboard = [
        [InlineKeyboardButton("JP-JP", callback_data='Jp_1')],
        [InlineKeyboardButton("ES-ES", callback_data='Es_2')],
        [InlineKeyboardButton("PL-PL", callback_data='Pl_3')],
        [InlineKeyboardButton("IT-IT", callback_data='It_4')],
        [InlineKeyboardButton("CA-EN", callback_data='Ca_5')],
        [InlineKeyboardButton("UK-EN", callback_data='Uk_6')],
        [InlineKeyboardButton("TR-EU", callback_data='Tru_7')],
        [InlineKeyboardButton("RO-RO", callback_data='Ro_8')],
        [InlineKeyboardButton("RU-EU", callback_data='RuE_9')],
        [InlineKeyboardButton("PL-EU", callback_data='PlE_10')],
        [InlineKeyboardButton("DE-DE", callback_data='De_11')],
        [InlineKeyboardButton("CZ-CZ", callback_data='Cz_12')],
        [InlineKeyboardButton("UZ-RU", callback_data='UzR_13')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def charge_menu():  #--кнопки меню чаржа---
    keyboard = [
        [InlineKeyboardButton("Charge EU-RU", callback_data='ChEU-RU_1')],
        [InlineKeyboardButton("Charge EU-EN", callback_data='ch_2')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)

def invalid_menu():  #---кнопки меню сверок 
    keyboard = [
        [InlineKeyboardButton("Invalids Brands", callback_data='inv_1')],
        [InlineKeyboardButton("Invalids Aff", callback_data='inv_2')],
        [InlineKeyboardButton("Cверка Brands", callback_data='inv_3')],
        [InlineKeyboardButton("Cверка Aff", callback_data='inv_4')],
        [InlineKeyboardButton("⬅️ Назад", callback_data='back_main')]
    ]
    return InlineKeyboardMarkup(keyboard)


    

# ---------------- /start ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Главное меню:",
        reply_markup=main_menu()
    )

# ---------------- Функция отправки фото ----------------
async def send_photos_from_folder(chat_id, context, folder_path):
    if not os.path.exists(folder_path):
        await context.bot.send_message(
            chat_id=chat_id,
            text="🚚 Товар в дорозі"
        )
        return

    media = []

    for file in os.listdir(folder_path):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            media.append(
                InputMediaPhoto(
                    media=open(os.path.join(folder_path, file), "rb")
                )
            )

    if not media:
        await context.bot.send_message(
            chat_id=chat_id,
            text="🚚 Товар в дорозі"
        )
        return

    for i in range(0, len(media), 10):
        await context.bot.send_media_group(
            chat_id=chat_id,
            media=media[i:i+10]
        )

# ---------------- Обработка кнопок ----------------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # --- Главное меню (только текст) ---
    if data in ('text1', 'text2', 'text3', 'text4'):
        await query.edit_message_text(
            text=button_texts.get(data, "скоро что-то будет"),
            reply_markup=main_menu()
        )
        return

    # --- Invalids (только текст) ---
    if data in ('inv_1', 'inv_2', 'inv_3', 'inv_4'):
        await query.edit_message_text(
            text=button_texts.get(data, "Текст отсутствует"),
            reply_markup=invalid_menu()
        )
        return

    # --- GEO с фото ---
    if data in submenus:
        await query.edit_message_text(
            text=button_texts.get(data, "Товар в дорозі"),
            reply_markup=main_menu()
        )

        folder_path = submenus[data]
        if os.path.exists(folder_path):
            await send_photos_from_folder(
                chat_id=query.message.chat_id,
                context=context,
                folder_path=folder_path
            )
        return

    # --- Подменю ---
    if data == 'menu_forex':
        await query.edit_message_text(
            "📊 Price Forex\nВыберите предложение:",
            reply_markup=forex_menu()
        )
        return

    if data == 'menu_charge':
        await query.edit_message_text(
            "💳 Price Charge\nВыберите предложение:",
            reply_markup=charge_menu()
        )
        return

    if data == 'menu_invalid':
        await query.edit_message_text(
            "❌ Invalids\nВыберите предложение:",
            reply_markup=invalid_menu()
        )
        return

    # --- Назад ---
    if data == 'back_main':
        await query.edit_message_text(
            "Главное меню:",
            reply_markup=main_menu()
        )


    # ---------------- Запуск ----------------
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()

