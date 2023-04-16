import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np
from enum import IntEnum
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from google.protobuf.json_format import MessageToDict
import screen_brightness_control as sbcontrol
import subprocess
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase,WebRtcMode, RTCConfiguration
import av
import threading

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)