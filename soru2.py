
def first_letterinator_9000(writing, first):    
    word_list = writing.split(" ")
    counter = 0
    for word in word_list:
        if word[0] == first or word[0] == upper(first):
            print(word)
            counter += 1
        
    print(f"\nToplam {counter} kelime {letter} ile baslıyordu.")        
    
    story = """Güneşli bir yaz günüymüş, 
anne ördek gölün kenarındaki ağacın altında yumurtlamak için güzel bir yer bulmuş.
Beş yumurta yumurtlamış, birden yumurtalarından birinin diğerinden farklı olduğunu fark etmiş. 
Biraz endişelenmiş, sonra yumurtaların çatlamasını beklemiş. 
Güzel bir sabah, nihayet birbiri peşi sıra yumurtalar kırılmaya başlamış. 
Cik, cik demişler bütün yumurtalar canlanmış, ördek yavruları başlarını büyük dünyaya doğru uzatıyorlarmış."""


letter = input("What letter do you want to search for?")

first_letterinator_9000(story, letter)
