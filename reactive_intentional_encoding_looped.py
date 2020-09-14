#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Tue Sep  1 17:40:13 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'reactive_intentional_encoding_looped'  # from the Builder filename that created this script
expInfo = {'participant': '', 'sex': '001', 'age': '', '': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/alexandradecker/Dropbox/Projects/reactivate/reactive_intentional_encoding_looped.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.992,0.992,0.992], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions_intentional_encoding"
instructions_intentional_encodingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions_text2 = visual.TextStim(win=win, name='instructions_text2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
response = keyboard.Keyboard()
image1 = visual.ImageStim(
    win=win,
    name='image1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image2 = visual.ImageStim(
    win=win,
    name='image2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
J_press_instructions = visual.TextStim(win=win, name='J_press_instructions',
    text='default text',
    font='Helvetica',
    pos=(0.2, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
F_key_instruct = visual.TextStim(win=win, name='F_key_instruct',
    text='default text',
    font='Helvetica',
    pos=[0,0], height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
arrow = visual.ImageStim(
    win=win,
    name='arrow', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.09, 0.09),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
yes_press = visual.TextStim(win=win, name='yes_press',
    text='default text',
    font='Helvetica',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
no_press = visual.TextStim(win=win, name='no_press',
    text='default text',
    font='Helvetica',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image_a = visual.ImageStim(
    win=win,
    name='image_a', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
b_image = visual.ImageStim(
    win=win,
    name='b_image', 
    image='sin', mask=None,
    ori=0, pos=(.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "intructions_post_practice_intentional_encoding"
intructions_post_practice_intentional_encodingClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='Great job! Now that you have a sense of the game, press space to start the real thing!',
    font='helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "real_intentional_encoding"
real_intentional_encodingClock = core.Clock()
image_pair1 = visual.ImageStim(
    win=win,
    name='image_pair1', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_pair2 = visual.ImageStim(
    win=win,
    name='image_pair2', 
    image='sin', mask=None,
    ori=0, pos=(.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instructions_retreival_testing1"
instructions_retreival_testing1Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instructions_retreival_testing"
instructions_retreival_testingClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
K = visual.TextStim(win=win, name='K',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
L = visual.TextStim(win=win, name='L',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
J = visual.TextStim(win=win, name='J',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "practice_retrieval_after_encoding"
practice_retrieval_after_encodingClock = core.Clock()
image_a_practice = visual.ImageStim(
    win=win,
    name='image_a_practice', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
afc_test_practice = visual.TextStim(win=win, name='afc_test_practice',
    text='Select the correct image',
    font='Arial',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
location1_practice = visual.ImageStim(
    win=win,
    name='location1_practice', 
    image='sin', mask=None,
    ori=0, pos=(-.5, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
location2_practice = visual.ImageStim(
    win=win,
    name='location2_practice', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
location3_practice = visual.ImageStim(
    win=win,
    name='location3_practice', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
j_key_test_practice = visual.TextStim(win=win, name='j_key_test_practice',
    text='J',
    font='helvetica',
    pos=(-0.5, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
K_key_practice = visual.TextStim(win=win, name='K_key_practice',
    text='K',
    font='Helvetica',
    pos=(0, -.25), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
L_key_practice = visual.TextStim(win=win, name='L_key_practice',
    text='L',
    font='Helvetica',
    pos=(0.5, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None,
    ori=0, pos=(.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
text_7 = visual.TextStim(win=win, name='text_7',
    text='Think of the image pair',
    font='Helvetica',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "post_retrievalpractice_instructions"
post_retrievalpractice_instructionsClock = core.Clock()
post_retreival_practice_intructions = visual.TextStim(win=win, name='post_retreival_practice_intructions',
    text="Great job! Now that you've finished the practice, we'll start the real thing. When you're ready to start the real thing, press space!",
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "test"
testClock = core.Clock()
instruct_text = visual.TextStim(win=win, name='instruct_text',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve = visual.ImageStim(
    win=win,
    name='a_image_retrieve', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
afc_text = visual.TextStim(win=win, name='afc_text',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
j_key_test = visual.TextStim(win=win, name='j_key_test',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
K_key_test = visual.TextStim(win=win, name='K_key_test',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
L_key_test = visual.TextStim(win=win, name='L_key_test',
    text='L',
    font='Helvetica',
    pos=(0.5, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
correct_image_ = visual.ImageStim(
    win=win,
    name='correct_image_', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
correct_image2 = visual.ImageStim(
    win=win,
    name='correct_image2', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
pre_fix_reencode = visual.TextStim(win=win, name='pre_fix_reencode',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
Feedback = visual.TextStim(win=win, name='Feedback',
    text='The correct pairs were',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "pre_intentional_encoding4"
pre_intentional_encoding4Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Great job. Now you will learn more pairs. When you are ready, press the space bar.',
    font='Helvetica',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "intentional_encoding_4"
intentional_encoding_4Clock = core.Clock()
image_pair1_2 = visual.ImageStim(
    win=win,
    name='image_pair1_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_pair2_2 = visual.ImageStim(
    win=win,
    name='image_pair2_2', 
    image='sin', mask=None,
    ori=0, pos=(.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instruct_retrieval4"
instruct_retrieval4Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='Great job. Now your memory for the image pairs will be tested. When you are ready, press start.',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "retrieval4"
retrieval4Clock = core.Clock()
instruct_text_2 = visual.TextStim(win=win, name='instruct_text_2',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve_2 = visual.ImageStim(
    win=win,
    name='a_image_retrieve_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_14 = visual.TextStim(win=win, name='text_14',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
afc_text_2 = visual.TextStim(win=win, name='afc_text_2',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
j_key_test_2 = visual.TextStim(win=win, name='j_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
L_key_test_2 = visual.TextStim(win=win, name='L_key_test_2',
    text='L',
    font='Helvetica',
    pos=(0.5, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
K_key_test_2 = visual.TextStim(win=win, name='K_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
correct_image__2 = visual.ImageStim(
    win=win,
    name='correct_image__2', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
correct_image2_2 = visual.ImageStim(
    win=win,
    name='correct_image2_2', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
pre_fix_reencode_2 = visual.TextStim(win=win, name='pre_fix_reencode_2',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='The correct pairs were',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "pre_intentional_encoding4"
pre_intentional_encoding4Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Great job. Now you will learn more pairs. When you are ready, press the space bar.',
    font='Helvetica',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "intentional_encoding_4"
intentional_encoding_4Clock = core.Clock()
image_pair1_2 = visual.ImageStim(
    win=win,
    name='image_pair1_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_pair2_2 = visual.ImageStim(
    win=win,
    name='image_pair2_2', 
    image='sin', mask=None,
    ori=0, pos=(.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instruct_retrieval4"
instruct_retrieval4Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='Great job. Now your memory for the image pairs will be tested. When you are ready, press start.',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "retrieval4"
retrieval4Clock = core.Clock()
instruct_text_2 = visual.TextStim(win=win, name='instruct_text_2',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve_2 = visual.ImageStim(
    win=win,
    name='a_image_retrieve_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_14 = visual.TextStim(win=win, name='text_14',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
afc_text_2 = visual.TextStim(win=win, name='afc_text_2',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
j_key_test_2 = visual.TextStim(win=win, name='j_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
L_key_test_2 = visual.TextStim(win=win, name='L_key_test_2',
    text='L',
    font='Helvetica',
    pos=(0.5, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
K_key_test_2 = visual.TextStim(win=win, name='K_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
correct_image__2 = visual.ImageStim(
    win=win,
    name='correct_image__2', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
correct_image2_2 = visual.ImageStim(
    win=win,
    name='correct_image2_2', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
pre_fix_reencode_2 = visual.TextStim(win=win, name='pre_fix_reencode_2',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='The correct pairs were',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "pre_intentional_encoding4"
pre_intentional_encoding4Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Great job. Now you will learn more pairs. When you are ready, press the space bar.',
    font='Helvetica',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "intentional_encoding_4"
intentional_encoding_4Clock = core.Clock()
image_pair1_2 = visual.ImageStim(
    win=win,
    name='image_pair1_2', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_pair2_2 = visual.ImageStim(
    win=win,
    name='image_pair2_2', 
    image='sin', mask=None,
    ori=0, pos=(.25, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instruct_retrieval4"
instruct_retrieval4Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='Great job. Now your memory for the image pairs will be tested. When you are ready, press start.',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "retrieval4"
retrieval4Clock = core.Clock()
instruct_text_2 = visual.TextStim(win=win, name='instruct_text_2',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve_2 = visual.ImageStim(
    win=win,
    name='a_image_retrieve_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_14 = visual.TextStim(win=win, name='text_14',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
afc_text_2 = visual.TextStim(win=win, name='afc_text_2',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
j_key_test_2 = visual.TextStim(win=win, name='j_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
L_key_test_2 = visual.TextStim(win=win, name='L_key_test_2',
    text='L',
    font='Helvetica',
    pos=(0.5, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
K_key_test_2 = visual.TextStim(win=win, name='K_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
correct_image__2 = visual.ImageStim(
    win=win,
    name='correct_image__2', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
correct_image2_2 = visual.ImageStim(
    win=win,
    name='correct_image2_2', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
pre_fix_reencode_2 = visual.TextStim(win=win, name='pre_fix_reencode_2',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='The correct pairs were',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "final_ab_retrieval_test_instruct"
final_ab_retrieval_test_instructClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Great job! Now we will test your memory once more for all of the images that you have learned. When you are ready, press space bar to start.',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "retrieval4"
retrieval4Clock = core.Clock()
instruct_text_2 = visual.TextStim(win=win, name='instruct_text_2',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve_2 = visual.ImageStim(
    win=win,
    name='a_image_retrieve_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_14 = visual.TextStim(win=win, name='text_14',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
afc_text_2 = visual.TextStim(win=win, name='afc_text_2',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
j_key_test_2 = visual.TextStim(win=win, name='j_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
L_key_test_2 = visual.TextStim(win=win, name='L_key_test_2',
    text='L',
    font='Helvetica',
    pos=(0.5, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
K_key_test_2 = visual.TextStim(win=win, name='K_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
correct_image__2 = visual.ImageStim(
    win=win,
    name='correct_image__2', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
correct_image2_2 = visual.ImageStim(
    win=win,
    name='correct_image2_2', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
pre_fix_reencode_2 = visual.TextStim(win=win, name='pre_fix_reencode_2',
    text='+',
    font='Helvetica',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='The correct pairs were',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);

# Initialize components for Routine "instructions_intentional_encoding"
instructions_intentional_encodingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions_text2 = visual.TextStim(win=win, name='instructions_text2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
response = keyboard.Keyboard()
image1 = visual.ImageStim(
    win=win,
    name='image1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image2 = visual.ImageStim(
    win=win,
    name='image2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
J_press_instructions = visual.TextStim(win=win, name='J_press_instructions',
    text='default text',
    font='Helvetica',
    pos=(0.2, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
F_key_instruct = visual.TextStim(win=win, name='F_key_instruct',
    text='default text',
    font='Helvetica',
    pos=[0,0], height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
arrow = visual.ImageStim(
    win=win,
    name='arrow', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.09, 0.09),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
yes_press = visual.TextStim(win=win, name='yes_press',
    text='default text',
    font='Helvetica',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
no_press = visual.TextStim(win=win, name='no_press',
    text='default text',
    font='Helvetica',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "sustained_attention_arrows_practice"
sustained_attention_arrows_practiceClock = core.Clock()
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.09, 0.09),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_9 = keyboard.Keyboard()
F_press = visual.TextStim(win=win, name='F_press',
    text='F',
    font='Helvetica',
    pos=(-0.3, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
J_press = visual.TextStim(win=win, name='J_press',
    text='J',
    font='Helvetica',
    pos=(0.3, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
left_press = visual.TextStim(win=win, name='left_press',
    text='left',
    font='Helvetica',
    pos=(-0.3, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
right_press = visual.TextStim(win=win, name='right_press',
    text='right',
    font='Helvetica',
    pos=(0.3, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
fixation_ = visual.ShapeStim(
    win=win, name='fixation_', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "practice_incidental_encoding"
practice_incidental_encodingClock = core.Clock()
incidental_image1_ = visual.ImageStim(
    win=win,
    name='incidental_image1_', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
incidental_image2_ = visual.ImageStim(
    win=win,
    name='incidental_image2_', 
    image='sin', mask=None,
    ori=0, pos=(0.3, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_17 = visual.TextStim(win=win, name='text_17',
    text='Together, do they weigh more than a small dog?',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_10 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instruction_intentional_encoding = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions_intentional_encoding.xlsx', selection='0:8'),
    seed=None, name='instruction_intentional_encoding')
thisExp.addLoop(instruction_intentional_encoding)  # add the loop to the experiment
thisInstruction_intentional_encoding = instruction_intentional_encoding.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction_intentional_encoding.rgb)
if thisInstruction_intentional_encoding != None:
    for paramName in thisInstruction_intentional_encoding:
        exec('{} = thisInstruction_intentional_encoding[paramName]'.format(paramName))

for thisInstruction_intentional_encoding in instruction_intentional_encoding:
    currentLoop = instruction_intentional_encoding
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction_intentional_encoding.rgb)
    if thisInstruction_intentional_encoding != None:
        for paramName in thisInstruction_intentional_encoding:
            exec('{} = thisInstruction_intentional_encoding[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions_intentional_encoding"-------
    # update component parameters for each repeat
    text.setColor('black', colorSpace='rgb')
    text.setPos((position_1x, position_1y))
    text.setText(instructions1)
    text.setFont('Helvetica')
    text.setHeight(0.03)
    instructions_text2.setColor('black', colorSpace='rgb')
    instructions_text2.setPos((position_2x, position_2y))
    instructions_text2.setText(Instructions2)
    instructions_text2.setFont('Helvetica')
    instructions_text2.setHeight(0.03)
    response.keys = []
    response.rt = []
    J_press_instructions.setText(J_key)
    F_key_instruct.setPos((-0.2, -0.2))
    F_key_instruct.setText(K_key)
    arrow.setImage(Image3)
    yes_press.setPos((-0.2, -0.27))
    yes_press.setText(yes_text)
    no_press.setPos((0.2, -0.27))
    no_press.setText(no_text)
    # keep track of which components have finished
    instructions_intentional_encodingComponents = [text, instructions_text2, response, image1, image2, J_press_instructions, F_key_instruct, arrow, yes_press, no_press]
    for thisComponent in instructions_intentional_encodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_intentional_encodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instructions_intentional_encoding"-------
    while continueRoutine:
        # get current time
        t = instructions_intentional_encodingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_intentional_encodingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *instructions_text2* updates
        if instructions_text2.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            instructions_text2.frameNStart = frameN  # exact frame index
            instructions_text2.tStart = t  # local t and not account for scr refresh
            instructions_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text2, 'tStartRefresh')  # time at next scr refresh
            instructions_text2.setAutoDraw(True)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys.name  # just the first key pressed
                    response.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # *image1* updates
        if image1.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            image1.frameNStart = frameN  # exact frame index
            image1.tStart = t  # local t and not account for scr refresh
            image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
            image1.setAutoDraw(True)
        if image1.status == STARTED:  # only update if drawing
            image1.setPos((0.25, 0), log=False)
            image1.setSize((0.3, 0.3), log=False)
            image1.setImage(Image1, log=False)
        
        # *image2* updates
        if image2.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            image2.frameNStart = frameN  # exact frame index
            image2.tStart = t  # local t and not account for scr refresh
            image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
            image2.setAutoDraw(True)
        if image2.status == STARTED:  # only update if drawing
            image2.setPos((-.25, 0), log=False)
            image2.setSize((0.3, 0.3), log=False)
            image2.setImage(Image2, log=False)
        
        # *J_press_instructions* updates
        if J_press_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J_press_instructions.frameNStart = frameN  # exact frame index
            J_press_instructions.tStart = t  # local t and not account for scr refresh
            J_press_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J_press_instructions, 'tStartRefresh')  # time at next scr refresh
            J_press_instructions.setAutoDraw(True)
        
        # *F_key_instruct* updates
        if F_key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F_key_instruct.frameNStart = frameN  # exact frame index
            F_key_instruct.tStart = t  # local t and not account for scr refresh
            F_key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F_key_instruct, 'tStartRefresh')  # time at next scr refresh
            F_key_instruct.setAutoDraw(True)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            arrow.setAutoDraw(True)
        
        # *yes_press* updates
        if yes_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yes_press.frameNStart = frameN  # exact frame index
            yes_press.tStart = t  # local t and not account for scr refresh
            yes_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yes_press, 'tStartRefresh')  # time at next scr refresh
            yes_press.setAutoDraw(True)
        
        # *no_press* updates
        if no_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no_press.frameNStart = frameN  # exact frame index
            no_press.tStart = t  # local t and not account for scr refresh
            no_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no_press, 'tStartRefresh')  # time at next scr refresh
            no_press.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_intentional_encodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_intentional_encoding"-------
    for thisComponent in instructions_intentional_encodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instruction_intentional_encoding.addData('text.started', text.tStartRefresh)
    instruction_intentional_encoding.addData('text.stopped', text.tStopRefresh)
    instruction_intentional_encoding.addData('instructions_text2.started', instructions_text2.tStartRefresh)
    instruction_intentional_encoding.addData('instructions_text2.stopped', instructions_text2.tStopRefresh)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
    instruction_intentional_encoding.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        instruction_intentional_encoding.addData('response.rt', response.rt)
    instruction_intentional_encoding.addData('response.started', response.tStartRefresh)
    instruction_intentional_encoding.addData('response.stopped', response.tStopRefresh)
    instruction_intentional_encoding.addData('image1.started', image1.tStartRefresh)
    instruction_intentional_encoding.addData('image1.stopped', image1.tStopRefresh)
    instruction_intentional_encoding.addData('image2.started', image2.tStartRefresh)
    instruction_intentional_encoding.addData('image2.stopped', image2.tStopRefresh)
    instruction_intentional_encoding.addData('J_press_instructions.started', J_press_instructions.tStartRefresh)
    instruction_intentional_encoding.addData('J_press_instructions.stopped', J_press_instructions.tStopRefresh)
    instruction_intentional_encoding.addData('F_key_instruct.started', F_key_instruct.tStartRefresh)
    instruction_intentional_encoding.addData('F_key_instruct.stopped', F_key_instruct.tStopRefresh)
    instruction_intentional_encoding.addData('arrow.started', arrow.tStartRefresh)
    instruction_intentional_encoding.addData('arrow.stopped', arrow.tStopRefresh)
    instruction_intentional_encoding.addData('yes_press.started', yes_press.tStartRefresh)
    instruction_intentional_encoding.addData('yes_press.stopped', yes_press.tStopRefresh)
    instruction_intentional_encoding.addData('no_press.started', no_press.tStartRefresh)
    instruction_intentional_encoding.addData('no_press.stopped', no_press.tStopRefresh)
    # the Routine "instructions_intentional_encoding" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'instruction_intentional_encoding'


# set up handler to look after randomisation of conditions etc
practice_trials_intentional_encoding = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/practice_intention_encoding.xlsx', selection='0:5'),
    seed=None, name='practice_trials_intentional_encoding')
thisExp.addLoop(practice_trials_intentional_encoding)  # add the loop to the experiment
thisPractice_trials_intentional_encoding = practice_trials_intentional_encoding.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trials_intentional_encoding.rgb)
if thisPractice_trials_intentional_encoding != None:
    for paramName in thisPractice_trials_intentional_encoding:
        exec('{} = thisPractice_trials_intentional_encoding[paramName]'.format(paramName))

for thisPractice_trials_intentional_encoding in practice_trials_intentional_encoding:
    currentLoop = practice_trials_intentional_encoding
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trials_intentional_encoding.rgb)
    if thisPractice_trials_intentional_encoding != None:
        for paramName in thisPractice_trials_intentional_encoding:
            exec('{} = thisPractice_trials_intentional_encoding[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    routineTimer.add(0.100000)
    # update component parameters for each repeat
    b_image.setImage(ImageB)
    # keep track of which components have finished
    trialComponents = [image_a, b_image]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_a* updates
        if image_a.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            image_a.frameNStart = frameN  # exact frame index
            image_a.tStart = t  # local t and not account for scr refresh
            image_a.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_a, 'tStartRefresh')  # time at next scr refresh
            image_a.setAutoDraw(True)
        if image_a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_a.tStartRefresh + .05-frameTolerance:
                # keep track of stop time/frame for later
                image_a.tStop = t  # not accounting for scr refresh
                image_a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_a, 'tStopRefresh')  # time at next scr refresh
                image_a.setAutoDraw(False)
        if image_a.status == STARTED:  # only update if drawing
            image_a.setImage(ImageA, log=False)
        
        # *b_image* updates
        if b_image.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            b_image.frameNStart = frameN  # exact frame index
            b_image.tStart = t  # local t and not account for scr refresh
            b_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_image, 'tStartRefresh')  # time at next scr refresh
            b_image.setAutoDraw(True)
        if b_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_image.tStartRefresh + .05-frameTolerance:
                # keep track of stop time/frame for later
                b_image.tStop = t  # not accounting for scr refresh
                b_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(b_image, 'tStopRefresh')  # time at next scr refresh
                b_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trials_intentional_encoding.addData('image_a.started', image_a.tStartRefresh)
    practice_trials_intentional_encoding.addData('image_a.stopped', image_a.tStopRefresh)
    practice_trials_intentional_encoding.addData('b_image.started', b_image.tStartRefresh)
    practice_trials_intentional_encoding.addData('b_image.stopped', b_image.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'practice_trials_intentional_encoding'


# ------Prepare to start Routine "intructions_post_practice_intentional_encoding"-------
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
intructions_post_practice_intentional_encodingComponents = [text_9, key_resp_3]
for thisComponent in intructions_post_practice_intentional_encodingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intructions_post_practice_intentional_encodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "intructions_post_practice_intentional_encoding"-------
while continueRoutine:
    # get current time
    t = intructions_post_practice_intentional_encodingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intructions_post_practice_intentional_encodingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_3.keys = theseKeys.name  # just the last key pressed
            key_resp_3.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intructions_post_practice_intentional_encodingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intructions_post_practice_intentional_encoding"-------
for thisComponent in intructions_post_practice_intentional_encodingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "intructions_post_practice_intentional_encoding" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/intentional_encoding.xlsx', selection='0:12'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "real_intentional_encoding"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image_pair1.setImage(ImageA)
    image_pair2.setImage(ImageB)
    # keep track of which components have finished
    real_intentional_encodingComponents = [image_pair1, image_pair2]
    for thisComponent in real_intentional_encodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    real_intentional_encodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "real_intentional_encoding"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = real_intentional_encodingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=real_intentional_encodingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_pair1* updates
        if image_pair1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            image_pair1.frameNStart = frameN  # exact frame index
            image_pair1.tStart = t  # local t and not account for scr refresh
            image_pair1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair1, 'tStartRefresh')  # time at next scr refresh
            image_pair1.setAutoDraw(True)
        if image_pair1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair1.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair1.tStop = t  # not accounting for scr refresh
                image_pair1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair1, 'tStopRefresh')  # time at next scr refresh
                image_pair1.setAutoDraw(False)
        
        # *image_pair2* updates
        if image_pair2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            image_pair2.frameNStart = frameN  # exact frame index
            image_pair2.tStart = t  # local t and not account for scr refresh
            image_pair2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair2, 'tStartRefresh')  # time at next scr refresh
            image_pair2.setAutoDraw(True)
        if image_pair2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair2.tStop = t  # not accounting for scr refresh
                image_pair2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair2, 'tStopRefresh')  # time at next scr refresh
                image_pair2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in real_intentional_encodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "real_intentional_encoding"-------
    for thisComponent in real_intentional_encodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image_pair1.started', image_pair1.tStartRefresh)
    trials.addData('image_pair1.stopped', image_pair1.tStopRefresh)
    trials.addData('image_pair2.started', image_pair2.tStartRefresh)
    trials.addData('image_pair2.stopped', image_pair2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions_intentional_encoding.xlsx', selection='8:11'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions_retreival_testing1"-------
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    instructions_retreival_testing1Components = [text_3, text_4, image_3, key_resp]
    for thisComponent in instructions_retreival_testing1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_retreival_testing1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instructions_retreival_testing1"-------
    while continueRoutine:
        # get current time
        t = instructions_retreival_testing1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_retreival_testing1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:  # only update if drawing
            text_3.setColor('black', colorSpace='rgb', log=False)
            text_3.setPos((position_1x, position_1y), log=False)
            text_3.setText(instructions1, log=False)
            text_3.setFont('Helvetica', log=False)
            text_3.setHeight(0.03, log=False)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:  # only update if drawing
            text_4.setColor('black', colorSpace='rgb', log=False)
            text_4.setPos((position_2x, position_2y), log=False)
            text_4.setText(Instructions2, log=False)
            text_4.setFont('Helvetica', log=False)
            text_4.setHeight(0.03, log=False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:  # only update if drawing
            image_3.setOpacity(1, log=False)
            image_3.setPos((0, 0), log=False)
            image_3.setSize((0.3, 0.3), log=False)
            image_3.setOri(0, log=False)
            image_3.setImage(Image1, log=False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_retreival_testing1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_retreival_testing1"-------
    for thisComponent in instructions_retreival_testing1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_4.addData('text_3.started', text_3.tStartRefresh)
    trials_4.addData('text_3.stopped', text_3.tStopRefresh)
    trials_4.addData('text_4.started', text_4.tStartRefresh)
    trials_4.addData('text_4.stopped', text_4.tStopRefresh)
    trials_4.addData('image_3.started', image_3.tStartRefresh)
    trials_4.addData('image_3.stopped', image_3.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_4.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_4.addData('key_resp.rt', key_resp.rt)
    trials_4.addData('key_resp.started', key_resp.tStartRefresh)
    trials_4.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "instructions_retreival_testing1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_4'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions_intentional_encoding.xlsx', selection='11:17'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions_retreival_testing"-------
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    K.setText(K_key)
    L.setText(L_key)
    J.setText(J_key)
    # keep track of which components have finished
    instructions_retreival_testingComponents = [text_5, text_8, key_resp_2, image, image_2, image_5, image_6, K, L, J]
    for thisComponent in instructions_retreival_testingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_retreival_testingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instructions_retreival_testing"-------
    while continueRoutine:
        # get current time
        t = instructions_retreival_testingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_retreival_testingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:  # only update if drawing
            text_5.setColor('black', colorSpace='rgb', log=False)
            text_5.setPos((position_1x, position_1y), log=False)
            text_5.setText(instructions1, log=False)
            text_5.setFont('Helvetica', log=False)
            text_5.setHeight(0.03, log=False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:  # only update if drawing
            text_8.setColor('black', colorSpace='rgb', log=False)
            text_8.setPos((position_2x, position_2y), log=False)
            text_8.setText(Instructions2, log=False)
            text_8.setFont('Helvetica', log=False)
            text_8.setHeight(0.03, log=False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'l'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_2.keys = theseKeys.name  # just the last key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:  # only update if drawing
            image.setOpacity(1, log=False)
            image.setPos((0, 0), log=False)
            image.setSize((0.3, 0.3), log=False)
            image.setOri(0, log=False)
            image.setImage(Image1, log=False)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:  # only update if drawing
            image_2.setOpacity(1, log=False)
            image_2.setPos((0.52, 0), log=False)
            image_2.setSize((0.3, 0.3), log=False)
            image_2.setOri(0, log=False)
            image_2.setImage(Image2, log=False)
        
        # *image_5* updates
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            image_5.setAutoDraw(True)
        if image_5.status == STARTED:  # only update if drawing
            image_5.setOpacity(1, log=False)
            image_5.setPos((0, 0), log=False)
            image_5.setSize((0.3, 0.3), log=False)
            image_5.setOri(0, log=False)
            image_5.setImage(Image3, log=False)
        
        # *image_6* updates
        if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            image_6.setAutoDraw(True)
        if image_6.status == STARTED:  # only update if drawing
            image_6.setOpacity(1, log=False)
            image_6.setPos((-.52, 0), log=False)
            image_6.setSize((0.3, 0.3), log=False)
            image_6.setOri(0, log=False)
            image_6.setImage(Image_4, log=False)
        
        # *K* updates
        if K.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            K.frameNStart = frameN  # exact frame index
            K.tStart = t  # local t and not account for scr refresh
            K.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K, 'tStartRefresh')  # time at next scr refresh
            K.setAutoDraw(True)
        if K.status == STARTED:  # only update if drawing
            K.setColor('black', colorSpace='rgb', log=False)
            K.setPos((0, -.25), log=False)
            K.setFont('Arial', log=False)
            K.setHeight(0.03, log=False)
        
        # *L* updates
        if L.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            L.frameNStart = frameN  # exact frame index
            L.tStart = t  # local t and not account for scr refresh
            L.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L, 'tStartRefresh')  # time at next scr refresh
            L.setAutoDraw(True)
        if L.status == STARTED:  # only update if drawing
            L.setColor('black', colorSpace='rgb', log=False)
            L.setPos((0.5, -.25), log=False)
            L.setFont('Helvetica', log=False)
            L.setHeight(0.03, log=False)
        
        # *J* updates
        if J.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J.frameNStart = frameN  # exact frame index
            J.tStart = t  # local t and not account for scr refresh
            J.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J, 'tStartRefresh')  # time at next scr refresh
            J.setAutoDraw(True)
        if J.status == STARTED:  # only update if drawing
            J.setColor('black', colorSpace='rgb', log=False)
            J.setPos((-0.5, -0.25), log=False)
            J.setFont('Helvetica', log=False)
            J.setHeight(0.03, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_retreival_testingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_retreival_testing"-------
    for thisComponent in instructions_retreival_testingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_5.started', text_5.tStartRefresh)
    trials_2.addData('text_5.stopped', text_5.tStopRefresh)
    trials_2.addData('text_8.started', text_8.tStartRefresh)
    trials_2.addData('text_8.stopped', text_8.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    trials_2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials_2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    trials_2.addData('image.started', image.tStartRefresh)
    trials_2.addData('image.stopped', image.tStopRefresh)
    trials_2.addData('image_2.started', image_2.tStartRefresh)
    trials_2.addData('image_2.stopped', image_2.tStopRefresh)
    trials_2.addData('image_5.started', image_5.tStartRefresh)
    trials_2.addData('image_5.stopped', image_5.tStopRefresh)
    trials_2.addData('image_6.started', image_6.tStartRefresh)
    trials_2.addData('image_6.stopped', image_6.tStopRefresh)
    trials_2.addData('K.started', K.tStartRefresh)
    trials_2.addData('K.stopped', K.tStopRefresh)
    trials_2.addData('L.started', L.tStartRefresh)
    trials_2.addData('L.stopped', L.tStopRefresh)
    trials_2.addData('J.started', J.tStartRefresh)
    trials_2.addData('J.stopped', J.tStopRefresh)
    # the Routine "instructions_retreival_testing" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/test_practice.csv', selection='0:5'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_retrieval_after_encoding"-------
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    image_a_practice.setImage(image_a)
    location1_practice.setImage(location1)
    location2_practice.setImage(location2)
    location3_practice.setImage(location3)
    image_11.setImage(image_a)
    image_12.setImage(correct_image)
    # keep track of which components have finished
    practice_retrieval_after_encodingComponents = [image_a_practice, fixation, afc_test_practice, location1_practice, location2_practice, location3_practice, j_key_test_practice, K_key_practice, L_key_practice, fix, image_11, image_12, text_7]
    for thisComponent in practice_retrieval_after_encodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_retrieval_after_encodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice_retrieval_after_encoding"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_retrieval_after_encodingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_retrieval_after_encodingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_a_practice* updates
        if image_a_practice.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            image_a_practice.frameNStart = frameN  # exact frame index
            image_a_practice.tStart = t  # local t and not account for scr refresh
            image_a_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_a_practice, 'tStartRefresh')  # time at next scr refresh
            image_a_practice.setAutoDraw(True)
        if image_a_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_a_practice.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_a_practice.tStop = t  # not accounting for scr refresh
                image_a_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_a_practice, 'tStopRefresh')  # time at next scr refresh
                image_a_practice.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *afc_test_practice* updates
        if afc_test_practice.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            afc_test_practice.frameNStart = frameN  # exact frame index
            afc_test_practice.tStart = t  # local t and not account for scr refresh
            afc_test_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_test_practice, 'tStartRefresh')  # time at next scr refresh
            afc_test_practice.setAutoDraw(True)
        if afc_test_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_test_practice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                afc_test_practice.tStop = t  # not accounting for scr refresh
                afc_test_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_test_practice, 'tStopRefresh')  # time at next scr refresh
                afc_test_practice.setAutoDraw(False)
        
        # *location1_practice* updates
        if location1_practice.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            location1_practice.frameNStart = frameN  # exact frame index
            location1_practice.tStart = t  # local t and not account for scr refresh
            location1_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(location1_practice, 'tStartRefresh')  # time at next scr refresh
            location1_practice.setAutoDraw(True)
        if location1_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > location1_practice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                location1_practice.tStop = t  # not accounting for scr refresh
                location1_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(location1_practice, 'tStopRefresh')  # time at next scr refresh
                location1_practice.setAutoDraw(False)
        
        # *location2_practice* updates
        if location2_practice.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            location2_practice.frameNStart = frameN  # exact frame index
            location2_practice.tStart = t  # local t and not account for scr refresh
            location2_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(location2_practice, 'tStartRefresh')  # time at next scr refresh
            location2_practice.setAutoDraw(True)
        if location2_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > location2_practice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                location2_practice.tStop = t  # not accounting for scr refresh
                location2_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(location2_practice, 'tStopRefresh')  # time at next scr refresh
                location2_practice.setAutoDraw(False)
        
        # *location3_practice* updates
        if location3_practice.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            location3_practice.frameNStart = frameN  # exact frame index
            location3_practice.tStart = t  # local t and not account for scr refresh
            location3_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(location3_practice, 'tStartRefresh')  # time at next scr refresh
            location3_practice.setAutoDraw(True)
        if location3_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > location3_practice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                location3_practice.tStop = t  # not accounting for scr refresh
                location3_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(location3_practice, 'tStopRefresh')  # time at next scr refresh
                location3_practice.setAutoDraw(False)
        
        # *j_key_test_practice* updates
        if j_key_test_practice.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_practice.frameNStart = frameN  # exact frame index
            j_key_test_practice.tStart = t  # local t and not account for scr refresh
            j_key_test_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_practice, 'tStartRefresh')  # time at next scr refresh
            j_key_test_practice.setAutoDraw(True)
        if j_key_test_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_practice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_practice.tStop = t  # not accounting for scr refresh
                j_key_test_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_practice, 'tStopRefresh')  # time at next scr refresh
                j_key_test_practice.setAutoDraw(False)
        
        # *K_key_practice* updates
        if K_key_practice.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            K_key_practice.frameNStart = frameN  # exact frame index
            K_key_practice.tStart = t  # local t and not account for scr refresh
            K_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_practice, 'tStartRefresh')  # time at next scr refresh
            K_key_practice.setAutoDraw(True)
        if K_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_practice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                K_key_practice.tStop = t  # not accounting for scr refresh
                K_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_practice, 'tStopRefresh')  # time at next scr refresh
                K_key_practice.setAutoDraw(False)
        
        # *L_key_practice* updates
        if L_key_practice.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            L_key_practice.frameNStart = frameN  # exact frame index
            L_key_practice.tStart = t  # local t and not account for scr refresh
            L_key_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_practice, 'tStartRefresh')  # time at next scr refresh
            L_key_practice.setAutoDraw(True)
        if L_key_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_practice.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                L_key_practice.tStop = t  # not accounting for scr refresh
                L_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_practice, 'tStopRefresh')  # time at next scr refresh
                L_key_practice.setAutoDraw(False)
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # *image_11* updates
        if image_11.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            image_11.frameNStart = frameN  # exact frame index
            image_11.tStart = t  # local t and not account for scr refresh
            image_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
            image_11.setAutoDraw(True)
        if image_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_11.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                image_11.tStop = t  # not accounting for scr refresh
                image_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_11, 'tStopRefresh')  # time at next scr refresh
                image_11.setAutoDraw(False)
        
        # *image_12* updates
        if image_12.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            image_12.frameNStart = frameN  # exact frame index
            image_12.tStart = t  # local t and not account for scr refresh
            image_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
            image_12.setAutoDraw(True)
        if image_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_12.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                image_12.tStop = t  # not accounting for scr refresh
                image_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_12, 'tStopRefresh')  # time at next scr refresh
                image_12.setAutoDraw(False)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_retrieval_after_encodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_retrieval_after_encoding"-------
    for thisComponent in practice_retrieval_after_encodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_5.addData('image_a_practice.started', image_a_practice.tStartRefresh)
    trials_5.addData('image_a_practice.stopped', image_a_practice.tStopRefresh)
    trials_5.addData('fixation.started', fixation.tStartRefresh)
    trials_5.addData('fixation.stopped', fixation.tStopRefresh)
    trials_5.addData('afc_test_practice.started', afc_test_practice.tStartRefresh)
    trials_5.addData('afc_test_practice.stopped', afc_test_practice.tStopRefresh)
    trials_5.addData('location1_practice.started', location1_practice.tStartRefresh)
    trials_5.addData('location1_practice.stopped', location1_practice.tStopRefresh)
    trials_5.addData('location2_practice.started', location2_practice.tStartRefresh)
    trials_5.addData('location2_practice.stopped', location2_practice.tStopRefresh)
    trials_5.addData('location3_practice.started', location3_practice.tStartRefresh)
    trials_5.addData('location3_practice.stopped', location3_practice.tStopRefresh)
    trials_5.addData('j_key_test_practice.started', j_key_test_practice.tStartRefresh)
    trials_5.addData('j_key_test_practice.stopped', j_key_test_practice.tStopRefresh)
    trials_5.addData('K_key_practice.started', K_key_practice.tStartRefresh)
    trials_5.addData('K_key_practice.stopped', K_key_practice.tStopRefresh)
    trials_5.addData('L_key_practice.started', L_key_practice.tStartRefresh)
    trials_5.addData('L_key_practice.stopped', L_key_practice.tStopRefresh)
    trials_5.addData('fix.started', fix.tStartRefresh)
    trials_5.addData('fix.stopped', fix.tStopRefresh)
    trials_5.addData('image_11.started', image_11.tStartRefresh)
    trials_5.addData('image_11.stopped', image_11.tStopRefresh)
    trials_5.addData('image_12.started', image_12.tStartRefresh)
    trials_5.addData('image_12.stopped', image_12.tStopRefresh)
    trials_5.addData('text_7.started', text_7.tStartRefresh)
    trials_5.addData('text_7.stopped', text_7.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_5'


# ------Prepare to start Routine "post_retrievalpractice_instructions"-------
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
post_retrievalpractice_instructionsComponents = [post_retreival_practice_intructions, key_resp_4]
for thisComponent in post_retrievalpractice_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
post_retrievalpractice_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "post_retrievalpractice_instructions"-------
while continueRoutine:
    # get current time
    t = post_retrievalpractice_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=post_retrievalpractice_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *post_retreival_practice_intructions* updates
    if post_retreival_practice_intructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        post_retreival_practice_intructions.frameNStart = frameN  # exact frame index
        post_retreival_practice_intructions.tStart = t  # local t and not account for scr refresh
        post_retreival_practice_intructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(post_retreival_practice_intructions, 'tStartRefresh')  # time at next scr refresh
        post_retreival_practice_intructions.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_4.keys = theseKeys.name  # just the last key pressed
            key_resp_4.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in post_retrievalpractice_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "post_retrievalpractice_instructions"-------
for thisComponent in post_retrievalpractice_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('post_retreival_practice_intructions.started', post_retreival_practice_intructions.tStartRefresh)
thisExp.addData('post_retreival_practice_intructions.stopped', post_retreival_practice_intructions.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "post_retrievalpractice_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/test.csv', selection='0:12'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "test"-------
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    j_key_test.setColor('black', colorSpace='rgb')
    j_key_test.setPos((-0.5, -0.25))
    j_key_test.setFont('Helvetica')
    j_key_test.setHeight(0.03)
    K_key_test.setColor('black', colorSpace='rgb')
    K_key_test.setPos((0, -.25))
    K_key_test.setText('K')
    K_key_test.setFont('Helvetica')
    K_key_test.setHeight(0.03)
    correct_image_.setImage(correct_image)
    correct_image2.setImage(image_a)
    # keep track of which components have finished
    testComponents = [instruct_text, a_image_retrieve, text_2, afc_text, image_4, image_9, image_10, j_key_test, K_key_test, L_key_test, correct_image_, correct_image2, pre_fix_reencode, Feedback]
    for thisComponent in testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text* updates
        if instruct_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            instruct_text.frameNStart = frameN  # exact frame index
            instruct_text.tStart = t  # local t and not account for scr refresh
            instruct_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text, 'tStartRefresh')  # time at next scr refresh
            instruct_text.setAutoDraw(True)
        if instruct_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text.tStop = t  # not accounting for scr refresh
                instruct_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text, 'tStopRefresh')  # time at next scr refresh
                instruct_text.setAutoDraw(False)
        
        # *a_image_retrieve* updates
        if a_image_retrieve.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve.frameNStart = frameN  # exact frame index
            a_image_retrieve.tStart = t  # local t and not account for scr refresh
            a_image_retrieve.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve.setAutoDraw(True)
        if a_image_retrieve.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve.tStop = t  # not accounting for scr refresh
                a_image_retrieve.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve.setAutoDraw(False)
        if a_image_retrieve.status == STARTED:  # only update if drawing
            a_image_retrieve.setImage(image_a, log=False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *afc_text* updates
        if afc_text.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            afc_text.frameNStart = frameN  # exact frame index
            afc_text.tStart = t  # local t and not account for scr refresh
            afc_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text, 'tStartRefresh')  # time at next scr refresh
            afc_text.setAutoDraw(True)
        if afc_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                afc_text.tStop = t  # not accounting for scr refresh
                afc_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text, 'tStopRefresh')  # time at next scr refresh
                afc_text.setAutoDraw(False)
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            image_4.setAutoDraw(True)
        if image_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_4.tStop = t  # not accounting for scr refresh
                image_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                image_4.setAutoDraw(False)
        if image_4.status == STARTED:  # only update if drawing
            image_4.setPos((-.5, 0), log=False)
            image_4.setImage(location1, log=False)
        
        # *image_9* updates
        if image_9.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_9.frameNStart = frameN  # exact frame index
            image_9.tStart = t  # local t and not account for scr refresh
            image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
            image_9.setAutoDraw(True)
        if image_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_9.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_9.tStop = t  # not accounting for scr refresh
                image_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_9, 'tStopRefresh')  # time at next scr refresh
                image_9.setAutoDraw(False)
        if image_9.status == STARTED:  # only update if drawing
            image_9.setPos((0, 0), log=False)
            image_9.setImage(location2, log=False)
        
        # *image_10* updates
        if image_10.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_10.frameNStart = frameN  # exact frame index
            image_10.tStart = t  # local t and not account for scr refresh
            image_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
            image_10.setAutoDraw(True)
        if image_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_10.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_10.tStop = t  # not accounting for scr refresh
                image_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_10, 'tStopRefresh')  # time at next scr refresh
                image_10.setAutoDraw(False)
        if image_10.status == STARTED:  # only update if drawing
            image_10.setPos((0.5, 0), log=False)
            image_10.setImage(location3, log=False)
        
        # *j_key_test* updates
        if j_key_test.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            j_key_test.frameNStart = frameN  # exact frame index
            j_key_test.tStart = t  # local t and not account for scr refresh
            j_key_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test, 'tStartRefresh')  # time at next scr refresh
            j_key_test.setAutoDraw(True)
        if j_key_test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test.tStop = t  # not accounting for scr refresh
                j_key_test.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test, 'tStopRefresh')  # time at next scr refresh
                j_key_test.setAutoDraw(False)
        if j_key_test.status == STARTED:  # only update if drawing
            j_key_test.setText('J', log=False)
        
        # *K_key_test* updates
        if K_key_test.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            K_key_test.frameNStart = frameN  # exact frame index
            K_key_test.tStart = t  # local t and not account for scr refresh
            K_key_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test, 'tStartRefresh')  # time at next scr refresh
            K_key_test.setAutoDraw(True)
        if K_key_test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test.tStop = t  # not accounting for scr refresh
                K_key_test.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test, 'tStopRefresh')  # time at next scr refresh
                K_key_test.setAutoDraw(False)
        
        # *L_key_test* updates
        if L_key_test.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            L_key_test.frameNStart = frameN  # exact frame index
            L_key_test.tStart = t  # local t and not account for scr refresh
            L_key_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test, 'tStartRefresh')  # time at next scr refresh
            L_key_test.setAutoDraw(True)
        if L_key_test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test.tStop = t  # not accounting for scr refresh
                L_key_test.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test, 'tStopRefresh')  # time at next scr refresh
                L_key_test.setAutoDraw(False)
        
        # *correct_image_* updates
        if correct_image_.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image_.frameNStart = frameN  # exact frame index
            correct_image_.tStart = t  # local t and not account for scr refresh
            correct_image_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image_, 'tStartRefresh')  # time at next scr refresh
            correct_image_.setAutoDraw(True)
        if correct_image_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image_.tStop = t  # not accounting for scr refresh
                correct_image_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image_, 'tStopRefresh')  # time at next scr refresh
                correct_image_.setAutoDraw(False)
        
        # *correct_image2* updates
        if correct_image2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image2.frameNStart = frameN  # exact frame index
            correct_image2.tStart = t  # local t and not account for scr refresh
            correct_image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image2, 'tStartRefresh')  # time at next scr refresh
            correct_image2.setAutoDraw(True)
        if correct_image2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image2.tStop = t  # not accounting for scr refresh
                correct_image2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image2, 'tStopRefresh')  # time at next scr refresh
                correct_image2.setAutoDraw(False)
        
        # *pre_fix_reencode* updates
        if pre_fix_reencode.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            pre_fix_reencode.frameNStart = frameN  # exact frame index
            pre_fix_reencode.tStart = t  # local t and not account for scr refresh
            pre_fix_reencode.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_fix_reencode, 'tStartRefresh')  # time at next scr refresh
            pre_fix_reencode.setAutoDraw(True)
        if pre_fix_reencode.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_fix_reencode.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                pre_fix_reencode.tStop = t  # not accounting for scr refresh
                pre_fix_reencode.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pre_fix_reencode, 'tStopRefresh')  # time at next scr refresh
                pre_fix_reencode.setAutoDraw(False)
        
        # *Feedback* updates
        if Feedback.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            Feedback.frameNStart = frameN  # exact frame index
            Feedback.tStart = t  # local t and not account for scr refresh
            Feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
            Feedback.setAutoDraw(True)
        if Feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feedback.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Feedback.tStop = t  # not accounting for scr refresh
                Feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Feedback, 'tStopRefresh')  # time at next scr refresh
                Feedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('instruct_text.started', instruct_text.tStartRefresh)
    trials_3.addData('instruct_text.stopped', instruct_text.tStopRefresh)
    trials_3.addData('a_image_retrieve.started', a_image_retrieve.tStartRefresh)
    trials_3.addData('a_image_retrieve.stopped', a_image_retrieve.tStopRefresh)
    trials_3.addData('text_2.started', text_2.tStartRefresh)
    trials_3.addData('text_2.stopped', text_2.tStopRefresh)
    trials_3.addData('afc_text.started', afc_text.tStartRefresh)
    trials_3.addData('afc_text.stopped', afc_text.tStopRefresh)
    trials_3.addData('image_4.started', image_4.tStartRefresh)
    trials_3.addData('image_4.stopped', image_4.tStopRefresh)
    trials_3.addData('image_9.started', image_9.tStartRefresh)
    trials_3.addData('image_9.stopped', image_9.tStopRefresh)
    trials_3.addData('image_10.started', image_10.tStartRefresh)
    trials_3.addData('image_10.stopped', image_10.tStopRefresh)
    trials_3.addData('j_key_test.started', j_key_test.tStartRefresh)
    trials_3.addData('j_key_test.stopped', j_key_test.tStopRefresh)
    trials_3.addData('K_key_test.started', K_key_test.tStartRefresh)
    trials_3.addData('K_key_test.stopped', K_key_test.tStopRefresh)
    trials_3.addData('L_key_test.started', L_key_test.tStartRefresh)
    trials_3.addData('L_key_test.stopped', L_key_test.tStopRefresh)
    trials_3.addData('correct_image_.started', correct_image_.tStartRefresh)
    trials_3.addData('correct_image_.stopped', correct_image_.tStopRefresh)
    trials_3.addData('correct_image2.started', correct_image2.tStartRefresh)
    trials_3.addData('correct_image2.stopped', correct_image2.tStopRefresh)
    trials_3.addData('pre_fix_reencode.started', pre_fix_reencode.tStartRefresh)
    trials_3.addData('pre_fix_reencode.stopped', pre_fix_reencode.tStopRefresh)
    trials_3.addData('Feedback.started', Feedback.tStartRefresh)
    trials_3.addData('Feedback.stopped', Feedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_3'


# ------Prepare to start Routine "pre_intentional_encoding4"-------
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
# keep track of which components have finished
pre_intentional_encoding4Components = [text_12, key_resp_6]
for thisComponent in pre_intentional_encoding4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pre_intentional_encoding4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "pre_intentional_encoding4"-------
while continueRoutine:
    # get current time
    t = pre_intentional_encoding4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pre_intentional_encoding4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.04-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_intentional_encoding4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pre_intentional_encoding4"-------
for thisComponent in pre_intentional_encoding4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "pre_intentional_encoding4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/intentional_encoding.xlsx', selection='12:24'),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intentional_encoding_4"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image_pair1_2.setImage(ImageA)
    image_pair2_2.setImage(ImageB)
    # keep track of which components have finished
    intentional_encoding_4Components = [image_pair1_2, image_pair2_2]
    for thisComponent in intentional_encoding_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intentional_encoding_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intentional_encoding_4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = intentional_encoding_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intentional_encoding_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_pair1_2* updates
        if image_pair1_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            image_pair1_2.frameNStart = frameN  # exact frame index
            image_pair1_2.tStart = t  # local t and not account for scr refresh
            image_pair1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair1_2, 'tStartRefresh')  # time at next scr refresh
            image_pair1_2.setAutoDraw(True)
        if image_pair1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair1_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair1_2.tStop = t  # not accounting for scr refresh
                image_pair1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair1_2, 'tStopRefresh')  # time at next scr refresh
                image_pair1_2.setAutoDraw(False)
        
        # *image_pair2_2* updates
        if image_pair2_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            image_pair2_2.frameNStart = frameN  # exact frame index
            image_pair2_2.tStart = t  # local t and not account for scr refresh
            image_pair2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair2_2, 'tStartRefresh')  # time at next scr refresh
            image_pair2_2.setAutoDraw(True)
        if image_pair2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair2_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair2_2.tStop = t  # not accounting for scr refresh
                image_pair2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair2_2, 'tStopRefresh')  # time at next scr refresh
                image_pair2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intentional_encoding_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intentional_encoding_4"-------
    for thisComponent in intentional_encoding_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_6.addData('image_pair1_2.started', image_pair1_2.tStartRefresh)
    trials_6.addData('image_pair1_2.stopped', image_pair1_2.tStopRefresh)
    trials_6.addData('image_pair2_2.started', image_pair2_2.tStartRefresh)
    trials_6.addData('image_pair2_2.stopped', image_pair2_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_6'


# ------Prepare to start Routine "instruct_retrieval4"-------
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
# keep track of which components have finished
instruct_retrieval4Components = [text_13, key_resp_7]
for thisComponent in instruct_retrieval4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_retrieval4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_retrieval4"-------
while continueRoutine:
    # get current time
    t = instruct_retrieval4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_retrieval4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_7.keys = theseKeys.name  # just the last key pressed
            key_resp_7.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_retrieval4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_retrieval4"-------
for thisComponent in instruct_retrieval4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruct_retrieval4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/test.csv', selection='12:24'),
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7:
        exec('{} = thisTrial_7[paramName]'.format(paramName))

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "retrieval4"-------
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    j_key_test_2.setColor('black', colorSpace='rgb')
    j_key_test_2.setPos((-0.5, -0.25))
    j_key_test_2.setFont('Helvetica')
    j_key_test_2.setHeight(0.03)
    K_key_test_2.setColor('black', colorSpace='rgb')
    K_key_test_2.setPos((0, -.25))
    K_key_test_2.setText('K')
    K_key_test_2.setFont('Helvetica')
    K_key_test_2.setHeight(0.03)
    correct_image__2.setImage(correct_image)
    correct_image2_2.setImage(image_a)
    # keep track of which components have finished
    retrieval4Components = [instruct_text_2, a_image_retrieve_2, text_14, afc_text_2, image_13, image_14, image_15, j_key_test_2, L_key_test_2, K_key_test_2, correct_image__2, correct_image2_2, pre_fix_reencode_2, Feedback_2]
    for thisComponent in retrieval4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    retrieval4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "retrieval4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = retrieval4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=retrieval4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text_2* updates
        if instruct_text_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            instruct_text_2.frameNStart = frameN  # exact frame index
            instruct_text_2.tStart = t  # local t and not account for scr refresh
            instruct_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text_2, 'tStartRefresh')  # time at next scr refresh
            instruct_text_2.setAutoDraw(True)
        if instruct_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text_2.tStop = t  # not accounting for scr refresh
                instruct_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text_2, 'tStopRefresh')  # time at next scr refresh
                instruct_text_2.setAutoDraw(False)
        
        # *a_image_retrieve_2* updates
        if a_image_retrieve_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve_2.frameNStart = frameN  # exact frame index
            a_image_retrieve_2.tStart = t  # local t and not account for scr refresh
            a_image_retrieve_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve_2, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve_2.setAutoDraw(True)
        if a_image_retrieve_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve_2.tStop = t  # not accounting for scr refresh
                a_image_retrieve_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve_2, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve_2.setAutoDraw(False)
        if a_image_retrieve_2.status == STARTED:  # only update if drawing
            a_image_retrieve_2.setImage(image_a, log=False)
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        
        # *afc_text_2* updates
        if afc_text_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            afc_text_2.frameNStart = frameN  # exact frame index
            afc_text_2.tStart = t  # local t and not account for scr refresh
            afc_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text_2, 'tStartRefresh')  # time at next scr refresh
            afc_text_2.setAutoDraw(True)
        if afc_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                afc_text_2.tStop = t  # not accounting for scr refresh
                afc_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text_2, 'tStopRefresh')  # time at next scr refresh
                afc_text_2.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        if image_13.status == STARTED:  # only update if drawing
            image_13.setPos((-.5, 0), log=False)
            image_13.setImage(location1, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        if image_14.status == STARTED:  # only update if drawing
            image_14.setPos((0, 0), log=False)
            image_14.setImage(location2, log=False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        if image_15.status == STARTED:  # only update if drawing
            image_15.setPos((0.5, 0), log=False)
            image_15.setImage(location3, log=False)
        
        # *j_key_test_2* updates
        if j_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_2.frameNStart = frameN  # exact frame index
            j_key_test_2.tStart = t  # local t and not account for scr refresh
            j_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_2, 'tStartRefresh')  # time at next scr refresh
            j_key_test_2.setAutoDraw(True)
        if j_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_2.tStop = t  # not accounting for scr refresh
                j_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_2, 'tStopRefresh')  # time at next scr refresh
                j_key_test_2.setAutoDraw(False)
        if j_key_test_2.status == STARTED:  # only update if drawing
            j_key_test_2.setText('J', log=False)
        
        # *L_key_test_2* updates
        if L_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            L_key_test_2.frameNStart = frameN  # exact frame index
            L_key_test_2.tStart = t  # local t and not account for scr refresh
            L_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test_2, 'tStartRefresh')  # time at next scr refresh
            L_key_test_2.setAutoDraw(True)
        if L_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test_2.tStop = t  # not accounting for scr refresh
                L_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test_2, 'tStopRefresh')  # time at next scr refresh
                L_key_test_2.setAutoDraw(False)
        
        # *K_key_test_2* updates
        if K_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            K_key_test_2.frameNStart = frameN  # exact frame index
            K_key_test_2.tStart = t  # local t and not account for scr refresh
            K_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test_2, 'tStartRefresh')  # time at next scr refresh
            K_key_test_2.setAutoDraw(True)
        if K_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test_2.tStop = t  # not accounting for scr refresh
                K_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test_2, 'tStopRefresh')  # time at next scr refresh
                K_key_test_2.setAutoDraw(False)
        
        # *correct_image__2* updates
        if correct_image__2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image__2.frameNStart = frameN  # exact frame index
            correct_image__2.tStart = t  # local t and not account for scr refresh
            correct_image__2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image__2, 'tStartRefresh')  # time at next scr refresh
            correct_image__2.setAutoDraw(True)
        if correct_image__2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image__2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image__2.tStop = t  # not accounting for scr refresh
                correct_image__2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image__2, 'tStopRefresh')  # time at next scr refresh
                correct_image__2.setAutoDraw(False)
        
        # *correct_image2_2* updates
        if correct_image2_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image2_2.frameNStart = frameN  # exact frame index
            correct_image2_2.tStart = t  # local t and not account for scr refresh
            correct_image2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image2_2, 'tStartRefresh')  # time at next scr refresh
            correct_image2_2.setAutoDraw(True)
        if correct_image2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image2_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image2_2.tStop = t  # not accounting for scr refresh
                correct_image2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image2_2, 'tStopRefresh')  # time at next scr refresh
                correct_image2_2.setAutoDraw(False)
        
        # *pre_fix_reencode_2* updates
        if pre_fix_reencode_2.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            pre_fix_reencode_2.frameNStart = frameN  # exact frame index
            pre_fix_reencode_2.tStart = t  # local t and not account for scr refresh
            pre_fix_reencode_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_fix_reencode_2, 'tStartRefresh')  # time at next scr refresh
            pre_fix_reencode_2.setAutoDraw(True)
        if pre_fix_reencode_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_fix_reencode_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                pre_fix_reencode_2.tStop = t  # not accounting for scr refresh
                pre_fix_reencode_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pre_fix_reencode_2, 'tStopRefresh')  # time at next scr refresh
                pre_fix_reencode_2.setAutoDraw(False)
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            Feedback_2.frameNStart = frameN  # exact frame index
            Feedback_2.tStart = t  # local t and not account for scr refresh
            Feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feedback_2, 'tStartRefresh')  # time at next scr refresh
            Feedback_2.setAutoDraw(True)
        if Feedback_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feedback_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Feedback_2.tStop = t  # not accounting for scr refresh
                Feedback_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Feedback_2, 'tStopRefresh')  # time at next scr refresh
                Feedback_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in retrieval4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "retrieval4"-------
    for thisComponent in retrieval4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_7.addData('instruct_text_2.started', instruct_text_2.tStartRefresh)
    trials_7.addData('instruct_text_2.stopped', instruct_text_2.tStopRefresh)
    trials_7.addData('a_image_retrieve_2.started', a_image_retrieve_2.tStartRefresh)
    trials_7.addData('a_image_retrieve_2.stopped', a_image_retrieve_2.tStopRefresh)
    trials_7.addData('text_14.started', text_14.tStartRefresh)
    trials_7.addData('text_14.stopped', text_14.tStopRefresh)
    trials_7.addData('afc_text_2.started', afc_text_2.tStartRefresh)
    trials_7.addData('afc_text_2.stopped', afc_text_2.tStopRefresh)
    trials_7.addData('image_13.started', image_13.tStartRefresh)
    trials_7.addData('image_13.stopped', image_13.tStopRefresh)
    trials_7.addData('image_14.started', image_14.tStartRefresh)
    trials_7.addData('image_14.stopped', image_14.tStopRefresh)
    trials_7.addData('image_15.started', image_15.tStartRefresh)
    trials_7.addData('image_15.stopped', image_15.tStopRefresh)
    trials_7.addData('j_key_test_2.started', j_key_test_2.tStartRefresh)
    trials_7.addData('j_key_test_2.stopped', j_key_test_2.tStopRefresh)
    trials_7.addData('L_key_test_2.started', L_key_test_2.tStartRefresh)
    trials_7.addData('L_key_test_2.stopped', L_key_test_2.tStopRefresh)
    trials_7.addData('K_key_test_2.started', K_key_test_2.tStartRefresh)
    trials_7.addData('K_key_test_2.stopped', K_key_test_2.tStopRefresh)
    trials_7.addData('correct_image__2.started', correct_image__2.tStartRefresh)
    trials_7.addData('correct_image__2.stopped', correct_image__2.tStopRefresh)
    trials_7.addData('correct_image2_2.started', correct_image2_2.tStartRefresh)
    trials_7.addData('correct_image2_2.stopped', correct_image2_2.tStopRefresh)
    trials_7.addData('pre_fix_reencode_2.started', pre_fix_reencode_2.tStartRefresh)
    trials_7.addData('pre_fix_reencode_2.stopped', pre_fix_reencode_2.tStopRefresh)
    trials_7.addData('Feedback_2.started', Feedback_2.tStartRefresh)
    trials_7.addData('Feedback_2.stopped', Feedback_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_7'


# ------Prepare to start Routine "pre_intentional_encoding4"-------
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
# keep track of which components have finished
pre_intentional_encoding4Components = [text_12, key_resp_6]
for thisComponent in pre_intentional_encoding4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pre_intentional_encoding4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "pre_intentional_encoding4"-------
while continueRoutine:
    # get current time
    t = pre_intentional_encoding4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pre_intentional_encoding4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.04-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_intentional_encoding4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pre_intentional_encoding4"-------
for thisComponent in pre_intentional_encoding4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "pre_intentional_encoding4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/intentional_encoding.xlsx', selection='24:36'),
    seed=None, name='trials_8')
thisExp.addLoop(trials_8)  # add the loop to the experiment
thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
if thisTrial_8 != None:
    for paramName in thisTrial_8:
        exec('{} = thisTrial_8[paramName]'.format(paramName))

for thisTrial_8 in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            exec('{} = thisTrial_8[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intentional_encoding_4"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image_pair1_2.setImage(ImageA)
    image_pair2_2.setImage(ImageB)
    # keep track of which components have finished
    intentional_encoding_4Components = [image_pair1_2, image_pair2_2]
    for thisComponent in intentional_encoding_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intentional_encoding_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intentional_encoding_4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = intentional_encoding_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intentional_encoding_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_pair1_2* updates
        if image_pair1_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            image_pair1_2.frameNStart = frameN  # exact frame index
            image_pair1_2.tStart = t  # local t and not account for scr refresh
            image_pair1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair1_2, 'tStartRefresh')  # time at next scr refresh
            image_pair1_2.setAutoDraw(True)
        if image_pair1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair1_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair1_2.tStop = t  # not accounting for scr refresh
                image_pair1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair1_2, 'tStopRefresh')  # time at next scr refresh
                image_pair1_2.setAutoDraw(False)
        
        # *image_pair2_2* updates
        if image_pair2_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            image_pair2_2.frameNStart = frameN  # exact frame index
            image_pair2_2.tStart = t  # local t and not account for scr refresh
            image_pair2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair2_2, 'tStartRefresh')  # time at next scr refresh
            image_pair2_2.setAutoDraw(True)
        if image_pair2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair2_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair2_2.tStop = t  # not accounting for scr refresh
                image_pair2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair2_2, 'tStopRefresh')  # time at next scr refresh
                image_pair2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intentional_encoding_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intentional_encoding_4"-------
    for thisComponent in intentional_encoding_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_8.addData('image_pair1_2.started', image_pair1_2.tStartRefresh)
    trials_8.addData('image_pair1_2.stopped', image_pair1_2.tStopRefresh)
    trials_8.addData('image_pair2_2.started', image_pair2_2.tStartRefresh)
    trials_8.addData('image_pair2_2.stopped', image_pair2_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_8'


# ------Prepare to start Routine "instruct_retrieval4"-------
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
# keep track of which components have finished
instruct_retrieval4Components = [text_13, key_resp_7]
for thisComponent in instruct_retrieval4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_retrieval4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_retrieval4"-------
while continueRoutine:
    # get current time
    t = instruct_retrieval4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_retrieval4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_7.keys = theseKeys.name  # just the last key pressed
            key_resp_7.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_retrieval4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_retrieval4"-------
for thisComponent in instruct_retrieval4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruct_retrieval4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_9 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/test.csv', selection='24:36'),
    seed=None, name='trials_9')
thisExp.addLoop(trials_9)  # add the loop to the experiment
thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
if thisTrial_9 != None:
    for paramName in thisTrial_9:
        exec('{} = thisTrial_9[paramName]'.format(paramName))

for thisTrial_9 in trials_9:
    currentLoop = trials_9
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            exec('{} = thisTrial_9[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "retrieval4"-------
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    j_key_test_2.setColor('black', colorSpace='rgb')
    j_key_test_2.setPos((-0.5, -0.25))
    j_key_test_2.setFont('Helvetica')
    j_key_test_2.setHeight(0.03)
    K_key_test_2.setColor('black', colorSpace='rgb')
    K_key_test_2.setPos((0, -.25))
    K_key_test_2.setText('K')
    K_key_test_2.setFont('Helvetica')
    K_key_test_2.setHeight(0.03)
    correct_image__2.setImage(correct_image)
    correct_image2_2.setImage(image_a)
    # keep track of which components have finished
    retrieval4Components = [instruct_text_2, a_image_retrieve_2, text_14, afc_text_2, image_13, image_14, image_15, j_key_test_2, L_key_test_2, K_key_test_2, correct_image__2, correct_image2_2, pre_fix_reencode_2, Feedback_2]
    for thisComponent in retrieval4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    retrieval4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "retrieval4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = retrieval4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=retrieval4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text_2* updates
        if instruct_text_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            instruct_text_2.frameNStart = frameN  # exact frame index
            instruct_text_2.tStart = t  # local t and not account for scr refresh
            instruct_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text_2, 'tStartRefresh')  # time at next scr refresh
            instruct_text_2.setAutoDraw(True)
        if instruct_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text_2.tStop = t  # not accounting for scr refresh
                instruct_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text_2, 'tStopRefresh')  # time at next scr refresh
                instruct_text_2.setAutoDraw(False)
        
        # *a_image_retrieve_2* updates
        if a_image_retrieve_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve_2.frameNStart = frameN  # exact frame index
            a_image_retrieve_2.tStart = t  # local t and not account for scr refresh
            a_image_retrieve_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve_2, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve_2.setAutoDraw(True)
        if a_image_retrieve_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve_2.tStop = t  # not accounting for scr refresh
                a_image_retrieve_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve_2, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve_2.setAutoDraw(False)
        if a_image_retrieve_2.status == STARTED:  # only update if drawing
            a_image_retrieve_2.setImage(image_a, log=False)
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        
        # *afc_text_2* updates
        if afc_text_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            afc_text_2.frameNStart = frameN  # exact frame index
            afc_text_2.tStart = t  # local t and not account for scr refresh
            afc_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text_2, 'tStartRefresh')  # time at next scr refresh
            afc_text_2.setAutoDraw(True)
        if afc_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                afc_text_2.tStop = t  # not accounting for scr refresh
                afc_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text_2, 'tStopRefresh')  # time at next scr refresh
                afc_text_2.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        if image_13.status == STARTED:  # only update if drawing
            image_13.setPos((-.5, 0), log=False)
            image_13.setImage(location1, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        if image_14.status == STARTED:  # only update if drawing
            image_14.setPos((0, 0), log=False)
            image_14.setImage(location2, log=False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        if image_15.status == STARTED:  # only update if drawing
            image_15.setPos((0.5, 0), log=False)
            image_15.setImage(location3, log=False)
        
        # *j_key_test_2* updates
        if j_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_2.frameNStart = frameN  # exact frame index
            j_key_test_2.tStart = t  # local t and not account for scr refresh
            j_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_2, 'tStartRefresh')  # time at next scr refresh
            j_key_test_2.setAutoDraw(True)
        if j_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_2.tStop = t  # not accounting for scr refresh
                j_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_2, 'tStopRefresh')  # time at next scr refresh
                j_key_test_2.setAutoDraw(False)
        if j_key_test_2.status == STARTED:  # only update if drawing
            j_key_test_2.setText('J', log=False)
        
        # *L_key_test_2* updates
        if L_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            L_key_test_2.frameNStart = frameN  # exact frame index
            L_key_test_2.tStart = t  # local t and not account for scr refresh
            L_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test_2, 'tStartRefresh')  # time at next scr refresh
            L_key_test_2.setAutoDraw(True)
        if L_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test_2.tStop = t  # not accounting for scr refresh
                L_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test_2, 'tStopRefresh')  # time at next scr refresh
                L_key_test_2.setAutoDraw(False)
        
        # *K_key_test_2* updates
        if K_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            K_key_test_2.frameNStart = frameN  # exact frame index
            K_key_test_2.tStart = t  # local t and not account for scr refresh
            K_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test_2, 'tStartRefresh')  # time at next scr refresh
            K_key_test_2.setAutoDraw(True)
        if K_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test_2.tStop = t  # not accounting for scr refresh
                K_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test_2, 'tStopRefresh')  # time at next scr refresh
                K_key_test_2.setAutoDraw(False)
        
        # *correct_image__2* updates
        if correct_image__2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image__2.frameNStart = frameN  # exact frame index
            correct_image__2.tStart = t  # local t and not account for scr refresh
            correct_image__2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image__2, 'tStartRefresh')  # time at next scr refresh
            correct_image__2.setAutoDraw(True)
        if correct_image__2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image__2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image__2.tStop = t  # not accounting for scr refresh
                correct_image__2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image__2, 'tStopRefresh')  # time at next scr refresh
                correct_image__2.setAutoDraw(False)
        
        # *correct_image2_2* updates
        if correct_image2_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image2_2.frameNStart = frameN  # exact frame index
            correct_image2_2.tStart = t  # local t and not account for scr refresh
            correct_image2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image2_2, 'tStartRefresh')  # time at next scr refresh
            correct_image2_2.setAutoDraw(True)
        if correct_image2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image2_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image2_2.tStop = t  # not accounting for scr refresh
                correct_image2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image2_2, 'tStopRefresh')  # time at next scr refresh
                correct_image2_2.setAutoDraw(False)
        
        # *pre_fix_reencode_2* updates
        if pre_fix_reencode_2.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            pre_fix_reencode_2.frameNStart = frameN  # exact frame index
            pre_fix_reencode_2.tStart = t  # local t and not account for scr refresh
            pre_fix_reencode_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_fix_reencode_2, 'tStartRefresh')  # time at next scr refresh
            pre_fix_reencode_2.setAutoDraw(True)
        if pre_fix_reencode_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_fix_reencode_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                pre_fix_reencode_2.tStop = t  # not accounting for scr refresh
                pre_fix_reencode_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pre_fix_reencode_2, 'tStopRefresh')  # time at next scr refresh
                pre_fix_reencode_2.setAutoDraw(False)
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            Feedback_2.frameNStart = frameN  # exact frame index
            Feedback_2.tStart = t  # local t and not account for scr refresh
            Feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feedback_2, 'tStartRefresh')  # time at next scr refresh
            Feedback_2.setAutoDraw(True)
        if Feedback_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feedback_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Feedback_2.tStop = t  # not accounting for scr refresh
                Feedback_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Feedback_2, 'tStopRefresh')  # time at next scr refresh
                Feedback_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in retrieval4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "retrieval4"-------
    for thisComponent in retrieval4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_9.addData('instruct_text_2.started', instruct_text_2.tStartRefresh)
    trials_9.addData('instruct_text_2.stopped', instruct_text_2.tStopRefresh)
    trials_9.addData('a_image_retrieve_2.started', a_image_retrieve_2.tStartRefresh)
    trials_9.addData('a_image_retrieve_2.stopped', a_image_retrieve_2.tStopRefresh)
    trials_9.addData('text_14.started', text_14.tStartRefresh)
    trials_9.addData('text_14.stopped', text_14.tStopRefresh)
    trials_9.addData('afc_text_2.started', afc_text_2.tStartRefresh)
    trials_9.addData('afc_text_2.stopped', afc_text_2.tStopRefresh)
    trials_9.addData('image_13.started', image_13.tStartRefresh)
    trials_9.addData('image_13.stopped', image_13.tStopRefresh)
    trials_9.addData('image_14.started', image_14.tStartRefresh)
    trials_9.addData('image_14.stopped', image_14.tStopRefresh)
    trials_9.addData('image_15.started', image_15.tStartRefresh)
    trials_9.addData('image_15.stopped', image_15.tStopRefresh)
    trials_9.addData('j_key_test_2.started', j_key_test_2.tStartRefresh)
    trials_9.addData('j_key_test_2.stopped', j_key_test_2.tStopRefresh)
    trials_9.addData('L_key_test_2.started', L_key_test_2.tStartRefresh)
    trials_9.addData('L_key_test_2.stopped', L_key_test_2.tStopRefresh)
    trials_9.addData('K_key_test_2.started', K_key_test_2.tStartRefresh)
    trials_9.addData('K_key_test_2.stopped', K_key_test_2.tStopRefresh)
    trials_9.addData('correct_image__2.started', correct_image__2.tStartRefresh)
    trials_9.addData('correct_image__2.stopped', correct_image__2.tStopRefresh)
    trials_9.addData('correct_image2_2.started', correct_image2_2.tStartRefresh)
    trials_9.addData('correct_image2_2.stopped', correct_image2_2.tStopRefresh)
    trials_9.addData('pre_fix_reencode_2.started', pre_fix_reencode_2.tStartRefresh)
    trials_9.addData('pre_fix_reencode_2.stopped', pre_fix_reencode_2.tStopRefresh)
    trials_9.addData('Feedback_2.started', Feedback_2.tStartRefresh)
    trials_9.addData('Feedback_2.stopped', Feedback_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_9'


# ------Prepare to start Routine "pre_intentional_encoding4"-------
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
# keep track of which components have finished
pre_intentional_encoding4Components = [text_12, key_resp_6]
for thisComponent in pre_intentional_encoding4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pre_intentional_encoding4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "pre_intentional_encoding4"-------
while continueRoutine:
    # get current time
    t = pre_intentional_encoding4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pre_intentional_encoding4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.04-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_intentional_encoding4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pre_intentional_encoding4"-------
for thisComponent in pre_intentional_encoding4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "pre_intentional_encoding4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_10 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/intentional_encoding.xlsx', selection='36:48'),
    seed=None, name='trials_10')
thisExp.addLoop(trials_10)  # add the loop to the experiment
thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
if thisTrial_10 != None:
    for paramName in thisTrial_10:
        exec('{} = thisTrial_10[paramName]'.format(paramName))

for thisTrial_10 in trials_10:
    currentLoop = trials_10
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
    if thisTrial_10 != None:
        for paramName in thisTrial_10:
            exec('{} = thisTrial_10[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "intentional_encoding_4"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image_pair1_2.setImage(ImageA)
    image_pair2_2.setImage(ImageB)
    # keep track of which components have finished
    intentional_encoding_4Components = [image_pair1_2, image_pair2_2]
    for thisComponent in intentional_encoding_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    intentional_encoding_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "intentional_encoding_4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = intentional_encoding_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=intentional_encoding_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_pair1_2* updates
        if image_pair1_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            image_pair1_2.frameNStart = frameN  # exact frame index
            image_pair1_2.tStart = t  # local t and not account for scr refresh
            image_pair1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair1_2, 'tStartRefresh')  # time at next scr refresh
            image_pair1_2.setAutoDraw(True)
        if image_pair1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair1_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair1_2.tStop = t  # not accounting for scr refresh
                image_pair1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair1_2, 'tStopRefresh')  # time at next scr refresh
                image_pair1_2.setAutoDraw(False)
        
        # *image_pair2_2* updates
        if image_pair2_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            image_pair2_2.frameNStart = frameN  # exact frame index
            image_pair2_2.tStart = t  # local t and not account for scr refresh
            image_pair2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair2_2, 'tStartRefresh')  # time at next scr refresh
            image_pair2_2.setAutoDraw(True)
        if image_pair2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair2_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair2_2.tStop = t  # not accounting for scr refresh
                image_pair2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair2_2, 'tStopRefresh')  # time at next scr refresh
                image_pair2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in intentional_encoding_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "intentional_encoding_4"-------
    for thisComponent in intentional_encoding_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_10.addData('image_pair1_2.started', image_pair1_2.tStartRefresh)
    trials_10.addData('image_pair1_2.stopped', image_pair1_2.tStopRefresh)
    trials_10.addData('image_pair2_2.started', image_pair2_2.tStartRefresh)
    trials_10.addData('image_pair2_2.stopped', image_pair2_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_10'


# ------Prepare to start Routine "instruct_retrieval4"-------
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
# keep track of which components have finished
instruct_retrieval4Components = [text_13, key_resp_7]
for thisComponent in instruct_retrieval4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_retrieval4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_retrieval4"-------
while continueRoutine:
    # get current time
    t = instruct_retrieval4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_retrieval4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_7.keys = theseKeys.name  # just the last key pressed
            key_resp_7.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_retrieval4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_retrieval4"-------
for thisComponent in instruct_retrieval4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruct_retrieval4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_11 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/test.csv', selection='36:48'),
    seed=None, name='trials_11')
thisExp.addLoop(trials_11)  # add the loop to the experiment
thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
if thisTrial_11 != None:
    for paramName in thisTrial_11:
        exec('{} = thisTrial_11[paramName]'.format(paramName))

for thisTrial_11 in trials_11:
    currentLoop = trials_11
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
    if thisTrial_11 != None:
        for paramName in thisTrial_11:
            exec('{} = thisTrial_11[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "retrieval4"-------
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    j_key_test_2.setColor('black', colorSpace='rgb')
    j_key_test_2.setPos((-0.5, -0.25))
    j_key_test_2.setFont('Helvetica')
    j_key_test_2.setHeight(0.03)
    K_key_test_2.setColor('black', colorSpace='rgb')
    K_key_test_2.setPos((0, -.25))
    K_key_test_2.setText('K')
    K_key_test_2.setFont('Helvetica')
    K_key_test_2.setHeight(0.03)
    correct_image__2.setImage(correct_image)
    correct_image2_2.setImage(image_a)
    # keep track of which components have finished
    retrieval4Components = [instruct_text_2, a_image_retrieve_2, text_14, afc_text_2, image_13, image_14, image_15, j_key_test_2, L_key_test_2, K_key_test_2, correct_image__2, correct_image2_2, pre_fix_reencode_2, Feedback_2]
    for thisComponent in retrieval4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    retrieval4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "retrieval4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = retrieval4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=retrieval4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text_2* updates
        if instruct_text_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            instruct_text_2.frameNStart = frameN  # exact frame index
            instruct_text_2.tStart = t  # local t and not account for scr refresh
            instruct_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text_2, 'tStartRefresh')  # time at next scr refresh
            instruct_text_2.setAutoDraw(True)
        if instruct_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text_2.tStop = t  # not accounting for scr refresh
                instruct_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text_2, 'tStopRefresh')  # time at next scr refresh
                instruct_text_2.setAutoDraw(False)
        
        # *a_image_retrieve_2* updates
        if a_image_retrieve_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve_2.frameNStart = frameN  # exact frame index
            a_image_retrieve_2.tStart = t  # local t and not account for scr refresh
            a_image_retrieve_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve_2, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve_2.setAutoDraw(True)
        if a_image_retrieve_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve_2.tStop = t  # not accounting for scr refresh
                a_image_retrieve_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve_2, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve_2.setAutoDraw(False)
        if a_image_retrieve_2.status == STARTED:  # only update if drawing
            a_image_retrieve_2.setImage(image_a, log=False)
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        
        # *afc_text_2* updates
        if afc_text_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            afc_text_2.frameNStart = frameN  # exact frame index
            afc_text_2.tStart = t  # local t and not account for scr refresh
            afc_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text_2, 'tStartRefresh')  # time at next scr refresh
            afc_text_2.setAutoDraw(True)
        if afc_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                afc_text_2.tStop = t  # not accounting for scr refresh
                afc_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text_2, 'tStopRefresh')  # time at next scr refresh
                afc_text_2.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        if image_13.status == STARTED:  # only update if drawing
            image_13.setPos((-.5, 0), log=False)
            image_13.setImage(location1, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        if image_14.status == STARTED:  # only update if drawing
            image_14.setPos((0, 0), log=False)
            image_14.setImage(location2, log=False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        if image_15.status == STARTED:  # only update if drawing
            image_15.setPos((0.5, 0), log=False)
            image_15.setImage(location3, log=False)
        
        # *j_key_test_2* updates
        if j_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_2.frameNStart = frameN  # exact frame index
            j_key_test_2.tStart = t  # local t and not account for scr refresh
            j_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_2, 'tStartRefresh')  # time at next scr refresh
            j_key_test_2.setAutoDraw(True)
        if j_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_2.tStop = t  # not accounting for scr refresh
                j_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_2, 'tStopRefresh')  # time at next scr refresh
                j_key_test_2.setAutoDraw(False)
        if j_key_test_2.status == STARTED:  # only update if drawing
            j_key_test_2.setText('J', log=False)
        
        # *L_key_test_2* updates
        if L_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            L_key_test_2.frameNStart = frameN  # exact frame index
            L_key_test_2.tStart = t  # local t and not account for scr refresh
            L_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test_2, 'tStartRefresh')  # time at next scr refresh
            L_key_test_2.setAutoDraw(True)
        if L_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test_2.tStop = t  # not accounting for scr refresh
                L_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test_2, 'tStopRefresh')  # time at next scr refresh
                L_key_test_2.setAutoDraw(False)
        
        # *K_key_test_2* updates
        if K_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            K_key_test_2.frameNStart = frameN  # exact frame index
            K_key_test_2.tStart = t  # local t and not account for scr refresh
            K_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test_2, 'tStartRefresh')  # time at next scr refresh
            K_key_test_2.setAutoDraw(True)
        if K_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test_2.tStop = t  # not accounting for scr refresh
                K_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test_2, 'tStopRefresh')  # time at next scr refresh
                K_key_test_2.setAutoDraw(False)
        
        # *correct_image__2* updates
        if correct_image__2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image__2.frameNStart = frameN  # exact frame index
            correct_image__2.tStart = t  # local t and not account for scr refresh
            correct_image__2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image__2, 'tStartRefresh')  # time at next scr refresh
            correct_image__2.setAutoDraw(True)
        if correct_image__2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image__2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image__2.tStop = t  # not accounting for scr refresh
                correct_image__2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image__2, 'tStopRefresh')  # time at next scr refresh
                correct_image__2.setAutoDraw(False)
        
        # *correct_image2_2* updates
        if correct_image2_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image2_2.frameNStart = frameN  # exact frame index
            correct_image2_2.tStart = t  # local t and not account for scr refresh
            correct_image2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image2_2, 'tStartRefresh')  # time at next scr refresh
            correct_image2_2.setAutoDraw(True)
        if correct_image2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image2_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image2_2.tStop = t  # not accounting for scr refresh
                correct_image2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image2_2, 'tStopRefresh')  # time at next scr refresh
                correct_image2_2.setAutoDraw(False)
        
        # *pre_fix_reencode_2* updates
        if pre_fix_reencode_2.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            pre_fix_reencode_2.frameNStart = frameN  # exact frame index
            pre_fix_reencode_2.tStart = t  # local t and not account for scr refresh
            pre_fix_reencode_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_fix_reencode_2, 'tStartRefresh')  # time at next scr refresh
            pre_fix_reencode_2.setAutoDraw(True)
        if pre_fix_reencode_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_fix_reencode_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                pre_fix_reencode_2.tStop = t  # not accounting for scr refresh
                pre_fix_reencode_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pre_fix_reencode_2, 'tStopRefresh')  # time at next scr refresh
                pre_fix_reencode_2.setAutoDraw(False)
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            Feedback_2.frameNStart = frameN  # exact frame index
            Feedback_2.tStart = t  # local t and not account for scr refresh
            Feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feedback_2, 'tStartRefresh')  # time at next scr refresh
            Feedback_2.setAutoDraw(True)
        if Feedback_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feedback_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Feedback_2.tStop = t  # not accounting for scr refresh
                Feedback_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Feedback_2, 'tStopRefresh')  # time at next scr refresh
                Feedback_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in retrieval4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "retrieval4"-------
    for thisComponent in retrieval4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_11.addData('instruct_text_2.started', instruct_text_2.tStartRefresh)
    trials_11.addData('instruct_text_2.stopped', instruct_text_2.tStopRefresh)
    trials_11.addData('a_image_retrieve_2.started', a_image_retrieve_2.tStartRefresh)
    trials_11.addData('a_image_retrieve_2.stopped', a_image_retrieve_2.tStopRefresh)
    trials_11.addData('text_14.started', text_14.tStartRefresh)
    trials_11.addData('text_14.stopped', text_14.tStopRefresh)
    trials_11.addData('afc_text_2.started', afc_text_2.tStartRefresh)
    trials_11.addData('afc_text_2.stopped', afc_text_2.tStopRefresh)
    trials_11.addData('image_13.started', image_13.tStartRefresh)
    trials_11.addData('image_13.stopped', image_13.tStopRefresh)
    trials_11.addData('image_14.started', image_14.tStartRefresh)
    trials_11.addData('image_14.stopped', image_14.tStopRefresh)
    trials_11.addData('image_15.started', image_15.tStartRefresh)
    trials_11.addData('image_15.stopped', image_15.tStopRefresh)
    trials_11.addData('j_key_test_2.started', j_key_test_2.tStartRefresh)
    trials_11.addData('j_key_test_2.stopped', j_key_test_2.tStopRefresh)
    trials_11.addData('L_key_test_2.started', L_key_test_2.tStartRefresh)
    trials_11.addData('L_key_test_2.stopped', L_key_test_2.tStopRefresh)
    trials_11.addData('K_key_test_2.started', K_key_test_2.tStartRefresh)
    trials_11.addData('K_key_test_2.stopped', K_key_test_2.tStopRefresh)
    trials_11.addData('correct_image__2.started', correct_image__2.tStartRefresh)
    trials_11.addData('correct_image__2.stopped', correct_image__2.tStopRefresh)
    trials_11.addData('correct_image2_2.started', correct_image2_2.tStartRefresh)
    trials_11.addData('correct_image2_2.stopped', correct_image2_2.tStopRefresh)
    trials_11.addData('pre_fix_reencode_2.started', pre_fix_reencode_2.tStartRefresh)
    trials_11.addData('pre_fix_reencode_2.stopped', pre_fix_reencode_2.tStopRefresh)
    trials_11.addData('Feedback_2.started', Feedback_2.tStartRefresh)
    trials_11.addData('Feedback_2.stopped', Feedback_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_11'


# ------Prepare to start Routine "final_ab_retrieval_test_instruct"-------
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
# keep track of which components have finished
final_ab_retrieval_test_instructComponents = [text_15, key_resp_8]
for thisComponent in final_ab_retrieval_test_instructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
final_ab_retrieval_test_instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "final_ab_retrieval_test_instruct"-------
while continueRoutine:
    # get current time
    t = final_ab_retrieval_test_instructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=final_ab_retrieval_test_instructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_8.keys = theseKeys.name  # just the last key pressed
            key_resp_8.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_ab_retrieval_test_instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final_ab_retrieval_test_instruct"-------
for thisComponent in final_ab_retrieval_test_instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "final_ab_retrieval_test_instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_12 = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/test.csv'),
    seed=None, name='trials_12')
thisExp.addLoop(trials_12)  # add the loop to the experiment
thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
if thisTrial_12 != None:
    for paramName in thisTrial_12:
        exec('{} = thisTrial_12[paramName]'.format(paramName))

for thisTrial_12 in trials_12:
    currentLoop = trials_12
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
    if thisTrial_12 != None:
        for paramName in thisTrial_12:
            exec('{} = thisTrial_12[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "retrieval4"-------
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    j_key_test_2.setColor('black', colorSpace='rgb')
    j_key_test_2.setPos((-0.5, -0.25))
    j_key_test_2.setFont('Helvetica')
    j_key_test_2.setHeight(0.03)
    K_key_test_2.setColor('black', colorSpace='rgb')
    K_key_test_2.setPos((0, -.25))
    K_key_test_2.setText('K')
    K_key_test_2.setFont('Helvetica')
    K_key_test_2.setHeight(0.03)
    correct_image__2.setImage(correct_image)
    correct_image2_2.setImage(image_a)
    # keep track of which components have finished
    retrieval4Components = [instruct_text_2, a_image_retrieve_2, text_14, afc_text_2, image_13, image_14, image_15, j_key_test_2, L_key_test_2, K_key_test_2, correct_image__2, correct_image2_2, pre_fix_reencode_2, Feedback_2]
    for thisComponent in retrieval4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    retrieval4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "retrieval4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = retrieval4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=retrieval4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text_2* updates
        if instruct_text_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            instruct_text_2.frameNStart = frameN  # exact frame index
            instruct_text_2.tStart = t  # local t and not account for scr refresh
            instruct_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text_2, 'tStartRefresh')  # time at next scr refresh
            instruct_text_2.setAutoDraw(True)
        if instruct_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text_2.tStop = t  # not accounting for scr refresh
                instruct_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text_2, 'tStopRefresh')  # time at next scr refresh
                instruct_text_2.setAutoDraw(False)
        
        # *a_image_retrieve_2* updates
        if a_image_retrieve_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve_2.frameNStart = frameN  # exact frame index
            a_image_retrieve_2.tStart = t  # local t and not account for scr refresh
            a_image_retrieve_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve_2, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve_2.setAutoDraw(True)
        if a_image_retrieve_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve_2.tStop = t  # not accounting for scr refresh
                a_image_retrieve_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve_2, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve_2.setAutoDraw(False)
        if a_image_retrieve_2.status == STARTED:  # only update if drawing
            a_image_retrieve_2.setImage(image_a, log=False)
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        
        # *afc_text_2* updates
        if afc_text_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            afc_text_2.frameNStart = frameN  # exact frame index
            afc_text_2.tStart = t  # local t and not account for scr refresh
            afc_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text_2, 'tStartRefresh')  # time at next scr refresh
            afc_text_2.setAutoDraw(True)
        if afc_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                afc_text_2.tStop = t  # not accounting for scr refresh
                afc_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text_2, 'tStopRefresh')  # time at next scr refresh
                afc_text_2.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        if image_13.status == STARTED:  # only update if drawing
            image_13.setPos((-.5, 0), log=False)
            image_13.setImage(location1, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        if image_14.status == STARTED:  # only update if drawing
            image_14.setPos((0, 0), log=False)
            image_14.setImage(location2, log=False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        if image_15.status == STARTED:  # only update if drawing
            image_15.setPos((0.5, 0), log=False)
            image_15.setImage(location3, log=False)
        
        # *j_key_test_2* updates
        if j_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_2.frameNStart = frameN  # exact frame index
            j_key_test_2.tStart = t  # local t and not account for scr refresh
            j_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_2, 'tStartRefresh')  # time at next scr refresh
            j_key_test_2.setAutoDraw(True)
        if j_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_2.tStop = t  # not accounting for scr refresh
                j_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_2, 'tStopRefresh')  # time at next scr refresh
                j_key_test_2.setAutoDraw(False)
        if j_key_test_2.status == STARTED:  # only update if drawing
            j_key_test_2.setText('J', log=False)
        
        # *L_key_test_2* updates
        if L_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            L_key_test_2.frameNStart = frameN  # exact frame index
            L_key_test_2.tStart = t  # local t and not account for scr refresh
            L_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test_2, 'tStartRefresh')  # time at next scr refresh
            L_key_test_2.setAutoDraw(True)
        if L_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test_2.tStop = t  # not accounting for scr refresh
                L_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test_2, 'tStopRefresh')  # time at next scr refresh
                L_key_test_2.setAutoDraw(False)
        
        # *K_key_test_2* updates
        if K_key_test_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            K_key_test_2.frameNStart = frameN  # exact frame index
            K_key_test_2.tStart = t  # local t and not account for scr refresh
            K_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test_2, 'tStartRefresh')  # time at next scr refresh
            K_key_test_2.setAutoDraw(True)
        if K_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test_2.tStop = t  # not accounting for scr refresh
                K_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test_2, 'tStopRefresh')  # time at next scr refresh
                K_key_test_2.setAutoDraw(False)
        
        # *correct_image__2* updates
        if correct_image__2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image__2.frameNStart = frameN  # exact frame index
            correct_image__2.tStart = t  # local t and not account for scr refresh
            correct_image__2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image__2, 'tStartRefresh')  # time at next scr refresh
            correct_image__2.setAutoDraw(True)
        if correct_image__2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image__2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image__2.tStop = t  # not accounting for scr refresh
                correct_image__2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image__2, 'tStopRefresh')  # time at next scr refresh
                correct_image__2.setAutoDraw(False)
        
        # *correct_image2_2* updates
        if correct_image2_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            correct_image2_2.frameNStart = frameN  # exact frame index
            correct_image2_2.tStart = t  # local t and not account for scr refresh
            correct_image2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image2_2, 'tStartRefresh')  # time at next scr refresh
            correct_image2_2.setAutoDraw(True)
        if correct_image2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image2_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image2_2.tStop = t  # not accounting for scr refresh
                correct_image2_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image2_2, 'tStopRefresh')  # time at next scr refresh
                correct_image2_2.setAutoDraw(False)
        
        # *pre_fix_reencode_2* updates
        if pre_fix_reencode_2.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
            # keep track of start time/frame for later
            pre_fix_reencode_2.frameNStart = frameN  # exact frame index
            pre_fix_reencode_2.tStart = t  # local t and not account for scr refresh
            pre_fix_reencode_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pre_fix_reencode_2, 'tStartRefresh')  # time at next scr refresh
            pre_fix_reencode_2.setAutoDraw(True)
        if pre_fix_reencode_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pre_fix_reencode_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                pre_fix_reencode_2.tStop = t  # not accounting for scr refresh
                pre_fix_reencode_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pre_fix_reencode_2, 'tStopRefresh')  # time at next scr refresh
                pre_fix_reencode_2.setAutoDraw(False)
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            Feedback_2.frameNStart = frameN  # exact frame index
            Feedback_2.tStart = t  # local t and not account for scr refresh
            Feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feedback_2, 'tStartRefresh')  # time at next scr refresh
            Feedback_2.setAutoDraw(True)
        if Feedback_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feedback_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Feedback_2.tStop = t  # not accounting for scr refresh
                Feedback_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Feedback_2, 'tStopRefresh')  # time at next scr refresh
                Feedback_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in retrieval4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "retrieval4"-------
    for thisComponent in retrieval4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_12.addData('instruct_text_2.started', instruct_text_2.tStartRefresh)
    trials_12.addData('instruct_text_2.stopped', instruct_text_2.tStopRefresh)
    trials_12.addData('a_image_retrieve_2.started', a_image_retrieve_2.tStartRefresh)
    trials_12.addData('a_image_retrieve_2.stopped', a_image_retrieve_2.tStopRefresh)
    trials_12.addData('text_14.started', text_14.tStartRefresh)
    trials_12.addData('text_14.stopped', text_14.tStopRefresh)
    trials_12.addData('afc_text_2.started', afc_text_2.tStartRefresh)
    trials_12.addData('afc_text_2.stopped', afc_text_2.tStopRefresh)
    trials_12.addData('image_13.started', image_13.tStartRefresh)
    trials_12.addData('image_13.stopped', image_13.tStopRefresh)
    trials_12.addData('image_14.started', image_14.tStartRefresh)
    trials_12.addData('image_14.stopped', image_14.tStopRefresh)
    trials_12.addData('image_15.started', image_15.tStartRefresh)
    trials_12.addData('image_15.stopped', image_15.tStopRefresh)
    trials_12.addData('j_key_test_2.started', j_key_test_2.tStartRefresh)
    trials_12.addData('j_key_test_2.stopped', j_key_test_2.tStopRefresh)
    trials_12.addData('L_key_test_2.started', L_key_test_2.tStartRefresh)
    trials_12.addData('L_key_test_2.stopped', L_key_test_2.tStopRefresh)
    trials_12.addData('K_key_test_2.started', K_key_test_2.tStartRefresh)
    trials_12.addData('K_key_test_2.stopped', K_key_test_2.tStopRefresh)
    trials_12.addData('correct_image__2.started', correct_image__2.tStartRefresh)
    trials_12.addData('correct_image__2.stopped', correct_image__2.tStopRefresh)
    trials_12.addData('correct_image2_2.started', correct_image2_2.tStartRefresh)
    trials_12.addData('correct_image2_2.stopped', correct_image2_2.tStopRefresh)
    trials_12.addData('pre_fix_reencode_2.started', pre_fix_reencode_2.tStartRefresh)
    trials_12.addData('pre_fix_reencode_2.stopped', pre_fix_reencode_2.tStopRefresh)
    trials_12.addData('Feedback_2.started', Feedback_2.tStartRefresh)
    trials_12.addData('Feedback_2.stopped', Feedback_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_12'


# set up handler to look after randomisation of conditions etc
trials_13 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions_intentional_encoding.xlsx', selection='16:23'),
    seed=None, name='trials_13')
