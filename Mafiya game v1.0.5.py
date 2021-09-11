# بازی مافیا
# raandom  را با دستور import فراخوانی میکنیم
import random
from pyperclip import copy
# از کتابخانه پایپر کلیپ تابع کپی را وارد برنامه می کنیم. این کتابخانه کوچکی جهت کپی یا پیست داده در کلیپبورد می باشد.
# اگر نداریدش برای نصب میتوانید از طریق خط فرمان و با این دستور آن را نصب کنید.
#pip install pyperclip
import os
# این یکی از کتابخانه های استاندارد پایتون جهت کار با اعمالی که در سیستم عامل قابل انجام می باشد، هست. مثل کپی کات تغییر نام و غیره.
open('gameData.txt', 'w', encoding='utf-8').write('')
#با استفاده از تابع open که از توابع پیشفرض پایتون می باشد، فایلی را به نام gameData ساخته و با اختصاص استرینگ 'w' حالت آن را write گذاشته و encoding که استاندارد نوشتن کاراکتر هاست را بر روی UTF_8 که از تمامی زبان های رایج پشتیبانی می کند قرار دادیم.
# و با کمک دستور رایت یک استرینگ خالی وارد فایل کردیم.با استفاده از این دستور یک استرینگ خالی بر روی این فایل نوشتیم.

filePath = '"' + os.getcwd() + '\\gameData.txt"'
# با استفاده از تابعgetcwd() از کتابخانه OS آدرس محل اجرای فایل پایتون را گرفته و نام فایل را به انتهای آدرس اضافه کرده و به CMD دستور باز کردن فایل را می فرستیم.
nafarat = ["نفر اول", "نفر دوم", "نفر سوم", "نفر چهارم", "نفر پنجم", "نفر ششمم", "نفر هفتم", "نفر هشتم", "نفر نهم",
		   "نفر دهم", "نفر یازدهم", "نفر دوازدهم", "نفر سیزدهم", "نفر چهاردهم", "نفر پانزدهم", "نفر شانزدهم",
		   "نفر هِفتدهم", "نفر هجدهم", "نفر نونزدهم", "نفر بیستم"]
# یک لیست برای نگهداری ورودی نام بازیکن ها ایجاد میکنیم
list_players = []
####برای نقش ها یک لیست ایجاد میکنیم
list_rolls = ["پدر خوانده", "دکتر لکتر", "مافیای ساده", "مافیای ساده", "دکتر", "روانپزشک", "اسنایپر یا حرفه ای",
			  "کارآگاه", "شهردار", "جان سخت", "شهروند ساده", "شهروند ساده"]
len_roll = len(list_rolls)
# یک لیست برای نگهداری نقش های اتفاقی ایجاد میکنیم
new_rolls = []

# برای اینکه تست کنیم در هر شرایطی تعداد نقش شهروندان دو برابر نقش مافیا باشد دو لیست جداگانه از نقش مافیا و شهروندان ایجاد میکنیم
white_list = ["شهروند ساده", "شهروند ساده", "شهردار", "دکتر", "روانپزشک", "کارآگاه", "اسنایپر یا حرفه ای", "جان سخت"]
len_white = len(white_list)
black_list = ["پدر خوانده", "دکتر لکتر", "مافیای ساده", "مافیای ساده"]
len_black = len(black_list)

print("مشخص کردن نقش در بازی مافیا", "\n", "نسخه: 1.0.5")

try:
	number_of_player = int(input("تعداد شرکت کننده در این بازی را وارد کنید!"))
	text_int = int(number_of_player)
	pass
except:
	print("خطای نوع داده ورودی! تعداد شرکت کننده را با عدد وارد کنید.")
# با ایجاد شرط مشخص میکنیم اگر تعداد شرکت کننده ها بیشتر از دوازده نفر بود با کاربر اجازه بدیم که نقش های جدید را اضافه کند
if number_of_player > 12:
	new_number = number_of_player - 12
	while not new_number == 0:
		print("شما باید {} نقش جدید را اضافه کنید!".format(new_number))
		rolls_input = input("نقش جدید را وارد کنید!")
		list_rolls.append(rolls_input)
		new_number -= 1
