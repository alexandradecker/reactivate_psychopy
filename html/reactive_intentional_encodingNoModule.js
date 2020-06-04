/************************************** 
 * Reactive_Intentional_Encoding Test *
 **************************************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.992, 0.992, 0.992]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'reactive_intentional_encoding';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'sex': '001', 'age': '', '': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin);
flowScheduler.add(instructionsRoutineEachFrame);
flowScheduler.add(instructionsRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(instruction2RoutineBegin);
flowScheduler.add(instruction2RoutineEachFrame);
flowScheduler.add(instruction2RoutineEnd);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var instructionsClock;
var Instruction_text;
var instruction_key_response;
var trialClock;
var a_image;
var b_image;
var instruction2Clock;
var text;
var key_resp_instruction2_0;
var testClock;
var instruct_text;
var a_image_retrieve;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  Instruction_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instruction_text',
    text: "Remember the image pairs\n\nPress 'space' to continue",
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  instruction_key_response = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  a_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'a_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.3), 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  b_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'b_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.3, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "instruction2"
  instruction2Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Great job.\n\nNow your memory will be tested on what you learned\n\nPress space to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_instruction2_0 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "test"
  testClock = new util.Clock();
  instruct_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text',
    text: 'Retrieve the associate',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.2], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  a_image_retrieve = new visual.ImageStim({
    win : psychoJS.window,
    name : 'a_image_retrieve', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.5), 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var instructionsComponents;
function instructionsRoutineBegin() {
  //------Prepare to start Routine 'instructions'-------
  t = 0;
  instructionsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instruction_key_response.keys = undefined;
  instruction_key_response.rt = undefined;
  // keep track of which components have finished
  instructionsComponents = [];
  instructionsComponents.push(Instruction_text);
  instructionsComponents.push(instruction_key_response);
  
  instructionsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instructionsRoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructionsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Instruction_text* updates
  if (t >= 0.0 && Instruction_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Instruction_text.tStart = t;  // (not accounting for frame time here)
    Instruction_text.frameNStart = frameN;  // exact frame index
    Instruction_text.setAutoDraw(true);
  }

  
  // *instruction_key_response* updates
  if (t >= 0.5 && instruction_key_response.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruction_key_response.tStart = t;  // (not accounting for frame time here)
    instruction_key_response.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instruction_key_response.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { instruction_key_response.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { instruction_key_response.clearEvents(); });
  }

  if (instruction_key_response.status === PsychoJS.Status.STARTED) {
    let theseKeys = instruction_key_response.getKeys({keyList: [], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  instructionsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEnd() {
  //------Ending Routine 'instructions'-------
  instructionsComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials;
var currentLoop;
var trialIterator;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'intentional_encoding.xlsx', '0:12'),
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial = result.value;
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var trials_2;
function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'test_encoding.xlsx', '0:12'),
    seed: undefined, name: 'trials_2'});
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_2[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_2 = result.value;
    thisScheduler.add(importConditions(trials_2));
    thisScheduler.add(testRoutineBegin);
    thisScheduler.add(testRoutineEachFrame);
    thisScheduler.add(testRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}

var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  b_image.setImage(image_b);
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(a_image);
  trialComponents.push(b_image);
  
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *a_image* updates
  if (t >= 1 && a_image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    a_image.tStart = t;  // (not accounting for frame time here)
    a_image.frameNStart = frameN;  // exact frame index
    a_image.setAutoDraw(true);
  }

  frameRemains = 1 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (a_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    a_image.setAutoDraw(false);
  }
  
  if (a_image.status === PsychoJS.Status.STARTED){ // only update if being drawn
    a_image.setImage(image_a);
  }
  
  // *b_image* updates
  if (t >= 1 && b_image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    b_image.tStart = t;  // (not accounting for frame time here)
    b_image.frameNStart = frameN;  // exact frame index
    b_image.setAutoDraw(true);
  }

  frameRemains = 1 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (b_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    b_image.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  trialComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var instruction2Components;
function instruction2RoutineBegin() {
  //------Prepare to start Routine 'instruction2'-------
  t = 0;
  instruction2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_instruction2_0.keys = undefined;
  key_resp_instruction2_0.rt = undefined;
  // keep track of which components have finished
  instruction2Components = [];
  instruction2Components.push(text);
  instruction2Components.push(key_resp_instruction2_0);
  
  instruction2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function instruction2RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruction2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruction2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  
  // *key_resp_instruction2_0* updates
  if (t >= 0.0 && key_resp_instruction2_0.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_instruction2_0.tStart = t;  // (not accounting for frame time here)
    key_resp_instruction2_0.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_instruction2_0.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_instruction2_0.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_instruction2_0.clearEvents(); });
  }

  if (key_resp_instruction2_0.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_instruction2_0.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_instruction2_0.keys = theseKeys[0].name;  // just the last key pressed
      key_resp_instruction2_0.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  instruction2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruction2RoutineEnd() {
  //------Ending Routine 'instruction2'-------
  instruction2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_instruction2_0.keys', key_resp_instruction2_0.keys);
  if (typeof key_resp_instruction2_0.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_instruction2_0.rt', key_resp_instruction2_0.rt);
      routineTimer.reset();
      }
  
  key_resp_instruction2_0.stop();
  // the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var testComponents;
function testRoutineBegin() {
  //------Prepare to start Routine 'test'-------
  t = 0;
  testClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  testComponents = [];
  testComponents.push(instruct_text);
  testComponents.push(a_image_retrieve);
  
  testComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function testRoutineEachFrame() {
  //------Loop for each frame of Routine 'test'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = testClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instruct_text* updates
  if (t >= 0.0 && instruct_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text.tStart = t;  // (not accounting for frame time here)
    instruct_text.frameNStart = frameN;  // exact frame index
    instruct_text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instruct_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instruct_text.setAutoDraw(false);
  }
  
  // *a_image_retrieve* updates
  if (t >= 0.0 && a_image_retrieve.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    a_image_retrieve.tStart = t;  // (not accounting for frame time here)
    a_image_retrieve.frameNStart = frameN;  // exact frame index
    a_image_retrieve.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (a_image_retrieve.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    a_image_retrieve.setAutoDraw(false);
  }
  
  if (a_image_retrieve.status === PsychoJS.Status.STARTED){ // only update if being drawn
    a_image_retrieve.setImage(image_a);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  testComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function testRoutineEnd() {
  //------Ending Routine 'test'-------
  testComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
