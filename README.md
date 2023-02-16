# TranslateMe-backend

TranslateMe-backend is the part of an IOS application that translates manga in place.


# Description

The backend uses Google Cloud Vision API to locate text on manga images and store the text and bounding boxes coordinates. From there the pillow library is used to cover old text based on the area of the bounding box. The text is passed into the Google Translate API and the language is based on the user's selection. Once the image has been processed it is sent to Firebase Storage. 

# Dependencies 
TranslateMe-Backend relies on:

Pillow library

Google Firebase 
* Firestore Database
* Storage


Google Cloud Vision Api

Google Translate API


# Getting Started

# Google Cloud Vision API

To use the Google Cloud vision API, you need to create a service account. Steps for this can be found in the Cloud Vision API documentation guides. Next, you will create a service account key that is a JSON file. The JSON file will be loaded in the root directory. You will also need to install Google Cloud into the python environment to use the API.


# Google Translate API

You need to set up a project and enable the Cloud Translation API. They will ask for billing information, though Google provides a $300 credit to use the API. Next, you need to create a service account and download the service key. Once downloaded, place the JSON file at the root directory and set the environment variable to the file path. 

# Google Firebase

1. Create an iOS app and select Firestore Database and Storage.
2. Follow the specific configurations necessary for both, as detailed in Firebase.
3. Save a GoogleService.plist file into the project root directory as it is a mandatory requirement to connect the app to Firebase.
4. Hide the GoogleService.plist in .gitignore as it is unique to your project.
5. Add the Firebase SDK to your project.
6. Begin working with Firebase.
