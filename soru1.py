
def manav():
    fruits = {"elma": 3, 
              "armut": 5, 
              "mandalina": 6}

    elma_kilo = input("Kaç kilo elma alcan? ")
    armut_kilo = input("Peki kaç kilo armut? ")
    mandalina_kilo = input("Mandalina ne kadar vereyim? ")
    
    elma_fiyat = int(elma_kilo) * fruits["elma"]
    armut_fiyat = int(armut_kilo) * fruits["armut"]
    mandalina_fiyat = int(mandalina_kilo) * fruits["mandalina"]
    
    full_fiyat = elma_fiyat + armut_fiyat + mandalina_fiyat
    
    print(f"Elma {elma_fiyat}, armut {armut_fiyat}, mandalina da {mandalina_fiyat} tutuyor",
          f"Yani totalin {full_fiyat} oluyor.  ")
    
manav()    
