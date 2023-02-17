import os
import io
from google.cloud import vision
from google.cloud.vision_v1 import types
from google.cloud import translate_v2 as translate
from PIL import Image, ImageDraw 
from text_placements import fit_text

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ServiceAccountToken.json"

translate_client = translate.Client()

def translate_to(target):

    language_key = {
        "Arabic" : "ar",
        "Chinese": "zh-CN",
        "English": "en",
        "German": "de",
        "Indonesian": "id",
        "Japanese": "ja",
        "Korean": "ko",
        "Russian": "ru",
        "Spanish": "es"
    }

    try:
        for lang in language_key:
            if lang == target:
                return language_key[lang]
    except TypeError:
        print("Input generates error")


def detect_text(path):
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image_bytes = types.Image(content=content)
    image = Image.open(io.BytesIO(content)).convert('L')
    canvas = ImageDraw.Draw(image)

    response = client.text_detection(image=image_bytes)

    texts = response.full_text_annotation

    text_boxes = []

    for block in texts.pages[0].blocks:
        
        text = ''
        pos = block.bounding_box.vertices
        pos1 = (pos[0].x - 5, pos[0].y - 3)
        pos2 = (pos[2].x + 5, pos[2].y + 5)


        canvas.rectangle([pos1, pos2], fill=image.getpixel((pos1[0] + 10, pos1[1] - 5)))

        for pg in block.paragraphs:
            for word in pg.words:
                for sym in word.symbols:
                    text += str(sym.text)
                text += ' '

        
        text_boxes.append({
            "text": text,
            "font_color": image.getpixel((pos1[0] + 10, pos1[1] - 5)),
            "area": (
                (pos[0].x - 5, pos[0].y),
                (pos[2].x - 5, pos[2].y)
            ),
            "box_size": (
                pos[2].x - pos[0].x,
                pos[2].y - pos[0].y
            )
        })

    
    return (image, text_boxes)


def processed_image(path, language):

    translations = []

    response = detect_text(path)

    target = translate_to(language)

    for block in response[1]:
        translations.append({
            "font_color": block.get("font_color"),
            "translated": translate_client.translate(block.get('text', ''), target_language=target)["translatedText"],
            "area": block.get('area'),
            "box_size": block.get('box_size')
        })

    img = response[0]

    canvas = ImageDraw.Draw(img)

    for dicts in translations:
        rows = fit_text(row_dict=dicts, canvas=canvas)

    img.save('new_result.png', 'png')


# print(processed_image("test_images/060.jpg", "Chinese"))