# ARIA-The-bot
ARIA-The bot is an AI based assistant that uses voice recognition, language based algorithms and specified voice commands which returns relevant information which is requested by the user. It will help the user to search results on internet using “Google” keyword as well as finds the path in the local system, if that particular file is not available in the local computer then it will automatically redirect this search on internet. 
# Research Paper
We have also publish Research paper of this project 
Link of the Research paper :- https://ieeexplore.ieee.org/document/9753961
# Python Module USED:-
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import wikipedia
import webbrowser
import datetime
