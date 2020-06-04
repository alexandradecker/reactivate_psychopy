#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Thu Jun  4 16:24:52 2020
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

# Initialize components for Routine "trial"
trialClock = core.Clock()
a_image = visual.ImageStim(
    win=win,
    name='a_image', 
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
b_image = visual.ImageStim(
    win=win,
    name='b_image', 
    image='sin', mask=None,
    ori=0, pos=(.25, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_12 = visual.TextStim(win=win, name='text_12',
    text='Remember the image pairs',
    font='Helvetica',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

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

# Initialize components for Routine "test"
testClock = core.Clock()
instruct_text = visual.TextStim(win=win, name='instruct_text',
    text='Retrieve the associate',
    font='Arial',
    pos=(0, .4), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
a_image_retrieve = visual.ImageStim(
    win=win,
    name='a_image_retrieve', 
    image='sin', mask=None,
    ori=0, pos=(-.5, -.1), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
correct_pair = visual.ImageStim(
    win=win,
    name='correct_pair', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
afc_text = visual.TextStim(win=win, name='afc_text',
    text='Select the correct image',
    font='Arial',
    pos=(0, 3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
alternative_1 = visual.ImageStim(
    win=win,
    name='alternative_1', 
    image='sin', mask=None,
    ori=0, pos=(-.3, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
alternative_2 = visual.ImageStim(
    win=win,
    name='alternative_2', 
    image='sin', mask=None,
    ori=0, pos=(0, .3), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instruction_intentional_encoding = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions_intentional_encoding.xlsx', selection='0:8'),
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
    # keep track of which components have finished
    instructions_intentional_encodingComponents = [text, instructions_text2, response, image1, image2]
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
            theseKeys = response.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
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
            image1.setPos((0.25, -0.05), log=False)
            image1.setSize((0.4, 0.4), log=False)
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
            image2.setPos((-.25, -.05), log=False)
            image2.setSize((0.4, 0.4), log=False)
            image2.setImage(Image2, log=False)
        
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
    # the Routine "instructions_intentional_encoding" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instruction_intentional_encoding'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('intentional_encoding.xlsx', selection='0:12'),
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
    
    # ------Prepare to start Routine "trial"-------
    routineTimer.add(0.100000)
    # update component parameters for each repeat
    b_image.setImage(image_b)
    # keep track of which components have finished
    trialComponents = [a_image, b_image, text_12]
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
        
        # *a_image* updates
        if a_image.status == NOT_STARTED and tThisFlip >= .05-frameTolerance:
            # keep track of start time/frame for later
            a_image.frameNStart = frameN  # exact frame index
            a_image.tStart = t  # local t and not account for scr refresh
            a_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(a_image, 'tStartRefresh')  # time at next scr refresh
            a_image.setAutoDraw(True)
        if a_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > a_image.tStartRefresh + .05-frameTolerance:
                # keep track of stop time/frame for later
                a_image.tStop = t  # not accounting for scr refresh
                a_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(a_image, 'tStopRefresh')  # time at next scr refresh
                a_image.setAutoDraw(False)
        if a_image.status == STARTED:  # only update if drawing
            a_image.setImage(image_a, log=False)
        
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
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        if text_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_12.tStartRefresh + .05-frameTolerance:
                # keep track of stop time/frame for later
                text_12.tStop = t  # not accounting for scr refresh
                text_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                text_12.setAutoDraw(False)
        
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
    trials.addData('a_image.started', a_image.tStartRefresh)
    trials.addData('a_image.stopped', a_image.tStopRefresh)
    trials.addData('b_image.started', b_image.tStartRefresh)
    trials.addData('b_image.stopped', b_image.tStopRefresh)
    trials.addData('text_12.started', text_12.tStartRefresh)
    trials.addData('text_12.stopped', text_12.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions_intentional_encoding.xlsx', selection='8:11'),
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
            image_3.setSize((0.4, 0.4), log=False)
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
    
# completed 1 repeats of 'trials_4'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions_intentional_encoding.xlsx', selection='11:17'),
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
            theseKeys = key_resp_2.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
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
            image.setSize((0.4, 0.4), log=False)
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
            image_2.setSize((0.4, 0.4), log=False)
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
            image_5.setSize((0.4, 0.4), log=False)
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
            image_6.setSize((0.4, 0.4), log=False)
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
    
# completed 1 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test_encoding.xlsx', selection='0:12'),
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
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    testComponents = [instruct_text, a_image_retrieve, text_2, correct_pair, afc_text, alternative_1, alternative_2]
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
        if instruct_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
        if a_image_retrieve.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
        if text_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
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
        
        # *correct_pair* updates
        if correct_pair.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            correct_pair.frameNStart = frameN  # exact frame index
            correct_pair.tStart = t  # local t and not account for scr refresh
            correct_pair.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct_pair, 'tStartRefresh')  # time at next scr refresh
            correct_pair.setAutoDraw(True)
        if correct_pair.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct_pair.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                correct_pair.tStop = t  # not accounting for scr refresh
                correct_pair.frameNStop = frameN  # exact frame index
                win.timeOnFlip(correct_pair, 'tStopRefresh')  # time at next scr refresh
                correct_pair.setAutoDraw(False)
        if correct_pair.status == STARTED:  # only update if drawing
            correct_pair.setImage(image_correct, log=False)
        
        # *afc_text* updates
        if afc_text.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
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
        
        # *alternative_1* updates
        if alternative_1.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            alternative_1.frameNStart = frameN  # exact frame index
            alternative_1.tStart = t  # local t and not account for scr refresh
            alternative_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alternative_1, 'tStartRefresh')  # time at next scr refresh
            alternative_1.setAutoDraw(True)
        if alternative_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alternative_1.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                alternative_1.tStop = t  # not accounting for scr refresh
                alternative_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alternative_1, 'tStopRefresh')  # time at next scr refresh
                alternative_1.setAutoDraw(False)
        if alternative_1.status == STARTED:  # only update if drawing
            alternative_1.setImage(image_alternative1, log=False)
        
        # *alternative_2* updates
        if alternative_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            alternative_2.frameNStart = frameN  # exact frame index
            alternative_2.tStart = t  # local t and not account for scr refresh
            alternative_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alternative_2, 'tStartRefresh')  # time at next scr refresh
            alternative_2.setAutoDraw(True)
        if alternative_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > alternative_2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                alternative_2.tStop = t  # not accounting for scr refresh
                alternative_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(alternative_2, 'tStopRefresh')  # time at next scr refresh
                alternative_2.setAutoDraw(False)
        if alternative_2.status == STARTED:  # only update if drawing
            alternative_2.setImage(image_alternative2, log=False)
        
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
    trials_3.addData('correct_pair.started', correct_pair.tStartRefresh)
    trials_3.addData('correct_pair.stopped', correct_pair.tStopRefresh)
    trials_3.addData('afc_text.started', afc_text.tStartRefresh)
    trials_3.addData('afc_text.stopped', afc_text.tStopRefresh)
    trials_3.addData('alternative_1.started', alternative_1.tStartRefresh)
    trials_3.addData('alternative_1.stopped', alternative_1.tStopRefresh)
    trials_3.addData('alternative_2.started', alternative_2.tStartRefresh)
    trials_3.addData('alternative_2.stopped', alternative_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


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
