story = """Güneşli bir yaz günüymüş, 
anne ördek gölün kenarındaki ağacın altında yumurtlamak için güzel bir yer bulmuş.
Beş yumurta yumurtlamış, birden yumurtalarından birinin diğerinden farklı olduğunu fark etmiş. 
Biraz endişelenmiş, sonra yumurtaların çatlamasını beklemiş. 
Güzel bir sabah, nihayet birbiri peşi sıra yumurtalar kırılmaya başlamış. 
Cik, cik demişler bütün yumurtalar canlanmış, ördek yavruları başlarını büyük dünyaya doğru uzatıyorlarmış."""

word_list = story.split(" ")
counter = 0
for word in word_list:
    if word[0] == "b" or word[0] == "B":
        print(word)
        counter += 1
        
print(f"\nToplam {counter} kelime b ile baslıyordu.")        