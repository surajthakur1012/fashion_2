import streamlit as st
import os
from PIL import Image
import numpy as np


import pickle


filenames = pickle.load(open("filenames.pkl", "rb"))


st.image("fashion-recommender-system-main\images\\7563.jpg")
