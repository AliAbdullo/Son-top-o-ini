
import random as r

def son_top(x=10):
  """Son topga qiymat berilganda shu songacha O'yin o'ynaladi"""
  t_son=r.randint(1,x)
  print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?") 

  taxminlar=0
  while True:
    taxmin= int(input("Son kirting >>>"))
    taxminlar+=1
    
    if taxmin<t_son:
      print("Xato. Men o'ylagan son bundan kattaroq. Yana xarakat qiling: ")
    elif taxmin>t_son:
      print("Xato. Men o'ylagan son bundan kichikroq. Yana xarakat qiling: ")
    else:
      break
  print(f"TOPDINGIZ! {t_son} ni o'ylagan edim. {taxminlar} taxmin bilan topdingiz. Tabriklayman !!!")


  

import random as d
def sontop(x=10):
  """Son kiritiladi va shu songacha bo'lgan sonlar orolig'ida o'yinimiz ishalaydi"""
  input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
  
  quyi=1
  yuqori=x
  taxminlar=0
  while True:
    taxminlar+=1
    if quyi != yuqori:
      taxminiy_son= d.randint(1,x)
    else:
      quyi= yuqori
    javob = input(f"Siz {taxminiy_son} ni o'yladingiz. To'g'ri bo'lsa (T)ni, katta bolsa (-), kichik bo'sa (+)ni belgilang! ".lower())
    if javob =='-':
      yuqori=taxminiy_son-1
    elif javob=='+':
      quyi=taxminiy_son+1
    else:
      break
  print(f"Men {taxminlar} taxmin bilan topdim!")
  return taxminlar  