import PyPDF2
from PIL import Image
import sys
from os import path
import warnings
import os
from fpdf import FPDF
import math
import getopt

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path   
    
def recurse(page, xObject):
    '''extract images from pdf; function copied from stack, and modified'''
    global number
    
    xObject = xObject['/Resources']['/XObject'].getObject()
    for key, obj in enumerate(xObject):
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            try:
                data = xObject[obj].getData()
            except:
                data = xObject[obj]._data
            if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                mode = "RGB"
            else:
                mode = "P"

            imagename = "page_{}".format(str(page).zfill(3))        #3 leading zeros
            # print(page, xObject[obj]['/Filter'])
            if xObject[obj]['/Filter'] == '/FlateDecode':
                img = Image.frombytes(mode, size, data)
                img.save(imagename + ".png")
                number += 1
            elif xObject[obj]['/Filter'] == '/DCTDecode':
                img = open(imagename + ".jpg", "wb")
                img.write(data)
                img.close()
                number += 1
            elif xObject[obj]['/Filter'] == '/JPXDecode':
                img = open(imagename + ".jp2", "wb")
                img.write(data)
                img.close()
                number += 1
        else:
            recurse(page, xObject[obj])
            # pass
    return True
    
def images_to_pdf(pdfName="newPdf.pdf", fitSize=True):
    '''list files(images) from current dir and save it as pdf'''
    files = [file for file in os.listdir() if file.endswith(('.png', '.jpg', '.jpeg', '.jp2'))]
    files.sort()
    
    #make pdf (think about 2 images on 1 page vs 1 img on 1 page)
    pdf = FPDF(orientation="P", unit="mm", format="A4")             #orientation -> L/P, A4 -> 210x297
    for key, image in enumerate(files):
        pdf.add_page()
        # pdf.line(5, 287, 205, 287)
        cover = Image.open(image)
        if fitSize:
            '''auto resize and position setting'''
            width, height = cover.size
            if width/height > 210/297:
                maxFactor = math.trunc((210/width)*10000)/10000
            elif width/height < 210/297:
                maxFactor = math.trunc((297/height)*10000)/10000
            else:
                maxFactor = math.trunc((297/height)*10000)/10000
            # print(maxFactor)
            xMove = math.trunc((210 - width*maxFactor)/2)
            yMove = math.trunc((297 - height*maxFactor)/2)
            pdf.image(image, xMove, yMove, width*maxFactor, height*maxFactor)
        else:
            pdf.image(image, 0, 0, 0, 0)
    pdf.set_display_mode(zoom="fullpage", layout="two")
    pdf.set_creator("streanger")
    pdf.output(pdfName, "F")
    return True

def usage():
    print("> script for extract images from pdf, and vice-versa")
    print("> usage:")
    print("     python script.py <parameters>")
    print("     -e some.pdf         --extract images from specified file")
    print("     -o outFile.pdf      --create pdf from collected images(from current dir)")
    print("     -h                  --this usage help")
    return True
    
def get_opt(argv):
    '''get argv and return final options'''
    warnings.filterwarnings("ignore")       #?
    
    try:
        opts, arg = getopt.getopt(argv, "he:o:")
    except getopt.GetoptError as err:
        print(str(err))
        return False

    fileIn = ""
    fileOut = ""
    
    for opt, arg in opts:
        if opt in "-h":
            usage()
            return False
        elif opt in '-e':
            fileIn = arg
        elif opt in '-o':
            fileOut = arg
    if not opts:
        usage()
        return False
    
    #************** extract images from pdf **************
    if fileIn:
        file = PyPDF2.PdfFileReader(open(fileIn, "rb"))
        pages = file.getNumPages()
        global number
        number = 0
        print("--< reading from file... ({})".format(fileIn))
        for p in range(pages):
            try:
                currentPage = file.getPage(p)
                recurse(p, currentPage)
            except:
                print("failed, page: ", p)
        print('--< %s extracted images'% number)

    #************** save images as pdf **************
    if fileOut:
        print("-> creating pdf in process... ({})".format(fileOut))
        status = images_to_pdf(pdfName=fileOut, fitSize=True)
        if status:
            print("-> pdf saved as: {}".format(fileOut))
        else:
            print("-> failed to save pdf: {}".format(fileOut))
            
    return True
    
    
if __name__ == "__main__":
    path = script_path()
    get_opt(sys.argv[1:])
