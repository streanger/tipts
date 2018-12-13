''' simple wrapper for google tesseract '''

import sys
import os
import codecs
from PIL import Image
import subprocess
import numpy
import cv2


import PyPDF2
from fpdf import FPDF
import math

import json
import time
import unicodedata

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
def simple_read(file):
    ''' simple_read data from specified file '''
    with codecs.open(file, "r", encoding="ascii", errors='ignore') as f:
        content = f.read()
    return content
    
def simple_write(file, str_content):
    '''simple_write data to .txt file, with specified strContent'''
    with open(file, "a", encoding="utf-8") as f:
        f.write(str_content + "\n")
        f.close()
    return True
    
def text_from_image(filename):
    outfile = "temp"
    lang = "pol"        # eng
    begin = time.time()
    tesseractPath = 'D:\\Programy\\Tesseract-OCR\\tesseract.exe'
    
    commands = [tesseractPath, filename, outfile, '-l', lang, 'txt']
    response = subprocess.getoutput(commands)
    text = simple_read(outfile + ".txt")
    elapsed = round(time.time() - begin, 2)
    return text, elapsed
    
def show_image(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def split_image_vertically(img):
    ySize, xSize = img.shape
    center = xSize//2
    left = img[:, :center]
    right = img[:, center:]
    return left, right
    
def resize_image(image, newSize=100):
    height = round((image.shape[0])*(newSize/100))
    width = round((image.shape[1])*(newSize/100))
    resized = cv2.resize(image, (width, height))
    return resized
    
def unicode_normalize(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
    
def write_to_pdf(dictio, out):
    pdf = FPDF()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', True)
    for key, text in dictio.items():
        text = '\n'.join(text.split('\n')[:-1])
        pdf.add_page()
        pdf.set_xy(10, 20)
        # pdf.set_font('arial', 'B', 11)
        pdf.set_font('DejaVu', size=10)

        # single cell
        # for line in text.split('\n'):
            # pdf.cell(0, 5, line, border=0, ln=1)
            
        # or multi_cell
        pdf.multi_cell(w = 180.0, h = 7.0, txt = text, border = 0, align = 'J', fill = False)
        # fpdf.multi_cell(w: float, h: float, txt: str, border = 0, align: str = 'J', fill: bool = False)
        
    pdf.output(out, 'F')
    return True
    

    
def read_json_to_dict(file):
    with open(file, "r", encoding="utf-8", errors='ignore') as f:
        data = json.load(f)
    return data
    
    
if __name__ == '__main__':
    path = script_path()
    
    # list images
    # split it two two and iter one by one
    # extract text from each page and save it to dictio like -> {"124": "this is very text", "125": "this is very text"}
    # format text in every page with proper way, and try to justify it
    # save pages to pdf out with current formatting and page number    
    
    # pdf pages range -> 65-70
    # convert it to proper real pages -> 124 - 135    
    
    
    
    #**************** split pages & save them ****************
    images = [item for item in os.listdir() if item.endswith(".png")][:6]       # do not read single images again
    pages = {str(124 + key*2) + '-' + str(124 + key*2 + 1): image for key, image in enumerate(images)}
    if False:
        for key, page in pages.items():
            img = cv2.imread(page, 0)
            left, right = split_image_vertically(img)
            leftName, rightName = key.split('-')
            leftName += ".png"
            rightName += ".png"
            cv2.imwrite(leftName, left)
            cv2.imwrite(rightName, right)
            print(leftName, rightName)
            
            # left = resize_image(left, 25)
            # right = resize_image(right, 25)
            # show_image(key + " left", left)
            # show_image(key + " right", right)
    
    
    
    
    #**************** extract text ****************
    # singleImages = [item + '.png' for item in '-'.join(list(pages.keys())).split('-')]
    # dictio = {page.split('.')[0]: text_from_image(page) for page in singleImages}
    # dictio = {}
    # for page in singleImages:
        # text, elapsed = text_from_image(page)
        # print("{} extracted after {} [s]".format(page, elapsed))
        # dictio[page.split('.')[0]] = text
    
    
    
    
    
    #**************** save in pretty way as json, to take a look ****************
    # dictio = collections.OrderedDict(dictio)
    # with open('data.json', 'w') as fp:
        # json.dump(dictio, fp, sort_keys=True, indent=4)     # save to json
    
    
    
    #**************** save raw data to  raw_pdf.pdf ****************
    dictio = read_json_to_dict('data.json')
    # status = write_to_pdf(dictio, 'raw_pdf.pdf')
    
    
    
    
    #**************** format text in every page ****************
    formatted = {key: item.strip() for key, item in dictio.items()}
    status = write_to_pdf(formatted, 'format_pdf.pdf')


    formatted = {key: '\n'.join([' '.join(part.split('\n')).replace('- ', '') for part in item.split('\n\n')]) for key, item in formatted.items()}
    for key, value in formatted.items():
        title = 2*"\n" + "***"*8 + "> " + key + " <" + "***"*8 + 3*"\n"
        simple_write("file.txt", title + str(value))
    
    
    
    #**************** save fromatted data to  format_pdf.pdf ****************
    status = write_to_pdf(formatted, 'multi_pdf.pdf')
    
    
    
    
    
    
