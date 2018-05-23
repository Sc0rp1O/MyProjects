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
		 bot.send_message(callobj.message.chat.id, 'Столкновение с бездной\n\n1998 США Боевик 116 мин.\n\nРейтинги: ivi 6,7  КиноПоиск 7,1  IMDb 6,1')
		 bot.send_message(callobj.message.chat.id, 'deep.jpeg')
		elif '16+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Матрица\n\n1999 США Боевик. 131 мин.\n\nРейтинги: ivi 8,4  КиноПоиск 8,5  IMDb 8,7')
		 bot.send_message(callobj.message.chat.id, 'matrix.jpeg')
		elif '18+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Возвращение Суперфлая\n\n18+ 1990 США Боевик 95 мин. \n\nРейтинги: ivi 4,4  КиноПоиск 4,6 IMDb 5,0')
		 bot.send_message(callobj.message.chat.id, 'superfly.jpeg')

	elif '2000 - 2010' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Таинственный Остров\n\n2005 США Боевик. \n\nРейтинги: ivi 4,4  КиноПоиск4,8  IMDb4,5')
			bot.send_message(callobj.message.chat.id, 'island.jpeg')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Пираты Карибского моря\n\n2007 США Боевик 161 мин. \n\nРейтинги: ivi 7,5  КиноПоиск 8,0  IMDb 7,1')
			bot.send_message(callobj.message.chat.id, 'piratkm.jpeg')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Убивая мертвецов\n\n2010 США Боевик 89 мин.\n\nРейтинги: ivi 2,8  КиноПоиск 3,3  IMDb 3,0')
			bot.send_message(callobj.message.chat.id, 'deadun.jpeg')

	elif '2011 - 2018' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Стражи Галактики\n\n2014 США Боевик 121 мин.\n\nРейтинги: ivi 7,8  КиноПоиск 7,8  IMDb 8,1')
			bot.send_message(callobj.message.chat.id, 'galakt.jpeg')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Риддик\n\n2013 США Боевик 118 мин.\n\nРейтинги: ivi 6,4  КиноПоиск 6,6  IMDb 6,4')
			bot.send_message(callobj.message.chat.id, 'riddik.jpeg')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Расплата\n\n2011 США Боевик 84 мин.\n\nРейтинги: ivi 4,3  КиноПоиск 5,0  IMDb 4,6')
			bot.send_message(callobj.message.chat.id, 'payback.jpeg')


	if callobj.data == 'Ужасы':
		line_kb100 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk100 = telebot.types.InlineKeyboardButton(text = '<2000',
		 callback_data = '<=2000') 
		line_kb100.add(but_poisk100)
		but_serial100 = telebot.types.InlineKeyboardButton(text = '2000 - 2010',
		 callback_data = '=2000 - 2010')
		line_kb100.add(but_serial100)
		but100_film = telebot.types.InlineKeyboardButton(text = '2011 - 2018',
		 callback_data = '=2011 - 2018')
		line_kb100.add(but100_film)
		bot.send_message(callobj.message.chat.id, 'Фильм какого года ты хочешь увидеть?',reply_markup = line_kb100)


	if callobj.data == '<=2000':
		line_kb200 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk200 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '<=200012+') 
		line_kb200.add(but_poisk200)
		but_serial200 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '<=200016+')
		line_kb200.add(but_serial200)
		but200_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '<=200018+')
		line_kb200.add(but200_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb200)
		 
		
	elif callobj.data == '=2000 - 2010':
		
		line_kb300 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk300 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '=2000 - 201012+') 
		line_kb300.add(but_poisk300)
		but_serial300 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '=2000 - 201016+')
		line_kb300.add(but_serial300)
		but300_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '=2000 - 201018+')
		line_kb300.add(but300_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb300)

		
	elif callobj.data == '=2011 - 2018':
		
		line_kb400 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk400 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '=2011 - 201812+') 
		line_kb400.add(but_poisk400)
		but_serial400 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '=2011 - 201816+')
		line_kb400.add(but_serial400)
		but400_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '=2011 - 201818+')
		line_kb400.add(but400_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb400)

	if '<=2000' in callobj.data:
		if '12+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Пьющие кровь\n\n1991 СССР Ужасы 101 мин.\n\nРейтинги: ivi 6,5  КиноПоиск 6,8  IMDb 6,8')
		 bot.send_message(callobj.message.chat.id, 'blood.jpeg')
		elif '16+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Молчание ягнят\n\n1990 США Ужасы 118 мин.\n\nРейтинги: ivi 9,0  КиноПоиск 8,3  IMDb 8,6')
		 bot.send_message(callobj.message.chat.id, 'molchan.jpeg')
		elif '18+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Зависимость\n\n1994 США Ужасы 82 мин.\n\nРейтинги: ivi 6,2  КиноПоиск 6,3  IMDb 6,4')
		 bot.send_message(callobj.message.chat.id, 'zavisim.jpeg')

	elif '=2000 - 2010' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Забытое\n\n2004 США Ужасы 94 мин.\n\nРейтинги: ivi 6,7  КиноПоиск 6,6  IMDb 5,8')
			bot.send_message(callobj.message.chat.id, 'zabitoye.jpeg')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Амфибия\n\n2010 Нидерланды Ужасы 83 мин.\n\nРейтинги: ivi 4,2  КиноПоиск 3,7  IMDb 3,6')
			bot.send_message(callobj.message.chat.id, 'amfib.jpeg')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Теория убийств\n\n2008 США Ужасы 81 мин.\n\nРейтинги: ivi 5,3  КиноПоиск 5,9  IMDb 5,5')
			bot.send_message(callobj.message.chat.id, 'theory.jpeg')

	elif '=2011 - 2018' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Взаперти\n\n2016 Канада Ужасы 87 мин.\n\nРейтинги: ivi 4,7  КиноПоиск 4,8  IMDb 4,7')
			bot.send_message(callobj.message.chat.id, 'vzapert.jpeg')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Квест\n\n2017 США Ужасы 83 мин.\n\nРейтинги: ivi 3,8  КиноПоиск 4,4  IMDb 4,3')
			bot.send_message(callobj.message.chat.id, 'quest.jpeg')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Оно\n\n2017 США Ужасы 128 мин.\n\nРейтинги: ivi 7,2  КиноПоиск 7,4  IMDb 7,5')
			bot.send_message(callobj.message.chat.id, 'ono.jpeg')


	if callobj.data == 'Комедии':
		line_kb500 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk500 = telebot.types.InlineKeyboardButton(text = '<2000',
		 callback_data = '<-2000') 
		line_kb500.add(but_poisk500)
		but_serial500 = telebot.types.InlineKeyboardButton(text = '2000 - 2010',
		 callback_data = '-2000 - 2010')
		line_kb500.add(but_serial500)
		but500_film = telebot.types.InlineKeyboardButton(text = '2011 - 2018',
		 callback_data = '-2011 - 2018')
		line_kb500.add(but500_film)
		bot.send_message(callobj.message.chat.id, 'Фильм какого года ты хочешь увидеть?',reply_markup = line_kb500)


	if callobj.data == '<-2000':
		line_kb600 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk600 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '<-200012+') 
		line_kb600.add(but_poisk600)
		but_serial600 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '<-200016+')
		line_kb600.add(but_serial600)
		but600_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '<-200018+')
		line_kb600.add(but600_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb600)
		 
		
	elif callobj.data == '-2000 - 2010':
		
		line_kb700 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk700 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '-2000 - 201012+') 
		line_kb700.add(but_poisk700)
		but_serial700 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '-2000 - 201016+')
		line_kb700.add(but_serial700)
		but700_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '-2000 - 201018+')
		line_kb700.add(but700_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb700)

		
	elif callobj.data == '-2011 - 2018':
		
		line_kb800 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk800 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '-2011 - 201812+') 
		line_kb800.add(but_poisk800)
		but_serial800 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '-2011 - 201816+')
		line_kb800.add(but_serial800)
		but800_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '-2011 - 201818+')
		line_kb800.add(but800_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb800)

	if '<-2000' in callobj.data:
		if '12+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Дети Понедельника\n\n1997 Россия Комедии 94 мин.\n\nРейтинги: ivi 6,3  КиноПоиск 7,2  IMDb 6,2')
		 bot.send_message(callobj.message.chat.id, 'deti_pn.jpeg')
		elif '16+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, '\n\n1997 США  Комедии 97 мин.\n\nРейтинги: ivi 7,0  КиноПоиск 7,6  IMDb 7,1')
		 bot.send_message(callobj.message.chat.id, 'plut.jpeg')
		elif '18+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Мама не горюй\n\n1997 Россия Комедии 83 мин.\n\nРейтинги: ivi 6,7  КиноПоиск 7,1  IMDb 6,9')
		 bot.send_message(callobj.message.chat.id, 'mama.jpeg')

	elif '-2000 - 2010' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Час Пик 3\n\n2007 США Комедии 90 мин.\n\nРейтинги: ivi 7,1  КиноПоиск 7,1  IMDb 6,2')
			bot.send_message(callobj.message.chat.id, 'chasp.jpeg')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Адреналин: Высокое напряжение\n\n2009 США Комедии 95 мин.\n\nРейтинги: ivi 5,8  КиноПоиск 6,3  IMDb 6,2')
			bot.send_message(callobj.message.chat.id, 'adrenaline.jpeg')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Казанова\n\n2005 США Комедии 106 мин.\n\nРейтинги: ivi 6,8  КиноПоиск 7,6  IMDb 6,5')
			bot.send_message(callobj.message.chat.id, 'kasanova.jpeg')

	elif '-2011 - 2018' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Чудо\n\n2017 США Комедии 113 мин.\n\nРейтинги: ivi 8,1  КиноПоиск 8,0  IMDb 8,0')
			bot.send_message(callobj.message.chat.id, 'wonder.jpeg')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Битва преподов\n\n2017 США Комедии 87 мин.\n\nРейтинги: ivi 5,0  КиноПоиск 5,4  IMDb 5,6')
			bot.send_message(callobj.message.chat.id, 'battle.jpeg')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Субурбикон\n\n2017 США Комедии 100 мин.\n\nРейтинги: ivi 6,3  КиноПоиск 6,3  IMDb 5,5')
			bot.send_message(callobj.message.chat.id, 'subur.jpeg')



if __name__ == '__main__':
	bot.polling()