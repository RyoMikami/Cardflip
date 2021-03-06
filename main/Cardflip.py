#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),

Title: Cardflip.py
Date: Dec 1th, 2020
Written by Ryo Mikami

This is main programe for card flip game.

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
expName = 'Cardflip'  # from the Builder filename that created this script
expInfo = {'session': '00', 'participant': '00'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expName, expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ryo/Google ドライブ/橘高/プログラム/github用/Cardflip.py',
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
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
import pandas as pd
from numpy import random
#from statistics import mean
import pathlib
#Practice round setting
import math

Practice_Round=3
Practice_Treat_s=[1,1,1]
Practice_Treat_q=[1,1,1]
a=1
b=20


Result=[]
Result_Fixed_part=[]
Result_Other_part=[]
Pay_off=[]

text_ready = visual.TextStim(win=win, name='text_ready',
    text='指示があるまで操作を行わないでください。\n準備が整ったら、実験者の指示に従い\n\n\n\nを押してください。\n実験が開始されます。',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
start_b = visual.Rect(
    win=win, name='start_b',
    width=(0.4, 0.1)[0], height=(0.4, 0.1)[1],
    ori=0, pos=(0, 0.05),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
start_text = visual.TextStim(win=win, name='start_text',
    text='開始する',
    font='Arial',
    pos=start_b.pos, height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ready_practice"
ready_practiceClock = core.Clock()
text_setting_practice = visual.TextStim(win=win, name='text_setting_practice',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_wait_practice = visual.TextStim(win=win, name='text_wait_practice',
    text='しばらくお待ちください…',
    font='Arial',
    pos=[0,-0.4], height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
next_b = visual.Rect(
    win=win, name='next_b',
    width=(0.9, 0.1)[0], height=(0.9, 0.1)[1],
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
text_start_practice = visual.TextStim(win=win, name='text_start_practice',
    text='ラウンドを開始する。',
    font='Arial',
    pos=next_b.pos, height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "practice"
practiceClock = core.Clock()
text_round_practice = visual.TextStim(win=win, name='text_round_practice',
    text='default text',
    font='Arial',
    pos=[-0.35, 0.45], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cost_practice = visual.TextStim(win=win, name='text_cost_practice',
    text='default text',
    font='Arial',
    pos=[0, 0.4], height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_cash__practice = visual.TextStim(win=win, name='text_cash__practice',
    text='default text',
    font='Arial',
    pos=[0, 0.3], height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
card_A_2 = visual.Rect(
    win=win, name='card_A_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.7, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
text_A_2 = visual.TextStim(win=win, name='text_A_2',
    text=None,
    font='Arial',
    pos=card_A_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
card_B_2 = visual.Rect(
    win=win, name='card_B_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.5, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_B_2 = visual.TextStim(win=win, name='text_B_2',
    text=None,
    font='Arial',
    pos=card_B_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
card_C_2 = visual.Rect(
    win=win, name='card_C_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.3, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
text_C_2 = visual.TextStim(win=win, name='text_C_2',
    text=None,
    font='Arial',
    pos=card_C_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
card_D_2 = visual.Rect(
    win=win, name='card_D_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.1, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
text_D_2 = visual.TextStim(win=win, name='text_D_2',
    text=None,
    font='Arial',
    pos=card_D_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
text_wait_practice_round = visual.TextStim(win=win, name='text_wait_practice_round',
    text='お待ちください…',
    font='Arial',
    pos=[0,-0.3], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_choice_2 = visual.TextStim(win=win, name='text_choice_2',
    text=None,
    font='Arial',
    pos=[0,-0.3], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
end_button_2 = visual.Rect(
    win=win, name='end_button_2',
    width=(0.26, 0.1)[0], height=(0.26, 0.1)[1],
    ori=0, pos=[0.3, -0.4],
    lineWidth=1, lineColor=[2,2,2], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
end_choise_2 = visual.TextStim(win=win, name='end_choise_2',
    text=None,
    font='Arial',
    pos=end_button_2.pos, height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
conti_button_2 = visual.Rect(
    win=win, name='conti_button_2',
    width=(0.26, 0.1)[0], height=(0.26, 0.1)[1],
    ori=0, pos=[-0.3, -0.4],
    lineWidth=1, lineColor=[2,2,2], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
conti_choise_2 = visual.TextStim(win=win, name='conti_choise_2',
    text=None,
    font='Arial',
    pos=conti_button_2.pos, height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
card_E_2 = visual.Rect(
    win=win, name='card_E_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.1, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
card_F_2 = visual.Rect(
    win=win, name='card_F_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.3, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-18.0, interpolate=True)
card_G_2 = visual.Rect(
    win=win, name='card_G_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.5, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-19.0, interpolate=True)
card_H_2 = visual.Rect(
    win=win, name='card_H_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.7, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)
text_E_2 = visual.TextStim(win=win, name='text_E_2',
    text=None,
    font='Arial',
    pos=card_E_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
text_F_2 = visual.TextStim(win=win, name='text_F_2',
    text=None,
    font='Arial',
    pos=card_F_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
text_G_2 = visual.TextStim(win=win, name='text_G_2',
    text=None,
    font='Arial',
    pos=card_G_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-23.0);
text_H_2 = visual.TextStim(win=win, name='text_H_2',
    text=None,
    font='Arial',
    pos=card_H_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
card_a_2 = visual.Rect(
    win=win, name='card_a_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.7, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-25.0, interpolate=True)
card_b_2 = visual.Rect(
    win=win, name='card_b_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.5, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-26.0, interpolate=True)
card_c_2 = visual.Rect(
    win=win, name='card_c_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.3, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-27.0, interpolate=True)
card_d_2 = visual.Rect(
    win=win, name='card_d_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.1, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-28.0, interpolate=True)
card_e_2 = visual.Rect(
    win=win, name='card_e_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.1, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-29.0, interpolate=True)
card_f_2 = visual.Rect(
    win=win, name='card_f_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.3, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-30.0, interpolate=True)
card_g_2 = visual.Rect(
    win=win, name='card_g_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.5, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-31.0, interpolate=True)
card_h_2 = visual.Rect(
    win=win, name='card_h_2',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.7, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-32.0, interpolate=True)
text_a_2 = visual.TextStim(win=win, name='text_a_2',
    text=None,
    font='Arial',
    pos=card_a_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-33.0);
text_b_2 = visual.TextStim(win=win, name='text_b_2',
    text=None,
    font='Arial',
    pos=card_b_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-34.0);
text_c_2 = visual.TextStim(win=win, name='text_c_2',
    text=None,
    font='Arial',
    pos=card_c_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-35.0);
text_d_2 = visual.TextStim(win=win, name='text_d_2',
    text=None,
    font='Arial',
    pos=card_d_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-36.0);
text_e_2 = visual.TextStim(win=win, name='text_e_2',
    text=None,
    font='Arial',
    pos=card_e_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-37.0);
text_f_2 = visual.TextStim(win=win, name='text_f_2',
    text=None,
    font='Arial',
    pos=card_f_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-38.0);
text_g_2 = visual.TextStim(win=win, name='text_g_2',
    text=None,
    font='Arial',
    pos=card_g_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-39.0);
text_h_2 = visual.TextStim(win=win, name='text_h_2',
    text=None,
    font='Arial',
    pos=card_h_2.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-40.0);
mouse_practice = event.Mouse(win=win)
x, y = [None, None]
mouse_practice.mouseClock = core.Clock()



# Initialize components for Routine "practice_result"
practice_resultClock = core.Clock()
search_num=0

text_practice_end = visual.TextStim(win=win, name='text_practice_end',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
button = visual.Rect(
    win=win, name='button',
    width=(0.9, 0.1)[0], height=(0.9, 0.1)[1],
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=button.pos, height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "start"
startClock = core.Clock()
text_wait_start = visual.TextStim(win=win, name='text_wait_start',
    text='以上で練習ラウンドは終了です。',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
go_regular_round = visual.Rect(
    win=win, name='go_regular_round',
    width=(0.9, 0.1)[0], height=(0.9, 0.1)[1],
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
start_regular_round = visual.TextStim(win=win, name='start_regular_round',
    text='本番を開始する',
    font='Arial',
    pos=go_regular_round.pos, height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "settingsession"
settingsessionClock = core.Clock()
text_setting = visual.TextStim(win=win, name='text_setting',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_wait_setting = visual.TextStim(win=win, name='text_wait_setting',
    text='しばらくお待ちください…',
    font='Arial',
    pos=[0,-0.4], height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
button_2 = visual.Rect(
    win=win, name='button_2',
    width=(0.9, 0.1)[0], height=(0.9, 0.1)[1],
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
text_start = visual.TextStim(win=win, name='text_start',
    text='ラウンドを開始する。',
    font='Arial',
    pos=button_2.pos, height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_round_setting = visual.TextStim(win=win, name='text_round_setting',
    text='default text',
    font='Arial',
    pos=[-0.35, 0.45], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text_round = visual.TextStim(win=win, name='text_round',
    text='default text',
    font='Arial',
    pos=[-0.35, 0.45], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_cost = visual.TextStim(win=win, name='text_cost',
    text='default text',
    font='Arial',
    pos=[0, 0.4], height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_cash = visual.TextStim(win=win, name='text_cash',
    text='default text',
    font='Arial',
    pos=[0, 0.3], height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
card_A = visual.Rect(
    win=win, name='card_A',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.7, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
text_A = visual.TextStim(win=win, name='text_A',
    text=None,
    font='Arial',
    pos=card_A.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
card_B = visual.Rect(
    win=win, name='card_B',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.5, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_B = visual.TextStim(win=win, name='text_B',
    text=None,
    font='Arial',
    pos=card_B.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
card_C = visual.Rect(
    win=win, name='card_C',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.3, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
text_C = visual.TextStim(win=win, name='text_C',
    text=None,
    font='Arial',
    pos=card_C.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
card_D = visual.Rect(
    win=win, name='card_D',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.1, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
text_D = visual.TextStim(win=win, name='text_D',
    text=None,
    font='Arial',
    pos=card_D.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
text_wait = visual.TextStim(win=win, name='text_wait',
    text='お待ちください…',
    font='Arial',
    pos=[0,-0.3], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_choice = visual.TextStim(win=win, name='text_choice',
    text=None,
    font='Arial',
    pos=[0,-0.3], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
end_button = visual.Rect(
    win=win, name='end_button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0, pos=[0.3, -0.4],
    lineWidth=1, lineColor=[2,2,2], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
end_choise = visual.TextStim(win=win, name='end_choise',
    text=None,
    font='Arial',
    pos=end_button.pos, height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
conti_button = visual.Rect(
    win=win, name='conti_button',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0, pos=[-0.3, -0.4],
    lineWidth=1, lineColor=[2,2,2], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
conti_choise = visual.TextStim(win=win, name='conti_choise',
    text=None,
    font='Arial',
    pos=conti_button.pos, height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
card_E = visual.Rect(
    win=win, name='card_E',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.1, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-17.0, interpolate=True)
card_F = visual.Rect(
    win=win, name='card_F',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.3, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-18.0, interpolate=True)
card_G = visual.Rect(
    win=win, name='card_G',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.5, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-19.0, interpolate=True)
card_H = visual.Rect(
    win=win, name='card_H',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.7, 0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-20.0, interpolate=True)
text_E = visual.TextStim(win=win, name='text_E',
    text=None,
    font='Arial',
    pos=card_E.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
text_F = visual.TextStim(win=win, name='text_F',
    text=None,
    font='Arial',
    pos=card_F.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
text_G = visual.TextStim(win=win, name='text_G',
    text=None,
    font='Arial',
    pos=card_G.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-23.0);
text_H = visual.TextStim(win=win, name='text_H',
    text=None,
    font='Arial',
    pos=card_H.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
card_a = visual.Rect(
    win=win, name='card_a',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.7, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-25.0, interpolate=True)
card_b = visual.Rect(
    win=win, name='card_b',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.5, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-26.0, interpolate=True)
card_c = visual.Rect(
    win=win, name='card_c',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.3, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-27.0, interpolate=True)
card_d = visual.Rect(
    win=win, name='card_d',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[-0.1, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-28.0, interpolate=True)
card_e = visual.Rect(
    win=win, name='card_e',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.1, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-29.0, interpolate=True)
card_f = visual.Rect(
    win=win, name='card_f',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.3, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-30.0, interpolate=True)
card_g = visual.Rect(
    win=win, name='card_g',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.5, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-31.0, interpolate=True)
card_h = visual.Rect(
    win=win, name='card_h',
    width=[0.1, 0.15][0], height=[0.1, 0.15][1],
    ori=0, pos=[0.7, -0.15],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-32.0, interpolate=True)
text_a = visual.TextStim(win=win, name='text_a',
    text=None,
    font='Arial',
    pos=card_a.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-33.0);
text_b = visual.TextStim(win=win, name='text_b',
    text=None,
    font='Arial',
    pos=card_b.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-34.0);
text_c = visual.TextStim(win=win, name='text_c',
    text=None,
    font='Arial',
    pos=card_c.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-35.0);
text_d = visual.TextStim(win=win, name='text_d',
    text=None,
    font='Arial',
    pos=card_d.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-36.0);
text_e = visual.TextStim(win=win, name='text_e',
    text=None,
    font='Arial',
    pos=card_e.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-37.0);
text_f = visual.TextStim(win=win, name='text_f',
    text=None,
    font='Arial',
    pos=card_f.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-38.0);
text_g = visual.TextStim(win=win, name='text_g',
    text=None,
    font='Arial',
    pos=card_g.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-39.0);
text_h = visual.TextStim(win=win, name='text_h',
    text=None,
    font='Arial',
    pos=card_h.pos, height=0.045, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-40.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()





# Initialize components for Routine "resultsession"
resultsessionClock = core.Clock()
text_wait_resultsession = visual.TextStim(win=win, name='text_wait_resultsession',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_round_resultsession = visual.TextStim(win=win, name='text_round_resultsession',
    text='default text',
    font='Arial',
    pos=[-0.35, 0.45], height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
button_3 = visual.Rect(
    win=win, name='button_3',
    width=(0.9, 0.1)[0], height=(0.9, 0.1)[1],
    ori=0, pos=(0, -0.4),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
text_3 = visual.TextStim(win=win, name='text_3',
    text='次のラウンドを開始する',
    font='Arial',
    pos=button_3.pos, height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_thanks = visual.TextStim(win=win, name='text_thanks',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
# update component parameters for each repeat
# keep track of which components have finished
InstructionComponents = [text_ready, start_b, start_text]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    if t>1:
        if mouse.isPressedIn(start_b,[0,]):
            break
    
    
    
    # *text_ready* updates
    if text_ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_ready.frameNStart = frameN  # exact frame index
        text_ready.tStart = t  # local t and not account for scr refresh
        text_ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_ready, 'tStartRefresh')  # time at next scr refresh
        text_ready.setAutoDraw(True)
    
    # *start_b* updates
    if start_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_b.frameNStart = frameN  # exact frame index
        start_b.tStart = t  # local t and not account for scr refresh
        start_b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_b, 'tStartRefresh')  # time at next scr refresh
        start_b.setAutoDraw(True)
    
    # *start_text* updates
    if start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text.frameNStart = frameN  # exact frame index
        start_text.tStart = t  # local t and not account for scr refresh
        start_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
        start_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=Practice_Round, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ready_practice"-------
    # update component parameters for each repeat
    search_cost=Practice_Treat_s[practice_loop.thisRepN]
    find_rate=Practice_Treat_q[practice_loop.thisRepN]
    utility=0
    before=0
    best_choise=0
    end_flag=0
    empty_flag=0
    Get_out=1
    Tie=0
    Best_update=0
    Recall=0
    Second_best=0
    Sequence=[0]
    
    
    card_list=[card_A_2,card_B_2,card_C_2,card_D_2,card_E_2,card_F_2,card_G_2,card_H_2,card_a_2,card_b_2,card_c_2,card_d_2,card_e_2,card_f_2,card_g_2,card_h_2]
    #card_pos=[[1,1],[1,2],[1,3],[1,4],[2,1],[2,2],[2,3],[2,4]]
    
    text_list=[text_A_2,text_B_2,text_C_2,text_D_2,text_E_2,text_F_2,text_G_2,text_H_2,text_a_2,text_b_2,text_c_2,text_d_2,text_e_2,text_f_2,text_g_2,text_h_2]
    text_A_2.text=""
    text_B_2.text=""
    text_C_2.text=""
    text_D_2.text=""
    text_E_2.text=""
    text_F_2.text=""
    text_G_2.text=""
    text_H_2.text=""
    
    text_a_2.text=""
    text_b_2.text=""
    text_c_2.text=""
    text_d_2.text=""
    text_e_2.text=""
    text_f_2.text=""
    text_g_2.text=""
    text_h_2.text=""
    
    text_setting_practice.setText('''これは練習ラウンドです


ただし、成功確率は

'''"                  "+str(find_rate)+'''

であり、

カードをめくるたびに毎回

'''"                  "+str(search_cost)+'''

だけコストがかかるものとします。


もう十分だと思うタイミングで探索を終了してください。

　　　　　　　　　　　　　　　　　　　　    　    　　　　　　　　''')
    # keep track of which components have finished
    ready_practiceComponents = [text_setting_practice, text_wait_practice, next_b, text_start_practice]
    for thisComponent in ready_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ready_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ready_practice"-------
    while continueRoutine:
        # get current time
        t = ready_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ready_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if t>1:
            if mouse.isPressedIn(next_b,[0,]):
                break
        
        
        
        # *text_setting_practice* updates
        if text_setting_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_setting_practice.frameNStart = frameN  # exact frame index
            text_setting_practice.tStart = t  # local t and not account for scr refresh
            text_setting_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_setting_practice, 'tStartRefresh')  # time at next scr refresh
            text_setting_practice.setAutoDraw(True)
        
        # *text_wait_practice* updates
        if text_wait_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_wait_practice.frameNStart = frameN  # exact frame index
            text_wait_practice.tStart = t  # local t and not account for scr refresh
            text_wait_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_wait_practice, 'tStartRefresh')  # time at next scr refresh
            text_wait_practice.setAutoDraw(True)
        if text_wait_practice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_wait_practice.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_wait_practice.tStop = t  # not accounting for scr refresh
                text_wait_practice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_wait_practice, 'tStopRefresh')  # time at next scr refresh
                text_wait_practice.setAutoDraw(False)
        
        # *next_b* updates
        if next_b.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            next_b.frameNStart = frameN  # exact frame index
            next_b.tStart = t  # local t and not account for scr refresh
            next_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_b, 'tStartRefresh')  # time at next scr refresh
            next_b.setAutoDraw(True)
        
        # *text_start_practice* updates
        if text_start_practice.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_start_practice.frameNStart = frameN  # exact frame index
            text_start_practice.tStart = t  # local t and not account for scr refresh
            text_start_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_start_practice, 'tStartRefresh')  # time at next scr refresh
            text_start_practice.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ready_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready_practice"-------
    for thisComponent in ready_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ready_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_trials = data.TrialHandler(nReps=99, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practice_trials')
    thisExp.addLoop(practice_trials)  # add the loop to the experiment
    thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    for thisPractice_trial in practice_trials:
        currentLoop = practice_trials
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
        if thisPractice_trial != None:
            for paramName in thisPractice_trial:
                exec('{} = thisPractice_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practice"-------
        # update component parameters for each repeat
        text_round_practice.setText(u'現在のラウンド　{}(練習)'.format(practice_loop.thisN+1))
        text_cost_practice.setText(u'コスト　　{}   '.format(search_cost)  +u'   成功確率{}'.format(find_rate))
        text_cash__practice.setText(u'現在の最大ポイント{}'.format(best_choise))
        # setup some python lists for storing info about the mouse_practice
        gotValidClick = False  # until a click is received
        mouse_practice.mouseClock.reset()
        consistency=0
        end_button_2.opacity=1
        conti_button_2.opacity=1
        conti_flag=0
        
        a=1
        b=20
        position=0
        
        end_flag=0
        #before=best_choise
        inconsistency=0
        final_choise=0
        
        before=utility
        # keep track of which components have finished
        practiceComponents = [text_round_practice, text_cost_practice, text_cash__practice, card_A_2, text_A_2, card_B_2, text_B_2, card_C_2, text_C_2, card_D_2, text_D_2, text_wait_practice_round, text_choice_2, end_button_2, end_choise_2, conti_button_2, conti_choise_2, card_E_2, card_F_2, card_G_2, card_H_2, text_E_2, text_F_2, text_G_2, text_H_2, card_a_2, card_b_2, card_c_2, card_d_2, card_e_2, card_f_2, card_g_2, card_h_2, text_a_2, text_b_2, text_c_2, text_d_2, text_e_2, text_f_2, text_g_2, text_h_2, mouse_practice]
        for thisComponent in practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "practice"-------
        while continueRoutine:
            # get current time
            t = practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_round_practice* updates
            if text_round_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_round_practice.frameNStart = frameN  # exact frame index
                text_round_practice.tStart = t  # local t and not account for scr refresh
                text_round_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_round_practice, 'tStartRefresh')  # time at next scr refresh
                text_round_practice.setAutoDraw(True)
            
            # *text_cost_practice* updates
            if text_cost_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_cost_practice.frameNStart = frameN  # exact frame index
                text_cost_practice.tStart = t  # local t and not account for scr refresh
                text_cost_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_cost_practice, 'tStartRefresh')  # time at next scr refresh
                text_cost_practice.setAutoDraw(True)
            
            # *text_cash__practice* updates
            if text_cash__practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_cash__practice.frameNStart = frameN  # exact frame index
                text_cash__practice.tStart = t  # local t and not account for scr refresh
                text_cash__practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_cash__practice, 'tStartRefresh')  # time at next scr refresh
                text_cash__practice.setAutoDraw(True)
            
            # *card_A_2* updates
            if card_A_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_A_2.frameNStart = frameN  # exact frame index
                card_A_2.tStart = t  # local t and not account for scr refresh
                card_A_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_A_2, 'tStartRefresh')  # time at next scr refresh
                card_A_2.setAutoDraw(True)
            
            # *text_A_2* updates
            if text_A_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_A_2.frameNStart = frameN  # exact frame index
                text_A_2.tStart = t  # local t and not account for scr refresh
                text_A_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_A_2, 'tStartRefresh')  # time at next scr refresh
                text_A_2.setAutoDraw(True)
            
            # *card_B_2* updates
            if card_B_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_B_2.frameNStart = frameN  # exact frame index
                card_B_2.tStart = t  # local t and not account for scr refresh
                card_B_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_B_2, 'tStartRefresh')  # time at next scr refresh
                card_B_2.setAutoDraw(True)
            
            # *text_B_2* updates
            if text_B_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_B_2.frameNStart = frameN  # exact frame index
                text_B_2.tStart = t  # local t and not account for scr refresh
                text_B_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_B_2, 'tStartRefresh')  # time at next scr refresh
                text_B_2.setAutoDraw(True)
            
            # *card_C_2* updates
            if card_C_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_C_2.frameNStart = frameN  # exact frame index
                card_C_2.tStart = t  # local t and not account for scr refresh
                card_C_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_C_2, 'tStartRefresh')  # time at next scr refresh
                card_C_2.setAutoDraw(True)
            
            # *text_C_2* updates
            if text_C_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_C_2.frameNStart = frameN  # exact frame index
                text_C_2.tStart = t  # local t and not account for scr refresh
                text_C_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_C_2, 'tStartRefresh')  # time at next scr refresh
                text_C_2.setAutoDraw(True)
            
            # *card_D_2* updates
            if card_D_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_D_2.frameNStart = frameN  # exact frame index
                card_D_2.tStart = t  # local t and not account for scr refresh
                card_D_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_D_2, 'tStartRefresh')  # time at next scr refresh
                card_D_2.setAutoDraw(True)
            
            # *text_D_2* updates
            if text_D_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_D_2.frameNStart = frameN  # exact frame index
                text_D_2.tStart = t  # local t and not account for scr refresh
                text_D_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_D_2, 'tStartRefresh')  # time at next scr refresh
                text_D_2.setAutoDraw(True)
            
            # *text_wait_practice_round* updates
            if text_wait_practice_round.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_wait_practice_round.frameNStart = frameN  # exact frame index
                text_wait_practice_round.tStart = t  # local t and not account for scr refresh
                text_wait_practice_round.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_wait_practice_round, 'tStartRefresh')  # time at next scr refresh
                text_wait_practice_round.setAutoDraw(True)
            if text_wait_practice_round.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_wait_practice_round.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_wait_practice_round.tStop = t  # not accounting for scr refresh
                    text_wait_practice_round.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_wait_practice_round, 'tStopRefresh')  # time at next scr refresh
                    text_wait_practice_round.setAutoDraw(False)
            
            # *text_choice_2* updates
            if text_choice_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_choice_2.frameNStart = frameN  # exact frame index
                text_choice_2.tStart = t  # local t and not account for scr refresh
                text_choice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_choice_2, 'tStartRefresh')  # time at next scr refresh
                text_choice_2.setAutoDraw(True)
            
            # *end_button_2* updates
            if end_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                end_button_2.frameNStart = frameN  # exact frame index
                end_button_2.tStart = t  # local t and not account for scr refresh
                end_button_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(end_button_2, 'tStartRefresh')  # time at next scr refresh
                end_button_2.setAutoDraw(True)
            
            # *end_choise_2* updates
            if end_choise_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                end_choise_2.frameNStart = frameN  # exact frame index
                end_choise_2.tStart = t  # local t and not account for scr refresh
                end_choise_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(end_choise_2, 'tStartRefresh')  # time at next scr refresh
                end_choise_2.setAutoDraw(True)
            
            # *conti_button_2* updates
            if conti_button_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                conti_button_2.frameNStart = frameN  # exact frame index
                conti_button_2.tStart = t  # local t and not account for scr refresh
                conti_button_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conti_button_2, 'tStartRefresh')  # time at next scr refresh
                conti_button_2.setAutoDraw(True)
            
            # *conti_choise_2* updates
            if conti_choise_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                conti_choise_2.frameNStart = frameN  # exact frame index
                conti_choise_2.tStart = t  # local t and not account for scr refresh
                conti_choise_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conti_choise_2, 'tStartRefresh')  # time at next scr refresh
                conti_choise_2.setAutoDraw(True)
            
            # *card_E_2* updates
            if card_E_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_E_2.frameNStart = frameN  # exact frame index
                card_E_2.tStart = t  # local t and not account for scr refresh
                card_E_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_E_2, 'tStartRefresh')  # time at next scr refresh
                card_E_2.setAutoDraw(True)
            
            # *card_F_2* updates
            if card_F_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_F_2.frameNStart = frameN  # exact frame index
                card_F_2.tStart = t  # local t and not account for scr refresh
                card_F_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_F_2, 'tStartRefresh')  # time at next scr refresh
                card_F_2.setAutoDraw(True)
            
            # *card_G_2* updates
            if card_G_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_G_2.frameNStart = frameN  # exact frame index
                card_G_2.tStart = t  # local t and not account for scr refresh
                card_G_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_G_2, 'tStartRefresh')  # time at next scr refresh
                card_G_2.setAutoDraw(True)
            
            # *card_H_2* updates
            if card_H_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_H_2.frameNStart = frameN  # exact frame index
                card_H_2.tStart = t  # local t and not account for scr refresh
                card_H_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_H_2, 'tStartRefresh')  # time at next scr refresh
                card_H_2.setAutoDraw(True)
            
            # *text_E_2* updates
            if text_E_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_E_2.frameNStart = frameN  # exact frame index
                text_E_2.tStart = t  # local t and not account for scr refresh
                text_E_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_E_2, 'tStartRefresh')  # time at next scr refresh
                text_E_2.setAutoDraw(True)
            
            # *text_F_2* updates
            if text_F_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_F_2.frameNStart = frameN  # exact frame index
                text_F_2.tStart = t  # local t and not account for scr refresh
                text_F_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_F_2, 'tStartRefresh')  # time at next scr refresh
                text_F_2.setAutoDraw(True)
            
            # *text_G_2* updates
            if text_G_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_G_2.frameNStart = frameN  # exact frame index
                text_G_2.tStart = t  # local t and not account for scr refresh
                text_G_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_G_2, 'tStartRefresh')  # time at next scr refresh
                text_G_2.setAutoDraw(True)
            
            # *text_H_2* updates
            if text_H_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_H_2.frameNStart = frameN  # exact frame index
                text_H_2.tStart = t  # local t and not account for scr refresh
                text_H_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_H_2, 'tStartRefresh')  # time at next scr refresh
                text_H_2.setAutoDraw(True)
            
            # *card_a_2* updates
            if card_a_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_a_2.frameNStart = frameN  # exact frame index
                card_a_2.tStart = t  # local t and not account for scr refresh
                card_a_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_a_2, 'tStartRefresh')  # time at next scr refresh
                card_a_2.setAutoDraw(True)
            
            # *card_b_2* updates
            if card_b_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_b_2.frameNStart = frameN  # exact frame index
                card_b_2.tStart = t  # local t and not account for scr refresh
                card_b_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_b_2, 'tStartRefresh')  # time at next scr refresh
                card_b_2.setAutoDraw(True)
            
            # *card_c_2* updates
            if card_c_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_c_2.frameNStart = frameN  # exact frame index
                card_c_2.tStart = t  # local t and not account for scr refresh
                card_c_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_c_2, 'tStartRefresh')  # time at next scr refresh
                card_c_2.setAutoDraw(True)
            
            # *card_d_2* updates
            if card_d_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_d_2.frameNStart = frameN  # exact frame index
                card_d_2.tStart = t  # local t and not account for scr refresh
                card_d_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_d_2, 'tStartRefresh')  # time at next scr refresh
                card_d_2.setAutoDraw(True)
            
            # *card_e_2* updates
            if card_e_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_e_2.frameNStart = frameN  # exact frame index
                card_e_2.tStart = t  # local t and not account for scr refresh
                card_e_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_e_2, 'tStartRefresh')  # time at next scr refresh
                card_e_2.setAutoDraw(True)
            
            # *card_f_2* updates
            if card_f_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_f_2.frameNStart = frameN  # exact frame index
                card_f_2.tStart = t  # local t and not account for scr refresh
                card_f_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_f_2, 'tStartRefresh')  # time at next scr refresh
                card_f_2.setAutoDraw(True)
            
            # *card_g_2* updates
            if card_g_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_g_2.frameNStart = frameN  # exact frame index
                card_g_2.tStart = t  # local t and not account for scr refresh
                card_g_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_g_2, 'tStartRefresh')  # time at next scr refresh
                card_g_2.setAutoDraw(True)
            
            # *card_h_2* updates
            if card_h_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_h_2.frameNStart = frameN  # exact frame index
                card_h_2.tStart = t  # local t and not account for scr refresh
                card_h_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_h_2, 'tStartRefresh')  # time at next scr refresh
                card_h_2.setAutoDraw(True)
            
            # *text_a_2* updates
            if text_a_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_a_2.frameNStart = frameN  # exact frame index
                text_a_2.tStart = t  # local t and not account for scr refresh
                text_a_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_a_2, 'tStartRefresh')  # time at next scr refresh
                text_a_2.setAutoDraw(True)
            
            # *text_b_2* updates
            if text_b_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_b_2.frameNStart = frameN  # exact frame index
                text_b_2.tStart = t  # local t and not account for scr refresh
                text_b_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_b_2, 'tStartRefresh')  # time at next scr refresh
                text_b_2.setAutoDraw(True)
            
            # *text_c_2* updates
            if text_c_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_c_2.frameNStart = frameN  # exact frame index
                text_c_2.tStart = t  # local t and not account for scr refresh
                text_c_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_c_2, 'tStartRefresh')  # time at next scr refresh
                text_c_2.setAutoDraw(True)
            
            # *text_d_2* updates
            if text_d_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_d_2.frameNStart = frameN  # exact frame index
                text_d_2.tStart = t  # local t and not account for scr refresh
                text_d_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_d_2, 'tStartRefresh')  # time at next scr refresh
                text_d_2.setAutoDraw(True)
            
            # *text_e_2* updates
            if text_e_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_e_2.frameNStart = frameN  # exact frame index
                text_e_2.tStart = t  # local t and not account for scr refresh
                text_e_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_e_2, 'tStartRefresh')  # time at next scr refresh
                text_e_2.setAutoDraw(True)
            
            # *text_f_2* updates
            if text_f_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_f_2.frameNStart = frameN  # exact frame index
                text_f_2.tStart = t  # local t and not account for scr refresh
                text_f_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_f_2, 'tStartRefresh')  # time at next scr refresh
                text_f_2.setAutoDraw(True)
            
            # *text_g_2* updates
            if text_g_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_g_2.frameNStart = frameN  # exact frame index
                text_g_2.tStart = t  # local t and not account for scr refresh
                text_g_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_g_2, 'tStartRefresh')  # time at next scr refresh
                text_g_2.setAutoDraw(True)
            
            # *text_h_2* updates
            if text_h_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_h_2.frameNStart = frameN  # exact frame index
                text_h_2.tStart = t  # local t and not account for scr refresh
                text_h_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_h_2, 'tStartRefresh')  # time at next scr refresh
                text_h_2.setAutoDraw(True)
            # *mouse_practice* updates
            if mouse_practice.status == NOT_STARTED and t >= 1-frameTolerance:
                # keep track of start time/frame for later
                mouse_practice.frameNStart = frameN  # exact frame index
                mouse_practice.tStart = t  # local t and not account for scr refresh
                mouse_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_practice, 'tStartRefresh')  # time at next scr refresh
                mouse_practice.status = STARTED
                prevButtonState = mouse_practice.getPressed()  # if button is down already this ISN'T a new click
            if mouse_practice.status == STARTED:  # only update if started and not finished!
                buttons = mouse_practice.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            if t>1 and conti_flag==1:
                for id, card in enumerate(card_list):
                    if mouse.isPressedIn(card,[0,]):
                        
                        practice_trials.addData('decision_time', t)
                        
                        Get_out=0
                        position=id+1
                        utility=np.random.randint(a, b, 1,int)[0]
                        text_list[id].text=str(utility)
                        del card_list[id]
                        del text_list[id]
                        continueRoutine = False
                        break
            
            
            if  conti_flag==0:
                text_choice_2.text="ラウンドを続行しますか"
                conti_choise_2.text='選択肢.1\nカードをめくる'
                end_choise_2.text='選択肢.2\nラウンドを終了する'
            else:
                text_choice_2.text="次にめくるカードをクリックしてください"
                conti_choise_2.text=''
                conti_button_2.opacity=0
            
            
            
            
            if t>1 and mouse.isPressedIn(end_button,[0,]):
                practice_trials.addData('choise_time', t)
                practice_trials.addData('decision_time', t)
                end_flag=1
                continueRoutine = False
            
            if t>1 and conti_flag==0 and mouse.isPressedIn(conti_button,[0,]):
                
                practice_trials.addData('choise_time', t)
                conti_flag=1
                if empty_flag==1:
                    card_list=[card_A_2,card_B_2,card_C_2,card_D_2,card_E_2,card_F_2,card_G_2,card_H_2,card_a_2,card_b_2,card_c_2,card_d_2,card_e_2,card_f_2,card_g_2,card_h_2]
                    text_list=[text_A_2,text_B_2,text_C_2,text_D_2,text_E_2,text_F_2,text_G_2,text_H_2,text_a_2,text_b_2,text_c_2,text_d_2,text_e_2,text_f_2,text_g_2,text_h_2]
                    text_A_2.text=""
                    text_B_2.text=""
                    text_C_2.text=""
                    text_D_2.text=""
                    text_E_2.text=""
                    text_F_2.text=""
                    text_G_2.text=""
                    text_H_2.text=""
                    text_a_2.text=""
                    text_b_2.text=""
                    text_c_2.text=""
                    text_d_2.text=""
                    text_e_2.text=""
                    text_f_2.text=""
                    text_g_2.text=""
                    text_h_2.text=""
            
            
            
            
            
            
            #for card in [card_A, card_B, card_C, card_D]:
            #    if card.contains([selected_card_xpos,0]):
            #        card.opacity =0
            #    else:
            #        card.fillColor='white'
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice"-------
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for practice_trials (TrialHandler)
        practice_trials.addData('mouse_practice.started', mouse_practice.tStart)
        practice_trials.addData('mouse_practice.stopped', mouse_practice.tStop)
        
        practice_trials.addData('practice',1)
        
        practice_trials.addData('position', position)
        
        
        practice_trials.addData('round_num', practice_loop.thisN+1)
        
        practice_trials.addData('best_choise', best_choise)
        search_num= practice_trials.thisRepN+1
        practice_trials.addData('search_num', practice_trials.thisRepN)
        practice_trials.addData('entry', conti_flag)
        practice_trials.addData('end_choise', end_flag)
        
        practice_trials.addData('Reshuffle', empty_flag)
        practice_trials.addData('search_cost', search_cost)
        total_cost=search_cost*practice_trials.thisRepN
        practice_trials.addData('total_cost', total_cost)
        
        
        #trials.addData('payoff', best_choise-search_cost*trials.thisRepN)
        
        
        if len(text_list)==0:
            empty_flag=1
            final_choise=1
        else:
            empty_flag=0
        
        Sequence.append(utility)
        
        
        if len(Sequence)<2:
            before=0
        else:
            before=Sequence[-2]
        
        practice_trials.addData('before', before)
        practice_trials.addData('Tie', Tie)
        Tie=int(best_choise==utility)
        
        Recall=int(Best_update==0 and end_flag==1)
        practice_trials.addData('Recall', Recall)
        
        Best_update=int(utility>best_choise)
        practice_trials.addData('Best_update', Best_update)
        
        if len(sorted(set(Sequence)))<2:
            Second_best=0
        else:
            Second_best=sorted(set(Sequence))[-2]
            
        practice_trials.addData('Second_best',Second_best)
        
        
        
        best_choise=max(utility,best_choise)
        inconsistency=int(best_choise>utility and end_flag==1)
        practice_trials.addData('utility', utility)
        
        final_choise=max(utility,best_choise)*end_flag
        practice_trials.addData('final_choise', final_choise)
        practice_trials.addData('inconsistency', inconsistency)
        practice_trials.addData('Get_out', Get_out)
        if end_flag==1:
            break
        
        
        
        
        # the Routine "practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 99 repeats of 'practice_trials'
    
    
    # ------Prepare to start Routine "practice_result"-------
    # update component parameters for each repeat
    tmp=best_choise-total_cost
    
    
    text_practice_end.setText(u'\nこのラウンドであなたがみつけたカードの最大ポイントは'+'\n{}ポイントでした。'.format(best_choise)+u'\nコストは{}で、カードをめくった回数は{}回なので'.format(search_cost,search_num-1)+u'\n総コストは{}となります。   '.format(total_cost)+'\nよってこのラウンドでのあなたの最終的な結果は　   '  +u'\n{}ポイントです。\n'.format(tmp)+"\n　\n ")
    button.setOpacity(0)
    text.setColor('white', colorSpace='rgb')
    text.setText('しばらく、お待ちください')
    # keep track of which components have finished
    practice_resultComponents = [text_practice_end, button, text]
    for thisComponent in practice_resultComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_resultClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice_result"-------
    while continueRoutine:
        # get current time
        t = practice_resultClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_resultClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if t>1:
            text.text="次のラウンドへ"
            text.color ="black"
            button.opacity=1
            if mouse.isPressedIn(button,[0,]):
                break
        
        
        # *text_practice_end* updates
        if text_practice_end.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_practice_end.frameNStart = frameN  # exact frame index
            text_practice_end.tStart = t  # local t and not account for scr refresh
            text_practice_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_practice_end, 'tStartRefresh')  # time at next scr refresh
            text_practice_end.setAutoDraw(True)
        
        # *button* updates
        if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            button.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_resultComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_result"-------
    for thisComponent in practice_resultComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Search_num=0
    # the Routine "practice_result" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed Practice_Round repeats of 'practice_loop'


# ------Prepare to start Routine "start"-------
# update component parameters for each repeat
Fixed_cost=0
# keep track of which components have finished
startComponents = [text_wait_start, go_regular_round, start_regular_round]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if t>1:
        if mouse.isPressedIn(next_b,[0,]):
            break
    
    
    # *text_wait_start* updates
    if text_wait_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_wait_start.frameNStart = frameN  # exact frame index
        text_wait_start.tStart = t  # local t and not account for scr refresh
        text_wait_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_wait_start, 'tStartRefresh')  # time at next scr refresh
        text_wait_start.setAutoDraw(True)
    
    # *go_regular_round* updates
    if go_regular_round.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        go_regular_round.frameNStart = frameN  # exact frame index
        go_regular_round.tStart = t  # local t and not account for scr refresh
        go_regular_round.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(go_regular_round, 'tStartRefresh')  # time at next scr refresh
        go_regular_round.setAutoDraw(True)
    
    # *start_regular_round* updates
    if start_regular_round.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        start_regular_round.frameNStart = frameN  # exact frame index
        start_regular_round.tStart = t  # local t and not account for scr refresh
        start_regular_round.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_regular_round, 'tStartRefresh')  # time at next scr refresh
        start_regular_round.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
round_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_treatment.xlsx'),
    seed=None, name='round_loop')
thisExp.addLoop(round_loop)  # add the loop to the experiment
thisRound_loop = round_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRound_loop.rgb)
if thisRound_loop != None:
    for paramName in thisRound_loop:
        exec('{} = thisRound_loop[paramName]'.format(paramName))

for thisRound_loop in round_loop:
    currentLoop = round_loop
    # abbreviate parameter names if possible (e.g. rgb = thisRound_loop.rgb)
    if thisRound_loop != None:
        for paramName in thisRound_loop:
            exec('{} = thisRound_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "settingsession"-------
    # update component parameters for each repeat
    search_cost=Treat_s
    find_rate=Treat_q
    
    utility=0
    before=0
    best_choise=0
    search_num=0
    
    
    end_flag=0
    empty_flag=0
    
    Get_out=1
    Tie=0
    Best_update=0
    Recall=0
    Second_best=0
    Sequence=[0]
    
    practice_trials.addData('Second_best',Second_best)
    card_list=[card_A,card_B,card_C,card_D,card_E,card_F,card_G,card_H,card_a,card_b,card_c,card_d,card_e,card_f,card_g,card_h]
    #card_pos=[[1,1],[1,2],[1,3],[1,4],[2,1],[2,2],[2,3],[2,4]]
    
    text_list=[text_A,text_B,text_C,text_D,text_E,text_F,text_G,text_H,text_a,text_b,text_c,text_d,text_e,text_f,text_g,text_h]
    text_A.text=""
    text_B.text=""
    text_C.text=""
    text_D.text=""
    text_E.text=""
    text_F.text=""
    text_G.text=""
    text_H.text=""
    
    text_a.text=""
    text_b.text=""
    text_c.text=""
    text_d.text=""
    text_e.text=""
    text_f.text=""
    text_g.text=""
    text_h.text=""
    
    text_setting.setText('''ラウンドを開始し、自由にカードをめくってください。

ただし、成功確率は

'''"                  "+str(find_rate)+'''

であり、

カードをめくるたびに毎回

'''"                  "+str(search_cost)+'''

だけコストがかかるものとします。

もう十分だと思うタイミングで探索を終了してください。

　　　　　　　　　　　　　　　　　　　　    　    　　　　　　　　''')
    text_round_setting.setText(u'現在のラウンド　 {}'.format(round_loop.thisN+1))
    # keep track of which components have finished
    settingsessionComponents = [text_setting, text_wait_setting, button_2, text_start, text_round_setting]
    for thisComponent in settingsessionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    settingsessionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "settingsession"-------
    while continueRoutine:
        # get current time
        t = settingsessionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=settingsessionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if t>1:
            if mouse.isPressedIn(button_2,[0,]):
                break
        
        
        # *text_setting* updates
        if text_setting.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_setting.frameNStart = frameN  # exact frame index
            text_setting.tStart = t  # local t and not account for scr refresh
            text_setting.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_setting, 'tStartRefresh')  # time at next scr refresh
            text_setting.setAutoDraw(True)
        
        # *text_wait_setting* updates
        if text_wait_setting.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_wait_setting.frameNStart = frameN  # exact frame index
            text_wait_setting.tStart = t  # local t and not account for scr refresh
            text_wait_setting.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_wait_setting, 'tStartRefresh')  # time at next scr refresh
            text_wait_setting.setAutoDraw(True)
        if text_wait_setting.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_wait_setting.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                text_wait_setting.tStop = t  # not accounting for scr refresh
                text_wait_setting.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_wait_setting, 'tStopRefresh')  # time at next scr refresh
                text_wait_setting.setAutoDraw(False)
        
        # *button_2* updates
        if button_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            button_2.frameNStart = frameN  # exact frame index
            button_2.tStart = t  # local t and not account for scr refresh
            button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
            button_2.setAutoDraw(True)
        
        # *text_start* updates
        if text_start.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            text_start.frameNStart = frameN  # exact frame index
            text_start.tStart = t  # local t and not account for scr refresh
            text_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_start, 'tStartRefresh')  # time at next scr refresh
            text_start.setAutoDraw(True)
        
        # *text_round_setting* updates
        if text_round_setting.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_round_setting.frameNStart = frameN  # exact frame index
            text_round_setting.tStart = t  # local t and not account for scr refresh
            text_round_setting.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_round_setting, 'tStartRefresh')  # time at next scr refresh
            text_round_setting.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in settingsessionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "settingsession"-------
    for thisComponent in settingsessionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "settingsession" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=999, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
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
        # update component parameters for each repeat
        text_round.setText(u'現在のラウンド　 {}'.format(round_loop.thisN+1))
        text_cost.setText(u'コスト　　{}   '.format(search_cost)  +u'   成功確率{}'.format(find_rate))
        text_cash.setText(u'現在の最大ポイント{}'.format(best_choise))
        # setup some python lists for storing info about the mouse
        gotValidClick = False  # until a click is received
        mouse.mouseClock.reset()
        end_button.opacity=1
        conti_button.opacity=1
        conti_flag=0
        
        position=0
        
        end_flag=0
        
        inconsistency=0
        final_choise=0
        
        before=utility
        # keep track of which components have finished
        trialComponents = [text_round, text_cost, text_cash, card_A, text_A, card_B, text_B, card_C, text_C, card_D, text_D, text_wait, text_choice, end_button, end_choise, conti_button, conti_choise, card_E, card_F, card_G, card_H, text_E, text_F, text_G, text_H, card_a, card_b, card_c, card_d, card_e, card_f, card_g, card_h, text_a, text_b, text_c, text_d, text_e, text_f, text_g, text_h, mouse]
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
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_round* updates
            if text_round.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_round.frameNStart = frameN  # exact frame index
                text_round.tStart = t  # local t and not account for scr refresh
                text_round.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_round, 'tStartRefresh')  # time at next scr refresh
                text_round.setAutoDraw(True)
            
            # *text_cost* updates
            if text_cost.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_cost.frameNStart = frameN  # exact frame index
                text_cost.tStart = t  # local t and not account for scr refresh
                text_cost.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_cost, 'tStartRefresh')  # time at next scr refresh
                text_cost.setAutoDraw(True)
            
            # *text_cash* updates
            if text_cash.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_cash.frameNStart = frameN  # exact frame index
                text_cash.tStart = t  # local t and not account for scr refresh
                text_cash.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_cash, 'tStartRefresh')  # time at next scr refresh
                text_cash.setAutoDraw(True)
            
            # *card_A* updates
            if card_A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_A.frameNStart = frameN  # exact frame index
                card_A.tStart = t  # local t and not account for scr refresh
                card_A.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_A, 'tStartRefresh')  # time at next scr refresh
                card_A.setAutoDraw(True)
            
            # *text_A* updates
            if text_A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_A.frameNStart = frameN  # exact frame index
                text_A.tStart = t  # local t and not account for scr refresh
                text_A.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_A, 'tStartRefresh')  # time at next scr refresh
                text_A.setAutoDraw(True)
            
            # *card_B* updates
            if card_B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_B.frameNStart = frameN  # exact frame index
                card_B.tStart = t  # local t and not account for scr refresh
                card_B.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_B, 'tStartRefresh')  # time at next scr refresh
                card_B.setAutoDraw(True)
            
            # *text_B* updates
            if text_B.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_B.frameNStart = frameN  # exact frame index
                text_B.tStart = t  # local t and not account for scr refresh
                text_B.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_B, 'tStartRefresh')  # time at next scr refresh
                text_B.setAutoDraw(True)
            
            # *card_C* updates
            if card_C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_C.frameNStart = frameN  # exact frame index
                card_C.tStart = t  # local t and not account for scr refresh
                card_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_C, 'tStartRefresh')  # time at next scr refresh
                card_C.setAutoDraw(True)
            
            # *text_C* updates
            if text_C.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_C.frameNStart = frameN  # exact frame index
                text_C.tStart = t  # local t and not account for scr refresh
                text_C.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_C, 'tStartRefresh')  # time at next scr refresh
                text_C.setAutoDraw(True)
            
            # *card_D* updates
            if card_D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_D.frameNStart = frameN  # exact frame index
                card_D.tStart = t  # local t and not account for scr refresh
                card_D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_D, 'tStartRefresh')  # time at next scr refresh
                card_D.setAutoDraw(True)
            
            # *text_D* updates
            if text_D.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_D.frameNStart = frameN  # exact frame index
                text_D.tStart = t  # local t and not account for scr refresh
                text_D.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_D, 'tStartRefresh')  # time at next scr refresh
                text_D.setAutoDraw(True)
            
            # *text_wait* updates
            if text_wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_wait.frameNStart = frameN  # exact frame index
                text_wait.tStart = t  # local t and not account for scr refresh
                text_wait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_wait, 'tStartRefresh')  # time at next scr refresh
                text_wait.setAutoDraw(True)
            if text_wait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_wait.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_wait.tStop = t  # not accounting for scr refresh
                    text_wait.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_wait, 'tStopRefresh')  # time at next scr refresh
                    text_wait.setAutoDraw(False)
            
            # *text_choice* updates
            if text_choice.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_choice.frameNStart = frameN  # exact frame index
                text_choice.tStart = t  # local t and not account for scr refresh
                text_choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_choice, 'tStartRefresh')  # time at next scr refresh
                text_choice.setAutoDraw(True)
            
            # *end_button* updates
            if end_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                end_button.frameNStart = frameN  # exact frame index
                end_button.tStart = t  # local t and not account for scr refresh
                end_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(end_button, 'tStartRefresh')  # time at next scr refresh
                end_button.setAutoDraw(True)
            
            # *end_choise* updates
            if end_choise.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                end_choise.frameNStart = frameN  # exact frame index
                end_choise.tStart = t  # local t and not account for scr refresh
                end_choise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(end_choise, 'tStartRefresh')  # time at next scr refresh
                end_choise.setAutoDraw(True)
            
            # *conti_button* updates
            if conti_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                conti_button.frameNStart = frameN  # exact frame index
                conti_button.tStart = t  # local t and not account for scr refresh
                conti_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conti_button, 'tStartRefresh')  # time at next scr refresh
                conti_button.setAutoDraw(True)
            
            # *conti_choise* updates
            if conti_choise.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                conti_choise.frameNStart = frameN  # exact frame index
                conti_choise.tStart = t  # local t and not account for scr refresh
                conti_choise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conti_choise, 'tStartRefresh')  # time at next scr refresh
                conti_choise.setAutoDraw(True)
            
            # *card_E* updates
            if card_E.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_E.frameNStart = frameN  # exact frame index
                card_E.tStart = t  # local t and not account for scr refresh
                card_E.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_E, 'tStartRefresh')  # time at next scr refresh
                card_E.setAutoDraw(True)
            
            # *card_F* updates
            if card_F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_F.frameNStart = frameN  # exact frame index
                card_F.tStart = t  # local t and not account for scr refresh
                card_F.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_F, 'tStartRefresh')  # time at next scr refresh
                card_F.setAutoDraw(True)
            
            # *card_G* updates
            if card_G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_G.frameNStart = frameN  # exact frame index
                card_G.tStart = t  # local t and not account for scr refresh
                card_G.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_G, 'tStartRefresh')  # time at next scr refresh
                card_G.setAutoDraw(True)
            
            # *card_H* updates
            if card_H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_H.frameNStart = frameN  # exact frame index
                card_H.tStart = t  # local t and not account for scr refresh
                card_H.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_H, 'tStartRefresh')  # time at next scr refresh
                card_H.setAutoDraw(True)
            
            # *text_E* updates
            if text_E.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_E.frameNStart = frameN  # exact frame index
                text_E.tStart = t  # local t and not account for scr refresh
                text_E.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_E, 'tStartRefresh')  # time at next scr refresh
                text_E.setAutoDraw(True)
            
            # *text_F* updates
            if text_F.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_F.frameNStart = frameN  # exact frame index
                text_F.tStart = t  # local t and not account for scr refresh
                text_F.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_F, 'tStartRefresh')  # time at next scr refresh
                text_F.setAutoDraw(True)
            
            # *text_G* updates
            if text_G.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_G.frameNStart = frameN  # exact frame index
                text_G.tStart = t  # local t and not account for scr refresh
                text_G.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_G, 'tStartRefresh')  # time at next scr refresh
                text_G.setAutoDraw(True)
            
            # *text_H* updates
            if text_H.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_H.frameNStart = frameN  # exact frame index
                text_H.tStart = t  # local t and not account for scr refresh
                text_H.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_H, 'tStartRefresh')  # time at next scr refresh
                text_H.setAutoDraw(True)
            
            # *card_a* updates
            if card_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_a.frameNStart = frameN  # exact frame index
                card_a.tStart = t  # local t and not account for scr refresh
                card_a.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_a, 'tStartRefresh')  # time at next scr refresh
                card_a.setAutoDraw(True)
            
            # *card_b* updates
            if card_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_b.frameNStart = frameN  # exact frame index
                card_b.tStart = t  # local t and not account for scr refresh
                card_b.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_b, 'tStartRefresh')  # time at next scr refresh
                card_b.setAutoDraw(True)
            
            # *card_c* updates
            if card_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_c.frameNStart = frameN  # exact frame index
                card_c.tStart = t  # local t and not account for scr refresh
                card_c.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_c, 'tStartRefresh')  # time at next scr refresh
                card_c.setAutoDraw(True)
            
            # *card_d* updates
            if card_d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_d.frameNStart = frameN  # exact frame index
                card_d.tStart = t  # local t and not account for scr refresh
                card_d.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_d, 'tStartRefresh')  # time at next scr refresh
                card_d.setAutoDraw(True)
            
            # *card_e* updates
            if card_e.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_e.frameNStart = frameN  # exact frame index
                card_e.tStart = t  # local t and not account for scr refresh
                card_e.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_e, 'tStartRefresh')  # time at next scr refresh
                card_e.setAutoDraw(True)
            
            # *card_f* updates
            if card_f.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_f.frameNStart = frameN  # exact frame index
                card_f.tStart = t  # local t and not account for scr refresh
                card_f.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_f, 'tStartRefresh')  # time at next scr refresh
                card_f.setAutoDraw(True)
            
            # *card_g* updates
            if card_g.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_g.frameNStart = frameN  # exact frame index
                card_g.tStart = t  # local t and not account for scr refresh
                card_g.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_g, 'tStartRefresh')  # time at next scr refresh
                card_g.setAutoDraw(True)
            
            # *card_h* updates
            if card_h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                card_h.frameNStart = frameN  # exact frame index
                card_h.tStart = t  # local t and not account for scr refresh
                card_h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(card_h, 'tStartRefresh')  # time at next scr refresh
                card_h.setAutoDraw(True)
            
            # *text_a* updates
            if text_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_a.frameNStart = frameN  # exact frame index
                text_a.tStart = t  # local t and not account for scr refresh
                text_a.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_a, 'tStartRefresh')  # time at next scr refresh
                text_a.setAutoDraw(True)
            
            # *text_b* updates
            if text_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_b.frameNStart = frameN  # exact frame index
                text_b.tStart = t  # local t and not account for scr refresh
                text_b.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_b, 'tStartRefresh')  # time at next scr refresh
                text_b.setAutoDraw(True)
            
            # *text_c* updates
            if text_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_c.frameNStart = frameN  # exact frame index
                text_c.tStart = t  # local t and not account for scr refresh
                text_c.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_c, 'tStartRefresh')  # time at next scr refresh
                text_c.setAutoDraw(True)
            
            # *text_d* updates
            if text_d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_d.frameNStart = frameN  # exact frame index
                text_d.tStart = t  # local t and not account for scr refresh
                text_d.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_d, 'tStartRefresh')  # time at next scr refresh
                text_d.setAutoDraw(True)
            
            # *text_e* updates
            if text_e.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_e.frameNStart = frameN  # exact frame index
                text_e.tStart = t  # local t and not account for scr refresh
                text_e.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_e, 'tStartRefresh')  # time at next scr refresh
                text_e.setAutoDraw(True)
            
            # *text_f* updates
            if text_f.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_f.frameNStart = frameN  # exact frame index
                text_f.tStart = t  # local t and not account for scr refresh
                text_f.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_f, 'tStartRefresh')  # time at next scr refresh
                text_f.setAutoDraw(True)
            
            # *text_g* updates
            if text_g.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_g.frameNStart = frameN  # exact frame index
                text_g.tStart = t  # local t and not account for scr refresh
                text_g.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_g, 'tStartRefresh')  # time at next scr refresh
                text_g.setAutoDraw(True)
            
            # *text_h* updates
            if text_h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_h.frameNStart = frameN  # exact frame index
                text_h.tStart = t  # local t and not account for scr refresh
                text_h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_h, 'tStartRefresh')  # time at next scr refresh
                text_h.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 1-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            
            if t>1 and conti_flag==1:
                for id, card in enumerate(card_list):
                    if mouse.isPressedIn(card,[0,]):
                        
                        trials.addData('decision_time', t)
                        Get_out=0
                        position=id+1
                        utility=np.random.randint(a, b, 1,int)[0]
                        text_list[id].text=str(utility)
                        del card_list[id]
                        del text_list[id]
                        continueRoutine = False
                        break
            
            
            if  conti_flag==0:
                text_choice.text="ラウンドを続行しますか？"
                conti_choise.text='選択肢.1\nカードをめくる'
                end_choise.text='選択肢.2\nラウンドを終了する'
            else:
                text_choice.text="次にめくるカードをクリックしてください"
                conti_choise.text=''
                conti_button.opacity=0
            
            
            if t>1 and mouse.isPressedIn(end_button,[0,]):
                trials.addData('choise_time', t)
                trials.addData('decision_time', t)
                end_flag=1
                continueRoutine = False
            
            if t>1 and conti_flag==0 and mouse.isPressedIn(conti_button,[0,]):
                trials.addData('choise_time', t)
                conti_flag=1
                if empty_flag==1:
                    card_list=[card_A,card_B,card_C,card_D,card_E,card_F,card_G,card_H,card_a,card_b,card_c,card_d,card_e,card_f,card_g,card_h]
                    text_list=[text_A,text_B,text_C,text_D,text_E,text_F,text_G,text_H,text_a,text_b,text_c,text_d,text_e,text_f,text_g,text_h]
                    text_A.text=""
                    text_B.text=""
                    text_C.text=""
                    text_D.text=""
                    text_E.text=""
                    text_F.text=""
                    text_G.text=""
                    text_H.text=""
                    text_a.text=""
                    text_b.text=""
                    text_c.text=""
                    text_d.text=""
                    text_e.text=""
                    text_f.text=""
                    text_g.text=""
                    text_h.text=""
            
            
            
            
            
            
            #for card in [card_A, card_B, card_C, card_D]:
            #    if card.contains([selected_card_xpos,0]):
            #        card.opacity =0
            #    else:
            #        card.fillColor='white'
            
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
        # store data for trials (TrialHandler)
        trials.addData('mouse.started', mouse.tStart)
        trials.addData('mouse.stopped', mouse.tStop)
        trials.addData('practice',0)
        
        
        trials.addData('position', position)
        
        
        trials.addData('round_num', round_loop.thisN+1)
        
        trials.addData('best_choise', best_choise)
        search_num= trials.thisRepN+1
        trials.addData('search_num', trials.thisRepN)
        trials.addData('entry', conti_flag)
        trials.addData('end_choise', end_flag)
        
        trials.addData('Reshuffle', empty_flag)
        trials.addData('search_cost', search_cost)
        total_cost=search_cost*trials.thisRepN
        trials.addData('total_cost', total_cost)
        
        
        #trials.addData('payoff', best_choise-search_cost*trials.thisRepN)
        
        
        if len(text_list)==0:
            empty_flag=1
            final_choise=1
        else:
            empty_flag=0
        
        
        Sequence.append(utility)
        
        if len(Sequence)<2:
            before=0
        else:
            before=Sequence[-2]
        
        trials.addData('before', before)
        trials.addData('Tie', Tie)
        Tie=int(best_choise==utility)
        
        Recall=int(Best_update==0 and end_flag==1)
        trials.addData('Recall', Recall)
        
        Best_update=int(utility>best_choise)
        trials.addData('Best_update', Best_update)
        
        
        if len(sorted(set(Sequence)))<2:
            Second_best=0
        else:
            Second_best=sorted(set(Sequence))[-2]
        
        trials.addData('Second_best', Second_best)
        
        best_choise=max(utility,best_choise)
        inconsistency=int(best_choise>utility and end_flag==1)
        
        trials.addData('utility', utility)
        
        final_choise=max(utility,best_choise)*end_flag
        trials.addData('final_choise', final_choise)
        trials.addData('inconsistency', inconsistency)
        trials.addData('Get_out', Get_out)
        if end_flag==1:
            break
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 999 repeats of 'trials'
    
    
    # ------Prepare to start Routine "resultsession"-------
    # update component parameters for each repeat
    tmp=best_choise-total_cost
    Result.append(best_choise-total_cost)
    
    text_wait_resultsession.setText(u'\nこのラウンドであなたがみつけたカードの最大ポイントは'+'\n{}ポイントでした。'.format(best_choise)+u'\nコストは{}で、カードをめくった回数は{}回なので'.format(search_cost,search_num-1,total_cost)+u'\n総コストは{}となります。   '.format(total_cost)+'\nよってこのラウンドでのあなたの最終的な結果は　   '  +u'\n{}ポイントです。\n'.format(tmp)+"\n　\n　")
    text_round_resultsession.setText(u'現在のラウンド　 {}'.format(round_loop.thisN+1))
    # keep track of which components have finished
    resultsessionComponents = [text_wait_resultsession, text_round_resultsession, button_3, text_3]
    for thisComponent in resultsessionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    resultsessionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "resultsession"-------
    while continueRoutine:
        # get current time
        t = resultsessionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=resultsessionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if t>1:
            if mouse.isPressedIn(button_3,[0,]):
                break
        
        
        
        # *text_wait_resultsession* updates
        if text_wait_resultsession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_wait_resultsession.frameNStart = frameN  # exact frame index
            text_wait_resultsession.tStart = t  # local t and not account for scr refresh
            text_wait_resultsession.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_wait_resultsession, 'tStartRefresh')  # time at next scr refresh
            text_wait_resultsession.setAutoDraw(True)
        
        # *text_round_resultsession* updates
        if text_round_resultsession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_round_resultsession.frameNStart = frameN  # exact frame index
            text_round_resultsession.tStart = t  # local t and not account for scr refresh
            text_round_resultsession.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_round_resultsession, 'tStartRefresh')  # time at next scr refresh
            text_round_resultsession.setAutoDraw(True)
        
        # *button_3* updates
        if button_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_3.frameNStart = frameN  # exact frame index
            button_3.tStart = t  # local t and not account for scr refresh
            button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
            button_3.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in resultsessionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "resultsession"-------
    for thisComponent in resultsessionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    suerch_num=0
    # the Routine "resultsession" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'round_loop'


