from lib import *

def hit_script(pv, dv, count):
    player, dealer, deck = Hand(), Hand(), Deck()
    game = Game([player, pv], [dealer, dv], [deck, count])
    
    game.do_player()
    game.do_dealer()

    print(game.player.cards)
    print(game.player.value)
    print(game.dealer.cards)
    print(game.dealer.value)

hit_script("20", "2", 0)