import re
from string import digits


def get_percent(s):
    '''
    info:
        -string is like with elements separated by space
        -some of them may contain percent value
        -get first value which occurs
        -if any found, set value to 0
    '''
    percent_value = ''
    possible_percent = [item for item in s.split() if '%' in item]
    if possible_percent:
        first_element = possible_percent[0]
        values = re.findall(r'\d+', first_element)
        if values:
            percent_value = str(values[0])
            
    return percent_value
    
    
def get_unit_val(s, mode=''):
    '''
    info:
        -it extracts elements values from left side
        -values are parsed with coma's
        -value out (if occurs) is replace from digit to coma
        -you can modify prefix_char, unit_char, last_char and prefix_values for your needs
        
    possible mode(s):
        < v >      -extract value (without prefix and unit)
        < p >      -extract prefix
        < u >      -extract unit
        < r >      -extract rest (prefix and unit)
        < m >      -extract value multiplied by prefix
        < f >      -extract value with unit and prefix
    '''
    
    prefix_char = [
        'M',        # Mega
        'k',        # kilo
        'µ',        # mikro
        'n',        # nano
        'p',        # piko
        ]
        
    unit_char = [
        'F',        # Farad
        'H',        # Henr
        # '',         # Resistor
        ]
        
    last_char = [
        'F',        # Farad
        'H',        # Henr
        'k',        # kilo
        'M',        # Mega
        ]
        
    prefix_values = {
        'M': 10**(6),
        'k': 10**(3),
        '': 1,
        'µ': 10**(-6),
        'n': 10**(-9),
        'p': 10**(-12),
        }        
        
        
    if not mode:
        mode = '-f'
        
    out = ''        # if somethins wrong, return empty string
    for character in last_char:
        index = s.find(character)
        if index > 0:
            possible = s[:index+1]
            if s.startswith(possible):
                if len(possible.split()) > 1:
                    # possible contain white char
                    break
                    
                # ******** full ********
                full = possible        # value with unit and prefix
                
                if mode == 'f':
                    out = full
                    break
                    
                    
                # ******** value ********
                value = re.findall(r'\d*\,\d+|\d+', full)[0]       # with coma's
                
                if mode == 'v':
                    out = value
                    break
                    
                    
                # ******** rest ********
                rest = full.replace(value, '')
                
                if mode == 'r':
                    out = rest
                    break
                    
                    
                # ******** prefix ********
                prefix = ''
                for p in prefix_char:
                    if rest.startswith(p):
                        prefix = p
                        break
                        
                if mode == 'p':
                    out = prefix
                    break
                    
                    
                # ******** unit ********
                unit = rest.replace(prefix, '')
                if not unit in unit_char:
                    unit = 'R'      # Resistor
                    
                if mode == 'u':
                    out = unit
                    break
                    
                    
                # ******** multiplied ********
                multiplied = float(value.replace(',', '.'))*prefix_values[prefix]
                multiplied = str(multiplied).replace('.', ',')  # go back to coma's
                
                if mode == 'm':
                    out = multiplied
                    break
    return out
    
    
def percent_example():
    '''get first percent value from given string'''
    s = 'some +-10% stuff +-50%'
    val = get_percent(s)
    
    print('str: {}\nvalue: {}'.format(s, val))
    return None
    
    
def unit_val_example():
    '''get value of element, like resistor, capacitor or coil'''
    thing = [
        '10µF some',
        '10pF some',
        '10k Resistor',
        '50 this is not the proper value',
        '5,2M',
        '2,4k',
        '10µH',
        '2,2k some text',
        '10µH',
        '23,2H',
        '23132 this is text',
        '1,2nF',
        '50nF',
        ]
        
    print(thing)
    print()
    
    modes = list('vpurmf')
    for mode in modes:
        out = [get_unit_val(line, mode=mode) for line in thing]
        print('{} --> {}'.format(mode, out))
        
    return None
    
    
if __name__ == "__main__":
    percent_example()
    unit_val_example()
