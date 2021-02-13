import itertools
from termcolor import colored


def generate_combinations(full=False):
	'''generate colors combinations'''
	text_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
	text_highlights = ['on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white']
	text_attributes = [None]
	if full:
		text_attributes = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']
	combinations = list(itertools.product(text_colors, text_highlights, text_attributes))
	combinations.insert(0, ('TEXT', 'HIGHLIGHT', 'ATTRIBUTE'))
	return combinations
	
	
def iter_colors(combinations, divided=True, covered=True):
	'''print colors and text of combined elements'''
	for key, item in enumerate(combinations):
		text_color, text_highlight, text_attribute = item
		centered = [str(element).center(12) for element in item]
		
		if covered:
			text_left = ''
			text_right = '{:03}. {}|{}|{}'.format(key, *centered)
		else:
			text_left = '{:03} |{}|{}|{}|'.format(key, *centered)
			text_right = '[ LOREM IPSUM ]'
			
		if text_attribute:
			text_attribute = [text_attribute]
			
		if key:
			print(text_left + colored(text_right, text_color, text_highlight, text_attribute))
		else:
			print(text_left + text_right)	# header
			
		if divided:
			print('-'*len(text_left + text_right))
	return None
	
	
if __name__ == "__main__":
	combinations = generate_combinations(full=False)		# 49/294 combinations
	iter_colors(combinations, divided=True, covered=False)
	
	
'''
Help on function colored in module termcolor:

colored(text, color=None, on_color=None, attrs=None)
	Colorize text.
	
	Available text colors:
		red, green, yellow, blue, magenta, cyan, white.
	
	Available text highlights:
		on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.
	
	Available attributes:
		bold, dark, underline, blink, reverse, concealed.
	
	Example:
		colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink'])
		colored('Hello, World!', 'green')
'''
