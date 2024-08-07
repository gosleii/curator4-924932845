import telebot

bot = telebot.TeleBot("6923151889:AAHSCrS-q-72Kq97t0UbRdw2fRxm_VdYqjg")


# обработка команды старт
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Приветствую, хочешь повторить материал?', parse_mode="Markdown")

@bot.message_handler(commands=['ball'])
def demo(message):
    bot.send_message(message.chat.id, " [Разбалловка заданий](https://vpr-ege.ru/ege/obshchestvoznanie/1481-bally-ege-2022-po-obshchestvoznaniyu-za-kazhdoe-zadanie)", parse_mode="Markdown")


@bot.message_handler(commands=['twopart'])
def two_part(message):
    bot.send_message(message.chat.id, '[Критерии оценивания второй части](https://docs.yandex.ru/docs/view?tm=1723032255&tld=ru&lang=ru&name=obschestvoznanie_mr_ege_2024.pdf&text=критерии%20егэ%20по%20обществознанию%202024&url=https%3A%2F%2Fdoc.fipi.ru%2Fege%2Fdlya-predmetnyh-komissiy-subektov-rf%2F2024%2Fobschestvoznanie_mr_ege_2024.pdf&lr=101022&mime=pdf&l10n=ru&sign=f768414134902d60f215868adcd81df4&keyno=0&nosw=1&serpParams=tm%3D1723032255%26tld%3Dru%26lang%3Dru%26name%3Dobschestvoznanie_mr_ege_2024.pdf%26text%3D%25D0%25BA%25D1%2580%25D0%25B8%25D1%2582%25D0%25B5%25D1%2580%25D0%25B8%25D0%25B8%2B%25D0%25B5%25D0%25B3%25D1%258D%2B%25D0%25BF%25D0%25BE%2B%25D0%25BE%25D0%25B1%25D1%2589%25D0%25B5%25D1%2581%25D1%2582%25D0%25B2%25D0%25BE%25D0%25B7%25D0%25BD%25D0%25B0%25D0%25BD%25D0%25B8%25D1%258E%2B2024%26url%3Dhttps%253A%2F%2Fdoc.fipi.ru%2Fege%2Fdlya-predmetnyh-komissiy-subektov-rf%2F2024%2Fobschestvoznanie_mr_ege_2024.pdf%26lr%3D101022%26mime%3Dpdf%26l10n%3Dru%26sign%3Df768414134902d60f215868adcd81df4%26keyno%3D0%26nosw%3D1)', parse_mode="Markdown")


@bot.message_handler(commands=['social'])
def social(message):
    bot.send_message(message.chat.id, '_Все темы_ [по социальной сфере](https://www.yaklass.ru/p/edinyj-gosudarstvennyj-ekzamen/obshchestvoznanie/poleznaia-informatciia-dlia-vypusknikov-7297553/navigator-podgotovki-7379309/re-a495be27-cd75-4be0-9eea-a11cfac2852a)', parse_mode="Markdown")


@bot.message_handler(commands=['spiritual'])
def spiritual(message):
    bot.send_message(message.chat.id, '_Все темы_ [по духовной сфере](https://obschestvoznanie-ege.ru/духовная-сфера-теория/)', parse_mode="Markdown")

@bot.message_handler(commands=['economic'])
def economic(message):
    bot.send_message(message.chat.id, '_Все темы_ [по экономической сфере](https://www.yaklass.ru/p/edinyj-gosudarstvennyj-ekzamen/obshchestvoznanie/poleznaia-informatciia-dlia-vypusknikov-7297553/navigator-podgotovki-7379309/re-96e53c39-9961-4f06-bbdc-8fbb6bf881ba)', parse_mode="Markdown")


@bot.message_handler(commands=['politic'])
def politic(message):
    bot.send_message(message.chat.id, '_Все темы_ [по политической сфере](https://www.yaklass.ru/p/edinyj-gosudarstvennyj-ekzamen/obshchestvoznanie/poleznaia-informatciia-dlia-vypusknikov-7297553/navigator-podgotovki-7379309/re-ff1142cb-6ab8-433d-9a97-f2521c07eeea)', parse_mode="Markdown")


@bot.message_handler(commands=['law'])
def law(message):
    bot.send_message(message.chat.id, '_Все темы_ [по правовой сфере](https://obschestvoznanie-ege.ru/егэ-право-теория-по-кодификатору/)', parse_mode="Markdown")


@bot.message_handler(commands=['bye'])
def bye_handler(message):
    bot.send_message(message.chat.id, '*Пока, был рад помочь тебе!*', parse_mode="Markdown")


bot.infinity_polling()