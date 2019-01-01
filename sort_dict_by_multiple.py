from collections import OrderedDict
import pprint


def data():
    npc_data = {'f0c28c18fd674217a55fb2eac7e1da1e': {'cross_value': True, 'distance': 59, 'enemy_turn': 'down', 'danger': True},
                'a54a32e871c34c01b804d4921f05e729': {'cross_value': True, 'distance': 999, 'enemy_turn': 'down', 'danger': True}, 
                '094e9132f44f483c9e800eb3db810f3b': {'cross_value': False, 'distance': 99, 'enemy_turn': 'down', 'danger': True}, 
                '03a18aa326204f8b96ddbb60094d873c': {'cross_value': True, 'distance': 199, 'enemy_turn': 'right', 'danger': True}, 
                '2116f26d681c4dc7b749f5f6110f6ec5': {'cross_value': True, 'distance': 999, 'enemy_turn': 'down', 'danger': False}}
    return npc_data
    
    
def sort_npc_data(d):
    out = sorted(d, key=lambda k: (d[k]['cross_value'], d[k]['danger'], 1/abs(d[k]['distance'])), reverse=True)
    sorted_dict = OrderedDict({item:d[item] for item in out})
    return sorted_dict
  
  
if __name__ == "__main__":
    d = data()
    sorted_dict = sort_npc_data(d)
    pprint.pprint(sorted_dict)