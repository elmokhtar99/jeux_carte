from random import randint, shuffle
import random
# def distribution():
#     cartes = create_carte()
#     joueur_1=[]
#     joueur_2=[]
#     while len(cartes)>0 :
#         random_index_1=randint(0,len(cartes)-1)
#         joueur_1.append(cartes[random_index_1])
#         cartes.pop(random_index_1)
#         random_index_2=randint(0,len(cartes)-1)
#         joueur_2.append(cartes[random_index_2])
#         cartes.pop(random_index_2)

#     return joueur_1,joueur_2

# def shuffle_carte(cartes):
#     random.shuffle(cartes)
#     return cartes

# def pop_carte(cartes):
#     cartes=shuffle_carte(cartes)
#     cartes.pop()

# a,b=distribution_main()
# print(len(a))
# print(len(b))
# print(a[0][1])
# print(b[0])


def create_carte():
    couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
    noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    cartes=[]
    for couleur in couleurs:
        for nom in noms :
            carte=(nom,couleur)
            cartes.append(carte)
    return cartes



def distribution_main():
    cartes = create_carte()
    random.shuffle(cartes)
    joueur_1=[]
    joueur_2=[]
    while len(cartes)>0 : 
        joueur_1.append(cartes.pop())
        joueur_2.append(cartes.pop())
    return joueur_1,joueur_2

        
def battle_card(carte_1,carte_2):
    valeurs_num = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}
    valeurs_color={'CARREAU':'Rouge', 'COEUR':'Rouge', 'TREFLE':'Noir', 'PIQUE':'Noir'}
    
    carte_1_valeur_num=valeurs_num[carte_1[0]]
    carte_2_valeur_num=valeurs_num[carte_2[0]]
    carte_1_valeur_color=valeurs_color[carte_1[1]]
    carte_2_valeur_color=valeurs_color[carte_2[1]]

    if carte_1_valeur_color != carte_2_valeur_color :
        if carte_1_valeur_color == "Noir":
            return 1
        else :
            return 2
    else:
        if carte_1_valeur_color == "Noir":
            if carte_1_valeur_num > carte_2_valeur_num :
                return 1
            elif carte_1_valeur_num < carte_2_valeur_num :
                return 2
            else:
                return 0
        else :
            if carte_1_valeur_num < carte_2_valeur_num :
                return 1
            elif carte_1_valeur_num > carte_2_valeur_num :
                return 2
            else:
                return 0


            
def jeux_de_carte():
    joueur_1,joueur_2=distribution_main()
    num_partie =1
    score_joueur_1 = 0
    score_joueur_2 = 0
    while len(joueur_1)>0:
        
        random_index_1=randint(0,len(joueur_1)-1)
        card_joueur_1=joueur_1[random_index_1]
        joueur_1.pop(random_index_1)
        random_index_2=randint(0,len(joueur_2)-1)
        card_joueur_2=joueur_2[random_index_2]
        joueur_2.pop(random_index_2)
        score = battle_card(card_joueur_1,card_joueur_2)
        print("****************************partie numero {}**************************** ".format(num_partie))
        print("Le joueur 1 a jouer avec la carte : "+ card_joueur_1[0]+" "+ card_joueur_1[1])
        print("Le joueur 2 a jouer avec la carte : "+ card_joueur_2[0]+" "+ card_joueur_2[1])
        if score==1:
            score_joueur_1+=1          
            print("****************************Le joueur 1 gagne****************************")

        elif score ==2:
            score_joueur_2+=1
            print("****************************Le joueur 2 gagne****************************")


        print("Score Joueur 1 : {} ".format(score_joueur_1))
        print("Score Joueur 2 : {} ".format(score_joueur_2))
        num_partie=+1
    
    if score_joueur_2 > score_joueur_1:
        print("le Joueur gagnant est le joueur 2")
    elif score_joueur_2 < score_joueur_1:
        print("le Joueur gagnant est le joueur 1")
    else:
        print("Egalite")


        

        


