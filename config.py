import math

import numpy as np
import pygame

# window settings
fullscreen = False
# fullscreen resolution can only be known after initializing the screen
if not fullscreen:
    resolution = np.array([1000, 500])
window_caption = "Pool"
fps_limit = 60
