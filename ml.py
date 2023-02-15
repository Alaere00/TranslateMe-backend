# from google.cloud import vision
# from google.cloud import translate_v2 as translate
# import cv2
# import numpy as np 
# from PIL import Image, ImageDraw, ImageFont
# import io
# import textwrap
# import deepl

# import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ServiceAccountToken.json"

# translate_client = translate.Client()

# def translate_to(language):

#     google_code = {
#         "Arabic" : "ar",
#         "Chinese": "zh-CN",
#         "English": "en",
#         "German": "de",
#         "Indonesian": "id",
#         "Japanese": "ja",
#         "Korean": "ko",
#         "Russian": "ru",
#         "Spanish": "es"
#     }

#     try:
#         for lang in google_code:
#             if lang == language:
#                 return google_code[lang]
#     except TypeError:
#         print("Input generate error")

# class Bounds:
#     def __init__(self, v1, v2, v3, v4):
#         self.vertices = [v1, v2, v3, v4]

# def detect_text(path):
    
#     client = vision.ImageAnnotatorClient()

#     with io.open(str(path), 'rb') as image_file:
#         content = image_file.read()

#     image = vision.Image(content=content)

#     response = client.text_detection(image=image)
#     texts = response.text_annotations
    

#     bounds = []
#     texts_list = []
#     for text in texts:
#         texts_list.append(text.description)
#         vertices = [(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices]
#         bounds.append(vertices)
    

#     return bounds, texts_list


# def add_padding(bound, padding):
#     new_bound = []
#     for vertex in bound:
#         x, y = vertex
#         x1 = x - padding
#         y1 = y - padding
#         new_bound.append((x1, y1))
#     return new_bound

# def remove_bounding(image, threshold=0.6):
    
#     bboxes, text_list = detect_text(image)
#     filtered_bboxes = []
#     for bbox in bboxes:
#         x1, y1 = bbox[0]
#         x2, y2 = bbox[2]
#         width = x2 - x1
#         height = y2 - y1
#         area = width * height
#         image_area = 1573 * 1029
#         if area / image_area < threshold:
#             filtered_bboxes.append(bbox)
#     return filtered_bboxes
    
# def clean_image(img):

#     bounds = remove_bounding(img, threshold=.6)

#     image = cv2.imread(img)

    
#     for box in bounds:
#         x = min(x for x, y in box)
#         y = min(y for x, y in box)
#         w = max(x for x, y in box) - x
#         h = max(y for x, y in box) - y

#         x -= 10
#         y -= 10
#         w += 20
#         h += 20

#         center = (int(x + w / 2), int(y + h / 2))
#         axes = (int(w / 2), int(h / 2))

#         cv2.ellipse(image, center, axes, 0, 0, 360, (255, 255, 255), thickness=-1)

#     cv2.imwrite("new_result.jpg", image)

#     return "new_result.jpg"

# # clean_image("060.jpg")

# def add_text(path, language):

#     target = translate_to(language)

#     bboxes, texts_list = detect_text(path)

#     image = clean_image(path)

#     new_path = Image.open(image)
#     img = new_path.convert("RGB")
#     draw = ImageDraw.Draw(img)
#     font = ImageFont.truetype("Arial Unicode.ttf", 16)
    
#     for bbox , text in zip(bboxes, texts_list):
#         translated_text = translate_client.translate(text, target_language=target)
#         x0, y0 = bbox[0]
#         x1, y1 = bbox[2]

#         draw.text((x0, y0), translated_text["translatedText"], fill=(255, 0, 0, 128), font=font)

#         # lines = textwrap.wrap(translated_text["translatedText"], width=x1-x0)
#         # line_height = font.getbbox("hg")[1]
#         # y_text = y0
        
#         # for line in lines:
#         #     width, height = font.getsize(line)
#         #     draw.text((x0, y_text), line, fill=(255, 0, 0, 128), font=font)
#         #     y_text += line_height
    
#     img.save('new_result.jpg', "JPEG", quality=95)

        
    

# add_text("test_images/006.jpg", "Spanish")







