import os
from flask import Flask, request, jsonify, make_response, Blueprint
import numpy as np
import firebase_admin
from firebase_admin import firestore, storage
from PIL import Image
from io import BytesIO
import io 
from find_box import processed_image


fire_bp = Blueprint("images", __name__, url_prefix="/images")

cred = firebase_admin.credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "storageBucket": "translateme-4f1db.appspot.com",
})



db = firestore.client()

images_ref = db.collection("images")

# bucket = storage.bucket("translateme-4f1db.appspot.com")


def validate_docs(doc):
    query = images_ref.document(doc)

    document = query.get()

    if document.exists:
        return document
    else:
        return None


def resize_images(bytes):

    img = Image.open(io.BytesIO(bytes))

    if max(img.size) > 65500:
        scale = 65500 / max(img.size)
        img = img.resize((int(img.size[0] * scale), int(img.size[1] * scale)))

    return np.array(img)

@fire_bp.route('/<doc>', methods=["PATCH"])
def update_new_url(doc):

    doc_ref = db.collection("images").document(doc)
    doc_name = validate_docs(doc) 
    lang = doc_name.get("language")
    bucket = storage.bucket()
    image_url = doc_name.get("image_name") + ".jpg"
    Blob = bucket.blob(f"images/{image_url}")

    open_image = Blob.download_as_string()
    with open("temp.jpg", "wb") as f:
        f.write(open_image)

    processed_image("temp.jpg", lang)

    new_image_url = "new_" + image_url
    new_blob = bucket.blob("images/" + new_image_url)

    
    new_blob.upload_from_filename("new_result.png")


    doc_ref.update({"new_URL": new_image_url})
    Blob.delete()
    new_blob.make_public()

    return make_response(jsonify({"new_URL": new_image_url}), 200)


# @fire_bp.route("images/<doc>", methods=["DELETE"])
# def clean_storage(doc):

#     doc_name = validate_docs(doc)
#     image_url = doc_name.get("image_name") + ".jpg"

#     # blob = bucket.blog(image_url)

#     # blob.delete()

#     return jsonify({"details": "Image has been deleted"})




