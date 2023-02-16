# TranslateMe-backend

TranslateMe-backend is the part of an IOS application that translates manga in place.

![alt text](https://github.com/Alaere00/TranslateMe-backend/tree/main/test_images/060.jpg)

# Description

The backend uses Google Cloud Vision API to locate text on manga images and store the text and bounding boxes coordinates. From there the pillow library is used to cover old text based on the area of the bounding box. The text is passed into the Google Translate API and the language is based on the user's selection. Once the image has been processed it is sent to Firebase Storage. 

# Dependencies 
TranslateMe-Backend relies on:

Pillow library
Google Cloud Vision Api
Google Translate Api 
Google Firebase 
* Firestore Database
* Storage



# Getting Started

# Google Cloud Vision API

Users will need to create a google cloud account and create 

# Google Translate API

# Google Firebase

1. Create an iOS app and select Firestore Database and Storage.
2. Follow the specific configurations necessary for both, as detailed in Firebase.
3. Save a GoogleService.plist file into the project root directory as it is a mandatory requirement to connect the app to Firebase.
4. Hide the GoogleService.plist in .gitignore as it is unique to your project.
5. Add the Firebase SDK to your project.
6. Begin working with Firebase.