# ------Prepare to start Routine "thanks"-------
# update component parameters for each repeat

lot_1=int(len(Result))-1
lot_num_1=int(random.choice(lot_1,1,replace=False))
Pay_off_1=round(Result[lot_num_1]*para1)
lot_num_1+=1

Pay_off=Pay_off_1

current_folder=pathlib.Path(__file__).parent
Payoff_file_name="Payoff_file.csv"
Payoff_file_path=current_folder/Payoff_file_name

Payoff_file=open(Payoff_file_path,mode='a')
Payoff_file.write('{},{}\n'.format(expInfo['participant'],int(Pay_off+Fixed_fee)))
Payoff_file.close()



Result_filename =_thisDir + os.sep + u'%s_%s' %(expName, expInfo['participant'])
thisExp.saveAsWideText(Result_filename+'.csv',matrixOnly=False,appendFile=True)

text_thanks.setText('ありがとうございました。'+ u'\n コンピュータによって{}回目のラウンドが選ばれました。'.format(lot_num_1)+u'\n このラウンドであなたが獲得したポイント{}でした。'.format(Pay_off_1//para1)+u'\n よって{}がこのパートでのあなたの報酬になります。'.format(int(Pay_off+Fixed_fee)))
# keep track of which components have finished
thanksComponents = [text_thanks]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "thanks"-------
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_thanks* updates
    if text_thanks.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_thanks.frameNStart = frameN  # exact frame index
        text_thanks.tStart = t  # local t and not account for scr refresh
        text_thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_thanks, 'tStartRefresh')  # time at next scr refresh
        text_thanks.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
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
