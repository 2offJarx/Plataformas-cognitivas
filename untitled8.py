# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17wYBWoF4nVSV2Lj43D1L6X0oqdlwfHCv
"""

import requests
resposta=requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=13z1syhzgYeN1dMlxRd6yyEeHD0nIQBU16sHSp25')

imagens = resposta.json()
for a in imagens['photos']:
  print(a['img_src'])
  continuar = input("Digite sim para mostrar a próxima imagem e não para parar:")
  if continuar=="não":
    break