#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Sun Sep 20 22:42:16 2020
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
    originPath='/Users/alexandradecker/Dropbox/Projects/reactivate/reactive_intentional_encoding_looped_lastrun.py',
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
    winType='pyglet', allowGUI=True, allowStencil=False,
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

# Initialize components for Routine "expParam"
expParamClock = core.Clock()

# Initialize components for Routine "instructions_first"
instructions_firstClock = core.Clock()
text_34 = visual.TextStim(win=win, name='text_34',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions_text2_2 = visual.TextStim(win=win, name='instructions_text2_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
response_2 = keyboard.Keyboard()
image1_2 = visual.ImageStim(
    win=win,
    name='image1_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image2_2 = visual.ImageStim(
    win=win,
    name='image2_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
imageA = visual.ImageStim(
    win=win,
    name='imageA', 
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

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "intructions_post_practice_intentional_encoding"
intructions_post_practice_intentional_encodingClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='Great job! Now that you have had practice, you can start the real game. Remember to memorize that the two images go together. It is important you remember because your memory will be tested later. Press space to start the real thing!',
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

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
afc_test_practice = visual.TextStim(win=win, name='afc_test_practice',
    text='Select the correct image',
    font='Arial',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
location1_practice = visual.ImageStim(
    win=win,
    name='location1_practice', 
    image='sin', mask=None,
    ori=0, pos=(-.4, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
location2_practice = visual.ImageStim(
    win=win,
    name='location2_practice', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
location3_practice = visual.ImageStim(
    win=win,
    name='location3_practice', 
    image='sin', mask=None,
    ori=0, pos=(0.4, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
j_key_test_practice = visual.TextStim(win=win, name='j_key_test_practice',
    text='J',
    font='helvetica',
    pos=(-0.4, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
K_key_practice = visual.TextStim(win=win, name='K_key_practice',
    text='K',
    font='Helvetica',
    pos=(0, -.25), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
L_key_practice = visual.TextStim(win=win, name='L_key_practice',
    text='L',
    font='Helvetica',
    pos=(0.4, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None,
    ori=0, pos=(.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
text_7 = visual.TextStim(win=win, name='text_7',
    text='Think of the image pair',
    font='Helvetica',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='Re-study the correct pairs',
    font='Helvetica',
    pos=(0, .3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
key_resp_13 = keyboard.Keyboard()

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

# Initialize components for Routine "think_image_pair"
think_image_pairClock = core.Clock()
instruct_text_3 = visual.TextStim(win=win, name='instruct_text_3',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve_3 = visual.ImageStim(
    win=win,
    name='a_image_retrieve_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "retrieval4"
retrieval4Clock = core.Clock()
afc_text_2 = visual.TextStim(win=win, name='afc_text_2',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
j_key_test_2 = visual.TextStim(win=win, name='j_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
L_key_test_2 = visual.TextStim(win=win, name='L_key_test_2',
    text='L',
    font='Helvetica',
    pos=(0.4, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
K_key_test_2 = visual.TextStim(win=win, name='K_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
correct_image__a = visual.ImageStim(
    win=win,
    name='correct_image__a', 
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
correct_image2_2 = visual.ImageStim(
    win=win,
    name='correct_image2_2', 
    image='sin', mask=None,
    ori=0, pos=(0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='Re-study the correct pairs',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
retrieval_test_resp = keyboard.Keyboard()

# Initialize components for Routine "pre_intentional_encoding4"
pre_intentional_encoding4Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Great job. Keep those image pairs in mind because you will be tested again at the end the experiment. For now, you will learn more image pairs. When you are ready, press the space bar.',
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

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruct_retrieval4"
instruct_retrieval4Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text=' When you are ready to start the memory test, press space bar. ',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "think_image_pair"
think_image_pairClock = core.Clock()
instruct_text_3 = visual.TextStim(win=win, name='instruct_text_3',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve_3 = visual.ImageStim(
    win=win,
    name='a_image_retrieve_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "retrieval4"
retrieval4Clock = core.Clock()
afc_text_2 = visual.TextStim(win=win, name='afc_text_2',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
j_key_test_2 = visual.TextStim(win=win, name='j_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
L_key_test_2 = visual.TextStim(win=win, name='L_key_test_2',
    text='L',
    font='Helvetica',
    pos=(0.4, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
K_key_test_2 = visual.TextStim(win=win, name='K_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
correct_image__a = visual.ImageStim(
    win=win,
    name='correct_image__a', 
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
correct_image2_2 = visual.ImageStim(
    win=win,
    name='correct_image2_2', 
    image='sin', mask=None,
    ori=0, pos=(0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='Re-study the correct pairs',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
retrieval_test_resp = keyboard.Keyboard()

# Initialize components for Routine "pre_intentional_encoding4"
pre_intentional_encoding4Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Great job. Keep those image pairs in mind because you will be tested again at the end the experiment. For now, you will learn more image pairs. When you are ready, press the space bar.',
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

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruct_retrieval4"
instruct_retrieval4Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text=' When you are ready to start the memory test, press space bar. ',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "think_image_pair"
think_image_pairClock = core.Clock()
instruct_text_3 = visual.TextStim(win=win, name='instruct_text_3',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve_3 = visual.ImageStim(
    win=win,
    name='a_image_retrieve_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "retrieval4"
retrieval4Clock = core.Clock()
afc_text_2 = visual.TextStim(win=win, name='afc_text_2',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
j_key_test_2 = visual.TextStim(win=win, name='j_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
L_key_test_2 = visual.TextStim(win=win, name='L_key_test_2',
    text='L',
    font='Helvetica',
    pos=(0.4, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
K_key_test_2 = visual.TextStim(win=win, name='K_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
correct_image__a = visual.ImageStim(
    win=win,
    name='correct_image__a', 
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
correct_image2_2 = visual.ImageStim(
    win=win,
    name='correct_image2_2', 
    image='sin', mask=None,
    ori=0, pos=(0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='Re-study the correct pairs',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
retrieval_test_resp = keyboard.Keyboard()

# Initialize components for Routine "pre_intentional_encoding4"
pre_intentional_encoding4Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Great job. Keep those image pairs in mind because you will be tested again at the end the experiment. For now, you will learn more image pairs. When you are ready, press the space bar.',
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

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruct_retrieval4"
instruct_retrieval4Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text=' When you are ready to start the memory test, press space bar. ',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "think_image_pair"
think_image_pairClock = core.Clock()
instruct_text_3 = visual.TextStim(win=win, name='instruct_text_3',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve_3 = visual.ImageStim(
    win=win,
    name='a_image_retrieve_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "retrieval4"
retrieval4Clock = core.Clock()
afc_text_2 = visual.TextStim(win=win, name='afc_text_2',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
j_key_test_2 = visual.TextStim(win=win, name='j_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
L_key_test_2 = visual.TextStim(win=win, name='L_key_test_2',
    text='L',
    font='Helvetica',
    pos=(0.4, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
K_key_test_2 = visual.TextStim(win=win, name='K_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
correct_image__a = visual.ImageStim(
    win=win,
    name='correct_image__a', 
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
correct_image2_2 = visual.ImageStim(
    win=win,
    name='correct_image2_2', 
    image='sin', mask=None,
    ori=0, pos=(0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='Re-study the correct pairs',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
retrieval_test_resp = keyboard.Keyboard()

# Initialize components for Routine "final_ab_retrieval_test_instruct"
final_ab_retrieval_test_instructClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Now we will test your memory for ALL of the images that you have learned. You will be presented with the correct impair pair after you have made your response. Re-study this. Your memory will be tested later. When you are ready, press space bar to start.',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "think_image_pair"
think_image_pairClock = core.Clock()
instruct_text_3 = visual.TextStim(win=win, name='instruct_text_3',
    text='Think of the image pair',
    font='Arial',
    pos=(0, .20), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve_3 = visual.ImageStim(
    win=win,
    name='a_image_retrieve_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "retrieval4"
retrieval4Clock = core.Clock()
afc_text_2 = visual.TextStim(win=win, name='afc_text_2',
    text='Select the correct image',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
j_key_test_2 = visual.TextStim(win=win, name='j_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
L_key_test_2 = visual.TextStim(win=win, name='L_key_test_2',
    text='L',
    font='Helvetica',
    pos=(0.4, -.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
K_key_test_2 = visual.TextStim(win=win, name='K_key_test_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
correct_image__a = visual.ImageStim(
    win=win,
    name='correct_image__a', 
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
correct_image2_2 = visual.ImageStim(
    win=win,
    name='correct_image2_2', 
    image='sin', mask=None,
    ori=0, pos=(0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='Re-study the correct pairs',
    font='Helvetica',
    pos=(0, .25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
retrieval_test_resp = keyboard.Keyboard()

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

# Initialize components for Routine "small_dog_question"
small_dog_questionClock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='Do the following images, together, weigh more than a small dog?',
    font='helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice_incidental_encoding"
practice_incidental_encodingClock = core.Clock()
incidental_image1_ = visual.ImageStim(
    win=win,
    name='incidental_image1_', 
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
incidental_encoding_resp = keyboard.Keyboard()
text_18 = visual.TextStim(win=win, name='text_18',
    text='F',
    font='Helvetica',
    pos=(-0.2, -0.27), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='J',
    font='Helvetica',
    pos=(0.2, -0.27), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_20 = visual.TextStim(win=win, name='text_20',
    text='Yes',
    font='Helvetica',
    pos=(0.2, -0.32), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='No',
    font='Helvetica',
    pos=(-0.2, -0.32), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
incidental_image2_ = visual.ImageStim(
    win=win,
    name='incidental_image2_', 
    image='sin', mask=None,
    ori=0, pos=(0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

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
arrows_resp = keyboard.Keyboard()
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
    pos=(-0.3, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
right_press = visual.TextStim(win=win, name='right_press',
    text='right',
    font='Helvetica',
    pos=(0.3, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pre_instruct_sustainedAttention"
pre_instruct_sustainedAttentionClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You are now finished with the practice. When you are ready to start the real thing, press space. ',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_14 = keyboard.Keyboard()

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
arrows_resp = keyboard.Keyboard()
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
    pos=(-0.3, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
right_press = visual.TextStim(win=win, name='right_press',
    text='right',
    font='Helvetica',
    pos=(0.3, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "small_dog_question"
small_dog_questionClock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='Do the following images, together, weigh more than a small dog?',
    font='helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "incidental_encoding_real"
incidental_encoding_realClock = core.Clock()
image_A = visual.ImageStim(
    win=win,
    name='image_A', 
    image='sin', mask=None,
    ori=0, pos=(-0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_c = visual.ImageStim(
    win=win,
    name='image_c', 
    image='sin', mask=None,
    ori=0, pos=(0.2, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_resp_15 = keyboard.Keyboard()
text_23 = visual.TextStim(win=win, name='text_23',
    text='F',
    font='Helvetica',
    pos=(-0.2, -0.27), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_24 = visual.TextStim(win=win, name='text_24',
    text='J',
    font='Helvetica',
    pos=(0.2, -0.27), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_25 = visual.TextStim(win=win, name='text_25',
    text='Yes',
    font='Helvetica',
    pos=(0.2, -0.32), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_26 = visual.TextStim(win=win, name='text_26',
    text='No',
    font='Helvetica',
    pos=(-0.2, -0.32), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

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
arrows_resp = keyboard.Keyboard()
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
    pos=(-0.3, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
right_press = visual.TextStim(win=win, name='right_press',
    text='right',
    font='Helvetica',
    pos=(0.3, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pre_instruct_final_memory"
pre_instruct_final_memoryClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pressspace = visual.TextStim(win=win, name='pressspace',
    text='default text',
    font='Helvetica',
    pos=[0,0], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_16 = keyboard.Keyboard()
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
Jkey = visual.TextStim(win=win, name='Jkey',
    text='default text',
    font='Helvetica',
    pos=(0.2, -0.27), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
F_key = visual.TextStim(win=win, name='F_key',
    text='default text',
    font='Helvetica',
    pos=(-0.2, -0.27), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
oldText = visual.TextStim(win=win, name='oldText',
    text='default text',
    font='Helvetica',
    pos=(-0.20, -0.32), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
newtext = visual.TextStim(win=win, name='newtext',
    text='default text',
    font='Helvetica',
    pos=(0.2, -0.32), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "practice_abc_memory_test"
practice_abc_memory_testClock = core.Clock()
imageabc = visual.ImageStim(
    win=win,
    name='imageabc', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
primed_memory_resp = keyboard.Keyboard()
Jkey_2 = visual.TextStim(win=win, name='Jkey_2',
    text='default text',
    font='Helvetica',
    pos=(0.2, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
F_key_2 = visual.TextStim(win=win, name='F_key_2',
    text='default text',
    font='Helvetica',
    pos=(-0.2, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
old = visual.TextStim(win=win, name='old',
    text='default text',
    font='Helvetica',
    pos=(-0.20, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
newtext_2 = visual.TextStim(win=win, name='newtext_2',
    text='default text',
    font='Helvetica',
    pos=(0.2, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pre_instruction_real_abc_final_memory"
pre_instruction_real_abc_final_memoryClock = core.Clock()
text_27 = visual.TextStim(win=win, name='text_27',
    text='Great job! You are now finished the practice. When you are ready to start the real thing, press space!',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_18 = keyboard.Keyboard()

# Initialize components for Routine "practice_abc_memory_test"
practice_abc_memory_testClock = core.Clock()
imageabc = visual.ImageStim(
    win=win,
    name='imageabc', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
primed_memory_resp = keyboard.Keyboard()
Jkey_2 = visual.TextStim(win=win, name='Jkey_2',
    text='default text',
    font='Helvetica',
    pos=(0.2, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
F_key_2 = visual.TextStim(win=win, name='F_key_2',
    text='default text',
    font='Helvetica',
    pos=(-0.2, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
old = visual.TextStim(win=win, name='old',
    text='default text',
    font='Helvetica',
    pos=(-0.20, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
newtext_2 = visual.TextStim(win=win, name='newtext_2',
    text='default text',
    font='Helvetica',
    pos=(0.2, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "questionairre"
questionairreClock = core.Clock()
questioniarre = visual.TextStim(win=win, name='questioniarre',
    text='default text',
    font='Helvetica',
    pos=(0, 0.4), height=.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
questionairre_resp = keyboard.Keyboard()
text_29 = visual.TextStim(win=win, name='text_29',
    text='default text',
    font='Helvetica',
    pos=(0, -0.3), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='sin', mask=None,
    ori=0, pos=(-0.1, 0.13), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='sin', mask=None,
    ori=0, pos=(0.1, 0.13), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image_20 = visual.ImageStim(
    win=win,
    name='image_20', 
    image='sin', mask=None,
    ori=0, pos=(-0.1, -0.1), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image_21 = visual.ImageStim(
    win=win,
    name='image_21', 
    image='sin', mask=None,
    ori=0, pos=(0.1, -0.1), size=(0.15, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
A_txt1 = visual.TextStim(win=win, name='A_txt1',
    text='default text',
    font='Helvetica',
    pos=(-0.1, 0.25), height=0.02, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
B_text = visual.TextStim(win=win, name='B_text',
    text='default text',
    font='Helvetica',
    pos=(0.1, 0.25), height=0.02, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
a_text2 = visual.TextStim(win=win, name='a_text2',
    text='default text',
    font='Helvetica',
    pos=(-0.1, 0), height=0.02, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
C_text = visual.TextStim(win=win, name='C_text',
    text='default text',
    font='Helvetica',
    pos=(0.1, 0), height=0.02, wrapWidth=None, ori=0, 
    color='blue', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "questionairre2"
questionairre2Clock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='default text',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_32 = visual.TextStim(win=win, name='text_32',
    text='default text',
    font='Helvetica',
    pos=(-0.35, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_33 = visual.TextStim(win=win, name='text_33',
    text='default text',
    font='Helvetica',
    pos=(0.35, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
questionairre_resp2 = keyboard.Keyboard()
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=10, labels=[''], scale='', markerStart='5')

# Initialize components for Routine "end"
endClock = core.Clock()
text_28 = visual.TextStim(win=win, name='text_28',
    text='You are now finished the game. Congratulations. Press space to exit.',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
exit = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "expParam"-------
# update component parameters for each repeat
intentional_encoding_path = ('trialorder/' + str(int(expInfo['participant']) % 4) + '_intentional_encoding.csv')
intentional_encoding_test_path = ('trialorder/' + str(int(expInfo['participant']) % 4) + '_intentional_encoding_test.csv')
intentional_encoding_test_final_path = ('trialorder/' + str(int(expInfo['participant']) % 4) + '_intentional_encoding_test_final.csv')
priming_recognition_path = ('trialorder/' + str(int(expInfo['participant']) % 4) + '_priming_recognition_test.csv')

# keep track of which components have finished
expParamComponents = []
for thisComponent in expParamComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
expParamClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "expParam"-------
while continueRoutine:
    # get current time
    t = expParamClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=expParamClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in expParamComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "expParam"-------
for thisComponent in expParamComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "expParam" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_24 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions_first.csv'),
    seed=None, name='trials_24')
thisExp.addLoop(trials_24)  # add the loop to the experiment
thisTrial_24 = trials_24.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
if thisTrial_24 != None:
    for paramName in thisTrial_24:
        exec('{} = thisTrial_24[paramName]'.format(paramName))

for thisTrial_24 in trials_24:
    currentLoop = trials_24
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_24.rgb)
    if thisTrial_24 != None:
        for paramName in thisTrial_24:
            exec('{} = thisTrial_24[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions_first"-------
    # update component parameters for each repeat
    text_34.setColor('black', colorSpace='rgb')
    text_34.setPos((position_1x, position_1y))
    text_34.setText(instructions1)
    text_34.setFont('Helvetica')
    text_34.setHeight(0.03)
    instructions_text2_2.setColor('black', colorSpace='rgb')
    instructions_text2_2.setPos((position_2x, position_2y))
    instructions_text2_2.setText(Instructions2)
    instructions_text2_2.setFont('Helvetica')
    instructions_text2_2.setHeight(0.03)
    response_2.keys = []
    response_2.rt = []
    # keep track of which components have finished
    instructions_firstComponents = [text_34, instructions_text2_2, response_2, image1_2, image2_2]
    for thisComponent in instructions_firstComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_firstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instructions_first"-------
    while continueRoutine:
        # get current time
        t = instructions_firstClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_firstClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_34* updates
        if text_34.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            text_34.frameNStart = frameN  # exact frame index
            text_34.tStart = t  # local t and not account for scr refresh
            text_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_34, 'tStartRefresh')  # time at next scr refresh
            text_34.setAutoDraw(True)
        
        # *instructions_text2_2* updates
        if instructions_text2_2.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            instructions_text2_2.frameNStart = frameN  # exact frame index
            instructions_text2_2.tStart = t  # local t and not account for scr refresh
            instructions_text2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_text2_2, 'tStartRefresh')  # time at next scr refresh
            instructions_text2_2.setAutoDraw(True)
        
        # *response_2* updates
        waitOnFlip = False
        if response_2.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            response_2.frameNStart = frameN  # exact frame index
            response_2.tStart = t  # local t and not account for scr refresh
            response_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_2, 'tStartRefresh')  # time at next scr refresh
            response_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_2.status == STARTED and not waitOnFlip:
            theseKeys = response_2.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if response_2.keys == []:  # then this was the first keypress
                    response_2.keys = theseKeys.name  # just the first key pressed
                    response_2.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # *image1_2* updates
        if image1_2.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            image1_2.frameNStart = frameN  # exact frame index
            image1_2.tStart = t  # local t and not account for scr refresh
            image1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1_2, 'tStartRefresh')  # time at next scr refresh
            image1_2.setAutoDraw(True)
        if image1_2.status == STARTED:  # only update if drawing
            image1_2.setPos((0.25, 0), log=False)
            image1_2.setSize((0.3, 0.3), log=False)
            image1_2.setImage(Image1, log=False)
        
        # *image2_2* updates
        if image2_2.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            image2_2.frameNStart = frameN  # exact frame index
            image2_2.tStart = t  # local t and not account for scr refresh
            image2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2_2, 'tStartRefresh')  # time at next scr refresh
            image2_2.setAutoDraw(True)
        if image2_2.status == STARTED:  # only update if drawing
            image2_2.setPos((-.25, 0), log=False)
            image2_2.setSize((0.3, 0.3), log=False)
            image2_2.setImage(Image2, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_firstComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_first"-------
    for thisComponent in instructions_firstComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_2.keys in ['', [], None]:  # No response was made
        response_2.keys = None
    trials_24.addData('response_2.keys',response_2.keys)
    if response_2.keys != None:  # we had a response
        trials_24.addData('response_2.rt', response_2.rt)
    # the Routine "instructions_first" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
# completed 1 repeats of 'trials_24'


# ------Prepare to start Routine "fixation_2"-------
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
fixation_2Components = [text_31]
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
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
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

# set up handler to look after randomisation of conditions etc
practice_trials_intentional_encoding = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/test_practice.csv', selection='0:5'),
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
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    b_image.setImage(correct_image)
    # keep track of which components have finished
    trialComponents = [imageA, b_image]
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
        
        # *imageA* updates
        if imageA.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            imageA.frameNStart = frameN  # exact frame index
            imageA.tStart = t  # local t and not account for scr refresh
            imageA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageA, 'tStartRefresh')  # time at next scr refresh
            imageA.setAutoDraw(True)
        if imageA.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageA.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                imageA.tStop = t  # not accounting for scr refresh
                imageA.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageA, 'tStopRefresh')  # time at next scr refresh
                imageA.setAutoDraw(False)
        if imageA.status == STARTED:  # only update if drawing
            imageA.setImage(image_a, log=False)
        
        # *b_image* updates
        if b_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            b_image.frameNStart = frameN  # exact frame index
            b_image.tStart = t  # local t and not account for scr refresh
            b_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(b_image, 'tStartRefresh')  # time at next scr refresh
            b_image.setAutoDraw(True)
        if b_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > b_image.tStartRefresh + 3.5-frameTolerance:
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
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
# completed 1 repeats of 'practice_trials_intentional_encoding'


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
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_path, selection='0:12'),
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
    routineTimer.add(3.500000)
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
        if image_pair1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_pair1.frameNStart = frameN  # exact frame index
            image_pair1.tStart = t  # local t and not account for scr refresh
            image_pair1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair1, 'tStartRefresh')  # time at next scr refresh
            image_pair1.setAutoDraw(True)
        if image_pair1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair1.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair1.tStop = t  # not accounting for scr refresh
                image_pair1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair1, 'tStopRefresh')  # time at next scr refresh
                image_pair1.setAutoDraw(False)
        
        # *image_pair2* updates
        if image_pair2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_pair2.frameNStart = frameN  # exact frame index
            image_pair2.tStart = t  # local t and not account for scr refresh
            image_pair2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair2, 'tStartRefresh')  # time at next scr refresh
            image_pair2.setAutoDraw(True)
        if image_pair2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair2.tStartRefresh + 3.5-frameTolerance:
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
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
# completed 1 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions.csv', selection='8:11'),
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
                if key_resp.keys == []:  # then this was the first keypress
                    key_resp.keys = theseKeys.name  # just the first key pressed
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
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials_4.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials_4.addData('key_resp.rt', key_resp.rt)
    # the Routine "instructions_retreival_testing1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trials_4'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions.csv', selection='11:16'),
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
                if key_resp_2.keys == []:  # then this was the first keypress
                    key_resp_2.keys = theseKeys.name  # just the first key pressed
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
            image_6.setImage(Image4, log=False)
        
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
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "instructions_retreival_testing" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/test_practice.csv', selection='0:3'),
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
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    image_a_practice.setImage(image_a)
    location1_practice.setImage(location1)
    location2_practice.setImage(location2)
    location3_practice.setImage(location3)
    image_11.setImage(image_a)
    image_12.setImage(correct_image)
    key_resp_13.keys = []
    key_resp_13.rt = []
    # keep track of which components have finished
    practice_retrieval_after_encodingComponents = [image_a_practice, afc_test_practice, location1_practice, location2_practice, location3_practice, j_key_test_practice, K_key_practice, L_key_practice, image_11, image_12, text_7, text_17, key_resp_13]
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
            if tThisFlipGlobal > afc_test_practice.tStartRefresh + 2-frameTolerance:
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
            if tThisFlipGlobal > location1_practice.tStartRefresh + 2-frameTolerance:
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
            if tThisFlipGlobal > location2_practice.tStartRefresh + 2-frameTolerance:
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
            if tThisFlipGlobal > location3_practice.tStartRefresh + 2-frameTolerance:
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
            if tThisFlipGlobal > j_key_test_practice.tStartRefresh + 2-frameTolerance:
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
            if tThisFlipGlobal > K_key_practice.tStartRefresh + 2-frameTolerance:
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
            if tThisFlipGlobal > L_key_practice.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                L_key_practice.tStop = t  # not accounting for scr refresh
                L_key_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_practice, 'tStopRefresh')  # time at next scr refresh
                L_key_practice.setAutoDraw(False)
        
        # *image_11* updates
        if image_11.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            image_11.frameNStart = frameN  # exact frame index
            image_11.tStart = t  # local t and not account for scr refresh
            image_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
            image_11.setAutoDraw(True)
        if image_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_11.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                image_11.tStop = t  # not accounting for scr refresh
                image_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_11, 'tStopRefresh')  # time at next scr refresh
                image_11.setAutoDraw(False)
        
        # *image_12* updates
        if image_12.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            image_12.frameNStart = frameN  # exact frame index
            image_12.tStart = t  # local t and not account for scr refresh
            image_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
            image_12.setAutoDraw(True)
        if image_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_12.tStartRefresh + 3-frameTolerance:
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
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        if text_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_17.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_17.tStop = t  # not accounting for scr refresh
                text_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
                text_17.setAutoDraw(False)
        
        # *key_resp_13* updates
        waitOnFlip = False
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_13.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_13.tStop = t  # not accounting for scr refresh
                key_resp_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_13, 'tStopRefresh')  # time at next scr refresh
                key_resp_13.status = FINISHED
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_13.keys == []:  # then this was the first keypress
                    key_resp_13.keys = theseKeys.name  # just the first key pressed
                    key_resp_13.rt = theseKeys.rt
        
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
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys = None
    trials_5.addData('key_resp_13.keys',key_resp_13.keys)
    if key_resp_13.keys != None:  # we had a response
        trials_5.addData('key_resp_13.rt', key_resp_13.rt)
# completed 1 repeats of 'trials_5'


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
            if key_resp_4.keys == []:  # then this was the first keypress
                key_resp_4.keys = theseKeys.name  # just the first key pressed
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
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "post_retrievalpractice_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_test_path, selection='0:12'),
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
    
    # ------Prepare to start Routine "think_image_pair"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    think_image_pairComponents = [instruct_text_3, a_image_retrieve_3]
    for thisComponent in think_image_pairComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    think_image_pairClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "think_image_pair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = think_image_pairClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=think_image_pairClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text_3* updates
        if instruct_text_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            instruct_text_3.frameNStart = frameN  # exact frame index
            instruct_text_3.tStart = t  # local t and not account for scr refresh
            instruct_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text_3, 'tStartRefresh')  # time at next scr refresh
            instruct_text_3.setAutoDraw(True)
        if instruct_text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text_3.tStop = t  # not accounting for scr refresh
                instruct_text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text_3, 'tStopRefresh')  # time at next scr refresh
                instruct_text_3.setAutoDraw(False)
        
        # *a_image_retrieve_3* updates
        if a_image_retrieve_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve_3.frameNStart = frameN  # exact frame index
            a_image_retrieve_3.tStart = t  # local t and not account for scr refresh
            a_image_retrieve_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve_3, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve_3.setAutoDraw(True)
        if a_image_retrieve_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve_3.tStop = t  # not accounting for scr refresh
                a_image_retrieve_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve_3, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve_3.setAutoDraw(False)
        if a_image_retrieve_3.status == STARTED:  # only update if drawing
            a_image_retrieve_3.setImage(ImageA, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in think_image_pairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "think_image_pair"-------
    for thisComponent in think_image_pairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
    
    # ------Prepare to start Routine "retrieval4"-------
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    j_key_test_2.setColor('black', colorSpace='rgb')
    j_key_test_2.setPos((-0.4, -0.25))
    j_key_test_2.setFont('Helvetica')
    j_key_test_2.setHeight(0.03)
    K_key_test_2.setColor('black', colorSpace='rgb')
    K_key_test_2.setPos((0, -.25))
    K_key_test_2.setText('K')
    K_key_test_2.setFont('Helvetica')
    K_key_test_2.setHeight(0.03)
    correct_image__a.setImage(ImageA)
    correct_image2_2.setImage(ImageB)
    retrieval_test_resp.keys = []
    retrieval_test_resp.rt = []
    # keep track of which components have finished
    retrieval4Components = [afc_text_2, image_13, image_14, image_15, j_key_test_2, L_key_test_2, K_key_test_2, correct_image__a, correct_image2_2, Feedback_2, retrieval_test_resp]
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
        
        # *afc_text_2* updates
        if afc_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            afc_text_2.frameNStart = frameN  # exact frame index
            afc_text_2.tStart = t  # local t and not account for scr refresh
            afc_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text_2, 'tStartRefresh')  # time at next scr refresh
            afc_text_2.setAutoDraw(True)
        if afc_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                afc_text_2.tStop = t  # not accounting for scr refresh
                afc_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text_2, 'tStopRefresh')  # time at next scr refresh
                afc_text_2.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        if image_13.status == STARTED:  # only update if drawing
            image_13.setPos((-.4, 0), log=False)
            image_13.setImage(location1, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        if image_14.status == STARTED:  # only update if drawing
            image_14.setPos((0, 0), log=False)
            image_14.setImage(location2, log=False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        if image_15.status == STARTED:  # only update if drawing
            image_15.setPos((0.4, 0), log=False)
            image_15.setImage(location3, log=False)
        
        # *j_key_test_2* updates
        if j_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_2.frameNStart = frameN  # exact frame index
            j_key_test_2.tStart = t  # local t and not account for scr refresh
            j_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_2, 'tStartRefresh')  # time at next scr refresh
            j_key_test_2.setAutoDraw(True)
        if j_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_2.tStop = t  # not accounting for scr refresh
                j_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_2, 'tStopRefresh')  # time at next scr refresh
                j_key_test_2.setAutoDraw(False)
        if j_key_test_2.status == STARTED:  # only update if drawing
            j_key_test_2.setText('J', log=False)
        
        # *L_key_test_2* updates
        if L_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            L_key_test_2.frameNStart = frameN  # exact frame index
            L_key_test_2.tStart = t  # local t and not account for scr refresh
            L_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test_2, 'tStartRefresh')  # time at next scr refresh
            L_key_test_2.setAutoDraw(True)
        if L_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test_2.tStop = t  # not accounting for scr refresh
                L_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test_2, 'tStopRefresh')  # time at next scr refresh
                L_key_test_2.setAutoDraw(False)
        
        # *K_key_test_2* updates
        if K_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            K_key_test_2.frameNStart = frameN  # exact frame index
            K_key_test_2.tStart = t  # local t and not account for scr refresh
            K_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test_2, 'tStartRefresh')  # time at next scr refresh
            K_key_test_2.setAutoDraw(True)
        if K_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test_2.tStop = t  # not accounting for scr refresh
                K_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test_2, 'tStopRefresh')  # time at next scr refresh
                K_key_test_2.setAutoDraw(False)
        
        # *correct_image__a* updates
        if correct_image__a.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            correct_image__a.frameNStart = frameN  # exact frame index
            correct_image__a.tStart = t  # local t and not account for scr refresh
            correct_image__a.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image__a, 'tStartRefresh')  # time at next scr refresh
            correct_image__a.setAutoDraw(True)
        if correct_image__a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image__a.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image__a.tStop = t  # not accounting for scr refresh
                correct_image__a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image__a, 'tStopRefresh')  # time at next scr refresh
                correct_image__a.setAutoDraw(False)
        
        # *correct_image2_2* updates
        if correct_image2_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *retrieval_test_resp* updates
        waitOnFlip = False
        if retrieval_test_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            retrieval_test_resp.frameNStart = frameN  # exact frame index
            retrieval_test_resp.tStart = t  # local t and not account for scr refresh
            retrieval_test_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retrieval_test_resp, 'tStartRefresh')  # time at next scr refresh
            retrieval_test_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(retrieval_test_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(retrieval_test_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if retrieval_test_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > retrieval_test_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                retrieval_test_resp.tStop = t  # not accounting for scr refresh
                retrieval_test_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(retrieval_test_resp, 'tStopRefresh')  # time at next scr refresh
                retrieval_test_resp.status = FINISHED
        if retrieval_test_resp.status == STARTED and not waitOnFlip:
            theseKeys = retrieval_test_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l', 'J', 'K', 'L'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if retrieval_test_resp.keys == []:  # then this was the first keypress
                    retrieval_test_resp.keys = theseKeys.name  # just the first key pressed
                    retrieval_test_resp.rt = theseKeys.rt
        
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
    # check responses
    if retrieval_test_resp.keys in ['', [], None]:  # No response was made
        retrieval_test_resp.keys = None
    trials_3.addData('retrieval_test_resp.keys',retrieval_test_resp.keys)
    if retrieval_test_resp.keys != None:  # we had a response
        trials_3.addData('retrieval_test_resp.rt', retrieval_test_resp.rt)
    trials_3.addData('retrieval_test_resp.started', retrieval_test_resp.tStartRefresh)
    trials_3.addData('retrieval_test_resp.stopped', retrieval_test_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


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
            if key_resp_6.keys == []:  # then this was the first keypress
                key_resp_6.keys = theseKeys.name  # just the first key pressed
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
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "pre_intentional_encoding4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_path, selection='12:24'),
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
    routineTimer.add(3.500000)
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
        if image_pair1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_pair1_2.frameNStart = frameN  # exact frame index
            image_pair1_2.tStart = t  # local t and not account for scr refresh
            image_pair1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair1_2, 'tStartRefresh')  # time at next scr refresh
            image_pair1_2.setAutoDraw(True)
        if image_pair1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair1_2.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair1_2.tStop = t  # not accounting for scr refresh
                image_pair1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair1_2, 'tStopRefresh')  # time at next scr refresh
                image_pair1_2.setAutoDraw(False)
        
        # *image_pair2_2* updates
        if image_pair2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_pair2_2.frameNStart = frameN  # exact frame index
            image_pair2_2.tStart = t  # local t and not account for scr refresh
            image_pair2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair2_2, 'tStartRefresh')  # time at next scr refresh
            image_pair2_2.setAutoDraw(True)
        if image_pair2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair2_2.tStartRefresh + 3.5-frameTolerance:
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
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
# completed 1 repeats of 'trials_6'


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
            if key_resp_7.keys == []:  # then this was the first keypress
                key_resp_7.keys = theseKeys.name  # just the first key pressed
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
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "instruct_retrieval4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_test_path, selection='12:24'),
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
    
    # ------Prepare to start Routine "think_image_pair"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    think_image_pairComponents = [instruct_text_3, a_image_retrieve_3]
    for thisComponent in think_image_pairComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    think_image_pairClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "think_image_pair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = think_image_pairClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=think_image_pairClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text_3* updates
        if instruct_text_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            instruct_text_3.frameNStart = frameN  # exact frame index
            instruct_text_3.tStart = t  # local t and not account for scr refresh
            instruct_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text_3, 'tStartRefresh')  # time at next scr refresh
            instruct_text_3.setAutoDraw(True)
        if instruct_text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text_3.tStop = t  # not accounting for scr refresh
                instruct_text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text_3, 'tStopRefresh')  # time at next scr refresh
                instruct_text_3.setAutoDraw(False)
        
        # *a_image_retrieve_3* updates
        if a_image_retrieve_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve_3.frameNStart = frameN  # exact frame index
            a_image_retrieve_3.tStart = t  # local t and not account for scr refresh
            a_image_retrieve_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve_3, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve_3.setAutoDraw(True)
        if a_image_retrieve_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve_3.tStop = t  # not accounting for scr refresh
                a_image_retrieve_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve_3, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve_3.setAutoDraw(False)
        if a_image_retrieve_3.status == STARTED:  # only update if drawing
            a_image_retrieve_3.setImage(ImageA, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in think_image_pairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "think_image_pair"-------
    for thisComponent in think_image_pairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
    
    # ------Prepare to start Routine "retrieval4"-------
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    j_key_test_2.setColor('black', colorSpace='rgb')
    j_key_test_2.setPos((-0.4, -0.25))
    j_key_test_2.setFont('Helvetica')
    j_key_test_2.setHeight(0.03)
    K_key_test_2.setColor('black', colorSpace='rgb')
    K_key_test_2.setPos((0, -.25))
    K_key_test_2.setText('K')
    K_key_test_2.setFont('Helvetica')
    K_key_test_2.setHeight(0.03)
    correct_image__a.setImage(ImageA)
    correct_image2_2.setImage(ImageB)
    retrieval_test_resp.keys = []
    retrieval_test_resp.rt = []
    # keep track of which components have finished
    retrieval4Components = [afc_text_2, image_13, image_14, image_15, j_key_test_2, L_key_test_2, K_key_test_2, correct_image__a, correct_image2_2, Feedback_2, retrieval_test_resp]
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
        
        # *afc_text_2* updates
        if afc_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            afc_text_2.frameNStart = frameN  # exact frame index
            afc_text_2.tStart = t  # local t and not account for scr refresh
            afc_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text_2, 'tStartRefresh')  # time at next scr refresh
            afc_text_2.setAutoDraw(True)
        if afc_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                afc_text_2.tStop = t  # not accounting for scr refresh
                afc_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text_2, 'tStopRefresh')  # time at next scr refresh
                afc_text_2.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        if image_13.status == STARTED:  # only update if drawing
            image_13.setPos((-.4, 0), log=False)
            image_13.setImage(location1, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        if image_14.status == STARTED:  # only update if drawing
            image_14.setPos((0, 0), log=False)
            image_14.setImage(location2, log=False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        if image_15.status == STARTED:  # only update if drawing
            image_15.setPos((0.4, 0), log=False)
            image_15.setImage(location3, log=False)
        
        # *j_key_test_2* updates
        if j_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_2.frameNStart = frameN  # exact frame index
            j_key_test_2.tStart = t  # local t and not account for scr refresh
            j_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_2, 'tStartRefresh')  # time at next scr refresh
            j_key_test_2.setAutoDraw(True)
        if j_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_2.tStop = t  # not accounting for scr refresh
                j_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_2, 'tStopRefresh')  # time at next scr refresh
                j_key_test_2.setAutoDraw(False)
        if j_key_test_2.status == STARTED:  # only update if drawing
            j_key_test_2.setText('J', log=False)
        
        # *L_key_test_2* updates
        if L_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            L_key_test_2.frameNStart = frameN  # exact frame index
            L_key_test_2.tStart = t  # local t and not account for scr refresh
            L_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test_2, 'tStartRefresh')  # time at next scr refresh
            L_key_test_2.setAutoDraw(True)
        if L_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test_2.tStop = t  # not accounting for scr refresh
                L_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test_2, 'tStopRefresh')  # time at next scr refresh
                L_key_test_2.setAutoDraw(False)
        
        # *K_key_test_2* updates
        if K_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            K_key_test_2.frameNStart = frameN  # exact frame index
            K_key_test_2.tStart = t  # local t and not account for scr refresh
            K_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test_2, 'tStartRefresh')  # time at next scr refresh
            K_key_test_2.setAutoDraw(True)
        if K_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test_2.tStop = t  # not accounting for scr refresh
                K_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test_2, 'tStopRefresh')  # time at next scr refresh
                K_key_test_2.setAutoDraw(False)
        
        # *correct_image__a* updates
        if correct_image__a.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            correct_image__a.frameNStart = frameN  # exact frame index
            correct_image__a.tStart = t  # local t and not account for scr refresh
            correct_image__a.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image__a, 'tStartRefresh')  # time at next scr refresh
            correct_image__a.setAutoDraw(True)
        if correct_image__a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image__a.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image__a.tStop = t  # not accounting for scr refresh
                correct_image__a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image__a, 'tStopRefresh')  # time at next scr refresh
                correct_image__a.setAutoDraw(False)
        
        # *correct_image2_2* updates
        if correct_image2_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *retrieval_test_resp* updates
        waitOnFlip = False
        if retrieval_test_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            retrieval_test_resp.frameNStart = frameN  # exact frame index
            retrieval_test_resp.tStart = t  # local t and not account for scr refresh
            retrieval_test_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retrieval_test_resp, 'tStartRefresh')  # time at next scr refresh
            retrieval_test_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(retrieval_test_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(retrieval_test_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if retrieval_test_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > retrieval_test_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                retrieval_test_resp.tStop = t  # not accounting for scr refresh
                retrieval_test_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(retrieval_test_resp, 'tStopRefresh')  # time at next scr refresh
                retrieval_test_resp.status = FINISHED
        if retrieval_test_resp.status == STARTED and not waitOnFlip:
            theseKeys = retrieval_test_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l', 'J', 'K', 'L'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if retrieval_test_resp.keys == []:  # then this was the first keypress
                    retrieval_test_resp.keys = theseKeys.name  # just the first key pressed
                    retrieval_test_resp.rt = theseKeys.rt
        
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
    # check responses
    if retrieval_test_resp.keys in ['', [], None]:  # No response was made
        retrieval_test_resp.keys = None
    trials_7.addData('retrieval_test_resp.keys',retrieval_test_resp.keys)
    if retrieval_test_resp.keys != None:  # we had a response
        trials_7.addData('retrieval_test_resp.rt', retrieval_test_resp.rt)
    trials_7.addData('retrieval_test_resp.started', retrieval_test_resp.tStartRefresh)
    trials_7.addData('retrieval_test_resp.stopped', retrieval_test_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_7'


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
            if key_resp_6.keys == []:  # then this was the first keypress
                key_resp_6.keys = theseKeys.name  # just the first key pressed
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
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "pre_intentional_encoding4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_path, selection='24:36'),
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
    routineTimer.add(3.500000)
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
        if image_pair1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_pair1_2.frameNStart = frameN  # exact frame index
            image_pair1_2.tStart = t  # local t and not account for scr refresh
            image_pair1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair1_2, 'tStartRefresh')  # time at next scr refresh
            image_pair1_2.setAutoDraw(True)
        if image_pair1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair1_2.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair1_2.tStop = t  # not accounting for scr refresh
                image_pair1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair1_2, 'tStopRefresh')  # time at next scr refresh
                image_pair1_2.setAutoDraw(False)
        
        # *image_pair2_2* updates
        if image_pair2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_pair2_2.frameNStart = frameN  # exact frame index
            image_pair2_2.tStart = t  # local t and not account for scr refresh
            image_pair2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair2_2, 'tStartRefresh')  # time at next scr refresh
            image_pair2_2.setAutoDraw(True)
        if image_pair2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair2_2.tStartRefresh + 3.5-frameTolerance:
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
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
# completed 1 repeats of 'trials_8'


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
            if key_resp_7.keys == []:  # then this was the first keypress
                key_resp_7.keys = theseKeys.name  # just the first key pressed
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
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "instruct_retrieval4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_9 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_test_path, selection='24:36'),
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
    
    # ------Prepare to start Routine "think_image_pair"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    think_image_pairComponents = [instruct_text_3, a_image_retrieve_3]
    for thisComponent in think_image_pairComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    think_image_pairClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "think_image_pair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = think_image_pairClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=think_image_pairClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text_3* updates
        if instruct_text_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            instruct_text_3.frameNStart = frameN  # exact frame index
            instruct_text_3.tStart = t  # local t and not account for scr refresh
            instruct_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text_3, 'tStartRefresh')  # time at next scr refresh
            instruct_text_3.setAutoDraw(True)
        if instruct_text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text_3.tStop = t  # not accounting for scr refresh
                instruct_text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text_3, 'tStopRefresh')  # time at next scr refresh
                instruct_text_3.setAutoDraw(False)
        
        # *a_image_retrieve_3* updates
        if a_image_retrieve_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve_3.frameNStart = frameN  # exact frame index
            a_image_retrieve_3.tStart = t  # local t and not account for scr refresh
            a_image_retrieve_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve_3, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve_3.setAutoDraw(True)
        if a_image_retrieve_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve_3.tStop = t  # not accounting for scr refresh
                a_image_retrieve_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve_3, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve_3.setAutoDraw(False)
        if a_image_retrieve_3.status == STARTED:  # only update if drawing
            a_image_retrieve_3.setImage(ImageA, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in think_image_pairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "think_image_pair"-------
    for thisComponent in think_image_pairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
    
    # ------Prepare to start Routine "retrieval4"-------
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    j_key_test_2.setColor('black', colorSpace='rgb')
    j_key_test_2.setPos((-0.4, -0.25))
    j_key_test_2.setFont('Helvetica')
    j_key_test_2.setHeight(0.03)
    K_key_test_2.setColor('black', colorSpace='rgb')
    K_key_test_2.setPos((0, -.25))
    K_key_test_2.setText('K')
    K_key_test_2.setFont('Helvetica')
    K_key_test_2.setHeight(0.03)
    correct_image__a.setImage(ImageA)
    correct_image2_2.setImage(ImageB)
    retrieval_test_resp.keys = []
    retrieval_test_resp.rt = []
    # keep track of which components have finished
    retrieval4Components = [afc_text_2, image_13, image_14, image_15, j_key_test_2, L_key_test_2, K_key_test_2, correct_image__a, correct_image2_2, Feedback_2, retrieval_test_resp]
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
        
        # *afc_text_2* updates
        if afc_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            afc_text_2.frameNStart = frameN  # exact frame index
            afc_text_2.tStart = t  # local t and not account for scr refresh
            afc_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text_2, 'tStartRefresh')  # time at next scr refresh
            afc_text_2.setAutoDraw(True)
        if afc_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                afc_text_2.tStop = t  # not accounting for scr refresh
                afc_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text_2, 'tStopRefresh')  # time at next scr refresh
                afc_text_2.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        if image_13.status == STARTED:  # only update if drawing
            image_13.setPos((-.4, 0), log=False)
            image_13.setImage(location1, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        if image_14.status == STARTED:  # only update if drawing
            image_14.setPos((0, 0), log=False)
            image_14.setImage(location2, log=False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        if image_15.status == STARTED:  # only update if drawing
            image_15.setPos((0.4, 0), log=False)
            image_15.setImage(location3, log=False)
        
        # *j_key_test_2* updates
        if j_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_2.frameNStart = frameN  # exact frame index
            j_key_test_2.tStart = t  # local t and not account for scr refresh
            j_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_2, 'tStartRefresh')  # time at next scr refresh
            j_key_test_2.setAutoDraw(True)
        if j_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_2.tStop = t  # not accounting for scr refresh
                j_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_2, 'tStopRefresh')  # time at next scr refresh
                j_key_test_2.setAutoDraw(False)
        if j_key_test_2.status == STARTED:  # only update if drawing
            j_key_test_2.setText('J', log=False)
        
        # *L_key_test_2* updates
        if L_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            L_key_test_2.frameNStart = frameN  # exact frame index
            L_key_test_2.tStart = t  # local t and not account for scr refresh
            L_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test_2, 'tStartRefresh')  # time at next scr refresh
            L_key_test_2.setAutoDraw(True)
        if L_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test_2.tStop = t  # not accounting for scr refresh
                L_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test_2, 'tStopRefresh')  # time at next scr refresh
                L_key_test_2.setAutoDraw(False)
        
        # *K_key_test_2* updates
        if K_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            K_key_test_2.frameNStart = frameN  # exact frame index
            K_key_test_2.tStart = t  # local t and not account for scr refresh
            K_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test_2, 'tStartRefresh')  # time at next scr refresh
            K_key_test_2.setAutoDraw(True)
        if K_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test_2.tStop = t  # not accounting for scr refresh
                K_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test_2, 'tStopRefresh')  # time at next scr refresh
                K_key_test_2.setAutoDraw(False)
        
        # *correct_image__a* updates
        if correct_image__a.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            correct_image__a.frameNStart = frameN  # exact frame index
            correct_image__a.tStart = t  # local t and not account for scr refresh
            correct_image__a.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image__a, 'tStartRefresh')  # time at next scr refresh
            correct_image__a.setAutoDraw(True)
        if correct_image__a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image__a.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image__a.tStop = t  # not accounting for scr refresh
                correct_image__a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image__a, 'tStopRefresh')  # time at next scr refresh
                correct_image__a.setAutoDraw(False)
        
        # *correct_image2_2* updates
        if correct_image2_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *retrieval_test_resp* updates
        waitOnFlip = False
        if retrieval_test_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            retrieval_test_resp.frameNStart = frameN  # exact frame index
            retrieval_test_resp.tStart = t  # local t and not account for scr refresh
            retrieval_test_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retrieval_test_resp, 'tStartRefresh')  # time at next scr refresh
            retrieval_test_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(retrieval_test_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(retrieval_test_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if retrieval_test_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > retrieval_test_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                retrieval_test_resp.tStop = t  # not accounting for scr refresh
                retrieval_test_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(retrieval_test_resp, 'tStopRefresh')  # time at next scr refresh
                retrieval_test_resp.status = FINISHED
        if retrieval_test_resp.status == STARTED and not waitOnFlip:
            theseKeys = retrieval_test_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l', 'J', 'K', 'L'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if retrieval_test_resp.keys == []:  # then this was the first keypress
                    retrieval_test_resp.keys = theseKeys.name  # just the first key pressed
                    retrieval_test_resp.rt = theseKeys.rt
        
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
    # check responses
    if retrieval_test_resp.keys in ['', [], None]:  # No response was made
        retrieval_test_resp.keys = None
    trials_9.addData('retrieval_test_resp.keys',retrieval_test_resp.keys)
    if retrieval_test_resp.keys != None:  # we had a response
        trials_9.addData('retrieval_test_resp.rt', retrieval_test_resp.rt)
    trials_9.addData('retrieval_test_resp.started', retrieval_test_resp.tStartRefresh)
    trials_9.addData('retrieval_test_resp.stopped', retrieval_test_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_9'


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
            if key_resp_6.keys == []:  # then this was the first keypress
                key_resp_6.keys = theseKeys.name  # just the first key pressed
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
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "pre_intentional_encoding4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_10 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_path, selection='36:48'),
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
    routineTimer.add(3.500000)
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
        if image_pair1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_pair1_2.frameNStart = frameN  # exact frame index
            image_pair1_2.tStart = t  # local t and not account for scr refresh
            image_pair1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair1_2, 'tStartRefresh')  # time at next scr refresh
            image_pair1_2.setAutoDraw(True)
        if image_pair1_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair1_2.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                image_pair1_2.tStop = t  # not accounting for scr refresh
                image_pair1_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_pair1_2, 'tStopRefresh')  # time at next scr refresh
                image_pair1_2.setAutoDraw(False)
        
        # *image_pair2_2* updates
        if image_pair2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_pair2_2.frameNStart = frameN  # exact frame index
            image_pair2_2.tStart = t  # local t and not account for scr refresh
            image_pair2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_pair2_2, 'tStartRefresh')  # time at next scr refresh
            image_pair2_2.setAutoDraw(True)
        if image_pair2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_pair2_2.tStartRefresh + 3.5-frameTolerance:
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
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
# completed 1 repeats of 'trials_10'


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
            if key_resp_7.keys == []:  # then this was the first keypress
                key_resp_7.keys = theseKeys.name  # just the first key pressed
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
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "instruct_retrieval4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_11 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_test_path, selection='36:48'),
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
    
    # ------Prepare to start Routine "think_image_pair"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    think_image_pairComponents = [instruct_text_3, a_image_retrieve_3]
    for thisComponent in think_image_pairComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    think_image_pairClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "think_image_pair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = think_image_pairClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=think_image_pairClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text_3* updates
        if instruct_text_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            instruct_text_3.frameNStart = frameN  # exact frame index
            instruct_text_3.tStart = t  # local t and not account for scr refresh
            instruct_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text_3, 'tStartRefresh')  # time at next scr refresh
            instruct_text_3.setAutoDraw(True)
        if instruct_text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text_3.tStop = t  # not accounting for scr refresh
                instruct_text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text_3, 'tStopRefresh')  # time at next scr refresh
                instruct_text_3.setAutoDraw(False)
        
        # *a_image_retrieve_3* updates
        if a_image_retrieve_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve_3.frameNStart = frameN  # exact frame index
            a_image_retrieve_3.tStart = t  # local t and not account for scr refresh
            a_image_retrieve_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve_3, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve_3.setAutoDraw(True)
        if a_image_retrieve_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve_3.tStop = t  # not accounting for scr refresh
                a_image_retrieve_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve_3, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve_3.setAutoDraw(False)
        if a_image_retrieve_3.status == STARTED:  # only update if drawing
            a_image_retrieve_3.setImage(ImageA, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in think_image_pairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "think_image_pair"-------
    for thisComponent in think_image_pairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
    
    # ------Prepare to start Routine "retrieval4"-------
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    j_key_test_2.setColor('black', colorSpace='rgb')
    j_key_test_2.setPos((-0.4, -0.25))
    j_key_test_2.setFont('Helvetica')
    j_key_test_2.setHeight(0.03)
    K_key_test_2.setColor('black', colorSpace='rgb')
    K_key_test_2.setPos((0, -.25))
    K_key_test_2.setText('K')
    K_key_test_2.setFont('Helvetica')
    K_key_test_2.setHeight(0.03)
    correct_image__a.setImage(ImageA)
    correct_image2_2.setImage(ImageB)
    retrieval_test_resp.keys = []
    retrieval_test_resp.rt = []
    # keep track of which components have finished
    retrieval4Components = [afc_text_2, image_13, image_14, image_15, j_key_test_2, L_key_test_2, K_key_test_2, correct_image__a, correct_image2_2, Feedback_2, retrieval_test_resp]
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
        
        # *afc_text_2* updates
        if afc_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            afc_text_2.frameNStart = frameN  # exact frame index
            afc_text_2.tStart = t  # local t and not account for scr refresh
            afc_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text_2, 'tStartRefresh')  # time at next scr refresh
            afc_text_2.setAutoDraw(True)
        if afc_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                afc_text_2.tStop = t  # not accounting for scr refresh
                afc_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text_2, 'tStopRefresh')  # time at next scr refresh
                afc_text_2.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        if image_13.status == STARTED:  # only update if drawing
            image_13.setPos((-.4, 0), log=False)
            image_13.setImage(location1, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        if image_14.status == STARTED:  # only update if drawing
            image_14.setPos((0, 0), log=False)
            image_14.setImage(location2, log=False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        if image_15.status == STARTED:  # only update if drawing
            image_15.setPos((0.4, 0), log=False)
            image_15.setImage(location3, log=False)
        
        # *j_key_test_2* updates
        if j_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_2.frameNStart = frameN  # exact frame index
            j_key_test_2.tStart = t  # local t and not account for scr refresh
            j_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_2, 'tStartRefresh')  # time at next scr refresh
            j_key_test_2.setAutoDraw(True)
        if j_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_2.tStop = t  # not accounting for scr refresh
                j_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_2, 'tStopRefresh')  # time at next scr refresh
                j_key_test_2.setAutoDraw(False)
        if j_key_test_2.status == STARTED:  # only update if drawing
            j_key_test_2.setText('J', log=False)
        
        # *L_key_test_2* updates
        if L_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            L_key_test_2.frameNStart = frameN  # exact frame index
            L_key_test_2.tStart = t  # local t and not account for scr refresh
            L_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test_2, 'tStartRefresh')  # time at next scr refresh
            L_key_test_2.setAutoDraw(True)
        if L_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test_2.tStop = t  # not accounting for scr refresh
                L_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test_2, 'tStopRefresh')  # time at next scr refresh
                L_key_test_2.setAutoDraw(False)
        
        # *K_key_test_2* updates
        if K_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            K_key_test_2.frameNStart = frameN  # exact frame index
            K_key_test_2.tStart = t  # local t and not account for scr refresh
            K_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test_2, 'tStartRefresh')  # time at next scr refresh
            K_key_test_2.setAutoDraw(True)
        if K_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test_2.tStop = t  # not accounting for scr refresh
                K_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test_2, 'tStopRefresh')  # time at next scr refresh
                K_key_test_2.setAutoDraw(False)
        
        # *correct_image__a* updates
        if correct_image__a.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            correct_image__a.frameNStart = frameN  # exact frame index
            correct_image__a.tStart = t  # local t and not account for scr refresh
            correct_image__a.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image__a, 'tStartRefresh')  # time at next scr refresh
            correct_image__a.setAutoDraw(True)
        if correct_image__a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image__a.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image__a.tStop = t  # not accounting for scr refresh
                correct_image__a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image__a, 'tStopRefresh')  # time at next scr refresh
                correct_image__a.setAutoDraw(False)
        
        # *correct_image2_2* updates
        if correct_image2_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *retrieval_test_resp* updates
        waitOnFlip = False
        if retrieval_test_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            retrieval_test_resp.frameNStart = frameN  # exact frame index
            retrieval_test_resp.tStart = t  # local t and not account for scr refresh
            retrieval_test_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retrieval_test_resp, 'tStartRefresh')  # time at next scr refresh
            retrieval_test_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(retrieval_test_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(retrieval_test_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if retrieval_test_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > retrieval_test_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                retrieval_test_resp.tStop = t  # not accounting for scr refresh
                retrieval_test_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(retrieval_test_resp, 'tStopRefresh')  # time at next scr refresh
                retrieval_test_resp.status = FINISHED
        if retrieval_test_resp.status == STARTED and not waitOnFlip:
            theseKeys = retrieval_test_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l', 'J', 'K', 'L'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if retrieval_test_resp.keys == []:  # then this was the first keypress
                    retrieval_test_resp.keys = theseKeys.name  # just the first key pressed
                    retrieval_test_resp.rt = theseKeys.rt
        
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
    # check responses
    if retrieval_test_resp.keys in ['', [], None]:  # No response was made
        retrieval_test_resp.keys = None
    trials_11.addData('retrieval_test_resp.keys',retrieval_test_resp.keys)
    if retrieval_test_resp.keys != None:  # we had a response
        trials_11.addData('retrieval_test_resp.rt', retrieval_test_resp.rt)
    trials_11.addData('retrieval_test_resp.started', retrieval_test_resp.tStartRefresh)
    trials_11.addData('retrieval_test_resp.stopped', retrieval_test_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_11'


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
            if key_resp_8.keys == []:  # then this was the first keypress
                key_resp_8.keys = theseKeys.name  # just the first key pressed
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
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "final_ab_retrieval_test_instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_12 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_test_final_path),
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
    
    # ------Prepare to start Routine "think_image_pair"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    think_image_pairComponents = [instruct_text_3, a_image_retrieve_3]
    for thisComponent in think_image_pairComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    think_image_pairClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "think_image_pair"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = think_image_pairClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=think_image_pairClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text_3* updates
        if instruct_text_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            instruct_text_3.frameNStart = frameN  # exact frame index
            instruct_text_3.tStart = t  # local t and not account for scr refresh
            instruct_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text_3, 'tStartRefresh')  # time at next scr refresh
            instruct_text_3.setAutoDraw(True)
        if instruct_text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruct_text_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                instruct_text_3.tStop = t  # not accounting for scr refresh
                instruct_text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruct_text_3, 'tStopRefresh')  # time at next scr refresh
                instruct_text_3.setAutoDraw(False)
        
        # *a_image_retrieve_3* updates
        if a_image_retrieve_3.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            a_image_retrieve_3.frameNStart = frameN  # exact frame index
            a_image_retrieve_3.tStart = t  # local t and not account for scr refresh
            a_image_retrieve_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image_retrieve_3, 'tStartRefresh')  # time at next scr refresh
            a_image_retrieve_3.setAutoDraw(True)
        if a_image_retrieve_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image_retrieve_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                a_image_retrieve_3.tStop = t  # not accounting for scr refresh
                a_image_retrieve_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image_retrieve_3, 'tStopRefresh')  # time at next scr refresh
                a_image_retrieve_3.setAutoDraw(False)
        if a_image_retrieve_3.status == STARTED:  # only update if drawing
            a_image_retrieve_3.setImage(ImageA, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in think_image_pairComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "think_image_pair"-------
    for thisComponent in think_image_pairComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
    
    # ------Prepare to start Routine "retrieval4"-------
    routineTimer.add(4.500000)
    # update component parameters for each repeat
    j_key_test_2.setColor('black', colorSpace='rgb')
    j_key_test_2.setPos((-0.4, -0.25))
    j_key_test_2.setFont('Helvetica')
    j_key_test_2.setHeight(0.03)
    K_key_test_2.setColor('black', colorSpace='rgb')
    K_key_test_2.setPos((0, -.25))
    K_key_test_2.setText('K')
    K_key_test_2.setFont('Helvetica')
    K_key_test_2.setHeight(0.03)
    correct_image__a.setImage(ImageA)
    correct_image2_2.setImage(ImageB)
    retrieval_test_resp.keys = []
    retrieval_test_resp.rt = []
    # keep track of which components have finished
    retrieval4Components = [afc_text_2, image_13, image_14, image_15, j_key_test_2, L_key_test_2, K_key_test_2, correct_image__a, correct_image2_2, Feedback_2, retrieval_test_resp]
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
        
        # *afc_text_2* updates
        if afc_text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            afc_text_2.frameNStart = frameN  # exact frame index
            afc_text_2.tStart = t  # local t and not account for scr refresh
            afc_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(afc_text_2, 'tStartRefresh')  # time at next scr refresh
            afc_text_2.setAutoDraw(True)
        if afc_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > afc_text_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                afc_text_2.tStop = t  # not accounting for scr refresh
                afc_text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(afc_text_2, 'tStopRefresh')  # time at next scr refresh
                afc_text_2.setAutoDraw(False)
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        if image_13.status == STARTED:  # only update if drawing
            image_13.setPos((-.4, 0), log=False)
            image_13.setImage(location1, log=False)
        
        # *image_14* updates
        if image_14.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_14.frameNStart = frameN  # exact frame index
            image_14.tStart = t  # local t and not account for scr refresh
            image_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
            image_14.setAutoDraw(True)
        if image_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_14.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_14.tStop = t  # not accounting for scr refresh
                image_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
                image_14.setAutoDraw(False)
        if image_14.status == STARTED:  # only update if drawing
            image_14.setPos((0, 0), log=False)
            image_14.setImage(location2, log=False)
        
        # *image_15* updates
        if image_15.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            image_15.frameNStart = frameN  # exact frame index
            image_15.tStart = t  # local t and not account for scr refresh
            image_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
            image_15.setAutoDraw(True)
        if image_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_15.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_15.tStop = t  # not accounting for scr refresh
                image_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
                image_15.setAutoDraw(False)
        if image_15.status == STARTED:  # only update if drawing
            image_15.setPos((0.4, 0), log=False)
            image_15.setImage(location3, log=False)
        
        # *j_key_test_2* updates
        if j_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            j_key_test_2.frameNStart = frameN  # exact frame index
            j_key_test_2.tStart = t  # local t and not account for scr refresh
            j_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(j_key_test_2, 'tStartRefresh')  # time at next scr refresh
            j_key_test_2.setAutoDraw(True)
        if j_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > j_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                j_key_test_2.tStop = t  # not accounting for scr refresh
                j_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(j_key_test_2, 'tStopRefresh')  # time at next scr refresh
                j_key_test_2.setAutoDraw(False)
        if j_key_test_2.status == STARTED:  # only update if drawing
            j_key_test_2.setText('J', log=False)
        
        # *L_key_test_2* updates
        if L_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            L_key_test_2.frameNStart = frameN  # exact frame index
            L_key_test_2.tStart = t  # local t and not account for scr refresh
            L_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_key_test_2, 'tStartRefresh')  # time at next scr refresh
            L_key_test_2.setAutoDraw(True)
        if L_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > L_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                L_key_test_2.tStop = t  # not accounting for scr refresh
                L_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(L_key_test_2, 'tStopRefresh')  # time at next scr refresh
                L_key_test_2.setAutoDraw(False)
        
        # *K_key_test_2* updates
        if K_key_test_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            K_key_test_2.frameNStart = frameN  # exact frame index
            K_key_test_2.tStart = t  # local t and not account for scr refresh
            K_key_test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(K_key_test_2, 'tStartRefresh')  # time at next scr refresh
            K_key_test_2.setAutoDraw(True)
        if K_key_test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > K_key_test_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                K_key_test_2.tStop = t  # not accounting for scr refresh
                K_key_test_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(K_key_test_2, 'tStopRefresh')  # time at next scr refresh
                K_key_test_2.setAutoDraw(False)
        
        # *correct_image__a* updates
        if correct_image__a.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            correct_image__a.frameNStart = frameN  # exact frame index
            correct_image__a.tStart = t  # local t and not account for scr refresh
            correct_image__a.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_image__a, 'tStartRefresh')  # time at next scr refresh
            correct_image__a.setAutoDraw(True)
        if correct_image__a.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_image__a.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                correct_image__a.tStop = t  # not accounting for scr refresh
                correct_image__a.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_image__a, 'tStopRefresh')  # time at next scr refresh
                correct_image__a.setAutoDraw(False)
        
        # *correct_image2_2* updates
        if correct_image2_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
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
        
        # *retrieval_test_resp* updates
        waitOnFlip = False
        if retrieval_test_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            retrieval_test_resp.frameNStart = frameN  # exact frame index
            retrieval_test_resp.tStart = t  # local t and not account for scr refresh
            retrieval_test_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retrieval_test_resp, 'tStartRefresh')  # time at next scr refresh
            retrieval_test_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(retrieval_test_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(retrieval_test_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if retrieval_test_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > retrieval_test_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                retrieval_test_resp.tStop = t  # not accounting for scr refresh
                retrieval_test_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(retrieval_test_resp, 'tStopRefresh')  # time at next scr refresh
                retrieval_test_resp.status = FINISHED
        if retrieval_test_resp.status == STARTED and not waitOnFlip:
            theseKeys = retrieval_test_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l', 'J', 'K', 'L'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if retrieval_test_resp.keys == []:  # then this was the first keypress
                    retrieval_test_resp.keys = theseKeys.name  # just the first key pressed
                    retrieval_test_resp.rt = theseKeys.rt
        
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
    # check responses
    if retrieval_test_resp.keys in ['', [], None]:  # No response was made
        retrieval_test_resp.keys = None
    trials_12.addData('retrieval_test_resp.keys',retrieval_test_resp.keys)
    if retrieval_test_resp.keys != None:  # we had a response
        trials_12.addData('retrieval_test_resp.rt', retrieval_test_resp.rt)
    trials_12.addData('retrieval_test_resp.started', retrieval_test_resp.tStartRefresh)
    trials_12.addData('retrieval_test_resp.stopped', retrieval_test_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_12'


# set up handler to look after randomisation of conditions etc
trials_13 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions.csv', selection='16:22'),
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
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
    trials_13.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        trials_13.addData('response.rt', response.rt)
    # the Routine "instructions_intentional_encoding" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trials_13'


# set up handler to look after randomisation of conditions etc
trials_15 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/phase2_practice.xlsx'),
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
    
    # ------Prepare to start Routine "small_dog_question"-------
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    small_dog_questionComponents = [text_22]
    for thisComponent in small_dog_questionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    small_dog_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "small_dog_question"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = small_dog_questionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=small_dog_questionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_22* updates
        if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_22.frameNStart = frameN  # exact frame index
            text_22.tStart = t  # local t and not account for scr refresh
            text_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
            text_22.setAutoDraw(True)
        if text_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_22.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_22.tStop = t  # not accounting for scr refresh
                text_22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_22, 'tStopRefresh')  # time at next scr refresh
                text_22.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in small_dog_questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "small_dog_question"-------
    for thisComponent in small_dog_questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
    
    # ------Prepare to start Routine "practice_incidental_encoding"-------
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    incidental_image1_.setImage(incidental_image1)
    incidental_encoding_resp.keys = []
    incidental_encoding_resp.rt = []
    incidental_image2_.setImage(incidental_image2)
    # keep track of which components have finished
    practice_incidental_encodingComponents = [incidental_image1_, incidental_encoding_resp, text_18, text_19, text_20, text_21, incidental_image2_]
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
            if tThisFlipGlobal > incidental_image1_.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                incidental_image1_.tStop = t  # not accounting for scr refresh
                incidental_image1_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(incidental_image1_, 'tStopRefresh')  # time at next scr refresh
                incidental_image1_.setAutoDraw(False)
        
        # *incidental_encoding_resp* updates
        waitOnFlip = False
        if incidental_encoding_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            incidental_encoding_resp.frameNStart = frameN  # exact frame index
            incidental_encoding_resp.tStart = t  # local t and not account for scr refresh
            incidental_encoding_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(incidental_encoding_resp, 'tStartRefresh')  # time at next scr refresh
            incidental_encoding_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(incidental_encoding_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(incidental_encoding_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if incidental_encoding_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > incidental_encoding_resp.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                incidental_encoding_resp.tStop = t  # not accounting for scr refresh
                incidental_encoding_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(incidental_encoding_resp, 'tStopRefresh')  # time at next scr refresh
                incidental_encoding_resp.status = FINISHED
        if incidental_encoding_resp.status == STARTED and not waitOnFlip:
            theseKeys = incidental_encoding_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if incidental_encoding_resp.keys == []:  # then this was the first keypress
                    incidental_encoding_resp.keys = theseKeys.name  # just the first key pressed
                    incidental_encoding_resp.rt = theseKeys.rt
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            text_18.setAutoDraw(True)
        if text_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_18.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_18.tStop = t  # not accounting for scr refresh
                text_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_18, 'tStopRefresh')  # time at next scr refresh
                text_18.setAutoDraw(False)
        
        # *text_19* updates
        if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_19.frameNStart = frameN  # exact frame index
            text_19.tStart = t  # local t and not account for scr refresh
            text_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
            text_19.setAutoDraw(True)
        if text_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_19.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_19.tStop = t  # not accounting for scr refresh
                text_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_19, 'tStopRefresh')  # time at next scr refresh
                text_19.setAutoDraw(False)
        
        # *text_20* updates
        if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_20.frameNStart = frameN  # exact frame index
            text_20.tStart = t  # local t and not account for scr refresh
            text_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
            text_20.setAutoDraw(True)
        if text_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_20.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_20.tStop = t  # not accounting for scr refresh
                text_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_20, 'tStopRefresh')  # time at next scr refresh
                text_20.setAutoDraw(False)
        
        # *text_21* updates
        if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            text_21.setAutoDraw(True)
        if text_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_21.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_21.tStop = t  # not accounting for scr refresh
                text_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
                text_21.setAutoDraw(False)
        
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
            if tThisFlipGlobal > incidental_image2_.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                incidental_image2_.tStop = t  # not accounting for scr refresh
                incidental_image2_.frameNStop = frameN  # exact frame index
                win.timeOnFlip(incidental_image2_, 'tStopRefresh')  # time at next scr refresh
                incidental_image2_.setAutoDraw(False)
        
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
    # check responses
    if incidental_encoding_resp.keys in ['', [], None]:  # No response was made
        incidental_encoding_resp.keys = None
    trials_15.addData('incidental_encoding_resp.keys',incidental_encoding_resp.keys)
    if incidental_encoding_resp.keys != None:  # we had a response
        trials_15.addData('incidental_encoding_resp.rt', incidental_encoding_resp.rt)
    
    # set up handler to look after randomisation of conditions etc
    trials_14 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trialorder/phase2_practice.xlsx'),
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
        arrows_resp.keys = []
        arrows_resp.rt = []
        # keep track of which components have finished
        sustained_attention_arrows_practiceComponents = [image_16, arrows_resp, F_press, J_press, left_press, right_press]
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
            
            # *arrows_resp* updates
            waitOnFlip = False
            if arrows_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrows_resp.frameNStart = frameN  # exact frame index
                arrows_resp.tStart = t  # local t and not account for scr refresh
                arrows_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrows_resp, 'tStartRefresh')  # time at next scr refresh
                arrows_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(arrows_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(arrows_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if arrows_resp.status == STARTED and not waitOnFlip:
                theseKeys = arrows_resp.getKeys(keyList=['j', 'f', 'J', 'F'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if arrows_resp.keys == []:  # then this was the first keypress
                        arrows_resp.keys = theseKeys.name  # just the first key pressed
                        arrows_resp.rt = theseKeys.rt
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
        # check responses
        if arrows_resp.keys in ['', [], None]:  # No response was made
            arrows_resp.keys = None
        trials_14.addData('arrows_resp.keys',arrows_resp.keys)
        if arrows_resp.keys != None:  # we had a response
            trials_14.addData('arrows_resp.rt', arrows_resp.rt)
        trials_14.addData('arrows_resp.started', arrows_resp.tStartRefresh)
        trials_14.addData('arrows_resp.stopped', arrows_resp.tStopRefresh)
        # the Routine "sustained_attention_arrows_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixation_2"-------
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixation_2Components = [text_31]
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
            
            # *text_31* updates
            if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_31.frameNStart = frameN  # exact frame index
                text_31.tStart = t  # local t and not account for scr refresh
                text_31.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
                text_31.setAutoDraw(True)
            if text_31.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_31.tStop = t  # not accounting for scr refresh
                    text_31.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                    text_31.setAutoDraw(False)
            
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
    # completed 1 repeats of 'trials_14'
    
# completed 1 repeats of 'trials_15'


# ------Prepare to start Routine "pre_instruct_sustainedAttention"-------
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
# keep track of which components have finished
pre_instruct_sustainedAttentionComponents = [text_2, key_resp_14]
for thisComponent in pre_instruct_sustainedAttentionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pre_instruct_sustainedAttentionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "pre_instruct_sustainedAttention"-------
while continueRoutine:
    # get current time
    t = pre_instruct_sustainedAttentionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pre_instruct_sustainedAttentionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            if key_resp_14.keys == []:  # then this was the first keypress
                key_resp_14.keys = theseKeys.name  # just the first key pressed
                key_resp_14.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_instruct_sustainedAttentionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pre_instruct_sustainedAttention"-------
for thisComponent in pre_instruct_sustainedAttentionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.nextEntry()
# the Routine "pre_instruct_sustainedAttention" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_18 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/phase2_practice.xlsx'),
    seed=None, name='trials_18')
thisExp.addLoop(trials_18)  # add the loop to the experiment
thisTrial_18 = trials_18.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
if thisTrial_18 != None:
    for paramName in thisTrial_18:
        exec('{} = thisTrial_18[paramName]'.format(paramName))

for thisTrial_18 in trials_18:
    currentLoop = trials_18
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_18.rgb)
    if thisTrial_18 != None:
        for paramName in thisTrial_18:
            exec('{} = thisTrial_18[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sustained_attention_arrows_practice"-------
    # update component parameters for each repeat
    image_16.setImage(Arrow_direction)
    arrows_resp.keys = []
    arrows_resp.rt = []
    # keep track of which components have finished
    sustained_attention_arrows_practiceComponents = [image_16, arrows_resp, F_press, J_press, left_press, right_press]
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
        
        # *arrows_resp* updates
        waitOnFlip = False
        if arrows_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrows_resp.frameNStart = frameN  # exact frame index
            arrows_resp.tStart = t  # local t and not account for scr refresh
            arrows_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrows_resp, 'tStartRefresh')  # time at next scr refresh
            arrows_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(arrows_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(arrows_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if arrows_resp.status == STARTED and not waitOnFlip:
            theseKeys = arrows_resp.getKeys(keyList=['j', 'f', 'J', 'F'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if arrows_resp.keys == []:  # then this was the first keypress
                    arrows_resp.keys = theseKeys.name  # just the first key pressed
                    arrows_resp.rt = theseKeys.rt
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
    # check responses
    if arrows_resp.keys in ['', [], None]:  # No response was made
        arrows_resp.keys = None
    trials_18.addData('arrows_resp.keys',arrows_resp.keys)
    if arrows_resp.keys != None:  # we had a response
        trials_18.addData('arrows_resp.rt', arrows_resp.rt)
    trials_18.addData('arrows_resp.started', arrows_resp.tStartRefresh)
    trials_18.addData('arrows_resp.stopped', arrows_resp.tStopRefresh)
    # the Routine "sustained_attention_arrows_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_18'


# set up handler to look after randomisation of conditions etc
trials_17 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(intentional_encoding_test_path),
    seed=None, name='trials_17')
thisExp.addLoop(trials_17)  # add the loop to the experiment
thisTrial_17 = trials_17.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
if thisTrial_17 != None:
    for paramName in thisTrial_17:
        exec('{} = thisTrial_17[paramName]'.format(paramName))

for thisTrial_17 in trials_17:
    currentLoop = trials_17
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_17.rgb)
    if thisTrial_17 != None:
        for paramName in thisTrial_17:
            exec('{} = thisTrial_17[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "small_dog_question"-------
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    small_dog_questionComponents = [text_22]
    for thisComponent in small_dog_questionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    small_dog_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "small_dog_question"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = small_dog_questionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=small_dog_questionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_22* updates
        if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_22.frameNStart = frameN  # exact frame index
            text_22.tStart = t  # local t and not account for scr refresh
            text_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
            text_22.setAutoDraw(True)
        if text_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_22.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_22.tStop = t  # not accounting for scr refresh
                text_22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_22, 'tStopRefresh')  # time at next scr refresh
                text_22.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in small_dog_questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "small_dog_question"-------
    for thisComponent in small_dog_questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
    
    # ------Prepare to start Routine "incidental_encoding_real"-------
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    image_A.setImage(ImageA)
    image_c.setImage(ImageC)
    key_resp_15.keys = []
    key_resp_15.rt = []
    # keep track of which components have finished
    incidental_encoding_realComponents = [image_A, image_c, key_resp_15, text_23, text_24, text_25, text_26]
    for thisComponent in incidental_encoding_realComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    incidental_encoding_realClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "incidental_encoding_real"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = incidental_encoding_realClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=incidental_encoding_realClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_A* updates
        if image_A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_A.frameNStart = frameN  # exact frame index
            image_A.tStart = t  # local t and not account for scr refresh
            image_A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_A, 'tStartRefresh')  # time at next scr refresh
            image_A.setAutoDraw(True)
        if image_A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_A.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                image_A.tStop = t  # not accounting for scr refresh
                image_A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_A, 'tStopRefresh')  # time at next scr refresh
                image_A.setAutoDraw(False)
        
        # *image_c* updates
        if image_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_c.frameNStart = frameN  # exact frame index
            image_c.tStart = t  # local t and not account for scr refresh
            image_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_c, 'tStartRefresh')  # time at next scr refresh
            image_c.setAutoDraw(True)
        if image_c.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_c.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                image_c.tStop = t  # not accounting for scr refresh
                image_c.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_c, 'tStopRefresh')  # time at next scr refresh
                image_c.setAutoDraw(False)
        
        # *key_resp_15* updates
        waitOnFlip = False
        if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_15.frameNStart = frameN  # exact frame index
            key_resp_15.tStart = t  # local t and not account for scr refresh
            key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
            key_resp_15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_15.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_15.tStop = t  # not accounting for scr refresh
                key_resp_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_15, 'tStopRefresh')  # time at next scr refresh
                key_resp_15.status = FINISHED
        if key_resp_15.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_15.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'f', 'J', 'F'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_15.keys == []:  # then this was the first keypress
                    key_resp_15.keys = theseKeys.name  # just the first key pressed
                    key_resp_15.rt = theseKeys.rt
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            text_23.setAutoDraw(True)
        if text_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_23.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_23.tStop = t  # not accounting for scr refresh
                text_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_23, 'tStopRefresh')  # time at next scr refresh
                text_23.setAutoDraw(False)
        
        # *text_24* updates
        if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            text_24.setAutoDraw(True)
        if text_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_24.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_24.tStop = t  # not accounting for scr refresh
                text_24.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_24, 'tStopRefresh')  # time at next scr refresh
                text_24.setAutoDraw(False)
        
        # *text_25* updates
        if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_25.frameNStart = frameN  # exact frame index
            text_25.tStart = t  # local t and not account for scr refresh
            text_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
            text_25.setAutoDraw(True)
        if text_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_25.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_25.tStop = t  # not accounting for scr refresh
                text_25.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_25, 'tStopRefresh')  # time at next scr refresh
                text_25.setAutoDraw(False)
        
        # *text_26* updates
        if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_26.frameNStart = frameN  # exact frame index
            text_26.tStart = t  # local t and not account for scr refresh
            text_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
            text_26.setAutoDraw(True)
        if text_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_26.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_26.tStop = t  # not accounting for scr refresh
                text_26.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_26, 'tStopRefresh')  # time at next scr refresh
                text_26.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in incidental_encoding_realComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "incidental_encoding_real"-------
    for thisComponent in incidental_encoding_realComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_15.keys in ['', [], None]:  # No response was made
        key_resp_15.keys = None
    trials_17.addData('key_resp_15.keys',key_resp_15.keys)
    if key_resp_15.keys != None:  # we had a response
        trials_17.addData('key_resp_15.rt', key_resp_15.rt)
    trials_17.addData('key_resp_15.started', key_resp_15.tStartRefresh)
    trials_17.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials_16 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trialorder/phase2_practice.xlsx'),
        seed=None, name='trials_16')
    thisExp.addLoop(trials_16)  # add the loop to the experiment
    thisTrial_16 = trials_16.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
    if thisTrial_16 != None:
        for paramName in thisTrial_16:
            exec('{} = thisTrial_16[paramName]'.format(paramName))
    
    for thisTrial_16 in trials_16:
        currentLoop = trials_16
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_16.rgb)
        if thisTrial_16 != None:
            for paramName in thisTrial_16:
                exec('{} = thisTrial_16[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "sustained_attention_arrows_practice"-------
        # update component parameters for each repeat
        image_16.setImage(Arrow_direction)
        arrows_resp.keys = []
        arrows_resp.rt = []
        # keep track of which components have finished
        sustained_attention_arrows_practiceComponents = [image_16, arrows_resp, F_press, J_press, left_press, right_press]
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
            
            # *arrows_resp* updates
            waitOnFlip = False
            if arrows_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrows_resp.frameNStart = frameN  # exact frame index
                arrows_resp.tStart = t  # local t and not account for scr refresh
                arrows_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrows_resp, 'tStartRefresh')  # time at next scr refresh
                arrows_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(arrows_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(arrows_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if arrows_resp.status == STARTED and not waitOnFlip:
                theseKeys = arrows_resp.getKeys(keyList=['j', 'f', 'J', 'F'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if arrows_resp.keys == []:  # then this was the first keypress
                        arrows_resp.keys = theseKeys.name  # just the first key pressed
                        arrows_resp.rt = theseKeys.rt
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
        # check responses
        if arrows_resp.keys in ['', [], None]:  # No response was made
            arrows_resp.keys = None
        trials_16.addData('arrows_resp.keys',arrows_resp.keys)
        if arrows_resp.keys != None:  # we had a response
            trials_16.addData('arrows_resp.rt', arrows_resp.rt)
        trials_16.addData('arrows_resp.started', arrows_resp.tStartRefresh)
        trials_16.addData('arrows_resp.stopped', arrows_resp.tStopRefresh)
        # the Routine "sustained_attention_arrows_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixation_2"-------
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixation_2Components = [text_31]
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
            
            # *text_31* updates
            if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_31.frameNStart = frameN  # exact frame index
                text_31.tStart = t  # local t and not account for scr refresh
                text_31.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
                text_31.setAutoDraw(True)
            if text_31.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_31.tStop = t  # not accounting for scr refresh
                    text_31.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                    text_31.setAutoDraw(False)
            
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
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_16'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_17'


# ------Prepare to start Routine "fixation_2"-------
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
fixation_2Components = [text_31]
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
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
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

# set up handler to look after randomisation of conditions etc
trials_19 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions.csv', selection='22:26'),
    seed=None, name='trials_19')
thisExp.addLoop(trials_19)  # add the loop to the experiment
thisTrial_19 = trials_19.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
if thisTrial_19 != None:
    for paramName in thisTrial_19:
        exec('{} = thisTrial_19[paramName]'.format(paramName))

for thisTrial_19 in trials_19:
    currentLoop = trials_19
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_19.rgb)
    if thisTrial_19 != None:
        for paramName in thisTrial_19:
            exec('{} = thisTrial_19[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pre_instruct_final_memory"-------
    # update component parameters for each repeat
    text_14.setText(instructions1)
    pressspace.setColor('black', colorSpace='rgb')
    pressspace.setPos((0, -0.4))
    pressspace.setText('Press space to continue')
    key_resp_16.keys = []
    key_resp_16.rt = []
    image_17.setImage(Image1)
    Jkey.setText(J_key)
    F_key.setText(K_key)
    oldText.setText(yes_text)
    newtext.setText(no_text)
    # keep track of which components have finished
    pre_instruct_final_memoryComponents = [text_14, pressspace, key_resp_16, image_17, Jkey, F_key, oldText, newtext]
    for thisComponent in pre_instruct_final_memoryComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pre_instruct_final_memoryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pre_instruct_final_memory"-------
    while continueRoutine:
        # get current time
        t = pre_instruct_final_memoryClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pre_instruct_final_memoryClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        
        # *pressspace* updates
        if pressspace.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressspace.frameNStart = frameN  # exact frame index
            pressspace.tStart = t  # local t and not account for scr refresh
            pressspace.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressspace, 'tStartRefresh')  # time at next scr refresh
            pressspace.setAutoDraw(True)
        
        # *key_resp_16* updates
        waitOnFlip = False
        if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_16.frameNStart = frameN  # exact frame index
            key_resp_16.tStart = t  # local t and not account for scr refresh
            key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
            key_resp_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_16.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_16.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_16.keys == []:  # then this was the first keypress
                    key_resp_16.keys = theseKeys.name  # just the first key pressed
                    key_resp_16.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # *image_17* updates
        if image_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_17.frameNStart = frameN  # exact frame index
            image_17.tStart = t  # local t and not account for scr refresh
            image_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
            image_17.setAutoDraw(True)
        
        # *Jkey* updates
        if Jkey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Jkey.frameNStart = frameN  # exact frame index
            Jkey.tStart = t  # local t and not account for scr refresh
            Jkey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Jkey, 'tStartRefresh')  # time at next scr refresh
            Jkey.setAutoDraw(True)
        
        # *F_key* updates
        if F_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F_key.frameNStart = frameN  # exact frame index
            F_key.tStart = t  # local t and not account for scr refresh
            F_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F_key, 'tStartRefresh')  # time at next scr refresh
            F_key.setAutoDraw(True)
        
        # *oldText* updates
        if oldText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            oldText.frameNStart = frameN  # exact frame index
            oldText.tStart = t  # local t and not account for scr refresh
            oldText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oldText, 'tStartRefresh')  # time at next scr refresh
            oldText.setAutoDraw(True)
        
        # *newtext* updates
        if newtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            newtext.frameNStart = frameN  # exact frame index
            newtext.tStart = t  # local t and not account for scr refresh
            newtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(newtext, 'tStartRefresh')  # time at next scr refresh
            newtext.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_instruct_final_memoryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pre_instruct_final_memory"-------
    for thisComponent in pre_instruct_final_memoryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_16.keys in ['', [], None]:  # No response was made
        key_resp_16.keys = None
    trials_19.addData('key_resp_16.keys',key_resp_16.keys)
    if key_resp_16.keys != None:  # we had a response
        trials_19.addData('key_resp_16.rt', key_resp_16.rt)
    # the Routine "pre_instruct_final_memory" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trials_19'


# set up handler to look after randomisation of conditions etc
trials_20 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/final_acb_memory_test_practice.xlsx'),
    seed=None, name='trials_20')
thisExp.addLoop(trials_20)  # add the loop to the experiment
thisTrial_20 = trials_20.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
if thisTrial_20 != None:
    for paramName in thisTrial_20:
        exec('{} = thisTrial_20[paramName]'.format(paramName))

for thisTrial_20 in trials_20:
    currentLoop = trials_20
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_20.rgb)
    if thisTrial_20 != None:
        for paramName in thisTrial_20:
            exec('{} = thisTrial_20[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_abc_memory_test"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    imageabc.setImage(Image)
    primed_memory_resp.keys = []
    primed_memory_resp.rt = []
    Jkey_2.setText('J')
    F_key_2.setText('F')
    old.setText('old')
    newtext_2.setText('new')
    # keep track of which components have finished
    practice_abc_memory_testComponents = [imageabc, primed_memory_resp, Jkey_2, F_key_2, old, newtext_2]
    for thisComponent in practice_abc_memory_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_abc_memory_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice_abc_memory_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_abc_memory_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_abc_memory_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageabc* updates
        if imageabc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageabc.frameNStart = frameN  # exact frame index
            imageabc.tStart = t  # local t and not account for scr refresh
            imageabc.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageabc, 'tStartRefresh')  # time at next scr refresh
            imageabc.setAutoDraw(True)
        if imageabc.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageabc.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                imageabc.tStop = t  # not accounting for scr refresh
                imageabc.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageabc, 'tStopRefresh')  # time at next scr refresh
                imageabc.setAutoDraw(False)
        
        # *primed_memory_resp* updates
        waitOnFlip = False
        if primed_memory_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            primed_memory_resp.frameNStart = frameN  # exact frame index
            primed_memory_resp.tStart = t  # local t and not account for scr refresh
            primed_memory_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(primed_memory_resp, 'tStartRefresh')  # time at next scr refresh
            primed_memory_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(primed_memory_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(primed_memory_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if primed_memory_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > primed_memory_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                primed_memory_resp.tStop = t  # not accounting for scr refresh
                primed_memory_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(primed_memory_resp, 'tStopRefresh')  # time at next scr refresh
                primed_memory_resp.status = FINISHED
        if primed_memory_resp.status == STARTED and not waitOnFlip:
            theseKeys = primed_memory_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'f', 'J', 'F'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if primed_memory_resp.keys == []:  # then this was the first keypress
                    primed_memory_resp.keys = theseKeys.name  # just the first key pressed
                    primed_memory_resp.rt = theseKeys.rt
        
        # *Jkey_2* updates
        if Jkey_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Jkey_2.frameNStart = frameN  # exact frame index
            Jkey_2.tStart = t  # local t and not account for scr refresh
            Jkey_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Jkey_2, 'tStartRefresh')  # time at next scr refresh
            Jkey_2.setAutoDraw(True)
        if Jkey_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Jkey_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Jkey_2.tStop = t  # not accounting for scr refresh
                Jkey_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Jkey_2, 'tStopRefresh')  # time at next scr refresh
                Jkey_2.setAutoDraw(False)
        
        # *F_key_2* updates
        if F_key_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F_key_2.frameNStart = frameN  # exact frame index
            F_key_2.tStart = t  # local t and not account for scr refresh
            F_key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F_key_2, 'tStartRefresh')  # time at next scr refresh
            F_key_2.setAutoDraw(True)
        if F_key_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > F_key_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                F_key_2.tStop = t  # not accounting for scr refresh
                F_key_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(F_key_2, 'tStopRefresh')  # time at next scr refresh
                F_key_2.setAutoDraw(False)
        
        # *old* updates
        if old.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            old.frameNStart = frameN  # exact frame index
            old.tStart = t  # local t and not account for scr refresh
            old.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(old, 'tStartRefresh')  # time at next scr refresh
            old.setAutoDraw(True)
        if old.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > old.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                old.tStop = t  # not accounting for scr refresh
                old.frameNStop = frameN  # exact frame index
                win.timeOnFlip(old, 'tStopRefresh')  # time at next scr refresh
                old.setAutoDraw(False)
        
        # *newtext_2* updates
        if newtext_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            newtext_2.frameNStart = frameN  # exact frame index
            newtext_2.tStart = t  # local t and not account for scr refresh
            newtext_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(newtext_2, 'tStartRefresh')  # time at next scr refresh
            newtext_2.setAutoDraw(True)
        if newtext_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > newtext_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                newtext_2.tStop = t  # not accounting for scr refresh
                newtext_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(newtext_2, 'tStopRefresh')  # time at next scr refresh
                newtext_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_abc_memory_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_abc_memory_test"-------
    for thisComponent in practice_abc_memory_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if primed_memory_resp.keys in ['', [], None]:  # No response was made
        primed_memory_resp.keys = None
    trials_20.addData('primed_memory_resp.keys',primed_memory_resp.keys)
    if primed_memory_resp.keys != None:  # we had a response
        trials_20.addData('primed_memory_resp.rt', primed_memory_resp.rt)
    trials_20.addData('primed_memory_resp.started', primed_memory_resp.tStartRefresh)
    trials_20.addData('primed_memory_resp.stopped', primed_memory_resp.tStopRefresh)
    trials_20.addData('Jkey_2.started', Jkey_2.tStartRefresh)
    trials_20.addData('Jkey_2.stopped', Jkey_2.tStopRefresh)
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
# completed 1 repeats of 'trials_20'


# ------Prepare to start Routine "fixation_2"-------
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
fixation_2Components = [text_31]
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
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
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

# ------Prepare to start Routine "pre_instruction_real_abc_final_memory"-------
# update component parameters for each repeat
key_resp_18.keys = []
key_resp_18.rt = []
# keep track of which components have finished
pre_instruction_real_abc_final_memoryComponents = [text_27, key_resp_18]
for thisComponent in pre_instruction_real_abc_final_memoryComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pre_instruction_real_abc_final_memoryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "pre_instruction_real_abc_final_memory"-------
while continueRoutine:
    # get current time
    t = pre_instruction_real_abc_final_memoryClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pre_instruction_real_abc_final_memoryClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_27* updates
    if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_27.frameNStart = frameN  # exact frame index
        text_27.tStart = t  # local t and not account for scr refresh
        text_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
        text_27.setAutoDraw(True)
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            if key_resp_18.keys == []:  # then this was the first keypress
                key_resp_18.keys = theseKeys.name  # just the first key pressed
                key_resp_18.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pre_instruction_real_abc_final_memoryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pre_instruction_real_abc_final_memory"-------
for thisComponent in pre_instruction_real_abc_final_memoryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_18.keys in ['', [], None]:  # No response was made
    key_resp_18.keys = None
thisExp.addData('key_resp_18.keys',key_resp_18.keys)
if key_resp_18.keys != None:  # we had a response
    thisExp.addData('key_resp_18.rt', key_resp_18.rt)
thisExp.nextEntry()
# the Routine "pre_instruction_real_abc_final_memory" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_21 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(priming_recognition_path),
    seed=None, name='trials_21')
thisExp.addLoop(trials_21)  # add the loop to the experiment
thisTrial_21 = trials_21.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
if thisTrial_21 != None:
    for paramName in thisTrial_21:
        exec('{} = thisTrial_21[paramName]'.format(paramName))

for thisTrial_21 in trials_21:
    currentLoop = trials_21
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_21.rgb)
    if thisTrial_21 != None:
        for paramName in thisTrial_21:
            exec('{} = thisTrial_21[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_abc_memory_test"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    imageabc.setImage(Image)
    primed_memory_resp.keys = []
    primed_memory_resp.rt = []
    Jkey_2.setText('J')
    F_key_2.setText('F')
    old.setText('old')
    newtext_2.setText('new')
    # keep track of which components have finished
    practice_abc_memory_testComponents = [imageabc, primed_memory_resp, Jkey_2, F_key_2, old, newtext_2]
    for thisComponent in practice_abc_memory_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_abc_memory_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice_abc_memory_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_abc_memory_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_abc_memory_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageabc* updates
        if imageabc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageabc.frameNStart = frameN  # exact frame index
            imageabc.tStart = t  # local t and not account for scr refresh
            imageabc.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageabc, 'tStartRefresh')  # time at next scr refresh
            imageabc.setAutoDraw(True)
        if imageabc.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageabc.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                imageabc.tStop = t  # not accounting for scr refresh
                imageabc.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageabc, 'tStopRefresh')  # time at next scr refresh
                imageabc.setAutoDraw(False)
        
        # *primed_memory_resp* updates
        waitOnFlip = False
        if primed_memory_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            primed_memory_resp.frameNStart = frameN  # exact frame index
            primed_memory_resp.tStart = t  # local t and not account for scr refresh
            primed_memory_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(primed_memory_resp, 'tStartRefresh')  # time at next scr refresh
            primed_memory_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(primed_memory_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(primed_memory_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if primed_memory_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > primed_memory_resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                primed_memory_resp.tStop = t  # not accounting for scr refresh
                primed_memory_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(primed_memory_resp, 'tStopRefresh')  # time at next scr refresh
                primed_memory_resp.status = FINISHED
        if primed_memory_resp.status == STARTED and not waitOnFlip:
            theseKeys = primed_memory_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'f', 'J', 'F'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if primed_memory_resp.keys == []:  # then this was the first keypress
                    primed_memory_resp.keys = theseKeys.name  # just the first key pressed
                    primed_memory_resp.rt = theseKeys.rt
        
        # *Jkey_2* updates
        if Jkey_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Jkey_2.frameNStart = frameN  # exact frame index
            Jkey_2.tStart = t  # local t and not account for scr refresh
            Jkey_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Jkey_2, 'tStartRefresh')  # time at next scr refresh
            Jkey_2.setAutoDraw(True)
        if Jkey_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Jkey_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Jkey_2.tStop = t  # not accounting for scr refresh
                Jkey_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Jkey_2, 'tStopRefresh')  # time at next scr refresh
                Jkey_2.setAutoDraw(False)
        
        # *F_key_2* updates
        if F_key_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            F_key_2.frameNStart = frameN  # exact frame index
            F_key_2.tStart = t  # local t and not account for scr refresh
            F_key_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(F_key_2, 'tStartRefresh')  # time at next scr refresh
            F_key_2.setAutoDraw(True)
        if F_key_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > F_key_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                F_key_2.tStop = t  # not accounting for scr refresh
                F_key_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(F_key_2, 'tStopRefresh')  # time at next scr refresh
                F_key_2.setAutoDraw(False)
        
        # *old* updates
        if old.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            old.frameNStart = frameN  # exact frame index
            old.tStart = t  # local t and not account for scr refresh
            old.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(old, 'tStartRefresh')  # time at next scr refresh
            old.setAutoDraw(True)
        if old.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > old.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                old.tStop = t  # not accounting for scr refresh
                old.frameNStop = frameN  # exact frame index
                win.timeOnFlip(old, 'tStopRefresh')  # time at next scr refresh
                old.setAutoDraw(False)
        
        # *newtext_2* updates
        if newtext_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            newtext_2.frameNStart = frameN  # exact frame index
            newtext_2.tStart = t  # local t and not account for scr refresh
            newtext_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(newtext_2, 'tStartRefresh')  # time at next scr refresh
            newtext_2.setAutoDraw(True)
        if newtext_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > newtext_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                newtext_2.tStop = t  # not accounting for scr refresh
                newtext_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(newtext_2, 'tStopRefresh')  # time at next scr refresh
                newtext_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_abc_memory_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_abc_memory_test"-------
    for thisComponent in practice_abc_memory_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if primed_memory_resp.keys in ['', [], None]:  # No response was made
        primed_memory_resp.keys = None
    trials_21.addData('primed_memory_resp.keys',primed_memory_resp.keys)
    if primed_memory_resp.keys != None:  # we had a response
        trials_21.addData('primed_memory_resp.rt', primed_memory_resp.rt)
    trials_21.addData('primed_memory_resp.started', primed_memory_resp.tStartRefresh)
    trials_21.addData('primed_memory_resp.stopped', primed_memory_resp.tStopRefresh)
    trials_21.addData('Jkey_2.started', Jkey_2.tStartRefresh)
    trials_21.addData('Jkey_2.stopped', Jkey_2.tStopRefresh)
    
    # ------Prepare to start Routine "fixation_2"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_2Components = [text_31]
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
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
                text_31.setAutoDraw(False)
        
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
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_21'


# set up handler to look after randomisation of conditions etc
trials_22 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/instructions.csv', selection='26:30'),
    seed=None, name='trials_22')
thisExp.addLoop(trials_22)  # add the loop to the experiment
thisTrial_22 = trials_22.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
if thisTrial_22 != None:
    for paramName in thisTrial_22:
        exec('{} = thisTrial_22[paramName]'.format(paramName))

for thisTrial_22 in trials_22:
    currentLoop = trials_22
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_22.rgb)
    if thisTrial_22 != None:
        for paramName in thisTrial_22:
            exec('{} = thisTrial_22[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "questionairre"-------
    # update component parameters for each repeat
    questioniarre.setText(instructions1)
    questionairre_resp.keys = []
    questionairre_resp.rt = []
    text_29.setText(Instructions2)
    image_18.setImage(Image1)
    image_19.setImage(Image2)
    image_20.setImage(Image3)
    image_21.setImage(Image4)
    A_txt1.setText(J_key)
    B_text.setText(K_key)
    a_text2.setText(J_key)
    C_text.setText(L_key)
    # keep track of which components have finished
    questionairreComponents = [questioniarre, questionairre_resp, text_29, image_18, image_19, image_20, image_21, A_txt1, B_text, a_text2, C_text]
    for thisComponent in questionairreComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionairreClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "questionairre"-------
    while continueRoutine:
        # get current time
        t = questionairreClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionairreClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *questioniarre* updates
        if questioniarre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            questioniarre.frameNStart = frameN  # exact frame index
            questioniarre.tStart = t  # local t and not account for scr refresh
            questioniarre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(questioniarre, 'tStartRefresh')  # time at next scr refresh
            questioniarre.setAutoDraw(True)
        
        # *questionairre_resp* updates
        waitOnFlip = False
        if questionairre_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            questionairre_resp.frameNStart = frameN  # exact frame index
            questionairre_resp.tStart = t  # local t and not account for scr refresh
            questionairre_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(questionairre_resp, 'tStartRefresh')  # time at next scr refresh
            questionairre_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(questionairre_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(questionairre_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if questionairre_resp.status == STARTED and not waitOnFlip:
            theseKeys = questionairre_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'n', 'p', 't'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if questionairre_resp.keys == []:  # then this was the first keypress
                    questionairre_resp.keys = theseKeys.name  # just the first key pressed
                    questionairre_resp.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # *text_29* updates
        if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_29.frameNStart = frameN  # exact frame index
            text_29.tStart = t  # local t and not account for scr refresh
            text_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
            text_29.setAutoDraw(True)
        
        # *image_18* updates
        if image_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_18.frameNStart = frameN  # exact frame index
            image_18.tStart = t  # local t and not account for scr refresh
            image_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
            image_18.setAutoDraw(True)
        
        # *image_19* updates
        if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_19.frameNStart = frameN  # exact frame index
            image_19.tStart = t  # local t and not account for scr refresh
            image_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
            image_19.setAutoDraw(True)
        
        # *image_20* updates
        if image_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_20.frameNStart = frameN  # exact frame index
            image_20.tStart = t  # local t and not account for scr refresh
            image_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_20, 'tStartRefresh')  # time at next scr refresh
            image_20.setAutoDraw(True)
        
        # *image_21* updates
        if image_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_21.frameNStart = frameN  # exact frame index
            image_21.tStart = t  # local t and not account for scr refresh
            image_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_21, 'tStartRefresh')  # time at next scr refresh
            image_21.setAutoDraw(True)
        
        # *A_txt1* updates
        if A_txt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            A_txt1.frameNStart = frameN  # exact frame index
            A_txt1.tStart = t  # local t and not account for scr refresh
            A_txt1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(A_txt1, 'tStartRefresh')  # time at next scr refresh
            A_txt1.setAutoDraw(True)
        
        # *B_text* updates
        if B_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            B_text.frameNStart = frameN  # exact frame index
            B_text.tStart = t  # local t and not account for scr refresh
            B_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(B_text, 'tStartRefresh')  # time at next scr refresh
            B_text.setAutoDraw(True)
        
        # *a_text2* updates
        if a_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            a_text2.frameNStart = frameN  # exact frame index
            a_text2.tStart = t  # local t and not account for scr refresh
            a_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_text2, 'tStartRefresh')  # time at next scr refresh
            a_text2.setAutoDraw(True)
        
        # *C_text* updates
        if C_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            C_text.frameNStart = frameN  # exact frame index
            C_text.tStart = t  # local t and not account for scr refresh
            C_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(C_text, 'tStartRefresh')  # time at next scr refresh
            C_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionairreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questionairre"-------
    for thisComponent in questionairreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if questionairre_resp.keys in ['', [], None]:  # No response was made
        questionairre_resp.keys = None
    trials_22.addData('questionairre_resp.keys',questionairre_resp.keys)
    if questionairre_resp.keys != None:  # we had a response
        trials_22.addData('questionairre_resp.rt', questionairre_resp.rt)
    trials_22.addData('questionairre_resp.started', questionairre_resp.tStartRefresh)
    trials_22.addData('questionairre_resp.stopped', questionairre_resp.tStopRefresh)
    # the Routine "questionairre" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_22'


# set up handler to look after randomisation of conditions etc
trials_23 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialorder/questionairre2.csv'),
    seed=None, name='trials_23')
thisExp.addLoop(trials_23)  # add the loop to the experiment
thisTrial_23 = trials_23.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
if thisTrial_23 != None:
    for paramName in thisTrial_23:
        exec('{} = thisTrial_23[paramName]'.format(paramName))

for thisTrial_23 in trials_23:
    currentLoop = trials_23
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_23.rgb)
    if thisTrial_23 != None:
        for paramName in thisTrial_23:
            exec('{} = thisTrial_23[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "questionairre2"-------
    # update component parameters for each repeat
    text_30.setText(instructions1)
    text_32.setText(text1)
    text_33.setText(text2)
    questionairre_resp2.keys = []
    questionairre_resp2.rt = []
    rating.reset()
    # keep track of which components have finished
    questionairre2Components = [text_30, text_32, text_33, questionairre_resp2, rating]
    for thisComponent in questionairre2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionairre2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "questionairre2"-------
    while continueRoutine:
        # get current time
        t = questionairre2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionairre2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_30* updates
        if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_30.frameNStart = frameN  # exact frame index
            text_30.tStart = t  # local t and not account for scr refresh
            text_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
            text_30.setAutoDraw(True)
        
        # *text_32* updates
        if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_32.frameNStart = frameN  # exact frame index
            text_32.tStart = t  # local t and not account for scr refresh
            text_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
            text_32.setAutoDraw(True)
        
        # *text_33* updates
        if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_33.frameNStart = frameN  # exact frame index
            text_33.tStart = t  # local t and not account for scr refresh
            text_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
            text_33.setAutoDraw(True)
        
        # *questionairre_resp2* updates
        waitOnFlip = False
        if questionairre_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            questionairre_resp2.frameNStart = frameN  # exact frame index
            questionairre_resp2.tStart = t  # local t and not account for scr refresh
            questionairre_resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(questionairre_resp2, 'tStartRefresh')  # time at next scr refresh
            questionairre_resp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(questionairre_resp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(questionairre_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if questionairre_resp2.status == STARTED and not waitOnFlip:
            theseKeys = questionairre_resp2.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'return'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                questionairre_resp2.keys.append(theseKeys.name)  # storing all keys
                questionairre_resp2.rt.append(theseKeys.rt)
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionairre2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "questionairre2"-------
    for thisComponent in questionairre2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if questionairre_resp2.keys in ['', [], None]:  # No response was made
        questionairre_resp2.keys = None
    trials_23.addData('questionairre_resp2.keys',questionairre_resp2.keys)
    if questionairre_resp2.keys != None:  # we had a response
        trials_23.addData('questionairre_resp2.rt', questionairre_resp2.rt)
    trials_23.addData('questionairre_resp2.started', questionairre_resp2.tStartRefresh)
    trials_23.addData('questionairre_resp2.stopped', questionairre_resp2.tStopRefresh)
    # store data for trials_23 (TrialHandler)
    trials_23.addData('rating.response', rating.getRating())
    trials_23.addData('rating.rt', rating.getRT())
    trials_23.addData('rating.started', rating.tStart)
    trials_23.addData('rating.stopped', rating.tStop)
    # the Routine "questionairre2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_23'


# ------Prepare to start Routine "end"-------
# update component parameters for each repeat
exit.keys = []
exit.rt = []
# keep track of which components have finished
endComponents = [text_28, exit]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    
    # *exit* updates
    waitOnFlip = False
    if exit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exit.frameNStart = frameN  # exact frame index
        exit.tStart = t  # local t and not account for scr refresh
        exit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exit, 'tStartRefresh')  # time at next scr refresh
        exit.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(exit.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(exit.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if exit.status == STARTED and not waitOnFlip:
        theseKeys = exit.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            if exit.keys == []:  # then this was the first keypress
                exit.keys = theseKeys.name  # just the first key pressed
                exit.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if exit.keys in ['', [], None]:  # No response was made
    exit.keys = None
thisExp.addData('exit.keys',exit.keys)
if exit.keys != None:  # we had a response
    thisExp.addData('exit.rt', exit.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
