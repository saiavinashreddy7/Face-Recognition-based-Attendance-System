import webview
import threading
import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


def initialize_kommunicate():
    kommunicate_settings = {
        "appId": "22ec24a3bc307d9f358a809ee4c263338",
        "popupWidget": True,
        "automaticChatOpenOnNavigation": True
    }
    
    url = "https://widget.kommunicate.io/v2/kommunicate.app"
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=kommunicate_settings, headers=headers)
    
    if response.status_code == 200:
        print("Kommunicate initialized successfully.")
    else:
        print("Error initializing Kommunicate. Status code:", response.status_code)

def create_chatbot_window():
    initialize_kommunicate()
    webview.create_window("My Chatbot", "https://widget.kommunicate.io")

if __name__ == "__main__":
    create_chatbot_window()
    webview.start()

    # Start the webview in a separate thread to prevent blocking the Tkinter main loop
    threading.Thread(target=create_chatbot_window).start()
