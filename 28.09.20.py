# Soru 3'e göz at
####################################################################################################
####################################################################################################
# region Soru1
# dicti döngüye almayı dene


# fonksiyon filan?
def manav():
    fruits = {"elma": 3, "armut": 5, "mandalina": 6}

    elma_kilo = input("Kaç kilo elma alcan? ")
    armut_kilo = input("Peki kaç kilo armut? ")
    mandalina_kilo = input("Mandalina ne kadar vereyim? ")

    elma_fiyat = int(elma_kilo) * fruits["elma"]
    armut_fiyat = int(armut_kilo) * fruits["armut"]
    mandalina_fiyat = int(mandalina_kilo) * fruits["mandalina"]

    full_fiyat = elma_fiyat + armut_fiyat + mandalina_fiyat

    print(
        f"Elma {elma_fiyat}, armut {armut_fiyat}, mandalina da {mandalina_fiyat} tutuyor",
        f"Yani totalin {full_fiyat} oluyor.  ")


# f string güzel

manav()

# endregion
####################################################################################################
####################################################################################################
# region Soru2


def first_letterinator_9000(writing, first):
    # word_list = writing.split(" ")
    word_list = writing.split()  # göstermedik haklısın

    i = 0
    for word in word_list:
        # if word[0] == first or word[0] == first.upper(): # "or"u görmediniz o yüzden kabul etmiyorum
        if word[0].lower() == first.lower():
            i -= -1  # ha ha

    print(f"\nToplam {i} kelime {letter} ile baslıyordu.")


story = """Güneşli bir yaz günüymüş, anne ördek gölün kenarındaki ağacın altında yumurtlamak için güzel bir yer bulmuş. 
           Beş yumurta yumurtlamış, birden yumurtalarından birinin diğerinden farklı olduğunu fark etmiş. Biraz endişelenmiş, 
           sonra yumurtaların çatlamasını beklemiş. Güzel bir sabah, nihayet birbiri peşi sıra yumurtalar kırılmaya başlamış. 
           Cik, cik demişler bütün yumurtalar canlanmış, ördek yavruları başlarını büyük dünyaya doğru uzatıyorlarmış."""

letter = input("What letter do you want to search for?")

first_letterinator_9000(story, letter)

# endregion
####################################################################################################
####################################################################################################
# region Soru3


def square_sorter(list):
    # kardeşim sakin enumerate filan yavaş biraz
    # görmediğiniz bir şey kullandığın için kabul edemiyorum :-(
    for index, i in enumerate(list):
        list[index] = i * i

    list.sort()
    print(list)


def square_sorter(*a, **kw):
    raise Exception("TUNAPRO1234")


numbers = [2, 14, 9, 46, 20]
square_sorter(numbers)

# endregion
####################################################################################################
####################################################################################################