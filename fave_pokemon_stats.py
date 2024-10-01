
import datetime
import poke_greet

class pokemon:
    def __init__(self, pokemon, HP, ATK, DEF, SPATK, SPDEF, SPD, name = 'Trainer'):
        self.pokelst =          {}
        self.p_name =           pokemon
        self.hp =               HP
        self.atk =              ATK
        self.defense =          DEF
        self.spatk =            SPATK
        self.spdef =            SPDEF
        self.spd =              SPD
        self.name = poke_greet.poke_greet(name)
    
    #note: if you are importing the entire module, its module.module(variables) then you can instance. Otherwise, u can use from module import module to instance.
        


    #confirm the pokemon name, if not, get another pokemon name and capitaize the first letter if applicable.
    def confirm_poke(self):
        self.name.greet()
        print('...')
        print(f"'{self.p_name}.' Is that the Pokemon you want to add to your growing collection?")
        input('Enter Yes or No: ')

    #get pokemon name, then add them to the dictionary with its stats in a dct
    def add_poke(self, pokemon):

        input_poke = input()
        add_pokemon = self.pokelst

    def get_poke_stats(self):
        lst = self.pokelst



#pokemon 

if __name__ == '__main__':
    garchomp = pokemon('Garchomp', 108, 130, 95, 80, 85, 102)
    garchomp.confirm_poke()