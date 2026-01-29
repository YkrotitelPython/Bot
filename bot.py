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
   "inv_1": """Invalids: 
Wrong Number 
Wrong country
Wrong Person
Wrong Info
No Language
Under Age
Didn’t register


 -Сверка каждый понедельник или день в день для закрытия дневного пролива.
 -Замена невалидов осуществляется на следующий день после подачи 

При невалиде выше 20% необходимо предоставить записи разговоров""",
    "inv_2": """Invalids: 
Wrong info  
Wrong number  
Duplicate 
Invalid language
Fraud (пранкер  - троль)
Autologin 70/30
autoingekct ( бот ip/proxy)  
Didn’t register
Fake registartion (лид  говорит что  регистрировался  вчера и  более  дней  назад)
Wrong country
Under age: 21
Over age: 75
Test


 -Сверка и оплата понедельник - среда 
 При невалиде выше 20% предоставляем записи разговоров.
 Все остальные по запросу
 Мы рады работать с вами)""",
    "inv_3": """Доброе утро 🤗
Давайте сверимся  по невалиду  за прошлую неделю!

Предоставьте следующую информацию:
1. GEO
2. Количество - сколько получили  
3. Invalids  
Почта - Статус - Комментарий
Компания Consulting Leads жедает Вам Прибыльной недели)""",
    "inv_2": """Всем приветДавайте сверимся за прошлую неделю:
GEO:
Total Leads:
Invalid:
Valid:
Total sum: """
    
}