thisExp.addLoop(trials_13)  # add the loop to the experiment
thisTrial_13 = trials_13.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
if thisTrial_13 != None:
    for paramName in thisTrial_13:
        exec('{} = thisTrial_13[paramName]'.format(paramName))

for thisTrial_13 in trials_13:
    currentLoop = trials_13
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_13.rgb)
    if thisTrial_13 != None:
        for paramName in thisTrial_13:
            exec('{} = thisTrial_13[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions_intentional_encoding"-------
    # update component parameters for each repeat
    text.setColor('black', colorSpace='rgb')
    text.setPos((position_1x, position_1y))
    text.setText(instructions1)
    text.setFont('Helvetica')
    text.setHeight(0.03)
    instructions_text2.setColor('black', colorSpace='rgb')
    instructions_text2.setPos((position_2x, position_2y))
    instructions_text2.setText(Instructions2)
    instructions_text2.setFont('Helvetica')
    instructions_text2.setHeight(0.03)
    response.keys = []
    response.rt = []
    J_press_instructions.setText(J_key)
    F_key_instruct.setPos((-0.2, -0.2))
    F_key_instruct.setText(K_key)
    arrow.setImage(Image3)
    yes_press.setPos((-0.2, -0.27))
    yes_press.setText(yes_text)
    no_press.setPos((0.2, -0.27))
    no_press.setText(no_text)
    # keep track of which components have finished
    instructions_intentional_encodingComponents = [text, instructions_text2, response, image1, image2, J_press_instructions, F_key_instruct, arrow, yes_press, no_press]
    for thisComponent in instructions_intentional_encodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_intentional_encodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instructions_intentional_encoding"-------
    while continueRoutine:
        # get current time
        t = instructions_intentional_encodingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_intentional_encodingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *instructions_text2* updates
        if instructions_text2.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            instructions_text2.frameNStart = frameN  # exact frame index
            instructions_text2.tStart = t  # local t and not account for scr refresh
            instructions_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text2, 'tStartRefresh')  # time at next scr refresh
            instructions_text2.setAutoDraw(True)
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys.name  # just the first key pressed
                    response.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # *image1* updates
        if image1.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            image1.frameNStart = frameN  # exact frame index
            image1.tStart = t  # local t and not account for scr refresh
            image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
            image1.setAutoDraw(True)
        if image1.status == STARTED:  # only update if drawing
            image1.setPos((0.25, 0), log=False)
            image1.setSize((0.3, 0.3), log=False)
            image1.setImage(Image1, log=False)
        
        # *image2* updates
        if image2.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            image2.frameNStart = frameN  # exact frame index
            image2.tStart = t  # local t and not account for scr refresh
            image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
            image2.setAutoDraw(True)
        if image2.status == STARTED:  # only update if drawing
            image2.setPos((-.25, 0), log=False)
            image2.setSize((0.3, 0.3), log=False)
            image2.setImage(Image2, log=False)
        
        # *J_press_instructions* updates
        if J_press_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J_press_instructions.frameNStart = frameN  # exact frame index
            J_press_instructions.tStart = t  # local t and not account for scr refresh
            J_press_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J_press_instructions, 'tStartRefresh')  # time at next scr refresh
            J_press_instructions.setAutoDraw(True)
        
        # *F_key_instruct* updates
        if F_key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F_key_instruct.frameNStart = frameN  # exact frame index
            F_key_instruct.tStart = t  # local t and not account for scr refresh
            F_key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F_key_instruct, 'tStartRefresh')  # time at next scr refresh
            F_key_instruct.setAutoDraw(True)
        
        # *arrow* updates
        if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            arrow.setAutoDraw(True)
        
        # *yes_press* updates
        if yes_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yes_press.frameNStart = frameN  # exact frame index
            yes_press.tStart = t  # local t and not account for scr refresh
            yes_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yes_press, 'tStartRefresh')  # time at next scr refresh
            yes_press.setAutoDraw(True)
        
        # *no_press* updates
        if no_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no_press.frameNStart = frameN  # exact frame index
            no_press.tStart = t  # local t and not account for scr refresh
            no_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no_press, 'tStartRefresh')  # time at next scr refresh
            no_press.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_intentional_encodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_intentional_encoding"-------
    for thisComponent in instructions_intentional_encodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_13.addData('text.started', text.tStartRefresh)
    trials_13.addData('text.stopped', text.tStopRefresh)
    trials_13.addData('instructions_text2.started', instructions_text2.tStartRefresh)
    trials_13.addData('instructions_text2.stopped', instructions_text2.tStopRefresh)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
    trials_13.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        trials_13.addData('response.rt', response.rt)
    trials_13.addData('response.started', response.tStartRefresh)
    trials_13.addData('response.stopped', response.tStopRefresh)
    trials_13.addData('image1.started', image1.tStartRefresh)
    trials_13.addData('image1.stopped', image1.tStopRefresh)
    trials_13.addData('image2.started', image2.tStartRefresh)
    trials_13.addData('image2.stopped', image2.tStopRefresh)
    trials_13.addData('J_press_instructions.started', J_press_instructions.tStartRefresh)
    trials_13.addData('J_press_instructions.stopped', J_press_instructions.tStopRefresh)
    trials_13.addData('F_key_instruct.started', F_key_instruct.tStartRefresh)
    trials_13.addData('F_key_instruct.stopped', F_key_instruct.tStopRefresh)
    trials_13.addData('arrow.started', arrow.tStartRefresh)
    trials_13.addData('arrow.stopped', arrow.tStopRefresh)
    trials_13.addData('yes_press.started', yes_press.tStartRefresh)
    trials_13.addData('yes_press.stopped', yes_press.tStopRefresh)
    trials_13.addData('no_press.started', no_press.tStartRefresh)
    trials_13.addData('no_press.stopped', no_press.tStopRefresh)
    # the Routine "instructions_intentional_encoding" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_13'


