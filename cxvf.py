import telebot

TOKEN = '594167976:AAF_JFvTuN9cVL5g8kpDhJaGaIqn1ExcaRw'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['start'])
def beginning(message):
	bot.send_message(message.chat.id, 'введите команду /getFilm чтобы заполнить анкету')

@bot.message_handler(commands = ['getFilm'])
def answer(message):
 line_kb = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру
 but_film = telebot.types.InlineKeyboardButton(text = 'Боевик',
	callback_data = 'Боевик') # создаем кнопку
 line_kb.add(but_film) # вешаем кнопку на клавиатуру

 but_kinopoisk = telebot.types.InlineKeyboardButton(text = 'Ужасы',
	callback_data = 'Ужасы') 
 line_kb.add(but_kinopoisk)
 but_serial = telebot.types.InlineKeyboardButton(text = 'Комедии',
	callback_data = 'Комедии')
 line_kb.add(but_serial)
 msg = bot.send_message(message.chat.id, 'Я тебе помогу определиться с выбором фильма. Ответь на несколько вопросов. \nВаш любимый жанр?', reply_markup = line_kb)


@bot.callback_query_handler(func = lambda call:True) 
def random_film(callobj):
	if callobj.data == 'Боевик':
		line_kb2 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk = telebot.types.InlineKeyboardButton(text = '<2000',
		 callback_data = '<2000') 
		line_kb2.add(but_poisk)
		but_serial2 = telebot.types.InlineKeyboardButton(text = '2000 - 2010',
		 callback_data = '2000 - 2010')
		line_kb2.add(but_serial2)
		but3_film = telebot.types.InlineKeyboardButton(text = '2011 - 2018',
		 callback_data = '2011 - 2018')
		line_kb2.add(but3_film)
		bot.send_message(callobj.message.chat.id, 'Фильм какого года ты хочешь увидеть?',reply_markup = line_kb2)


	if callobj.data == '<2000':
		line_kb4 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk4 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '<200012+') 
		line_kb4.add(but_poisk4)
		but_serial5 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '<200016+')
		line_kb4.add(but_serial5)
		but6_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '<200018+')
		line_kb4.add(but6_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb4)
		 
		
	elif callobj.data == '2000 - 2010':
		
		line_kb6 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk7 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '2000 - 201012+') 
		line_kb6.add(but_poisk7)
		but_serial7 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '2000 - 201016+')
		line_kb6.add(but_serial7)
		but9_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '2000 - 201018+')
		line_kb6.add(but9_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb6)

		
	elif callobj.data == '2011 - 2018':
		
		line_kb10 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk10 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '2011 - 201812+') 
		line_kb10.add(but_poisk10)
		but_serial10 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '2011 - 201816+')
		line_kb10.add(but_serial10)
		but10_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '2011 - 201818+')
		line_kb10.add(but10_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb10)

	if '<2000' in callobj.data:
		if '12+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Люди Икс')
		elif '16+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Матрица')
		elif '18+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Фильм не найден')

	elif '2000 - 2010' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Таинственный Остров')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Пираты Карибского моря')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Убивая мертвецов')

	elif '2011 - 2018' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Стражи Галактики')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Риддик')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Расплата')


	if callobj.data == 'Ужасы':
		line_kb100 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk100 = telebot.types.InlineKeyboardButton(text = '<2000',
		 callback_data = '<2000') 
		line_kb100.add(but_poisk100)
		but_serial100 = telebot.types.InlineKeyboardButton(text = '2000 - 2010',
		 callback_data = '2000 - 2010')
		line_kb100.add(but_serial100)
		but100_film = telebot.types.InlineKeyboardButton(text = '2011 - 2018',
		 callback_data = '2011 - 2018')
		line_kb100.add(but100_film)
		bot.send_message(callobj.message.chat.id, 'Фильм какого года ты хочешь увидеть?',reply_markup = line_kb100)


	if callobj.data == '<2000':
		line_kb200 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk200 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '<200012+') 
		line_kb200.add(but_poisk200)
		but_serial200 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '<200016+')
		line_kb200.add(but_serial200)
		but200_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '<200018+')
		line_kb200.add(but200_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb200)
		 
		
	elif callobj.data == '2000 - 2010':
		
		line_kb300 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk300 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '2000 - 201012+') 
		line_kb300.add(but_poisk300)
		but_serial300 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '2000 - 201016+')
		line_kb300.add(but_serial300)
		but300_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '2000 - 201018+')
		line_kb300.add(but300_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb300)

		
	elif callobj.data == '2011 - 2018':
		
		line_kb400 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk400 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '2011 - 201812+') 
		line_kb400.add(but_poisk400)
		but_serial400 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '2011 - 201816+')
		line_kb400.add(but_serial400)
		but400_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '2011 - 201818+')
		line_kb400.add(but400_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb400)

	if '<2000' in callobj.data:
		if '12+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Пьющие кровь')
		elif '16+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Молчание ягнят')
		elif '18+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Зависимость')

	elif '2000 - 2010' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Забытое')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Амфибия')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Теория убийств')

	elif '2011 - 2018' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Взаперти')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Квест')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Оно')


	if callobj.data == 'Комедии':
		line_kb500 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk500 = telebot.types.InlineKeyboardButton(text = '<2000',
		 callback_data = '<2000') 
		line_kb500.add(but_poisk500)
		but_serial500 = telebot.types.InlineKeyboardButton(text = '2000 - 2010',
		 callback_data = '2000 - 2010')
		line_kb500.add(but_serial500)
		but500_film = telebot.types.InlineKeyboardButton(text = '2011 - 2018',
		 callback_data = '2011 - 2018')
		line_kb500.add(but500_film)
		bot.send_message(callobj.message.chat.id, 'Фильм какого года ты хочешь увидеть?',reply_markup = line_kb500)


	if callobj.data == '<2000':
		line_kb600 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk600 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '<200012+') 
		line_kb600.add(but_poisk600)
		but_serial600 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '<200016+')
		line_kb600.add(but_serial600)
		but600_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '<200018+')
		line_kb600.add(but600_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb600)
		 
		
	elif callobj.data == '2000 - 2010':
		
		line_kb700 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk700 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '2000 - 201012+') 
		line_kb700.add(but_poisk700)
		but_serial700 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '2000 - 201016+')
		line_kb700.add(but_serial700)
		but700_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '2000 - 201018+')
		line_kb700.add(but700_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb700)

		
	elif callobj.data == '2011 - 2018':
		
		line_kb800 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk800 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '2011 - 201812+') 
		line_kb800.add(but_poisk800)
		but_serial800 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '2011 - 201816+')
		line_kb800.add(but_serial800)
		but800_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '2011 - 201818+')
		line_kb800.add(but800_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb800)

	if '<2000' in callobj.data:
		if '12+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Дети Понедельника')
		elif '16+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Плутовство')
		elif '18+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Мама не горюй')

	elif '2000 - 2010' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Мой лучший друг')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Негодяи')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Стригой')

	elif '2011 - 2018' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'С новым годом!')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Паранормальный отряд')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Киллер поневоле')



if __name__ == '__main__':
	bot.polling()