# با ایجاد شرطی مشخث میکنیم اکه دتعدا شرکت کننده ها کمتر از 12 بود کدام نقش از لیست حذف شود
if number_of_player < 12:
	new_number = 12 - number_of_player
	while new_number > 0:
		if len_roll == 12 - new_number:
			break
		print("شما تنها مجاز به حذف این نقش ها هستید: شهروند ساده، مافیای ساده، روانپزشک، شهردار، دکتر لکتر، جان سخت.")
		print("شما میتوانید {} نقش را از لیست حذف کنید.".format(new_number))
		roll_input = input("نقشی را که میخواهید حذف شود را وارد کنید!")
		if roll_input == "پدرخوانده" or roll_input == "پدر خوانده":
			print("شما نمیتوانید نقش پدر خوانده را از لیست حذف کنید!")
			new_number += 1
		elif roll_input == "دکتر لکتر":
			list_rolls.remove("دکتر لکتر")
			black_list.remove("دکتر لکتر")
		elif roll_input == "مافیای ساده" or roll_input == "مافیا ساده" or roll_input == "مافیا":
			list_rolls.remove("مافیای ساده")
			black_list.remove("مافیای ساده")
		if roll_input == "شهردار":
			list_rolls.remove("شهردار")
			white_list.remove("شهردار")
		elif roll_input == "روانپزشک":
			list_rolls.remove("روانپزشک")
			white_list.remove("روانپزشک")
		elif roll_input == "شهروند ساده" or "شهروند":

			door = 0
			while not door == len_roll:
				if list_rolls[door] == "شهروند ساده":
					list_rolls.pop(door)
					door2 = 0
					while not door2 == len_white:
						if white_list[door2] == "شهروند ساده":
							white_list.pop(door2)
							break
						len_white = len(white_list)
						door2 += 1
					break
				len_roll = len(list_rolls)
				door += 1


		elif roll_input == "اسنایپر" or roll_input == "حرفه ای":
			print("شما نمیتوانید نقش اسنایپر یا حرفه ای را از لیست حذف کنید")
			new_number += 1
		elif roll_input == "کاراگاه" or roll_input == "کارآگاه":
			print("شما نمیتوانید نقش کارآگاه را از لیست حذف کنید!")
			new_number += 1
		elif roll_input == "جان سخت":
			list_rolls.remove("جان سخت")
			white_list.remove("جان سخت")
		elif roll_input == "دکتر":
			print("شما نمیتوانید نقش دکتر را از لیست حذف کنید!")
			new_number += 1

		len_roll = len(list_rolls)
		new_number -= 1
# با ایجاد یک شرط مشخص میکنیم که تعداد مافیا نباید بزرگتر از نصف شهروندان باشد
len_white = len(white_list)
len_black = len(black_list)
if len_white < len_black * 2:
	print("تعداد نقش شهروندان باید دو برابر نقش مافیا باشد!", "\n", "لیست را از ابتدا تکمیل کنید!")
open('gameData.txt', 'a', encoding='utf-8').write("لیست  نام شرکت کننده ها و نقش ها\n")
# عنوان بخش نقش ها را به فایل اطلاعات بازی اضافه می کنیم.
# بخش ورودی شرکت کننده ها

		# با ایجاد یک حلقه به اندازه تعداد شرکت کننده ها  ورودی از کاربر میگیریم
for chance in range(0, number_of_player):
	print("نام {}".format(nafarat[chance]))
	name_input = input("نام شرکت کننده  را وارد کنید!")
	# با دستور .append  ورودی ها را به لیست بازیکن ها اضافه میکنیم
	list_players.append(name_input)
	# یک متغییر رندم ایجاد میکنیم و محدوده آن را بین صفر و طول لیست نقش ها منهای یک. چون با هر بار اجرای حلقه یک نقش از لیست حذف خواهد شد تا نقش تکراری بصورت تصادفی نداشته باشیم
	rand_rolls = random.randint(0, len_roll - 1)
	roll = list_rolls[rand_rolls]
	new_rolls.insert(chance, roll)
	# با دستور .pop  نقش اتفاقی انتخاب شده را از لیست حذف میکنیم
	list_rolls.pop(rand_rolls)
	# طول لیست نقش ها را به روز میکنیم
	len_roll = len(list_rolls)
	eachPlayerRoll = "{}: {} در نقش {}.\n".format(chance + 1, list_players[chance], new_rolls[chance])
	copy(eachPlayerRoll)
	# محتوای نقش را که در متغیر eachPlayerRoll میباشد به کمک تابع کپی از کتابخانه پایپر کلیپ وارد حافظه کلیپبورد کامپیوتر می کنیم.
	print(eachPlayerRoll, end='')
	open('gameData.txt', 'a', encoding='utf-8').write(eachPlayerRoll)
	# محتوای متغیر eachPlayerRoll را  فایل اطلاعات بازی اضافه می کنیم.