# set up handler to look after randomisation of conditions etc
trials_14 = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/sustained_attention_trials_practice.xlsx', selection='0:2'),
    seed=None, name='trials_14')
thisExp.addLoop(trials_14)  # add the loop to the experiment
thisTrial_14 = trials_14.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
if thisTrial_14 != None:
    for paramName in thisTrial_14:
        exec('{} = thisTrial_14[paramName]'.format(paramName))

for thisTrial_14 in trials_14:
    currentLoop = trials_14
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_14.rgb)
    if thisTrial_14 != None:
        for paramName in thisTrial_14:
            exec('{} = thisTrial_14[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sustained_attention_arrows_practice"-------
    # update component parameters for each repeat
    image_16.setImage(Arrow_direction)
    key_resp_9.keys = []
    key_resp_9.rt = []
    # keep track of which components have finished
    sustained_attention_arrows_practiceComponents = [image_16, key_resp_9, F_press, J_press, left_press, right_press]
    for thisComponent in sustained_attention_arrows_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sustained_attention_arrows_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "sustained_attention_arrows_practice"-------
    while continueRoutine:
        # get current time
        t = sustained_attention_arrows_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sustained_attention_arrows_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_16* updates
        if image_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_16.frameNStart = frameN  # exact frame index
            image_16.tStart = t  # local t and not account for scr refresh
            image_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
            image_16.setAutoDraw(True)
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['j', 'f'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_9.keys == []:  # then this was the first keypress
                    key_resp_9.keys = theseKeys.name  # just the first key pressed
                    key_resp_9.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # *F_press* updates
        if F_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F_press.frameNStart = frameN  # exact frame index
            F_press.tStart = t  # local t and not account for scr refresh
            F_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F_press, 'tStartRefresh')  # time at next scr refresh
            F_press.setAutoDraw(True)
        
        # *J_press* updates
        if J_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            J_press.frameNStart = frameN  # exact frame index
            J_press.tStart = t  # local t and not account for scr refresh
            J_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(J_press, 'tStartRefresh')  # time at next scr refresh
            J_press.setAutoDraw(True)
        
        # *left_press* updates
        if left_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_press.frameNStart = frameN  # exact frame index
            left_press.tStart = t  # local t and not account for scr refresh
            left_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_press, 'tStartRefresh')  # time at next scr refresh
            left_press.setAutoDraw(True)
        
        # *right_press* updates
        if right_press.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_press.frameNStart = frameN  # exact frame index
            right_press.tStart = t  # local t and not account for scr refresh
            right_press.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_press, 'tStartRefresh')  # time at next scr refresh
            right_press.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sustained_attention_arrows_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sustained_attention_arrows_practice"-------
    for thisComponent in sustained_attention_arrows_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_14.addData('image_16.started', image_16.tStartRefresh)
    trials_14.addData('image_16.stopped', image_16.tStopRefresh)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    trials_14.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        trials_14.addData('key_resp_9.rt', key_resp_9.rt)
    trials_14.addData('key_resp_9.started', key_resp_9.tStartRefresh)
    trials_14.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
    trials_14.addData('F_press.started', F_press.tStartRefresh)
    trials_14.addData('F_press.stopped', F_press.tStopRefresh)
    trials_14.addData('J_press.started', J_press.tStartRefresh)
    trials_14.addData('J_press.stopped', J_press.tStopRefresh)
    trials_14.addData('left_press.started', left_press.tStartRefresh)
    trials_14.addData('left_press.stopped', left_press.tStopRefresh)
    trials_14.addData('right_press.started', right_press.tStartRefresh)
    trials_14.addData('right_press.stopped', right_press.tStopRefresh)
    # the Routine "sustained_attention_arrows_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [fixation_]
    for thisComponent in fixation_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixation_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "fixation_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixation_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_* updates
        if fixation_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_.frameNStart = frameN  # exact frame index
            fixation_.tStart = t  # local t and not account for scr refresh
            fixation_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_, 'tStartRefresh')  # time at next scr refresh
            fixation_.setAutoDraw(True)
        if fixation_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_.tStop = t  # not accounting for scr refresh
                fixation_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_, 'tStopRefresh')  # time at next scr refresh
                fixation_.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_2"-------
    for thisComponent in fixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_14.addData('fixation_.started', fixation_.tStartRefresh)
    trials_14.addData('fixation_.stopped', fixation_.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials_14'


# set up handler to look after randomisation of conditions etc
trials_15 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/sustained_attention_trials_practice.xlsx'),
    seed=None, name='trials_15')
