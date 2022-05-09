import random as r


def son_top(x=10):
    """Son topga qiymat berilganda shu songacha O'yin o'ynaladi"""
    t_son = r.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")

    taxminlar = 0
    while True:
        taxmin = int(input("Son kirting >>>"))
        taxminlar += 1

        if taxmin < t_son:
            print(
                "Xato. Men o'ylagan son bundan kattaroq. Yana xarakat qiling: "
            )
        elif taxmin> t_son:
            print(
                "Xato. Men o'ylagan son bundan kichikroq. Yana xarakat qiling: "
            )
        else:
            break
    print(
        f"TOPDINGIZ! \"{t_son}\" ni o'ylagan edim. {taxminlar} taxmin bilan topdingiz. Tabriklayman !"
    )
    return taxminlar


import random as d


def sontop(x=10):
    """Son kiritiladi va shu songacha bo'lgan sonlar orolig'ida o'yinimiz ishalaydi"""
    input(
        f"\n1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman."
    )

    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxminiy_son = d.randint(quyi, yuqori)
        else:
            quyi = yuqori
        javob = input(f"\nSiz {taxminiy_son} ni o'yladingiz. To'g'ri bo'lsa (T)ni, bundan kattaroq bo'lsa (+), yoki kichikroq (-)ni belgilang! ")
        if javob == '-':
            yuqori = taxminiy_son - 1
        elif javob == '+':
            quyi = taxminiy_son + 1
        else:
            break
    print(f"\nMen {taxminlar} taxmin bilan topdim!")
    return taxminlar


def play(x=10):
    
    yana = True
    while yana:
      menTopaman = son_top(x)
      pcTopadi = sontop(x)
      if menTopaman < pcTopadi:
            print(f"Siz yutdingiz!")
      elif menTopaman > pcTopadi:
            print(f"Men yutdim!")
      else:
            print("Durrang!")

      yana = int(input("Yana o'ynaysizmi Ha(1)/Yo'q(0):"))
