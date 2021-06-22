import requests
from bs4 import BeautifulSoup
import pyperclip
from PIL import ImageGrab
from PIL import Image
import PIL
from io import StringIO
import io
import base64
import numpy as np
import cv2
import pandas as pd
import os
import keyboard
false = 'Неверная исходная фраза'
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
URL = 'https://www.nftmaniaquest.com/en/'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

WALLET_ADRESS = '0xa065F580294fC6Cc116851c147942F9F2B41b9a7'

def get_html(html,params=None):
	r = requests.get(URL,headers=HEADERS)
	return r

def get_content(html):
	soup = BeautifulSoup(html,'html.parser')
	items = soup.find('div',class_='sidequest_sliderNFT__block__z8gWq sidequest_sliderNFT__block_purple__2QNdF')


	riddles =[]
	answer =''
	for item in items:
		for riddles_num in item.find_all('span',class_='button_button__text__1Soec'):
			riddl = riddles_num.get_text().replace('1 RIDDLE','egg').replace('2 RIDDLE','reveal').replace('3 RIDDLE','general').replace('4 RIDDLE','piano').replace('5 RIDDLE','lust').replace('6 RIDDLE','flush').replace('7 RIDDLE','diary').replace('8 RIDDLE','source').replace('9 RIDDLE','9').replace('10 RIDDLE','10').replace('11 RIDDLE','11').replace('12 RIDDLE','12')
			answer = answer +' '+ riddl 
			
	riddles.append({
		'riddles_num':riddles_num.get_text(),

		})



	pyperclip.copy(answer)
	print(answer)

def parse():
	html = get_html(URL)
	if html.status_code == 200:
		riddles = get_content(html.text)
		
	else:
		print('Error')

parse()


