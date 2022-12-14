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
import service

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов игры
TURN, MAX, NUMBER, ENEMY, MOVES = range(5)

# функция обратного вызова точки входа в игру


def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['ДА', 'Не хочу']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем с вопроса
    update.message.reply_text(
        'Я бот игры с конфетами. Я проведу с вами игру. '
        'Команда /cancel, чтобы прекратить игру.\n\n'
        'Сыграем?',
        reply_markup=markup_key,)
    # переходим к этапу `TURN`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список
    # обработчиков, определенных в виде значения ключа `TURN`
    return TURN

# Обрабатываем ответ пользователя о начале игры


def turn(update, _):
    # определяем пользователя
    user = update.message.from_user
    # определяем его выбор
    mess = update.message.text
    # Пишем в журнал ответ пользователя
    logger.info("Ответ %s: %s", user.first_name, mess)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    if (mess == 'ДА'):
        update.message.reply_text(
            'Отлично. Введите максимальное количество конфет, '
            'которое можно забрать за один ход.',
            reply_markup=ReplyKeyboardRemove(),
        )
        # переходим к этапу `MAX`
        return MAX
    else:
        # Заканчиваем игру.
        return ConversationHandler.END


# Определяем максимальное количество конфет, которое можно взять за один ход
def max(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    max_get_candies = update.message.text
    # Проверяем валидность ответа
    if service.validate_max_get_candies(max_get_candies):
        service.max_get_candies = int(max_get_candies)
        # Пишем в журнал ответ пользователя
        logger.info("Максимальное число конфет за один ход %s: %s",
                    user.first_name, max_get_candies)
        update.message.reply_text(
            f'Введите общее количество конфет, которое должно быть больше {service.max_get_candies}.',
        )
        return NUMBER
    else:
        update.message.reply_text(
            'Вы ввели не число или число меньше 0. '
            'Введите максимальное количество конфет, '
            'которое можно забрать за один ход.',
        )
        return MAX

# Установка максимального количества конфет всего
def number(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Список кнопок для ответа
    reply_keyboard = [['Человек', 'Компьютер']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # захватываем ответ
    number_of_candies = update.message.text
    # Проверяем валидность ответа
    if service.validate_number_of_candies(number_of_candies):
        service.number_of_candies = int(number_of_candies)
        # Пишем в журнал ответ пользователя
        logger.info("Общее число конфет за один ход %s: %s",
                    user.first_name, number_of_candies)
        update.message.reply_text(
            'Выберите противника. Человек - означает, что вы хотите играть с другом на одном (этом) устройстве!',
            reply_markup=markup_key,
        )
        return ENEMY
    else:
        update.message.reply_text(
            f'Вы ввели не число или число меньше {service.max_get_candies}. '
            'Введите общее количество конфет.',
        )
        return NUMBER

# Выбор режима игры
def enemy(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    logger.info("Режим игры %s: %s", user.first_name, mess)
    if mess == 'Компьютер':
        service.ai = True
        if not service.first_turn:
            update.message.reply_text(
            service.start_game() + ' ' + service.computer_move()
             + '\n' + service.next_move())
        else: 
            update.message.reply_text(
            service.start_game() 
             + '\n' + service.next_move())
        return MOVES
    
    update.message.reply_text(
        service.start_game() + '\n' + service.next_move(),
    )
    return MOVES


def moves(update, _):
     # определяем пользователя
    user = update.message.from_user
    # захватываем ответ
    mess = update.message.text
    if service.validation_move(mess):
        service.human_move(mess)
        logger.info("Игрок %s взял %s конфет. Всего конфет осталость %s.", 
        user.first_name, mess, service.number_of_candies)
        if service.number_of_candies > 0:
            if service.ai:
                update.message.reply_text(
                service.computer_move())
                if service.number_of_candies > 0:
                    update.message.reply_text(service.next_move()) 
                    return MOVES
            else:
                update.message.reply_text(
                service.next_move())  
                return MOVES
        update.message.reply_text(
            service.winner() +
            ' Спасибо за игру! Напишите /start если хотите сыграть ещё раз!')
        # Обнуляем данные
        service.restart()        
        return ConversationHandler.END  
    else: 
        update.message.reply_text(f'Вы ввели не число или число больше {service.max_get_candies}! '
         + service.next_move())
        return MOVES

def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не хочет играть
    logger.info("Пользователь %s отменил игру.", user.first_name)
    # Отвечаем на отказ
    update.message.reply_text(
        'Жаль! Заходите если что :)',
        reply_markup=ReplyKeyboardRemove()
    )
    # Обнуляем данные
    service.restart()        
    # Заканчиваем игру.
    return ConversationHandler.END


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
            TURN: [CommandHandler('cancel', cancel), MessageHandler(Filters.regex('^(ДА|Не хочу)$'), turn)],
            MAX: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, max)],
            NUMBER: [CommandHandler('cancel', cancel), MessageHandler(Filters.text, number)],
            ENEMY: [CommandHandler('cancel', cancel), MessageHandler(Filters.regex('^(Человек|Компьютер)$'), enemy)],
            MOVES:[CommandHandler('cancel', cancel), MessageHandler(Filters.text, moves)],
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