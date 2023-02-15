from PIL import ImageDraw, ImageFont
from cgitb import text
from tkinter import font 
import math

def break_line(words_in_row, row):
    if row + 1 > words_in_row:
        return True
    return False

def find_word_count_in_row(text, text_size, x_area):

    text_count = len(text)

    if x_area < 0:
        x_area = x_area * -1

    letters_per_row = math.ceil(x_area / (math.ceil(text_size[0] /text_count)))
    return letters_per_row

def size(row_dict, text_size):
    
    font = ImageFont.truetype("Arial Unicode.ttf", text_size)

    get_font_size = font.getsize(text=row_dict.get('translated'))

    
    
    words_per_row = find_word_count_in_row(
        text=row_dict.get('translated'),
        text_size=get_font_size,
        x_area=row_dict.get('box_size')[0]
    )

    return (words_per_row, font, get_font_size)


def change_font_size(row_dict):

    fonts = [12, 16, 20, 24]
    text_size = len(row_dict.get('translated'))
    
    font_proportions = [size(row_dict=row_dict, text_size=font) for font in fonts]
    

    default = font_proportions[0]

    for idx, props in enumerate(font_proportions):
        words, fonts, font_size = props


        if (math.ceil(text_size / words) * (font_size[1] + 5) >= row_dict.get('box_size')[1]):
            return (words, fonts, font_size)
        else:
            default = font_proportions[idx]

    return default

def row_with_slashes(row_dict):

    rows = []

    words_in_row, font, font_size = change_font_size(row_dict=row_dict)

    idx = 0
    cur_row = ''

    for index, letter in enumerate(row_dict.get('translated')):
        phrase_len = len(row_dict.get('translated'))
        idx += 1
        needs_slash = break_line(words_in_row=words_in_row, row=idx)

        if needs_slash is not True:
            cur_row += letter
        elif needs_slash is True:
            idx = 0
        
            if (row_dict.get('translated')[index] != ' ' and index < phrase_len - 1 and row_dict.get('translated')[index + 1] != ' '):
                cur_row += letter + '-'
            else:
                cur_row += letter
            rows.append(cur_row)
            cur_row = ''
    
        if index == len(row_dict.get('translated')) - 1:
            rows.append(cur_row)

    return (rows, (font, font_size))

def fit_text(row_dict, canvas):

    
    rows, font_properties = row_with_slashes(row_dict=row_dict)

    font, font_size = font_properties

    print(font)


    color = 0 if row_dict.get('font_color') >= 255 / 2 else 255

    x, y = row_dict.get('area')[0]

    shift_y = 0

    for row in rows:
        if len(row) - 1 > 0 and row[0] == ' ':
            row = row[1:]
        
        canvas.text((x - 1, shift_y + y), row, fill=color, font=font)
        shift_y += font_size[1] + 5









