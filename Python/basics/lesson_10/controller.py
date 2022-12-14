import check
import ui
import operations
import importdb
import exportdb
import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы 
TURN, NAME, SURNAME, MAIN_NUMBER, ADDITIONAL_NUMBER, DESCRIPTION, SEARCH, DELETE, EDIT, IMPORT, EXPORT  = range(11)

def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Просмотр', 'Создать контакт', 'Поиск', 'Удаление', 'Редактирование', 'Импорт', 'Экспорт']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем с вопроса
    update.message.reply_text(
        'Здравствуйте! Я бот справочника контактов. Выберите действие. Команда /cancel для отмены.',
        reply_markup=markup_key,)
    # переходим к этапу `TURN`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список
    # обработчиков, определенных в виде значения ключа `TURN`
    return TURN

def turn(update, _):
    # определяем пользователя
    user = update.message.from_user
    # определяем его выбор
    mess = update.message.text
     # Список кнопок для ответа
    reply_keyboard = [['Просмотр', 'Создать контакт', 'Поиск', 'Удаление', 'Редактирование', 'Импорт', 'Экспорт']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Пишем в журнал ответ пользователя
    logger.info("Действие %s: %s", user.first_name, mess)
    if (mess == 'Просмотр'):
        # отображаем справочник
        update.message.reply_text(ui.view(operations.db_parse()),
        reply_markup=markup_key,)
        logger.info("Отображен весь список для %s", user.first_name)
        return TURN
    elif (mess == 'Создать контакт'):
        # создание нового контакт
        update.message.reply_text('Введите Имя контакта: ',
        reply_markup=ReplyKeyboardRemove(),)
        logger.info("Пользователь %s создаёт новый контакт: ", user.first_name)
        # set flag for create
        operations.create = True
        return NAME
    elif (mess == 'Поиск'):
        # search
        update.message.reply_text('Введите слово для поиска: ',
        reply_markup=ReplyKeyboardRemove(),)
        logger.info("Пользователь %s ищет контакт: ", user.first_name)
        return SEARCH
    elif (mess == 'Удаление'):
        # удаление
        update.message.reply_text(ui.view(operations.db_parse()) + '\nВведите id контакта, который хотите удалить: ',
        reply_markup=ReplyKeyboardRemove(),)
        logger.info("Пользователь %s удаляет контакт: ", user.first_name)
        return DELETE
    elif (mess == 'Редактирование'):
        # edit
        update.message.reply_text(ui.view(operations.db_parse()) + '\nВведите id контакта, который хотите редактировать: ',
        reply_markup=ReplyKeyboardRemove(),)
        logger.info("Пользователь %s редактирует контакт: ", user.first_name)
        # set flag for edit
        operations.create = False
        return EDIT
    elif (mess == 'Импорт'):
        filename_json = "lesson_10/db_10.json"  
        filename_csv = "lesson_10/db_10.csv" 
        try:
            importdb.db_import(filename_json, filename_csv)
            update.message.reply_text('Импорт прошёл успешно!', reply_markup=markup_key,)
            logger.info(f'Произведён импорт данных, {filename_json} -> {filename_csv}')
        except Exception:
            update.message.reply_text('Ошибка! Импорт не выполнен!', reply_markup=markup_key,)
            logger.error("Импорт данных прошёл неудачно")
        return TURN
    elif (mess == 'Экспорт'):
        exportdb.db_export("lesson_10/db_10.csv","lesson_10/db_10.json")
        update.message.reply_text('Экспорт прошёл успешно!', reply_markup=markup_key,)
        logger.info("Произведён экспорт данных") 
        return TURN
    else:
        # при введении вручную невалидной команды
        update.message.reply_text('Выберите идно из возможных действий',
        reply_markup=markup_key,)
        logger.info("Пользователь %s балуется!", user.first_name)
        return TURN

def name(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    # Пишем в журнал действие
    logger.info("Пользователь %s ввёл имя контакта - %s.", user.first_name, mess)
    # запоминаем имя
    ui.contact.append(mess)
    # Просим ввести фамилию
    update.message.reply_text('Введите Фамилию контакта: ',)     
    return SURNAME

def surname(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    # запоминаем фамилию
    ui.contact.append(mess)
    # Пишем в журнал действие
    logger.info("Пользователь %s ввёл фамилию контакта - %s.", user.first_name, mess)
    # Отвечаем 
    update.message.reply_text(
        'Введите основной номер телефона контакта в формате +79239232233 : ',)       
    return MAIN_NUMBER

def main_number(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    # Проверка валидности ответа
    if check.check_phone_number(mess):
        # Пишем в журнал действие
        logger.info("Пользователь %s ввёл основной номер телефона контакта - %s.", user.first_name, mess)
        # запоминаем номер
        ui.contact.append(mess)
    else:
        # Отвечаем 
        update.message.reply_text('Вы ввели невалидный номер телефона (Пример - +79231322244).',)
        return MAIN_NUMBER
    # Отвечаем 
    update.message.reply_text(
        'Введите дополнительный номер телефона контакта в формате +79239232233 или - ,если не хотие его вводить: ',)       
    return ADDITIONAL_NUMBER

def additional_number(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    # Проверка валидности ответа
    if check.check_phone_number(mess):
        # Пишем в журнал действие
        logger.info("Пользователь %s ввёл дополнительный номер телефона контакта - %s.", user.first_name, mess)
        # запоминаем номер
        ui.contact.append(mess)
    else:
        # Отвечаем 
        update.message.reply_text(ui.PHONE_NUMBER_IS_INVALID,)
        return ADDITIONAL_NUMBER
    # Отвечаем 
    update.message.reply_text(
        'Введите описание контакта: ',)       
    return DESCRIPTION

def descrption(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['Просмотр', 'Создать контакт', 'Поиск', 'Удаление', 'Редактирование', 'Импорт', 'Экспорт']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    # запоминаем описание
    ui.contact.append(mess)
    if operations.create:
        # сохраняем контакт
        operations.db_input(ui.contact)
        # очищаем кэш
        ui.contact.clear()
        # Пишем в журнал действие
        logger.info("Пользователь %s ввёл описание контакта - %s. Новый контакт добавлен.", user.first_name, mess)
        # Отвечаем 
        update.message.reply_text(
            'Контакт сохранен!', reply_markup=markup_key) 
    else:
        operations.db_edit(mess,ui.contact)
        # очищаем кэш
        ui.contact.clear()
        # Пишем в журнал действие
        logger.info("Пользователь %s изменил контакт с id - %s. Если такой был :)", user.first_name, mess)
        update.message.reply_text(
            'Контакт наверное изменён :)!', reply_markup=markup_key) 
    return TURN

def search(update, _):
    reply_keyboard = [['Просмотр', 'Создать контакт', 'Поиск', 'Удаление', 'Редактирование', 'Импорт', 'Экспорт']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    # Пишем в журнал действие
    logger.info("Пользователь %s ищет контакт по строке - %s.", user.first_name, mess)
    # Отвечаем 
    update.message.reply_text(
        ui.view(operations.db_search(mess)),reply_markup=markup_key)  
        # Список кнопок для ответа
    return TURN

def delete(update, _):
            # Список кнопок для ответа
    reply_keyboard = [['Просмотр', 'Создать контакт', 'Поиск', 'Удаление', 'Редактирование', 'Импорт', 'Экспорт']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    operations.db_item_del(mess)
    # Пишем в журнал действие
    logger.info("Пользователь %s удалил контакт с id - %s. Но только если такой был :)", user.first_name, mess)
    # Отвечаем 
    update.message.reply_text(
        'Наверное удалили :)', reply_markup=markup_key)       
    return TURN

def edit(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    # Пишем в журнал действие
    logger.info("Пользователь %s планирует изменить контакт с id - %s. Но только если такой был :)", user.first_name, mess)
    # Отвечаем 
    update.message.reply_text('Введите Имя контакта: ',)
    return NAME      

def cancel(update, _):
        # Список кнопок для ответа
    reply_keyboard = [['Просмотр', 'Создать контакт', 'Поиск', 'Удаление', 'Редактирование', 'Импорт', 'Экспорт']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не хочет играть
    logger.info("Пользователь %s отменил программу.", user.first_name)
    # очищаем кэш
    ui.contact.clear()
    # Отвечаем на отказ
    update.message.reply_text(
        'Удачи :) Заходите если что :)',
        reply_markup=markup_key)       
    return TURN


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            TURN: [CommandHandler('cancel', cancel), MessageHandler(Filters.regex('^(Просмотр|Создать контакт|Поиск|Удаление|Редактирование|Импорт|Экспорт)$'), turn)],
            NAME: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, name)],
            SURNAME: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, surname)],
            MAIN_NUMBER: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, main_number)],
            ADDITIONAL_NUMBER: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, additional_number)],
            DESCRIPTION: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, descrption)],
            SEARCH: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, search)],
            DELETE: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, delete)],
            EDIT: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, edit)],
        },
        # точка выхода из игры
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    print('All is OK! :) Server is running! Go to testing! :)')
    updater.start_polling()
    updater.idle()