thisExp.addLoop(trials_15)  # add the loop to the experiment
thisTrial_15 = trials_15.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
if thisTrial_15 != None:
    for paramName in thisTrial_15:
        exec('{} = thisTrial_15[paramName]'.format(paramName))

for thisTrial_15 in trials_15:
    currentLoop = trials_15
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_15.rgb)
    if thisTrial_15 != None:
        for paramName in thisTrial_15:
            exec('{} = thisTrial_15[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_incidental_encoding"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    incidental_image1_.setImage(incidental_image1)
    incidental_image2_.setImage(incidental_image2)
    key_resp_10.keys = []
    key_resp_10.rt = []
    # keep track of which components have finished
    practice_incidental_encodingComponents = [incidental_image1_, incidental_image2_, text_17, key_resp_10]
    for thisComponent in practice_incidental_encodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_incidental_encodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice_incidental_encoding"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_incidental_encodingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_incidental_encodingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *incidental_image1_* updates
        if incidental_image1_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            incidental_image1_.frameNStart = frameN  # exact frame index
            incidental_image1_.tStart = t  # local t and not account for scr refresh
            incidental_image1_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(incidental_image1_, 'tStartRefresh')  # time at next scr refresh
            incidental_image1_.setAutoDraw(True)
        if incidental_image1_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > incidental_image1_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                incidental_image1_.tStop = t  # not accounting for scr refresh
                incidental_image1_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(incidental_image1_, 'tStopRefresh')  # time at next scr refresh
                incidental_image1_.setAutoDraw(False)
        
        # *incidental_image2_* updates
        if incidental_image2_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            incidental_image2_.frameNStart = frameN  # exact frame index
            incidental_image2_.tStart = t  # local t and not account for scr refresh
            incidental_image2_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(incidental_image2_, 'tStartRefresh')  # time at next scr refresh
            incidental_image2_.setAutoDraw(True)
        if incidental_image2_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > incidental_image2_.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                incidental_image2_.tStop = t  # not accounting for scr refresh
                incidental_image2_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(incidental_image2_, 'tStopRefresh')  # time at next scr refresh
                incidental_image2_.setAutoDraw(False)
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        if text_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_17.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_17.tStop = t  # not accounting for scr refresh
                text_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
                text_17.setAutoDraw(False)
        
        # *key_resp_10* updates
        waitOnFlip = False
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_10.tStop = t  # not accounting for scr refresh
                key_resp_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_10, 'tStopRefresh')  # time at next scr refresh
                key_resp_10.status = FINISHED
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_10.keys = theseKeys.name  # just the last key pressed
                key_resp_10.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_incidental_encodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_incidental_encoding"-------
    for thisComponent in practice_incidental_encodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_15.addData('incidental_image1_.started', incidental_image1_.tStartRefresh)
    trials_15.addData('incidental_image1_.stopped', incidental_image1_.tStopRefresh)
    trials_15.addData('incidental_image2_.started', incidental_image2_.tStartRefresh)
    trials_15.addData('incidental_image2_.stopped', incidental_image2_.tStopRefresh)
    trials_15.addData('text_17.started', text_17.tStartRefresh)
    trials_15.addData('text_17.stopped', text_17.tStopRefresh)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    trials_15.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        trials_15.addData('key_resp_10.rt', key_resp_10.rt)
    trials_15.addData('key_resp_10.started', key_resp_10.tStartRefresh)
    trials_15.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_15'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