# chance += 1

# بخش پرینت کلی نقش ها
print("لیست  نام شرکت کننده ها و نقش ها")
# chance = 0
# while chance < number_of_player:
# اینجا از استرینگ 'a' که مخفف append میباشد استفاده کردیم. فرق آ« با رایت این می باشد که محتوای قبلی فایل باقی مانده و انتهای آن متن اضافه می گردد.
chance = 0
for chance in range(0, number_of_player):
	print(f'{chance + 1}: {list_players[chance]} در نقش {new_rolls[chance]}.\n')
	# یک راه خلاصه تر برای استفاده از format string این است که قبل کوتیشن حرف f که مخفف format میباشد بگذاریم و هر جا که خواستیم داخل استرینگ متغییر یا نتیجه عملیاتی را وارد کنیم آن را داخل آکولاد می گذاریم. نیازی به ایجاد چند استرینگ در این روش نیست و میتوان داخل یک استرینگ بی نهایت متغیر یا داده را وارد آن کرد.

# بخش کارت ها
print('بخش انتخاب کارتها')
cart_number = [1, 2, 3, 4, 5, 6]
# متغییر طول لیست شماره کارت ها را ایجاد میکنیم
len_cart_number = len(cart_number)
cart_name = ["شلیک نهایی", "مسیر سبز", "بیخوابی", "دروغ سیزده", "ذهن زیبا", "فرش قرمز"]

# اکگه تعداد شرکت کننده ها بیشتراز 12 نفر بود به کاربر اجازه میدهیم شماره کارتهای جدید را اضافه کند
if number_of_player > 12:
	try:
		chand_cart = int(input("چه تعداد کارت را مایل هستید به لیست اضافه کنید!؟"))
		test_float = float(chand_cart)

		cart = chand_cart
		x = 0
		door = chand_cart
		while not door == 0:
			print("شما میتوانید {} کارت جدید وارد کنید!".format(cart))
			new_cart = input("نام کارت جدید را وارد کنید!")
			cart_name.append(new_cart)
			cart_number.append(7 + x)
			cart -= 1
			x += 1
			door -= 1
	except:
		pass
# متغییر طول لیست کارت ها را ایجاد میکنیم
len_cart_name = len(cart_name)
# با ایجاد حلقه به اندازه تعداد کارت ها از کاربر ورودی میگیریم

len_cart_name = len(cart_name)
# هر بار که فایل بسته شد، باید دوباره آن را با همان دستور open باز کرد.
gameData = open('gameData.txt', 'a', encoding='utf-8').write('\nبخش کارت ها:\n')
for door_caart in range(0, len_cart_name):
	print("شماره کارت های موجود : {}".format(cart_number))
	cart_qustion = int(input("شماره کارت را وارد کنید!"))
	if not cart_qustion in cart_number:
		print(('متأسفم! این کارت قبلاً استفاده شده است. لطفاً شماره دیگری را وارد نمایید.'))
		continue
	# شماره کارت وارد شده را از لیست شماره کارتها حذف میکنیم تا دوباره  آن شماره پرسیده نشود
	cart_number.remove(cart_qustion)
	# با ایجاد یک حلقه به تعداد عدد کارت وارد شده یک متغییر رندوم را تکرار میکنیم تا در نهایت یک عدد بدست آید. 
	# دقیقا شبیه بهمزدن کارت ها 

	ran_cart = random.randint(0, len_cart_name - 1)
	len_cart_name = len(cart_name)
	# عدد تصادفی بدست آمده در حلقه بلپالا را به عنوان یه شماره اندیس در نظر گرفته و از لیست cart_name مقدار آن کارت را انتخاب میکنیم
	cart = cart_name[ran_cart]
	# کارت انتخاب شده را از لیست حذف میکنیم تا دوباره تکرار نشود
	cart_name.pop(ran_cart)
	len_cart_name = len(cart_name)
	len_cart_number = len(cart_number)
	eachCard = "کارت شماره {} : {}.\n".format(cart_qustion, cart)
	print(eachCard, end='')
	gameData = open('gameData.txt', 'a', encoding='utf-8').write(eachCard)
os.system(filePath)
# با استفاده از تابع system() از کتابخانه استاندارد OS میتوان دستوری را در محیط خط فرمان اجرا کرد. که در این مثال دستور اجرای فایل از طریق CMD داده می شود.
INPUT('برنامه به پایان رسید. برای خروج اینتر نمایید.')