# ---------------- Главное меню ----------------
def main_menu():
    keyboard = [
        [InlineKeyboardButton("Наша Команда", callback_data='text1'),
         InlineKeyboardButton("Order", callback_data='text2')],
        [InlineKeyboardButton("Price Forex", callback_data='text3'),
         InlineKeyboardButton("GEO Fx", callback_data='menu_forex')],
        [InlineKeyboardButton("Price Charge", callback_data='text5'),
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
async def send_photos_from_folder(message, folder_path):
    if not os.path.exists(folder_path):
        await message.reply_text(f"🚚 Товар в дорозі: {folder_path}")
        return

    media = []
    for file in os.listdir(folder_path):
        # Отправляем jpg, jpeg и png
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            media.append(InputMediaPhoto(open(os.path.join(folder_path, file), "rb")))

    if not media:
        await message.reply_text("🚚 Товар в дорозі")
        return

    # Отправка альбомами по 10 фото
    for i in range(0, len(media), 10):
        await message.reply_media_group(media[i:i+10])
# ---------------- Обработка кнопок ----------------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # ----- Главное меню (тут менять только  текст) -----
    if query.data == 'text1':
        await query.edit_message_text(
            """Всем привет 🤗
Рады Знакомству 🤝

Наши рабочие дни :
      Пн - ПТ
 10:00 - 19:00 
      
Принимаем капы до 18:00 (За день до пролива ) 
Шаблона  заказа : 
GEO - 
Lead Per day -

Давайте  знакомится  с нашей командой:
  @Alex_ConsultingLeads - Finance
  @Consulting_Leads - CEO
  @Alena_Co_Leads - Affiliate manager
  @Consulting_Leads_Antony - Affiliate manager
  @Consultingleads_Support - Тех. поддержка""",
            reply_markup=main_menu()
        )
    elif query.data == 'text2': #----кнопка Order----
        await query.edit_message_text(
            """Кош  Январь

GEO:
Funnel:

Work Hours:
Lead per day:

Lead Price:
Total Leads:

Total Sum: 

Wallet USDT TRC20:
TMy1WXpPiXgLnoZD8GcFWm6p9Vpb4pG3mn
""",
            reply_markup=main_menu()
        )
    elif query.data == 'text3': #-----Price Forex----
        await query.edit_message_text(
            """
GEO:ES-ES  
CR:16%
Funnels: ai-app, bitfinex-invest*
Source: Outbrain
Price:1800+14%

GEO:JP-JP 
CR 12% 
Funnels: Quantum-elite, Finance-app
Source:Native
Price:1450$+11% 

GEO:CA EN
CR 12%
Funnel: bitcoin-ai, quantum, trader-ai, gpt
Source:Native
Price:1500+11%

GEO:IT-IT
CR:15%+
Funnels: ai-app, valioro-ai
Source: Outbrain
Price:1800+14%

GEO:TR-EU
СR: 10%
Funnels: Baykar ,WhatsApp, revolut, Turkiairinvest,Turkishairlines,Socar
Source: FB
Price: 1100+10%
Pull geo: CH,AT,BE,CZ,DK,FI,FR,DE,GR,IS,IE,IT,LI,LU, MT,NL,NO,PL,PT,RO,ES,SE,CH,TR,GB

GEO:RO-RO 
CR: 8% 
Funnels: Hidroelectrica, SCI, Neptun deep, CGI, OMV PETROM
Source: FB
Price: 75$ 

GEO:Ru-EU 
CR:5%
Funnels GPT Trade Global, Quantum System, Algorithm, WhatsApp Invest, Revolut, Поддержка наших(<5%)
Source:FB+Native 
Price: 95$

GEO:PL-EU 
CR:8-9%
Funnels:ChatGPT trade 
SourceFb+Native
Price: 1400+9% 

GEO:PL-PL
CR:10%
Funnels:ChatGPT trade 
SourceFb+Native
Price: 1400+11% 

GEO:IT-IT
Cr: 7%
Funnels: Revolut
Source :FB
Price: 90$

GEO:UK(EN) 
CR:10-11% 
Funnels:PrimecrestVoryx, QuantumAI, WealthProgram, InteractiveTrader
Price:1300+10%
Source: FB+SEO+in-app

GEI:DE-DE 
CR:13% 
Funnels:KI Platform, Quantum
Source: FB+SEO+in-app
Price:1700+13%

GEO:CZ_CZ 
CR:11-12%  
Funnels:TempoInvion
Source: FB+SEO
Priece:1300+10%

GEO:IT-IT 
CR:12%  
Funnels:Senvix, TrevaloxanoPro
Source: FB/SEO/IN-APP
Price: 1300+10%

GEO:ES-ES 
CR:12% 
Funnels:ElMundo
Source: FB/SEO/IN-APP
Price: 1500+12%

Geo: UZ-ru
CR: 3.5-4%
Funnel: USM, Hamkorbank
Source: FB
Price: 20$""",
            reply_markup=main_menu()
        )
    

    # ----- Меню с подменю -----
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # --- МЕНЮ ---
    if query.data == 'menu_forex':
        await query.edit_message_text(
            "📊 Price Forex\nВыберите предложение:",
            reply_markup=forex_menu()
        )
        return

    elif query.data == 'menu_charge':
        await query.edit_message_text(
            "💳 Price Charge\nВыберите предложение:",
            reply_markup=charge_menu()
        )
        return

    elif query.data == 'menu_invalid':
        await query.edit_message_text(
            "❌ Invalids\nВыберите предложение:",
            reply_markup=invalid_menu()
        )
        return

    # --- КНОПКИ С ФОТО ---
    elif query.data in submenus:
        await query.edit_message_text(
            text=button_texts.get(query.data, "Товар в дорозі"),
            reply_markup=main_menu()
        )
        await send_photos_from_folder(query.message, submenus[query.data])
        return

    # --- КНОПКИ ТОЛЬКО С ТЕКСТОМ (INVALIDS) ---
    elif query.data in ("inv_1", "inv_2", "inv_3", "inv_4"):
        await query.edit_message_text(
            text=button_texts[query.data],
            reply_markup=invalid_menu()
        )
        return

    # --- НАЗАД ---
    elif query.data == 'back_main':
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

