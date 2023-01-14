import telebot
from telebot import types
import main
import json

bot = telebot.TeleBot('5804441110:AAE43qyn4_1JwsIQiW8UpuG4chRoCZ2Ca9w')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    vessel = types.KeyboardButton('Vessel')
    aircraft = types.KeyboardButton('Aircraft')
    markup.add(vessel, aircraft)
    bot.send_message(message.chat.id, 'To fly or to sail?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Vessel':
        bot.send_message(message.chat.id,'Please apply IMO number')

        @bot.message_handler(content_types=['text'])  # Создаём новую функцию ,реагирующую на любое сообщение
        def imo_answer(message):
            global imo  # объявляем глобальную переменную
            imo = message.text
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            location = types.KeyboardButton('Location')
            vessel_position_age = types.KeyboardButton('Age of position')
            speed_heading = types.KeyboardButton('Speed/Heading')
            vessel_img = types.KeyboardButton('Vessel image')
            vessel_purpose = types.KeyboardButton('Vessel purpose')
            vessel_name = types.KeyboardButton('Vessel name')
            navigation_status = types.KeyboardButton('Navigation status')
            back = types.KeyboardButton('Back')
            markup.add(location, vessel_position_age, speed_heading, vessel_img, vessel_purpose, vessel_name, navigation_status, back)
            bot.send_message(message.chat.id, 'Please count to 20 (let it parse) and choose option', reply_markup=markup)
            with open('vessel_parsing.txt', 'w', )as file:
               file.write(f'{str(main.get_data_for_vessel(imo))}')
               file.close()
        bot.register_next_step_handler(message, imo_answer)

    elif message.text == 'Location':
        with open('vessel_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_location(message.chat.id, float(an.get('lat').replace('°','')), float(an.get('lon').replace('°','')))
            file.close()

    elif message.text == 'Age of position':
        with open('vessel_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('position_age'))
            file.close()

    elif message.text == 'Navigation status':
        with open('vessel_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('navigation_status'))
            file.close()

    elif message.text == 'Speed/Heading':
        with open('vessel_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('speed_heading'))
            file.close()

    elif message.text == 'Vessel image':
        with open('vessel_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('vessel_img'))
            file.close()

    elif message.text == 'Vessel purpose':
        with open('vessel_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('vessel_purpose'))
            file.close()

    # elif message.text == 'Navigation status':
    #     bot.send_message(message.chat.id, answer.an.get('navigation_status'))
    #
    elif message.text == 'Vessel name':
        with open('vessel_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('vessel_name'))
            file.close()

    # bot.register_message_handler(vessel_answer, main.get_data(vessel_answer))
    elif message.text == 'Back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        vessel = types.KeyboardButton('Vessel')
        aircraft = types.KeyboardButton('Aircraft')
        markup.add(vessel, aircraft)
        bot.send_message(message.chat.id, 'To fly or to sail?', reply_markup=markup)

    elif message.text == 'Aircraft':
        bot.send_message(message.chat.id, 'Please apply flight number')

        @bot.message_handler(content_types=['text'])  # Создаём новую функцию ,реагирующую на любое сообщение
        def flight_number_answer(message):
            global flight_number  # объявляем глобальную переменную
            flight_number = message.text
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            airline = types.KeyboardButton('Airline')
            route = types.KeyboardButton('Route')
            scheduled_time_of_departure = types.KeyboardButton('Scheduled departure')
            scheduled_time_of_arrival = types.KeyboardButton('Scheduled arrival')
            aircraft_img = types.KeyboardButton('Aircraft image')
            altitude = types.KeyboardButton('Altitude')
            aircraft_bearing = types.KeyboardButton('Aircraft bearing')
            aircraft_speed = types.KeyboardButton('Aircraft speed')
            aircraft_type = types.KeyboardButton('Aircraft type')
            position = types.KeyboardButton('Position')
            back = types.KeyboardButton('Back')
            markup.add(airline, route, scheduled_time_of_arrival, scheduled_time_of_departure, aircraft_img, altitude, aircraft_bearing, aircraft_speed, aircraft_type, position, back)
            bot.send_message(message.chat.id, 'Please count to 20 (let it parse) and choose option', reply_markup=markup)
            with open('aircraft_parsing.txt', 'w', )as file:
                file.write(f'{str(main.get_data_for_aircraft(flight_number))}')
                file.close()
        bot.register_next_step_handler(message, flight_number_answer)

    elif message.text == 'Airline':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('airline'))
            file.close()

    elif message.text == 'Route':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('route'))
            file.close()

    elif message.text == 'Scheduled departure':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('scheduled_time_of_departure'))
            file.close()

    elif message.text == 'Scheduled arrival':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('scheduled_time_of_arrival'))
            file.close()

    elif message.text == 'Aircraft image':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('aircraft_img'))
            file.close()

    elif message.text == 'Altitude':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('altitude'))
            file.close()

    elif message.text == 'Aircraft bearing':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('aircraft_bearing'))
            file.close()

    elif message.text == 'Aircraft speed':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('aircraft_speed'))
            file.close()

    elif message.text == 'Aircraft type':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_message(message.chat.id, an.get('aircraft_type'))
            file.close()

    elif message.text == 'Position':
        with open('aircraft_parsing.txt', 'r+' ) as file:
            f = file.read().replace("'", '"')
            an = json.loads(f)
            bot.send_location(message.chat.id, float(an.get('lat').replace('°', '')), float(an.get('lon').replace('°', '')))
            file.close()

bot.polling(none_stop=True)
