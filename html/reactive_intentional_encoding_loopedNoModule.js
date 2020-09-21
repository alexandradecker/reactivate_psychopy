/********************************************* 
 * Reactive_Intentional_Encoding_Looped Test *
 *********************************************/

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
let expName = 'reactive_intentional_encoding_looped';  // from the Builder filename that created this script
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
flowScheduler.add(expParamRoutineBegin);
flowScheduler.add(expParamRoutineEachFrame);
flowScheduler.add(expParamRoutineEnd);
const trials_24LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_24LoopBegin, trials_24LoopScheduler);
flowScheduler.add(trials_24LoopScheduler);
flowScheduler.add(trials_24LoopEnd);
flowScheduler.add(fixation_2RoutineBegin);
flowScheduler.add(fixation_2RoutineEachFrame);
flowScheduler.add(fixation_2RoutineEnd);
const practice_trials_intentional_encodingLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_trials_intentional_encodingLoopBegin, practice_trials_intentional_encodingLoopScheduler);
flowScheduler.add(practice_trials_intentional_encodingLoopScheduler);
flowScheduler.add(practice_trials_intentional_encodingLoopEnd);
flowScheduler.add(intructions_post_practice_intentional_encodingRoutineBegin);
flowScheduler.add(intructions_post_practice_intentional_encodingRoutineEachFrame);
flowScheduler.add(intructions_post_practice_intentional_encodingRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
const trials_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_4LoopBegin, trials_4LoopScheduler);
flowScheduler.add(trials_4LoopScheduler);
flowScheduler.add(trials_4LoopEnd);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
const trials_5LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_5LoopBegin, trials_5LoopScheduler);
flowScheduler.add(trials_5LoopScheduler);
flowScheduler.add(trials_5LoopEnd);
flowScheduler.add(post_retrievalpractice_instructionsRoutineBegin);
flowScheduler.add(post_retrievalpractice_instructionsRoutineEachFrame);
flowScheduler.add(post_retrievalpractice_instructionsRoutineEnd);
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin, trials_3LoopScheduler);
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(pre_intentional_encoding4RoutineBegin);
flowScheduler.add(pre_intentional_encoding4RoutineEachFrame);
flowScheduler.add(pre_intentional_encoding4RoutineEnd);
const trials_6LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_6LoopBegin, trials_6LoopScheduler);
flowScheduler.add(trials_6LoopScheduler);
flowScheduler.add(trials_6LoopEnd);
flowScheduler.add(instruct_retrieval4RoutineBegin);
flowScheduler.add(instruct_retrieval4RoutineEachFrame);
flowScheduler.add(instruct_retrieval4RoutineEnd);
const trials_7LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_7LoopBegin, trials_7LoopScheduler);
flowScheduler.add(trials_7LoopScheduler);
flowScheduler.add(trials_7LoopEnd);
flowScheduler.add(pre_intentional_encoding4RoutineBegin);
flowScheduler.add(pre_intentional_encoding4RoutineEachFrame);
flowScheduler.add(pre_intentional_encoding4RoutineEnd);
const trials_8LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_8LoopBegin, trials_8LoopScheduler);
flowScheduler.add(trials_8LoopScheduler);
flowScheduler.add(trials_8LoopEnd);
flowScheduler.add(instruct_retrieval4RoutineBegin);
flowScheduler.add(instruct_retrieval4RoutineEachFrame);
flowScheduler.add(instruct_retrieval4RoutineEnd);
const trials_9LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_9LoopBegin, trials_9LoopScheduler);
flowScheduler.add(trials_9LoopScheduler);
flowScheduler.add(trials_9LoopEnd);
flowScheduler.add(pre_intentional_encoding4RoutineBegin);
flowScheduler.add(pre_intentional_encoding4RoutineEachFrame);
flowScheduler.add(pre_intentional_encoding4RoutineEnd);
const trials_10LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_10LoopBegin, trials_10LoopScheduler);
flowScheduler.add(trials_10LoopScheduler);
flowScheduler.add(trials_10LoopEnd);
flowScheduler.add(instruct_retrieval4RoutineBegin);
flowScheduler.add(instruct_retrieval4RoutineEachFrame);
flowScheduler.add(instruct_retrieval4RoutineEnd);
const trials_11LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_11LoopBegin, trials_11LoopScheduler);
flowScheduler.add(trials_11LoopScheduler);
flowScheduler.add(trials_11LoopEnd);
flowScheduler.add(final_ab_retrieval_test_instructRoutineBegin);
flowScheduler.add(final_ab_retrieval_test_instructRoutineEachFrame);
flowScheduler.add(final_ab_retrieval_test_instructRoutineEnd);
const trials_12LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_12LoopBegin, trials_12LoopScheduler);
flowScheduler.add(trials_12LoopScheduler);
flowScheduler.add(trials_12LoopEnd);
const trials_13LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_13LoopBegin, trials_13LoopScheduler);
flowScheduler.add(trials_13LoopScheduler);
flowScheduler.add(trials_13LoopEnd);
const trials_15LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_15LoopBegin, trials_15LoopScheduler);
flowScheduler.add(trials_15LoopScheduler);
flowScheduler.add(trials_15LoopEnd);
flowScheduler.add(pre_instruct_sustainedAttentionRoutineBegin);
flowScheduler.add(pre_instruct_sustainedAttentionRoutineEachFrame);
flowScheduler.add(pre_instruct_sustainedAttentionRoutineEnd);
const trials_18LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_18LoopBegin, trials_18LoopScheduler);
flowScheduler.add(trials_18LoopScheduler);
flowScheduler.add(trials_18LoopEnd);
const trials_17LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_17LoopBegin, trials_17LoopScheduler);
flowScheduler.add(trials_17LoopScheduler);
flowScheduler.add(trials_17LoopEnd);
flowScheduler.add(fixation_2RoutineBegin);
flowScheduler.add(fixation_2RoutineEachFrame);
flowScheduler.add(fixation_2RoutineEnd);
const trials_19LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_19LoopBegin, trials_19LoopScheduler);
flowScheduler.add(trials_19LoopScheduler);
flowScheduler.add(trials_19LoopEnd);
const trials_20LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_20LoopBegin, trials_20LoopScheduler);
flowScheduler.add(trials_20LoopScheduler);
flowScheduler.add(trials_20LoopEnd);
flowScheduler.add(fixation_2RoutineBegin);
flowScheduler.add(fixation_2RoutineEachFrame);
flowScheduler.add(fixation_2RoutineEnd);
flowScheduler.add(pre_instruction_real_abc_final_memoryRoutineBegin);
flowScheduler.add(pre_instruction_real_abc_final_memoryRoutineEachFrame);
flowScheduler.add(pre_instruction_real_abc_final_memoryRoutineEnd);
const trials_21LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_21LoopBegin, trials_21LoopScheduler);
flowScheduler.add(trials_21LoopScheduler);
flowScheduler.add(trials_21LoopEnd);
const trials_22LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_22LoopBegin, trials_22LoopScheduler);
flowScheduler.add(trials_22LoopScheduler);
flowScheduler.add(trials_22LoopEnd);
const trials_23LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_23LoopBegin, trials_23LoopScheduler);
flowScheduler.add(trials_23LoopScheduler);
flowScheduler.add(trials_23LoopEnd);
flowScheduler.add(endRoutineBegin);
flowScheduler.add(endRoutineEachFrame);
flowScheduler.add(endRoutineEnd);
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

var expParamClock;
var instructions_firstClock;
var text_34;
var instructions_text2_2;
var response_2;
var image1_2;
var image2_2;
var fixation_2Clock;
var text_31;
var real_intentional_encodingClock;
var image_pair1;
var image_pair2;
var intructions_post_practice_intentional_encodingClock;
var text_9;
var key_resp_3;
var intentional_encoding_4Clock;
var image_pair1_2;
var image_pair2_2;
var instructions_retreival_testing1Clock;
var text_3;
var text_4;
var image_3;
var key_resp;
var instructions_retreival_testingClock;
var text_5;
var text_8;
var key_resp_2;
var image;
var image_2;
var image_5;
var image_6;
var K;
var L;
var J;
var practice_retrieval_after_encodingClock;
var image_a_practice;
var afc_test_practice;
var location1_practice;
var location2_practice;
var location3_practice;
var j_key_test_practice;
var K_key_practice;
var L_key_practice;
var image_11;
var image_12;
var text_7;
var text_17;
var key_resp_13;
var post_retrievalpractice_instructionsClock;
var post_retreival_practice_intructions;
var key_resp_4;
var think_image_pairClock;
var instruct_text_3;
var a_image_retrieve_3;
var retrieval4Clock;
var afc_text_2;
var image_13;
var image_14;
var image_15;
var j_key_test_2;
var L_key_test_2;
var K_key_test_2;
var correct_image__a;
var correct_image2_2;
var Feedback_2;
var retrieval_test_resp;
var pre_intentional_encoding4Clock;
var text_12;
var key_resp_6;
var instruct_retrieval4Clock;
var text_13;
var key_resp_7;
var final_ab_retrieval_test_instructClock;
var text_15;
var key_resp_8;
var instructions_intentional_encodingClock;
var text;
var instructions_text2;
var response;
var image1;
var image2;
var J_press_instructions;
var F_key_instruct;
var arrow;
var yes_press;
var no_press;
var small_dog_questionClock;
var text_22;
var practice_incidental_encodingClock;
var incidental_image1_;
var incidental_encoding_resp;
var text_18;
var text_19;
var text_20;
var text_21;
var incidental_image2_;
var sustained_attention_arrows_practiceClock;
var image_16;
var arrows_resp;
var F_press;
var J_press;
var left_press;
var right_press;
var pre_instruct_sustainedAttentionClock;
var text_2;
var key_resp_14;
var incidental_encoding_realClock;
var image_A;
var image_c;
var key_resp_15;
var text_23;
var text_24;
var text_25;
var text_26;
var pre_instruct_final_memoryClock;
var text_14;
var pressspace;
var key_resp_16;
var image_17;
var Jkey;
var F_key;
var oldText;
var newtext;
var practice_abc_memory_testClock;
var imageabc;
var primed_memory_resp;
var Jkey_2;
var F_key_2;
var old;
var newtext_2;
var pre_instruction_real_abc_final_memoryClock;
var text_27;
var key_resp_18;
var questionairreClock;
var questioniarre;
var questionairre_resp;
var text_29;
var image_18;
var image_19;
var image_20;
var image_21;
var A_txt1;
var B_text;
var a_text2;
var C_text;
var questionairre2Clock;
var text_30;
var text_32;
var text_33;
var questionairre_resp2;
var endClock;
var text_28;
var exit;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "expParam"
  expParamClock = new util.Clock();
  // Initialize components for Routine "instructions_first"
  instructions_firstClock = new util.Clock();
  text_34 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_34',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instructions_text2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text2_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  response_2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  image2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "real_intentional_encoding"
  real_intentional_encodingClock = new util.Clock();
  image_pair1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.25), 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  image_pair2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "intructions_post_practice_intentional_encoding"
  intructions_post_practice_intentional_encodingClock = new util.Clock();
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'Great job! Now that you have had practice, you can start the real game. Remember to memorize that the two images go together. It is important you remember because your memory will be tested later. Press space to start the real thing!',
    font: 'helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "intentional_encoding_4"
  intentional_encoding_4Clock = new util.Clock();
  image_pair1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.25), 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  image_pair2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "instructions_retreival_testing1"
  instructions_retreival_testing1Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_retreival_testing"
  instructions_retreival_testingClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.52, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_6', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  K = new visual.TextStim({
    win: psychoJS.window,
    name: 'K',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  L = new visual.TextStim({
    win: psychoJS.window,
    name: 'L',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -8.0 
  });
  
  J = new visual.TextStim({
    win: psychoJS.window,
    name: 'J',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  // Initialize components for Routine "practice_retrieval_after_encoding"
  practice_retrieval_after_encodingClock = new util.Clock();
  image_a_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_a_practice', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  afc_test_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'afc_test_practice',
    text: 'Select the correct image',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.25], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  location1_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'location1_practice', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  location2_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'location2_practice', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  location3_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'location3_practice', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  j_key_test_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'j_key_test_practice',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  K_key_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'K_key_practice',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  L_key_practice = new visual.TextStim({
    win: psychoJS.window,
    name: 'L_key_practice',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -7.0 
  });
  
  image_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_11', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  image_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_12', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -9.0 
  });
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -10.0 
  });
  
  text_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_17',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -11.0 
  });
  
  key_resp_13 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "post_retrievalpractice_instructions"
  post_retrievalpractice_instructionsClock = new util.Clock();
  post_retreival_practice_intructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'post_retreival_practice_intructions',
    text: "Great job! Now that you've finished the practice, we'll start the real thing. When you're ready to start the real thing, press space!",
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "think_image_pair"
  think_image_pairClock = new util.Clock();
  instruct_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_3',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.2], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  a_image_retrieve_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'a_image_retrieve_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "retrieval4"
  retrieval4Clock = new util.Clock();
  afc_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'afc_text_2',
    text: 'Select the correct image',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0.25], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_14', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  image_15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_15', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  j_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'j_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  L_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'L_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0.4, (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  K_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'K_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  correct_image__a = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image__a', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  correct_image2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  Feedback_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Feedback_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.25], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  retrieval_test_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pre_intentional_encoding4"
  pre_intentional_encoding4Clock = new util.Clock();
  text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_12',
    text: 'Great job. Keep those image pairs in mind because you will be tested again at the end the experiment. For now, you will learn more image pairs. When you are ready, press the space bar.',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "intentional_encoding_4"
  intentional_encoding_4Clock = new util.Clock();
  image_pair1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.25), 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  image_pair2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "instruct_retrieval4"
  instruct_retrieval4Clock = new util.Clock();
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: ' When you are ready to start the memory test, press space bar. ',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "think_image_pair"
  think_image_pairClock = new util.Clock();
  instruct_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_3',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.2], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  a_image_retrieve_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'a_image_retrieve_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "retrieval4"
  retrieval4Clock = new util.Clock();
  afc_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'afc_text_2',
    text: 'Select the correct image',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0.25], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_14', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  image_15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_15', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  j_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'j_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  L_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'L_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0.4, (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  K_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'K_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  correct_image__a = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image__a', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  correct_image2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  Feedback_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Feedback_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.25], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  retrieval_test_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pre_intentional_encoding4"
  pre_intentional_encoding4Clock = new util.Clock();
  text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_12',
    text: 'Great job. Keep those image pairs in mind because you will be tested again at the end the experiment. For now, you will learn more image pairs. When you are ready, press the space bar.',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "intentional_encoding_4"
  intentional_encoding_4Clock = new util.Clock();
  image_pair1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.25), 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  image_pair2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "instruct_retrieval4"
  instruct_retrieval4Clock = new util.Clock();
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: ' When you are ready to start the memory test, press space bar. ',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "think_image_pair"
  think_image_pairClock = new util.Clock();
  instruct_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_3',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.2], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  a_image_retrieve_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'a_image_retrieve_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "retrieval4"
  retrieval4Clock = new util.Clock();
  afc_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'afc_text_2',
    text: 'Select the correct image',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0.25], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_14', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  image_15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_15', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  j_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'j_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  L_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'L_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0.4, (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  K_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'K_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  correct_image__a = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image__a', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  correct_image2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  Feedback_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Feedback_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.25], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  retrieval_test_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pre_intentional_encoding4"
  pre_intentional_encoding4Clock = new util.Clock();
  text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_12',
    text: 'Great job. Keep those image pairs in mind because you will be tested again at the end the experiment. For now, you will learn more image pairs. When you are ready, press the space bar.',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "intentional_encoding_4"
  intentional_encoding_4Clock = new util.Clock();
  image_pair1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair1_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.25), 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  image_pair2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_pair2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.25, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "instruct_retrieval4"
  instruct_retrieval4Clock = new util.Clock();
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: ' When you are ready to start the memory test, press space bar. ',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "think_image_pair"
  think_image_pairClock = new util.Clock();
  instruct_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_3',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.2], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  a_image_retrieve_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'a_image_retrieve_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "retrieval4"
  retrieval4Clock = new util.Clock();
  afc_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'afc_text_2',
    text: 'Select the correct image',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0.25], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_14', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  image_15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_15', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  j_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'j_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  L_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'L_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0.4, (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  K_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'K_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  correct_image__a = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image__a', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  correct_image2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  Feedback_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Feedback_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.25], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  retrieval_test_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "final_ab_retrieval_test_instruct"
  final_ab_retrieval_test_instructClock = new util.Clock();
  text_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_15',
    text: 'Now we will test your memory for ALL of the images that you have learned. You will be presented with the correct impair pair after you have made your response. Re-study this. Your memory will be tested later. When you are ready, press space bar to start.',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "think_image_pair"
  think_image_pairClock = new util.Clock();
  instruct_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_3',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.2], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  a_image_retrieve_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'a_image_retrieve_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "retrieval4"
  retrieval4Clock = new util.Clock();
  afc_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'afc_text_2',
    text: 'Select the correct image',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0.25], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  image_14 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_14', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  image_15 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_15', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  j_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'j_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  L_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'L_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0.4, (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  K_key_test_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'K_key_test_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0 
  });
  
  correct_image__a = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image__a', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  correct_image2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_image2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  Feedback_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Feedback_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.25], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -9.0 
  });
  
  retrieval_test_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_intentional_encoding"
  instructions_intentional_encodingClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instructions_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  response = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  image2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  J_press_instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'J_press_instructions',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  F_key_instruct = new visual.TextStim({
    win: psychoJS.window,
    name: 'F_key_instruct',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  arrow = new visual.ImageStim({
    win : psychoJS.window,
    name : 'arrow', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.09, 0.09],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  yes_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'yes_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -8.0 
  });
  
  no_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'no_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -9.0 
  });
  
  // Initialize components for Routine "small_dog_question"
  small_dog_questionClock = new util.Clock();
  text_22 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_22',
    text: 'default text',
    font: 'helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "practice_incidental_encoding"
  practice_incidental_encodingClock = new util.Clock();
  incidental_image1_ = new visual.ImageStim({
    win : psychoJS.window,
    name : 'incidental_image1_', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.2), 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  incidental_encoding_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_18 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_18',
    text: 'F',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.27)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  text_19 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_19',
    text: 'J',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.27)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  text_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_20',
    text: 'Yes',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.32)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  text_21 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_21',
    text: 'No',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.32)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  incidental_image2_ = new visual.ImageStim({
    win : psychoJS.window,
    name : 'incidental_image2_', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.2, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  // Initialize components for Routine "sustained_attention_arrows_practice"
  sustained_attention_arrows_practiceClock = new util.Clock();
  image_16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_16', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.09, 0.09],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  arrows_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  F_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'F_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.3), (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  J_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'J_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.3, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  left_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'left_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.3), (- 0.35)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  right_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'right_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.3, (- 0.35)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "pre_instruct_sustainedAttention"
  pre_instruct_sustainedAttentionClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'You are now finished with the practice. When you are ready to start the real thing, press space. ',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_14 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "sustained_attention_arrows_practice"
  sustained_attention_arrows_practiceClock = new util.Clock();
  image_16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_16', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.09, 0.09],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  arrows_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  F_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'F_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.3), (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  J_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'J_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.3, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  left_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'left_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.3), (- 0.35)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  right_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'right_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.3, (- 0.35)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "small_dog_question"
  small_dog_questionClock = new util.Clock();
  text_22 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_22',
    text: 'default text',
    font: 'helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "incidental_encoding_real"
  incidental_encoding_realClock = new util.Clock();
  image_A = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_A', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.2), 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  image_c = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_c', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.2, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  key_resp_15 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_23 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_23',
    text: 'F',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.27)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  text_24 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_24',
    text: 'J',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.27)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  text_25 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_25',
    text: 'Yes',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.32)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  text_26 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_26',
    text: 'No',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.32)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "sustained_attention_arrows_practice"
  sustained_attention_arrows_practiceClock = new util.Clock();
  image_16 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_16', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.09, 0.09],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  arrows_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  F_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'F_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.3), (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  J_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'J_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.3, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  left_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'left_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.3), (- 0.35)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  right_press = new visual.TextStim({
    win: psychoJS.window,
    name: 'right_press',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.3, (- 0.35)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "pre_instruct_final_memory"
  pre_instruct_final_memoryClock = new util.Clock();
  text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_14',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.3], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  pressspace = new visual.TextStim({
    win: psychoJS.window,
    name: 'pressspace',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_16 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_17 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_17', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  Jkey = new visual.TextStim({
    win: psychoJS.window,
    name: 'Jkey',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.27)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  F_key = new visual.TextStim({
    win: psychoJS.window,
    name: 'F_key',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.27)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  oldText = new visual.TextStim({
    win: psychoJS.window,
    name: 'oldText',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.32)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -6.0 
  });
  
  newtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'newtext',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.32)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -7.0 
  });
  
  // Initialize components for Routine "practice_abc_memory_test"
  practice_abc_memory_testClock = new util.Clock();
  imageabc = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageabc', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  primed_memory_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Jkey_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Jkey_2',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.2)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  F_key_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'F_key_2',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.2)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  old = new visual.TextStim({
    win: psychoJS.window,
    name: 'old',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  newtext_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'newtext_2',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "pre_instruction_real_abc_final_memory"
  pre_instruction_real_abc_final_memoryClock = new util.Clock();
  text_27 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_27',
    text: 'Great job! You are now finished the practice. When you are ready to start the real thing, press space!',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_18 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_abc_memory_test"
  practice_abc_memory_testClock = new util.Clock();
  imageabc = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageabc', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  primed_memory_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Jkey_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Jkey_2',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.2)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  F_key_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'F_key_2',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.2)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  old = new visual.TextStim({
    win: psychoJS.window,
    name: 'old',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.2), (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  newtext_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'newtext_2',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.2, (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.2,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "questionairre"
  questionairreClock = new util.Clock();
  questioniarre = new visual.TextStim({
    win: psychoJS.window,
    name: 'questioniarre',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0.4], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  questionairre_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_29 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_29',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, (- 0.3)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  image_18 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_18', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.1), 0.13], size : [0.15, 0.15],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  image_19 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_19', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.1, 0.13], size : [0.15, 0.15],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  image_20 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_20', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [(- 0.1), (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  image_21 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_21', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0.1, (- 0.1)], size : [0.15, 0.15],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  A_txt1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'A_txt1',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.1), 0.25], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: -7.0 
  });
  
  B_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'B_text',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.1, 0.25], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: -8.0 
  });
  
  a_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'a_text2',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.1), 0], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: -9.0 
  });
  
  C_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'C_text',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.1, 0], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('blue'),  opacity: 1,
    depth: -10.0 
  });
  
  // Initialize components for Routine "questionairre2"
  questionairre2Clock = new util.Clock();
  text_30 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_30',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  text_32 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_32',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [(- 0.35), (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  text_33 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_33',
    text: 'default text',
    font: 'Helvetica',
    units : undefined, 
    pos: [0.35, (- 0.3)], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  questionairre_resp2 = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text_28 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_28',
    text: 'You are now finished the game. Congratulations. Press space to exit.',
    font: 'Helvetica',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  exit = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var expParamComponents;
function expParamRoutineBegin() {
  //------Prepare to start Routine 'expParam'-------
  t = 0;
  expParamClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  window.intentional_encoding_path = 'trialorder/' + String(expInfo['participant'] % 4) + '_intentional_encoding.csv';
  window.intentional_encoding_test_path = 'trialorder/' + String(expInfo['participant'] % 4) + '_intentional_encoding_test.csv';
  window.intentional_encoding_test_final_path = 'trialorder/' + String(expInfo['participant'] % 4) + '_intentional_encoding_test_final.csv';
  window.priming_recognition_path = 'trialorder/' + String(expInfo['participant'] % 4) + '_priming_recognition_test.csv';
  
  // keep track of which components have finished
  expParamComponents = [];
  
  expParamComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function expParamRoutineEachFrame() {
  //------Loop for each frame of Routine 'expParam'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = expParamClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  expParamComponents.forEach( function(thisComponent) {
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


function expParamRoutineEnd() {
  //------Ending Routine 'expParam'-------
  expParamComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "expParam" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials_24;
var currentLoop;
var trialIterator;
function trials_24LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_24 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialorder/instructions_first.csv',
    seed: undefined, name: 'trials_24'});
  psychoJS.experiment.addLoop(trials_24); // add the loop to the experiment
  currentLoop = trials_24;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_24[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_24 = result.value;
    thisScheduler.add(importConditions(trials_24));
    thisScheduler.add(instructions_firstRoutineBegin);
    thisScheduler.add(instructions_firstRoutineEachFrame);
    thisScheduler.add(instructions_firstRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_24LoopEnd() {
  psychoJS.experiment.removeLoop(trials_24);

  return Scheduler.Event.NEXT;
}

var practice_trials_intentional_encoding;
function practice_trials_intentional_encodingLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practice_trials_intentional_encoding = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialorder/test_practice.csv',
    seed: undefined, name: 'practice_trials_intentional_encoding'});
  psychoJS.experiment.addLoop(practice_trials_intentional_encoding); // add the loop to the experiment
  currentLoop = practice_trials_intentional_encoding;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = practice_trials_intentional_encoding[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisPractice_trials_intentional_encoding = result.value;
    thisScheduler.add(importConditions(practice_trials_intentional_encoding));
    thisScheduler.add(real_intentional_encodingRoutineBegin);
    thisScheduler.add(real_intentional_encodingRoutineEachFrame);
    thisScheduler.add(real_intentional_encodingRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function practice_trials_intentional_encodingLoopEnd() {
  psychoJS.experiment.removeLoop(practice_trials_intentional_encoding);

  return Scheduler.Event.NEXT;
}

var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, intentional_encoding_path, '0:12'),
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
    thisScheduler.add(intentional_encoding_4RoutineBegin);
    thisScheduler.add(intentional_encoding_4RoutineEachFrame);
    thisScheduler.add(intentional_encoding_4RoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var trials_4;
function trials_4LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_4 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'trialorder/instructions.csv', '8:11'),
    seed: undefined, name: 'trials_4'});
  psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
  currentLoop = trials_4;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_4[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_4 = result.value;
    thisScheduler.add(importConditions(trials_4));
    thisScheduler.add(instructions_retreival_testing1RoutineBegin);
    thisScheduler.add(instructions_retreival_testing1RoutineEachFrame);
    thisScheduler.add(instructions_retreival_testing1RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_4LoopEnd() {
  psychoJS.experiment.removeLoop(trials_4);

  return Scheduler.Event.NEXT;
}

var trials_2;
function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'trialorder/instructions.csv', '11:16'),
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
    thisScheduler.add(instructions_retreival_testingRoutineBegin);
    thisScheduler.add(instructions_retreival_testingRoutineEachFrame);
    thisScheduler.add(instructions_retreival_testingRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}

var trials_5;
function trials_5LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_5 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'trialorder/test_practice.csv', '0:3'),
    seed: undefined, name: 'trials_5'});
  psychoJS.experiment.addLoop(trials_5); // add the loop to the experiment
  currentLoop = trials_5;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_5[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_5 = result.value;
    thisScheduler.add(importConditions(trials_5));
    thisScheduler.add(practice_retrieval_after_encodingRoutineBegin);
    thisScheduler.add(practice_retrieval_after_encodingRoutineEachFrame);
    thisScheduler.add(practice_retrieval_after_encodingRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_5LoopEnd() {
  psychoJS.experiment.removeLoop(trials_5);

  return Scheduler.Event.NEXT;
}

var trials_3;
function trials_3LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, intentional_encoding_test_path, '0:12'),
    seed: undefined, name: 'trials_3'});
  psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
  currentLoop = trials_3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_3[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_3 = result.value;
    thisScheduler.add(importConditions(trials_3));
    thisScheduler.add(think_image_pairRoutineBegin);
    thisScheduler.add(think_image_pairRoutineEachFrame);
    thisScheduler.add(think_image_pairRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(retrieval4RoutineBegin);
    thisScheduler.add(retrieval4RoutineEachFrame);
    thisScheduler.add(retrieval4RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}

var trials_6;
function trials_6LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_6 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, intentional_encoding_path, '12:24'),
    seed: undefined, name: 'trials_6'});
  psychoJS.experiment.addLoop(trials_6); // add the loop to the experiment
  currentLoop = trials_6;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_6[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_6 = result.value;
    thisScheduler.add(importConditions(trials_6));
    thisScheduler.add(intentional_encoding_4RoutineBegin);
    thisScheduler.add(intentional_encoding_4RoutineEachFrame);
    thisScheduler.add(intentional_encoding_4RoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_6LoopEnd() {
  psychoJS.experiment.removeLoop(trials_6);

  return Scheduler.Event.NEXT;
}

var trials_7;
function trials_7LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_7 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, intentional_encoding_test_path, '12:24'),
    seed: undefined, name: 'trials_7'});
  psychoJS.experiment.addLoop(trials_7); // add the loop to the experiment
  currentLoop = trials_7;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_7[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_7 = result.value;
    thisScheduler.add(importConditions(trials_7));
    thisScheduler.add(think_image_pairRoutineBegin);
    thisScheduler.add(think_image_pairRoutineEachFrame);
    thisScheduler.add(think_image_pairRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(retrieval4RoutineBegin);
    thisScheduler.add(retrieval4RoutineEachFrame);
    thisScheduler.add(retrieval4RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_7LoopEnd() {
  psychoJS.experiment.removeLoop(trials_7);

  return Scheduler.Event.NEXT;
}

var trials_8;
function trials_8LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_8 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, intentional_encoding_path, '24:36'),
    seed: undefined, name: 'trials_8'});
  psychoJS.experiment.addLoop(trials_8); // add the loop to the experiment
  currentLoop = trials_8;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_8[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_8 = result.value;
    thisScheduler.add(importConditions(trials_8));
    thisScheduler.add(intentional_encoding_4RoutineBegin);
    thisScheduler.add(intentional_encoding_4RoutineEachFrame);
    thisScheduler.add(intentional_encoding_4RoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_8LoopEnd() {
  psychoJS.experiment.removeLoop(trials_8);

  return Scheduler.Event.NEXT;
}

var trials_9;
function trials_9LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_9 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, intentional_encoding_test_path, '24:36'),
    seed: undefined, name: 'trials_9'});
  psychoJS.experiment.addLoop(trials_9); // add the loop to the experiment
  currentLoop = trials_9;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_9[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_9 = result.value;
    thisScheduler.add(importConditions(trials_9));
    thisScheduler.add(think_image_pairRoutineBegin);
    thisScheduler.add(think_image_pairRoutineEachFrame);
    thisScheduler.add(think_image_pairRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(retrieval4RoutineBegin);
    thisScheduler.add(retrieval4RoutineEachFrame);
    thisScheduler.add(retrieval4RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_9LoopEnd() {
  psychoJS.experiment.removeLoop(trials_9);

  return Scheduler.Event.NEXT;
}

var trials_10;
function trials_10LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_10 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, intentional_encoding_path, '36:48'),
    seed: undefined, name: 'trials_10'});
  psychoJS.experiment.addLoop(trials_10); // add the loop to the experiment
  currentLoop = trials_10;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_10[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_10 = result.value;
    thisScheduler.add(importConditions(trials_10));
    thisScheduler.add(intentional_encoding_4RoutineBegin);
    thisScheduler.add(intentional_encoding_4RoutineEachFrame);
    thisScheduler.add(intentional_encoding_4RoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_10LoopEnd() {
  psychoJS.experiment.removeLoop(trials_10);

  return Scheduler.Event.NEXT;
}

var trials_11;
function trials_11LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_11 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, intentional_encoding_test_path, '36:48'),
    seed: undefined, name: 'trials_11'});
  psychoJS.experiment.addLoop(trials_11); // add the loop to the experiment
  currentLoop = trials_11;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_11[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_11 = result.value;
    thisScheduler.add(importConditions(trials_11));
    thisScheduler.add(think_image_pairRoutineBegin);
    thisScheduler.add(think_image_pairRoutineEachFrame);
    thisScheduler.add(think_image_pairRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(retrieval4RoutineBegin);
    thisScheduler.add(retrieval4RoutineEachFrame);
    thisScheduler.add(retrieval4RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_11LoopEnd() {
  psychoJS.experiment.removeLoop(trials_11);

  return Scheduler.Event.NEXT;
}

var trials_12;
function trials_12LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_12 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: intentional_encoding_test_final_path,
    seed: undefined, name: 'trials_12'});
  psychoJS.experiment.addLoop(trials_12); // add the loop to the experiment
  currentLoop = trials_12;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_12[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_12 = result.value;
    thisScheduler.add(importConditions(trials_12));
    thisScheduler.add(think_image_pairRoutineBegin);
    thisScheduler.add(think_image_pairRoutineEachFrame);
    thisScheduler.add(think_image_pairRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(retrieval4RoutineBegin);
    thisScheduler.add(retrieval4RoutineEachFrame);
    thisScheduler.add(retrieval4RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_12LoopEnd() {
  psychoJS.experiment.removeLoop(trials_12);

  return Scheduler.Event.NEXT;
}

var trials_13;
function trials_13LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_13 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'trialorder/instructions.csv', '16:22'),
    seed: undefined, name: 'trials_13'});
  psychoJS.experiment.addLoop(trials_13); // add the loop to the experiment
  currentLoop = trials_13;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_13[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_13 = result.value;
    thisScheduler.add(importConditions(trials_13));
    thisScheduler.add(instructions_intentional_encodingRoutineBegin);
    thisScheduler.add(instructions_intentional_encodingRoutineEachFrame);
    thisScheduler.add(instructions_intentional_encodingRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_13LoopEnd() {
  psychoJS.experiment.removeLoop(trials_13);

  return Scheduler.Event.NEXT;
}

var trials_15;
function trials_15LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_15 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialorder/phase2_practice.xlsx',
    seed: undefined, name: 'trials_15'});
  psychoJS.experiment.addLoop(trials_15); // add the loop to the experiment
  currentLoop = trials_15;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_15[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_15 = result.value;
    thisScheduler.add(importConditions(trials_15));
    thisScheduler.add(small_dog_questionRoutineBegin);
    thisScheduler.add(small_dog_questionRoutineEachFrame);
    thisScheduler.add(small_dog_questionRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(practice_incidental_encodingRoutineBegin);
    thisScheduler.add(practice_incidental_encodingRoutineEachFrame);
    thisScheduler.add(practice_incidental_encodingRoutineEnd);
    const trials_14LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trials_14LoopBegin, trials_14LoopScheduler);
    thisScheduler.add(trials_14LoopScheduler);
    thisScheduler.add(trials_14LoopEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}

var trials_14;
function trials_14LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_14 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialorder/phase2_practice.xlsx',
    seed: undefined, name: 'trials_14'});
  psychoJS.experiment.addLoop(trials_14); // add the loop to the experiment
  currentLoop = trials_14;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_14[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_14 = result.value;
    thisScheduler.add(importConditions(trials_14));
    thisScheduler.add(sustained_attention_arrows_practiceRoutineBegin);
    thisScheduler.add(sustained_attention_arrows_practiceRoutineEachFrame);
    thisScheduler.add(sustained_attention_arrows_practiceRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_14LoopEnd() {
  psychoJS.experiment.removeLoop(trials_14);

  return Scheduler.Event.NEXT;
}


function trials_15LoopEnd() {
  psychoJS.experiment.removeLoop(trials_15);

  return Scheduler.Event.NEXT;
}

var trials_18;
function trials_18LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_18 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialorder/phase2_practice.xlsx',
    seed: undefined, name: 'trials_18'});
  psychoJS.experiment.addLoop(trials_18); // add the loop to the experiment
  currentLoop = trials_18;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_18[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_18 = result.value;
    thisScheduler.add(importConditions(trials_18));
    thisScheduler.add(sustained_attention_arrows_practiceRoutineBegin);
    thisScheduler.add(sustained_attention_arrows_practiceRoutineEachFrame);
    thisScheduler.add(sustained_attention_arrows_practiceRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_18LoopEnd() {
  psychoJS.experiment.removeLoop(trials_18);

  return Scheduler.Event.NEXT;
}

var trials_17;
function trials_17LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_17 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: intentional_encoding_test_path,
    seed: undefined, name: 'trials_17'});
  psychoJS.experiment.addLoop(trials_17); // add the loop to the experiment
  currentLoop = trials_17;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_17[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_17 = result.value;
    thisScheduler.add(importConditions(trials_17));
    thisScheduler.add(small_dog_questionRoutineBegin);
    thisScheduler.add(small_dog_questionRoutineEachFrame);
    thisScheduler.add(small_dog_questionRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(incidental_encoding_realRoutineBegin);
    thisScheduler.add(incidental_encoding_realRoutineEachFrame);
    thisScheduler.add(incidental_encoding_realRoutineEnd);
    const trials_16LoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trials_16LoopBegin, trials_16LoopScheduler);
    thisScheduler.add(trials_16LoopScheduler);
    thisScheduler.add(trials_16LoopEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}

var trials_16;
function trials_16LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_16 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialorder/phase2_practice.xlsx',
    seed: undefined, name: 'trials_16'});
  psychoJS.experiment.addLoop(trials_16); // add the loop to the experiment
  currentLoop = trials_16;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_16[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_16 = result.value;
    thisScheduler.add(importConditions(trials_16));
    thisScheduler.add(sustained_attention_arrows_practiceRoutineBegin);
    thisScheduler.add(sustained_attention_arrows_practiceRoutineEachFrame);
    thisScheduler.add(sustained_attention_arrows_practiceRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_16LoopEnd() {
  psychoJS.experiment.removeLoop(trials_16);

  return Scheduler.Event.NEXT;
}


function trials_17LoopEnd() {
  psychoJS.experiment.removeLoop(trials_17);

  return Scheduler.Event.NEXT;
}

var trials_19;
function trials_19LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_19 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'trialorder/instructions.csv', '22:26'),
    seed: undefined, name: 'trials_19'});
  psychoJS.experiment.addLoop(trials_19); // add the loop to the experiment
  currentLoop = trials_19;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_19[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_19 = result.value;
    thisScheduler.add(importConditions(trials_19));
    thisScheduler.add(pre_instruct_final_memoryRoutineBegin);
    thisScheduler.add(pre_instruct_final_memoryRoutineEachFrame);
    thisScheduler.add(pre_instruct_final_memoryRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_19LoopEnd() {
  psychoJS.experiment.removeLoop(trials_19);

  return Scheduler.Event.NEXT;
}

var trials_20;
function trials_20LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_20 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialorder/final_acb_memory_test_practice.xlsx',
    seed: undefined, name: 'trials_20'});
  psychoJS.experiment.addLoop(trials_20); // add the loop to the experiment
  currentLoop = trials_20;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_20[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_20 = result.value;
    thisScheduler.add(importConditions(trials_20));
    thisScheduler.add(practice_abc_memory_testRoutineBegin);
    thisScheduler.add(practice_abc_memory_testRoutineEachFrame);
    thisScheduler.add(practice_abc_memory_testRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trials_20LoopEnd() {
  psychoJS.experiment.removeLoop(trials_20);

  return Scheduler.Event.NEXT;
}

var trials_21;
function trials_21LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_21 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: priming_recognition_path,
    seed: undefined, name: 'trials_21'});
  psychoJS.experiment.addLoop(trials_21); // add the loop to the experiment
  currentLoop = trials_21;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_21[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_21 = result.value;
    thisScheduler.add(importConditions(trials_21));
    thisScheduler.add(practice_abc_memory_testRoutineBegin);
    thisScheduler.add(practice_abc_memory_testRoutineEachFrame);
    thisScheduler.add(practice_abc_memory_testRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_21LoopEnd() {
  psychoJS.experiment.removeLoop(trials_21);

  return Scheduler.Event.NEXT;
}

var trials_22;
function trials_22LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_22 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'trialorder/instructions.csv', '26:30'),
    seed: undefined, name: 'trials_22'});
  psychoJS.experiment.addLoop(trials_22); // add the loop to the experiment
  currentLoop = trials_22;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_22[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_22 = result.value;
    thisScheduler.add(importConditions(trials_22));
    thisScheduler.add(questionairreRoutineBegin);
    thisScheduler.add(questionairreRoutineEachFrame);
    thisScheduler.add(questionairreRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_22LoopEnd() {
  psychoJS.experiment.removeLoop(trials_22);

  return Scheduler.Event.NEXT;
}

var trials_23;
function trials_23LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_23 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'trialorder/questionairre2.csv',
    seed: undefined, name: 'trials_23'});
  psychoJS.experiment.addLoop(trials_23); // add the loop to the experiment
  currentLoop = trials_23;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = trials_23[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisTrial_23 = result.value;
    thisScheduler.add(importConditions(trials_23));
    thisScheduler.add(questionairre2RoutineBegin);
    thisScheduler.add(questionairre2RoutineEachFrame);
    thisScheduler.add(questionairre2RoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trials_23LoopEnd() {
  psychoJS.experiment.removeLoop(trials_23);

  return Scheduler.Event.NEXT;
}

var instructions_firstComponents;
function instructions_firstRoutineBegin() {
  //------Prepare to start Routine 'instructions_first'-------
  t = 0;
  instructions_firstClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_34.setColor(new util.Color('black'));
  text_34.setPos([position_1x, position_1y]);
  text_34.setText(instructions1);
  text_34.setFont('Helvetica');
  text_34.setHeight(0.03);
  instructions_text2_2.setColor(new util.Color('black'));
  instructions_text2_2.setPos([position_2x, position_2y]);
  instructions_text2_2.setText(Instructions2);
  instructions_text2_2.setFont('Helvetica');
  instructions_text2_2.setHeight(0.03);
  response_2.keys = undefined;
  response_2.rt = undefined;
  image1_2.setPos([0.25, 0]);
  image1_2.setSize([0.3, 0.3]);
  image1_2.setImage(Image1);
  image2_2.setPos([(- 0.25), 0]);
  image2_2.setSize([0.3, 0.3]);
  image2_2.setImage(Image2);
  // keep track of which components have finished
  instructions_firstComponents = [];
  instructions_firstComponents.push(text_34);
  instructions_firstComponents.push(instructions_text2_2);
  instructions_firstComponents.push(response_2);
  instructions_firstComponents.push(image1_2);
  instructions_firstComponents.push(image2_2);
  
  instructions_firstComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function instructions_firstRoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions_first'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructions_firstClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_34* updates
  if (t >= 0.05 && text_34.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_34.tStart = t;  // (not accounting for frame time here)
    text_34.frameNStart = frameN;  // exact frame index
    text_34.setAutoDraw(true);
  }

  
  // *instructions_text2_2* updates
  if (t >= 0.05 && instructions_text2_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructions_text2_2.tStart = t;  // (not accounting for frame time here)
    instructions_text2_2.frameNStart = frameN;  // exact frame index
    instructions_text2_2.setAutoDraw(true);
  }

  
  // *response_2* updates
  if (t >= 0.05 && response_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    response_2.tStart = t;  // (not accounting for frame time here)
    response_2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { response_2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { response_2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { response_2.clearEvents(); });
  }

  if (response_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = response_2.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (response_2.keys === undefined) {  // then this was the first keypress
        response_2.keys = theseKeys[0].name;  // just the first key pressed
        response_2.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // *image1_2* updates
  if (t >= 0.05 && image1_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image1_2.tStart = t;  // (not accounting for frame time here)
    image1_2.frameNStart = frameN;  // exact frame index
    image1_2.setAutoDraw(true);
  }

  
  // *image2_2* updates
  if (t >= 0.05 && image2_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image2_2.tStart = t;  // (not accounting for frame time here)
    image2_2.frameNStart = frameN;  // exact frame index
    image2_2.setAutoDraw(true);
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
  instructions_firstComponents.forEach( function(thisComponent) {
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


function instructions_firstRoutineEnd() {
  //------Ending Routine 'instructions_first'-------
  instructions_firstComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('response_2.keys', response_2.keys);
  if (typeof response_2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('response_2.rt', response_2.rt);
      routineTimer.reset();
      }
  
  response_2.stop();
  // the Routine "instructions_first" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var fixation_2Components;
function fixation_2RoutineBegin() {
  //------Prepare to start Routine 'fixation_2'-------
  t = 0;
  fixation_2Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(0.500000);
  // update component parameters for each repeat
  text_31.setText(' ');
  // keep track of which components have finished
  fixation_2Components = [];
  fixation_2Components.push(text_31);
  
  fixation_2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function fixation_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'fixation_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = fixation_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_31* updates
  if (t >= 0.0 && text_31.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_31.tStart = t;  // (not accounting for frame time here)
    text_31.frameNStart = frameN;  // exact frame index
    text_31.setAutoDraw(true);
  }

  frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_31.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_31.setAutoDraw(false);
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
  fixation_2Components.forEach( function(thisComponent) {
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


function fixation_2RoutineEnd() {
  //------Ending Routine 'fixation_2'-------
  fixation_2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var real_intentional_encodingComponents;
function real_intentional_encodingRoutineBegin() {
  //------Prepare to start Routine 'real_intentional_encoding'-------
  t = 0;
  real_intentional_encodingClock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.500000);
  // update component parameters for each repeat
  image_pair1.setImage(image_a);
  image_pair2.setImage(correct_image);
  // keep track of which components have finished
  real_intentional_encodingComponents = [];
  real_intentional_encodingComponents.push(image_pair1);
  real_intentional_encodingComponents.push(image_pair2);
  
  real_intentional_encodingComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function real_intentional_encodingRoutineEachFrame() {
  //------Loop for each frame of Routine 'real_intentional_encoding'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = real_intentional_encodingClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *image_pair1* updates
  if (t >= 0 && image_pair1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_pair1.tStart = t;  // (not accounting for frame time here)
    image_pair1.frameNStart = frameN;  // exact frame index
    image_pair1.setAutoDraw(true);
  }

  frameRemains = 0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_pair1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_pair1.setAutoDraw(false);
  }
  
  // *image_pair2* updates
  if (t >= 0 && image_pair2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_pair2.tStart = t;  // (not accounting for frame time here)
    image_pair2.frameNStart = frameN;  // exact frame index
    image_pair2.setAutoDraw(true);
  }

  frameRemains = 0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_pair2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_pair2.setAutoDraw(false);
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
  real_intentional_encodingComponents.forEach( function(thisComponent) {
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


function real_intentional_encodingRoutineEnd() {
  //------Ending Routine 'real_intentional_encoding'-------
  real_intentional_encodingComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var intructions_post_practice_intentional_encodingComponents;
function intructions_post_practice_intentional_encodingRoutineBegin() {
  //------Prepare to start Routine 'intructions_post_practice_intentional_encoding'-------
  t = 0;
  intructions_post_practice_intentional_encodingClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_3.keys = undefined;
  key_resp_3.rt = undefined;
  // keep track of which components have finished
  intructions_post_practice_intentional_encodingComponents = [];
  intructions_post_practice_intentional_encodingComponents.push(text_9);
  intructions_post_practice_intentional_encodingComponents.push(key_resp_3);
  
  intructions_post_practice_intentional_encodingComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function intructions_post_practice_intentional_encodingRoutineEachFrame() {
  //------Loop for each frame of Routine 'intructions_post_practice_intentional_encoding'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = intructions_post_practice_intentional_encodingClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_9* updates
  if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_9.tStart = t;  // (not accounting for frame time here)
    text_9.frameNStart = frameN;  // exact frame index
    text_9.setAutoDraw(true);
  }

  
  // *key_resp_3* updates
  if (t >= 0.5 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_3.tStart = t;  // (not accounting for frame time here)
    key_resp_3.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
  }

  if (key_resp_3.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_3.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_3.keys = theseKeys[0].name;  // just the last key pressed
      key_resp_3.rt = theseKeys[0].rt;
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
  intructions_post_practice_intentional_encodingComponents.forEach( function(thisComponent) {
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


function intructions_post_practice_intentional_encodingRoutineEnd() {
  //------Ending Routine 'intructions_post_practice_intentional_encoding'-------
  intructions_post_practice_intentional_encodingComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
  if (typeof key_resp_3.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
      routineTimer.reset();
      }
  
  key_resp_3.stop();
  // the Routine "intructions_post_practice_intentional_encoding" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var intentional_encoding_4Components;
function intentional_encoding_4RoutineBegin() {
  //------Prepare to start Routine 'intentional_encoding_4'-------
  t = 0;
  intentional_encoding_4Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.500000);
  // update component parameters for each repeat
  image_pair1_2.setImage(ImageA);
  image_pair2_2.setImage(ImageB);
  // keep track of which components have finished
  intentional_encoding_4Components = [];
  intentional_encoding_4Components.push(image_pair1_2);
  intentional_encoding_4Components.push(image_pair2_2);
  
  intentional_encoding_4Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function intentional_encoding_4RoutineEachFrame() {
  //------Loop for each frame of Routine 'intentional_encoding_4'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = intentional_encoding_4Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *image_pair1_2* updates
  if (t >= 0 && image_pair1_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_pair1_2.tStart = t;  // (not accounting for frame time here)
    image_pair1_2.frameNStart = frameN;  // exact frame index
    image_pair1_2.setAutoDraw(true);
  }

  frameRemains = 0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_pair1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_pair1_2.setAutoDraw(false);
  }
  
  // *image_pair2_2* updates
  if (t >= 0 && image_pair2_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_pair2_2.tStart = t;  // (not accounting for frame time here)
    image_pair2_2.frameNStart = frameN;  // exact frame index
    image_pair2_2.setAutoDraw(true);
  }

  frameRemains = 0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_pair2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_pair2_2.setAutoDraw(false);
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
  intentional_encoding_4Components.forEach( function(thisComponent) {
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


function intentional_encoding_4RoutineEnd() {
  //------Ending Routine 'intentional_encoding_4'-------
  intentional_encoding_4Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var instructions_retreival_testing1Components;
function instructions_retreival_testing1RoutineBegin() {
  //------Prepare to start Routine 'instructions_retreival_testing1'-------
  t = 0;
  instructions_retreival_testing1Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_3.setColor(new util.Color('black'));
  text_3.setPos([position_1x, position_1y]);
  text_3.setText(instructions1);
  text_3.setFont('Helvetica');
  text_3.setHeight(0.03);
  text_4.setColor(new util.Color('black'));
  text_4.setPos([position_2x, position_2y]);
  text_4.setText(Instructions2);
  text_4.setFont('Helvetica');
  text_4.setHeight(0.03);
  image_3.setImage(Image1);
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  // keep track of which components have finished
  instructions_retreival_testing1Components = [];
  instructions_retreival_testing1Components.push(text_3);
  instructions_retreival_testing1Components.push(text_4);
  instructions_retreival_testing1Components.push(image_3);
  instructions_retreival_testing1Components.push(key_resp);
  
  instructions_retreival_testing1Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function instructions_retreival_testing1RoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions_retreival_testing1'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructions_retreival_testing1Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_3* updates
  if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_3.tStart = t;  // (not accounting for frame time here)
    text_3.frameNStart = frameN;  // exact frame index
    text_3.setAutoDraw(true);
  }

  
  // *text_4* updates
  if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_4.tStart = t;  // (not accounting for frame time here)
    text_4.frameNStart = frameN;  // exact frame index
    text_4.setAutoDraw(true);
  }

  
  // *image_3* updates
  if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_3.tStart = t;  // (not accounting for frame time here)
    image_3.frameNStart = frameN;  // exact frame index
    image_3.setAutoDraw(true);
  }

  
  // *key_resp* updates
  if (t >= 0.05 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp.keys === undefined) {  // then this was the first keypress
        key_resp.keys = theseKeys[0].name;  // just the first key pressed
        key_resp.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
  instructions_retreival_testing1Components.forEach( function(thisComponent) {
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


function instructions_retreival_testing1RoutineEnd() {
  //------Ending Routine 'instructions_retreival_testing1'-------
  instructions_retreival_testing1Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
  if (typeof key_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
      routineTimer.reset();
      }
  
  key_resp.stop();
  // the Routine "instructions_retreival_testing1" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instructions_retreival_testingComponents;
function instructions_retreival_testingRoutineBegin() {
  //------Prepare to start Routine 'instructions_retreival_testing'-------
  t = 0;
  instructions_retreival_testingClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_5.setColor(new util.Color('black'));
  text_5.setPos([position_1x, position_1y]);
  text_5.setText(instructions1);
  text_5.setFont('Helvetica');
  text_5.setHeight(0.03);
  text_8.setColor(new util.Color('black'));
  text_8.setPos([position_2x, position_2y]);
  text_8.setText(Instructions2);
  text_8.setFont('Helvetica');
  text_8.setHeight(0.03);
  key_resp_2.keys = undefined;
  key_resp_2.rt = undefined;
  image.setPos([0, 0]);
  image.setSize([0.3, 0.3]);
  image.setImage(Image1);
  image_2.setImage(Image2);
  image_5.setImage(Image3);
  image_6.setPos([(- 0.52), 0]);
  image_6.setSize([0.3, 0.3]);
  image_6.setImage(Image4);
  K.setColor(new util.Color('black'));
  K.setPos([0, (- 0.25)]);
  K.setText(K_key);
  K.setFont('Arial');
  K.setHeight(0.03);
  L.setColor(new util.Color('black'));
  L.setPos([0.5, (- 0.25)]);
  L.setText(L_key);
  L.setFont('Helvetica');
  L.setHeight(0.03);
  J.setColor(new util.Color('black'));
  J.setPos([(- 0.5), (- 0.25)]);
  J.setText(J_key);
  J.setFont('Helvetica');
  J.setHeight(0.03);
  // keep track of which components have finished
  instructions_retreival_testingComponents = [];
  instructions_retreival_testingComponents.push(text_5);
  instructions_retreival_testingComponents.push(text_8);
  instructions_retreival_testingComponents.push(key_resp_2);
  instructions_retreival_testingComponents.push(image);
  instructions_retreival_testingComponents.push(image_2);
  instructions_retreival_testingComponents.push(image_5);
  instructions_retreival_testingComponents.push(image_6);
  instructions_retreival_testingComponents.push(K);
  instructions_retreival_testingComponents.push(L);
  instructions_retreival_testingComponents.push(J);
  
  instructions_retreival_testingComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function instructions_retreival_testingRoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions_retreival_testing'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructions_retreival_testingClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_5* updates
  if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_5.tStart = t;  // (not accounting for frame time here)
    text_5.frameNStart = frameN;  // exact frame index
    text_5.setAutoDraw(true);
  }

  
  // *text_8* updates
  if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_8.tStart = t;  // (not accounting for frame time here)
    text_8.frameNStart = frameN;  // exact frame index
    text_8.setAutoDraw(true);
  }

  
  // *key_resp_2* updates
  if (t >= 0.3 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_2.tStart = t;  // (not accounting for frame time here)
    key_resp_2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
  }

  if (key_resp_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_2.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'l'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_2.keys === undefined) {  // then this was the first keypress
        key_resp_2.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_2.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // *image* updates
  if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image.tStart = t;  // (not accounting for frame time here)
    image.frameNStart = frameN;  // exact frame index
    image.setAutoDraw(true);
  }

  
  // *image_2* updates
  if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_2.tStart = t;  // (not accounting for frame time here)
    image_2.frameNStart = frameN;  // exact frame index
    image_2.setAutoDraw(true);
  }

  
  // *image_5* updates
  if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_5.tStart = t;  // (not accounting for frame time here)
    image_5.frameNStart = frameN;  // exact frame index
    image_5.setAutoDraw(true);
  }

  
  // *image_6* updates
  if (t >= 0.0 && image_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_6.tStart = t;  // (not accounting for frame time here)
    image_6.frameNStart = frameN;  // exact frame index
    image_6.setAutoDraw(true);
  }

  
  // *K* updates
  if (t >= 0.0 && K.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    K.tStart = t;  // (not accounting for frame time here)
    K.frameNStart = frameN;  // exact frame index
    K.setAutoDraw(true);
  }

  
  // *L* updates
  if (t >= 0.0 && L.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    L.tStart = t;  // (not accounting for frame time here)
    L.frameNStart = frameN;  // exact frame index
    L.setAutoDraw(true);
  }

  
  // *J* updates
  if (t >= 0.0 && J.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    J.tStart = t;  // (not accounting for frame time here)
    J.frameNStart = frameN;  // exact frame index
    J.setAutoDraw(true);
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
  instructions_retreival_testingComponents.forEach( function(thisComponent) {
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


function instructions_retreival_testingRoutineEnd() {
  //------Ending Routine 'instructions_retreival_testing'-------
  instructions_retreival_testingComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
  if (typeof key_resp_2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
      routineTimer.reset();
      }
  
  key_resp_2.stop();
  // the Routine "instructions_retreival_testing" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var practice_retrieval_after_encodingComponents;
function practice_retrieval_after_encodingRoutineBegin() {
  //------Prepare to start Routine 'practice_retrieval_after_encoding'-------
  t = 0;
  practice_retrieval_after_encodingClock.reset(); // clock
  frameN = -1;
  routineTimer.add(9.000000);
  // update component parameters for each repeat
  image_a_practice.setPos([0, 0]);
  image_a_practice.setSize([0.3, 0.3]);
  image_a_practice.setImage(image_a);
  location1_practice.setPos([(- 0.4), 0]);
  location1_practice.setSize([0.3, 0.3]);
  location1_practice.setImage(location1);
  location2_practice.setPos([0, 0]);
  location2_practice.setSize([0.3, 0.3]);
  location2_practice.setImage(location2);
  location3_practice.setPos([0.4, 0]);
  location3_practice.setSize([0.3, 0.3]);
  location3_practice.setImage(location3);
  j_key_test_practice.setColor(new util.Color('black'));
  j_key_test_practice.setPos([(- 0.4), (- 0.25)]);
  j_key_test_practice.setText('J');
  j_key_test_practice.setFont('helvetica');
  j_key_test_practice.setHeight(0.03);
  K_key_practice.setColor(new util.Color('black'));
  K_key_practice.setPos([0, (- 0.25)]);
  K_key_practice.setText('K');
  K_key_practice.setFont('Helvetica');
  K_key_practice.setHeight(0.04);
  L_key_practice.setColor(new util.Color('black'));
  L_key_practice.setPos([0.4, (- 0.25)]);
  L_key_practice.setText('L');
  L_key_practice.setFont('Helvetica');
  L_key_practice.setHeight(0.03);
  image_11.setPos([(- 0.2), 0]);
  image_11.setSize([0.3, 0.3]);
  image_11.setImage(image_a);
  image_12.setPos([0.2, 0]);
  image_12.setSize([0.3, 0.3]);
  image_12.setImage(correct_image);
  text_7.setColor(new util.Color('black'));
  text_7.setPos([0, 0.2]);
  text_7.setText('Think of the image pair');
  text_7.setFont('Helvetica');
  text_7.setHeight(0.03);
  text_17.setColor(new util.Color('black'));
  text_17.setPos([0, 0.3]);
  text_17.setText('Re-study the correct pairs');
  text_17.setFont('Helvetica');
  text_17.setHeight(0.03);
  key_resp_13.keys = undefined;
  key_resp_13.rt = undefined;
  // keep track of which components have finished
  practice_retrieval_after_encodingComponents = [];
  practice_retrieval_after_encodingComponents.push(image_a_practice);
  practice_retrieval_after_encodingComponents.push(afc_test_practice);
  practice_retrieval_after_encodingComponents.push(location1_practice);
  practice_retrieval_after_encodingComponents.push(location2_practice);
  practice_retrieval_after_encodingComponents.push(location3_practice);
  practice_retrieval_after_encodingComponents.push(j_key_test_practice);
  practice_retrieval_after_encodingComponents.push(K_key_practice);
  practice_retrieval_after_encodingComponents.push(L_key_practice);
  practice_retrieval_after_encodingComponents.push(image_11);
  practice_retrieval_after_encodingComponents.push(image_12);
  practice_retrieval_after_encodingComponents.push(text_7);
  practice_retrieval_after_encodingComponents.push(text_17);
  practice_retrieval_after_encodingComponents.push(key_resp_13);
  
  practice_retrieval_after_encodingComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function practice_retrieval_after_encodingRoutineEachFrame() {
  //------Loop for each frame of Routine 'practice_retrieval_after_encoding'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = practice_retrieval_after_encodingClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *image_a_practice* updates
  if (t >= 1 && image_a_practice.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_a_practice.tStart = t;  // (not accounting for frame time here)
    image_a_practice.frameNStart = frameN;  // exact frame index
    image_a_practice.setAutoDraw(true);
  }

  frameRemains = 1 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_a_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_a_practice.setAutoDraw(false);
  }
  
  // *afc_test_practice* updates
  if (t >= 3.5 && afc_test_practice.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    afc_test_practice.tStart = t;  // (not accounting for frame time here)
    afc_test_practice.frameNStart = frameN;  // exact frame index
    afc_test_practice.setAutoDraw(true);
  }

  frameRemains = 3.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (afc_test_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    afc_test_practice.setAutoDraw(false);
  }
  
  // *location1_practice* updates
  if (t >= 3.5 && location1_practice.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    location1_practice.tStart = t;  // (not accounting for frame time here)
    location1_practice.frameNStart = frameN;  // exact frame index
    location1_practice.setAutoDraw(true);
  }

  frameRemains = 3.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (location1_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    location1_practice.setAutoDraw(false);
  }
  
  // *location2_practice* updates
  if (t >= 3.5 && location2_practice.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    location2_practice.tStart = t;  // (not accounting for frame time here)
    location2_practice.frameNStart = frameN;  // exact frame index
    location2_practice.setAutoDraw(true);
  }

  frameRemains = 3.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (location2_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    location2_practice.setAutoDraw(false);
  }
  
  // *location3_practice* updates
  if (t >= 3.5 && location3_practice.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    location3_practice.tStart = t;  // (not accounting for frame time here)
    location3_practice.frameNStart = frameN;  // exact frame index
    location3_practice.setAutoDraw(true);
  }

  frameRemains = 3.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (location3_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    location3_practice.setAutoDraw(false);
  }
  
  // *j_key_test_practice* updates
  if (t >= 3.5 && j_key_test_practice.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    j_key_test_practice.tStart = t;  // (not accounting for frame time here)
    j_key_test_practice.frameNStart = frameN;  // exact frame index
    j_key_test_practice.setAutoDraw(true);
  }

  frameRemains = 3.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (j_key_test_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    j_key_test_practice.setAutoDraw(false);
  }
  
  // *K_key_practice* updates
  if (t >= 3.5 && K_key_practice.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    K_key_practice.tStart = t;  // (not accounting for frame time here)
    K_key_practice.frameNStart = frameN;  // exact frame index
    K_key_practice.setAutoDraw(true);
  }

  frameRemains = 3.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (K_key_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    K_key_practice.setAutoDraw(false);
  }
  
  // *L_key_practice* updates
  if (t >= 3.5 && L_key_practice.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    L_key_practice.tStart = t;  // (not accounting for frame time here)
    L_key_practice.frameNStart = frameN;  // exact frame index
    L_key_practice.setAutoDraw(true);
  }

  frameRemains = 3.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (L_key_practice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    L_key_practice.setAutoDraw(false);
  }
  
  // *image_11* updates
  if (t >= 6 && image_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_11.tStart = t;  // (not accounting for frame time here)
    image_11.frameNStart = frameN;  // exact frame index
    image_11.setAutoDraw(true);
  }

  frameRemains = 6 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_11.setAutoDraw(false);
  }
  
  // *image_12* updates
  if (t >= 6 && image_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_12.tStart = t;  // (not accounting for frame time here)
    image_12.frameNStart = frameN;  // exact frame index
    image_12.setAutoDraw(true);
  }

  frameRemains = 6 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_12.setAutoDraw(false);
  }
  
  // *text_7* updates
  if (t >= 1 && text_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_7.tStart = t;  // (not accounting for frame time here)
    text_7.frameNStart = frameN;  // exact frame index
    text_7.setAutoDraw(true);
  }

  frameRemains = 1 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_7.setAutoDraw(false);
  }
  
  // *text_17* updates
  if (t >= 6 && text_17.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_17.tStart = t;  // (not accounting for frame time here)
    text_17.frameNStart = frameN;  // exact frame index
    text_17.setAutoDraw(true);
  }

  frameRemains = 6 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_17.setAutoDraw(false);
  }
  
  // *key_resp_13* updates
  if (t >= 3.5 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_13.tStart = t;  // (not accounting for frame time here)
    key_resp_13.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
  }

  frameRemains = 3.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_resp_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_resp_13.status = PsychoJS.Status.FINISHED;
  }

  if (key_resp_13.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_13.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_13.keys === undefined) {  // then this was the first keypress
        key_resp_13.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_13.rt = theseKeys[0].rt;
      }
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
  practice_retrieval_after_encodingComponents.forEach( function(thisComponent) {
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


function practice_retrieval_after_encodingRoutineEnd() {
  //------Ending Routine 'practice_retrieval_after_encoding'-------
  practice_retrieval_after_encodingComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
  if (typeof key_resp_13.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
      }
  
  key_resp_13.stop();
  return Scheduler.Event.NEXT;
}

var post_retrievalpractice_instructionsComponents;
function post_retrievalpractice_instructionsRoutineBegin() {
  //------Prepare to start Routine 'post_retrievalpractice_instructions'-------
  t = 0;
  post_retrievalpractice_instructionsClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_4.keys = undefined;
  key_resp_4.rt = undefined;
  // keep track of which components have finished
  post_retrievalpractice_instructionsComponents = [];
  post_retrievalpractice_instructionsComponents.push(post_retreival_practice_intructions);
  post_retrievalpractice_instructionsComponents.push(key_resp_4);
  
  post_retrievalpractice_instructionsComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function post_retrievalpractice_instructionsRoutineEachFrame() {
  //------Loop for each frame of Routine 'post_retrievalpractice_instructions'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = post_retrievalpractice_instructionsClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *post_retreival_practice_intructions* updates
  if (t >= 0.0 && post_retreival_practice_intructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    post_retreival_practice_intructions.tStart = t;  // (not accounting for frame time here)
    post_retreival_practice_intructions.frameNStart = frameN;  // exact frame index
    post_retreival_practice_intructions.setAutoDraw(true);
  }

  
  // *key_resp_4* updates
  if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_4.tStart = t;  // (not accounting for frame time here)
    key_resp_4.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
  }

  if (key_resp_4.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_4.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_4.keys === undefined) {  // then this was the first keypress
        key_resp_4.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_4.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
  post_retrievalpractice_instructionsComponents.forEach( function(thisComponent) {
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


function post_retrievalpractice_instructionsRoutineEnd() {
  //------Ending Routine 'post_retrievalpractice_instructions'-------
  post_retrievalpractice_instructionsComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
  if (typeof key_resp_4.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
      routineTimer.reset();
      }
  
  key_resp_4.stop();
  // the Routine "post_retrievalpractice_instructions" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var think_image_pairComponents;
function think_image_pairRoutineBegin() {
  //------Prepare to start Routine 'think_image_pair'-------
  t = 0;
  think_image_pairClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.500000);
  // update component parameters for each repeat
  instruct_text_3.setText('Think of the image pair');
  a_image_retrieve_3.setImage(ImageA);
  // keep track of which components have finished
  think_image_pairComponents = [];
  think_image_pairComponents.push(instruct_text_3);
  think_image_pairComponents.push(a_image_retrieve_3);
  
  think_image_pairComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function think_image_pairRoutineEachFrame() {
  //------Loop for each frame of Routine 'think_image_pair'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = think_image_pairClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instruct_text_3* updates
  if (t >= 0.5 && instruct_text_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_3.tStart = t;  // (not accounting for frame time here)
    instruct_text_3.frameNStart = frameN;  // exact frame index
    instruct_text_3.setAutoDraw(true);
  }

  frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instruct_text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instruct_text_3.setAutoDraw(false);
  }
  
  // *a_image_retrieve_3* updates
  if (t >= 0.5 && a_image_retrieve_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    a_image_retrieve_3.tStart = t;  // (not accounting for frame time here)
    a_image_retrieve_3.frameNStart = frameN;  // exact frame index
    a_image_retrieve_3.setAutoDraw(true);
  }

  frameRemains = 0.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (a_image_retrieve_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    a_image_retrieve_3.setAutoDraw(false);
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
  think_image_pairComponents.forEach( function(thisComponent) {
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


function think_image_pairRoutineEnd() {
  //------Ending Routine 'think_image_pair'-------
  think_image_pairComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var retrieval4Components;
function retrieval4RoutineBegin() {
  //------Prepare to start Routine 'retrieval4'-------
  t = 0;
  retrieval4Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(4.500000);
  // update component parameters for each repeat
  image_13.setPos([(- 0.4), 0]);
  image_13.setImage(location1);
  image_14.setPos([0, 0]);
  image_14.setImage(location2);
  image_15.setPos([0.4, 0]);
  image_15.setImage(location3);
  j_key_test_2.setColor(new util.Color('black'));
  j_key_test_2.setPos([(- 0.4), (- 0.25)]);
  j_key_test_2.setFont('Helvetica');
  j_key_test_2.setHeight(0.03);
  L_key_test_2.setColor(new util.Color('black'));
  L_key_test_2.setText('L');
  L_key_test_2.setFont('Helvetica');
  K_key_test_2.setColor(new util.Color('black'));
  K_key_test_2.setPos([0, (- 0.25)]);
  K_key_test_2.setText('K');
  K_key_test_2.setFont('Helvetica');
  K_key_test_2.setHeight(0.03);
  correct_image__a.setPos([(- 0.2), 0]);
  correct_image__a.setSize([0.3, 0.3]);
  correct_image__a.setImage(ImageA);
  correct_image2_2.setPos([0.2, 0]);
  correct_image2_2.setSize([0.3, 0.3]);
  correct_image2_2.setImage(ImageB);
  Feedback_2.setColor(new util.Color('black'));
  Feedback_2.setText('Re-study the correct pairs');
  Feedback_2.setFont('Helvetica');
  Feedback_2.setHeight(0.03);
  retrieval_test_resp.keys = undefined;
  retrieval_test_resp.rt = undefined;
  // keep track of which components have finished
  retrieval4Components = [];
  retrieval4Components.push(afc_text_2);
  retrieval4Components.push(image_13);
  retrieval4Components.push(image_14);
  retrieval4Components.push(image_15);
  retrieval4Components.push(j_key_test_2);
  retrieval4Components.push(L_key_test_2);
  retrieval4Components.push(K_key_test_2);
  retrieval4Components.push(correct_image__a);
  retrieval4Components.push(correct_image2_2);
  retrieval4Components.push(Feedback_2);
  retrieval4Components.push(retrieval_test_resp);
  
  retrieval4Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function retrieval4RoutineEachFrame() {
  //------Loop for each frame of Routine 'retrieval4'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = retrieval4Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *afc_text_2* updates
  if (t >= 0 && afc_text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    afc_text_2.tStart = t;  // (not accounting for frame time here)
    afc_text_2.frameNStart = frameN;  // exact frame index
    afc_text_2.setAutoDraw(true);
  }

  frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (afc_text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    afc_text_2.setAutoDraw(false);
  }
  
  // *image_13* updates
  if (t >= 0 && image_13.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_13.tStart = t;  // (not accounting for frame time here)
    image_13.frameNStart = frameN;  // exact frame index
    image_13.setAutoDraw(true);
  }

  frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_13.setAutoDraw(false);
  }
  
  // *image_14* updates
  if (t >= 0 && image_14.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_14.tStart = t;  // (not accounting for frame time here)
    image_14.frameNStart = frameN;  // exact frame index
    image_14.setAutoDraw(true);
  }

  frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_14.setAutoDraw(false);
  }
  
  // *image_15* updates
  if (t >= 0 && image_15.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_15.tStart = t;  // (not accounting for frame time here)
    image_15.frameNStart = frameN;  // exact frame index
    image_15.setAutoDraw(true);
  }

  frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_15.setAutoDraw(false);
  }
  
  // *j_key_test_2* updates
  if (t >= 0 && j_key_test_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    j_key_test_2.tStart = t;  // (not accounting for frame time here)
    j_key_test_2.frameNStart = frameN;  // exact frame index
    j_key_test_2.setAutoDraw(true);
  }

  frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (j_key_test_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    j_key_test_2.setAutoDraw(false);
  }
  
  if (j_key_test_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
    j_key_test_2.setText('J');
  }
  
  // *L_key_test_2* updates
  if (t >= 0 && L_key_test_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    L_key_test_2.tStart = t;  // (not accounting for frame time here)
    L_key_test_2.frameNStart = frameN;  // exact frame index
    L_key_test_2.setAutoDraw(true);
  }

  frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (L_key_test_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    L_key_test_2.setAutoDraw(false);
  }
  
  // *K_key_test_2* updates
  if (t >= 0 && K_key_test_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    K_key_test_2.tStart = t;  // (not accounting for frame time here)
    K_key_test_2.frameNStart = frameN;  // exact frame index
    K_key_test_2.setAutoDraw(true);
  }

  frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (K_key_test_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    K_key_test_2.setAutoDraw(false);
  }
  
  // *correct_image__a* updates
  if (t >= 2.5 && correct_image__a.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    correct_image__a.tStart = t;  // (not accounting for frame time here)
    correct_image__a.frameNStart = frameN;  // exact frame index
    correct_image__a.setAutoDraw(true);
  }

  frameRemains = 2.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (correct_image__a.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    correct_image__a.setAutoDraw(false);
  }
  
  // *correct_image2_2* updates
  if (t >= 2.5 && correct_image2_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    correct_image2_2.tStart = t;  // (not accounting for frame time here)
    correct_image2_2.frameNStart = frameN;  // exact frame index
    correct_image2_2.setAutoDraw(true);
  }

  frameRemains = 2.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (correct_image2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    correct_image2_2.setAutoDraw(false);
  }
  
  // *Feedback_2* updates
  if (t >= 2.5 && Feedback_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Feedback_2.tStart = t;  // (not accounting for frame time here)
    Feedback_2.frameNStart = frameN;  // exact frame index
    Feedback_2.setAutoDraw(true);
  }

  frameRemains = 2.5 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Feedback_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Feedback_2.setAutoDraw(false);
  }
  
  // *retrieval_test_resp* updates
  if (t >= 0 && retrieval_test_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    retrieval_test_resp.tStart = t;  // (not accounting for frame time here)
    retrieval_test_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { retrieval_test_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { retrieval_test_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { retrieval_test_resp.clearEvents(); });
  }

  frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (retrieval_test_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    retrieval_test_resp.status = PsychoJS.Status.FINISHED;
  }

  if (retrieval_test_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = retrieval_test_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l', 'J', 'K', 'L'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (retrieval_test_resp.keys === undefined) {  // then this was the first keypress
        retrieval_test_resp.keys = theseKeys[0].name;  // just the first key pressed
        retrieval_test_resp.rt = theseKeys[0].rt;
      }
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
  retrieval4Components.forEach( function(thisComponent) {
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


function retrieval4RoutineEnd() {
  //------Ending Routine 'retrieval4'-------
  retrieval4Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('retrieval_test_resp.keys', retrieval_test_resp.keys);
  if (typeof retrieval_test_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('retrieval_test_resp.rt', retrieval_test_resp.rt);
      }
  
  retrieval_test_resp.stop();
  return Scheduler.Event.NEXT;
}

var pre_intentional_encoding4Components;
function pre_intentional_encoding4RoutineBegin() {
  //------Prepare to start Routine 'pre_intentional_encoding4'-------
  t = 0;
  pre_intentional_encoding4Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_6.keys = undefined;
  key_resp_6.rt = undefined;
  // keep track of which components have finished
  pre_intentional_encoding4Components = [];
  pre_intentional_encoding4Components.push(text_12);
  pre_intentional_encoding4Components.push(key_resp_6);
  
  pre_intentional_encoding4Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function pre_intentional_encoding4RoutineEachFrame() {
  //------Loop for each frame of Routine 'pre_intentional_encoding4'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = pre_intentional_encoding4Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_12* updates
  if (t >= 0.04 && text_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_12.tStart = t;  // (not accounting for frame time here)
    text_12.frameNStart = frameN;  // exact frame index
    text_12.setAutoDraw(true);
  }

  
  // *key_resp_6* updates
  if (t >= 0.25 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_6.tStart = t;  // (not accounting for frame time here)
    key_resp_6.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
  }

  if (key_resp_6.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_6.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_6.keys === undefined) {  // then this was the first keypress
        key_resp_6.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_6.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
  pre_intentional_encoding4Components.forEach( function(thisComponent) {
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


function pre_intentional_encoding4RoutineEnd() {
  //------Ending Routine 'pre_intentional_encoding4'-------
  pre_intentional_encoding4Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
  if (typeof key_resp_6.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
      routineTimer.reset();
      }
  
  key_resp_6.stop();
  // the Routine "pre_intentional_encoding4" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instruct_retrieval4Components;
function instruct_retrieval4RoutineBegin() {
  //------Prepare to start Routine 'instruct_retrieval4'-------
  t = 0;
  instruct_retrieval4Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_7.keys = undefined;
  key_resp_7.rt = undefined;
  // keep track of which components have finished
  instruct_retrieval4Components = [];
  instruct_retrieval4Components.push(text_13);
  instruct_retrieval4Components.push(key_resp_7);
  
  instruct_retrieval4Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function instruct_retrieval4RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_retrieval4'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_retrieval4Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_13* updates
  if (t >= 0.0 && text_13.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_13.tStart = t;  // (not accounting for frame time here)
    text_13.frameNStart = frameN;  // exact frame index
    text_13.setAutoDraw(true);
  }

  
  // *key_resp_7* updates
  if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_7.tStart = t;  // (not accounting for frame time here)
    key_resp_7.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
  }

  if (key_resp_7.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_7.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_7.keys === undefined) {  // then this was the first keypress
        key_resp_7.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_7.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
  instruct_retrieval4Components.forEach( function(thisComponent) {
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


function instruct_retrieval4RoutineEnd() {
  //------Ending Routine 'instruct_retrieval4'-------
  instruct_retrieval4Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
  if (typeof key_resp_7.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
      routineTimer.reset();
      }
  
  key_resp_7.stop();
  // the Routine "instruct_retrieval4" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var final_ab_retrieval_test_instructComponents;
function final_ab_retrieval_test_instructRoutineBegin() {
  //------Prepare to start Routine 'final_ab_retrieval_test_instruct'-------
  t = 0;
  final_ab_retrieval_test_instructClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_8.keys = undefined;
  key_resp_8.rt = undefined;
  // keep track of which components have finished
  final_ab_retrieval_test_instructComponents = [];
  final_ab_retrieval_test_instructComponents.push(text_15);
  final_ab_retrieval_test_instructComponents.push(key_resp_8);
  
  final_ab_retrieval_test_instructComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function final_ab_retrieval_test_instructRoutineEachFrame() {
  //------Loop for each frame of Routine 'final_ab_retrieval_test_instruct'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = final_ab_retrieval_test_instructClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_15* updates
  if (t >= 0.0 && text_15.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_15.tStart = t;  // (not accounting for frame time here)
    text_15.frameNStart = frameN;  // exact frame index
    text_15.setAutoDraw(true);
  }

  
  // *key_resp_8* updates
  if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_8.tStart = t;  // (not accounting for frame time here)
    key_resp_8.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
  }

  if (key_resp_8.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_8.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_8.keys === undefined) {  // then this was the first keypress
        key_resp_8.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_8.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
  final_ab_retrieval_test_instructComponents.forEach( function(thisComponent) {
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


function final_ab_retrieval_test_instructRoutineEnd() {
  //------Ending Routine 'final_ab_retrieval_test_instruct'-------
  final_ab_retrieval_test_instructComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
  if (typeof key_resp_8.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
      routineTimer.reset();
      }
  
  key_resp_8.stop();
  // the Routine "final_ab_retrieval_test_instruct" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instructions_intentional_encodingComponents;
function instructions_intentional_encodingRoutineBegin() {
  //------Prepare to start Routine 'instructions_intentional_encoding'-------
  t = 0;
  instructions_intentional_encodingClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text.setColor(new util.Color('black'));
  text.setPos([position_1x, position_1y]);
  text.setText(instructions1);
  text.setFont('Helvetica');
  text.setHeight(0.03);
  instructions_text2.setColor(new util.Color('black'));
  instructions_text2.setPos([position_2x, position_2y]);
  instructions_text2.setText(Instructions2);
  instructions_text2.setFont('Helvetica');
  instructions_text2.setHeight(0.03);
  response.keys = undefined;
  response.rt = undefined;
  J_press_instructions.setText(J_key);
  F_key_instruct.setPos([(- 0.2), (- 0.2)]);
  F_key_instruct.setText(K_key);
  arrow.setImage(Image3);
  yes_press.setPos([(- 0.2), (- 0.27)]);
  yes_press.setText(yes_text);
  no_press.setPos([0.2, (- 0.27)]);
  no_press.setText(no_text);
  // keep track of which components have finished
  instructions_intentional_encodingComponents = [];
  instructions_intentional_encodingComponents.push(text);
  instructions_intentional_encodingComponents.push(instructions_text2);
  instructions_intentional_encodingComponents.push(response);
  instructions_intentional_encodingComponents.push(image1);
  instructions_intentional_encodingComponents.push(image2);
  instructions_intentional_encodingComponents.push(J_press_instructions);
  instructions_intentional_encodingComponents.push(F_key_instruct);
  instructions_intentional_encodingComponents.push(arrow);
  instructions_intentional_encodingComponents.push(yes_press);
  instructions_intentional_encodingComponents.push(no_press);
  
  instructions_intentional_encodingComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function instructions_intentional_encodingRoutineEachFrame() {
  //------Loop for each frame of Routine 'instructions_intentional_encoding'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructions_intentional_encodingClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.05 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  
  // *instructions_text2* updates
  if (t >= 0.05 && instructions_text2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructions_text2.tStart = t;  // (not accounting for frame time here)
    instructions_text2.frameNStart = frameN;  // exact frame index
    instructions_text2.setAutoDraw(true);
  }

  
  // *response* updates
  if (t >= 0.05 && response.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    response.tStart = t;  // (not accounting for frame time here)
    response.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { response.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { response.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { response.clearEvents(); });
  }

  if (response.status === PsychoJS.Status.STARTED) {
    let theseKeys = response.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (response.keys === undefined) {  // then this was the first keypress
        response.keys = theseKeys[0].name;  // just the first key pressed
        response.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // *image1* updates
  if (t >= 0.05 && image1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image1.tStart = t;  // (not accounting for frame time here)
    image1.frameNStart = frameN;  // exact frame index
    image1.setAutoDraw(true);
  }

  
  if (image1.status === PsychoJS.Status.STARTED){ // only update if being drawn
    image1.setPos([0.25, 0]);
    image1.setSize([0.3, 0.3]);
    image1.setImage(Image1);
  }
  
  // *image2* updates
  if (t >= 0.05 && image2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image2.tStart = t;  // (not accounting for frame time here)
    image2.frameNStart = frameN;  // exact frame index
    image2.setAutoDraw(true);
  }

  
  if (image2.status === PsychoJS.Status.STARTED){ // only update if being drawn
    image2.setPos([(- 0.25), 0]);
    image2.setSize([0.3, 0.3]);
    image2.setImage(Image2);
  }
  
  // *J_press_instructions* updates
  if (t >= 0.0 && J_press_instructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    J_press_instructions.tStart = t;  // (not accounting for frame time here)
    J_press_instructions.frameNStart = frameN;  // exact frame index
    J_press_instructions.setAutoDraw(true);
  }

  
  // *F_key_instruct* updates
  if (t >= 0.0 && F_key_instruct.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    F_key_instruct.tStart = t;  // (not accounting for frame time here)
    F_key_instruct.frameNStart = frameN;  // exact frame index
    F_key_instruct.setAutoDraw(true);
  }

  
  // *arrow* updates
  if (t >= 0.0 && arrow.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    arrow.tStart = t;  // (not accounting for frame time here)
    arrow.frameNStart = frameN;  // exact frame index
    arrow.setAutoDraw(true);
  }

  
  // *yes_press* updates
  if (t >= 0.0 && yes_press.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    yes_press.tStart = t;  // (not accounting for frame time here)
    yes_press.frameNStart = frameN;  // exact frame index
    yes_press.setAutoDraw(true);
  }

  
  // *no_press* updates
  if (t >= 0.0 && no_press.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    no_press.tStart = t;  // (not accounting for frame time here)
    no_press.frameNStart = frameN;  // exact frame index
    no_press.setAutoDraw(true);
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
  instructions_intentional_encodingComponents.forEach( function(thisComponent) {
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


function instructions_intentional_encodingRoutineEnd() {
  //------Ending Routine 'instructions_intentional_encoding'-------
  instructions_intentional_encodingComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('response.keys', response.keys);
  if (typeof response.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('response.rt', response.rt);
      routineTimer.reset();
      }
  
  response.stop();
  // the Routine "instructions_intentional_encoding" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var small_dog_questionComponents;
function small_dog_questionRoutineBegin() {
  //------Prepare to start Routine 'small_dog_question'-------
  t = 0;
  small_dog_questionClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.500000);
  // update component parameters for each repeat
  text_22.setText('Do the following images, together, weigh more than a small dog?');
  // keep track of which components have finished
  small_dog_questionComponents = [];
  small_dog_questionComponents.push(text_22);
  
  small_dog_questionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function small_dog_questionRoutineEachFrame() {
  //------Loop for each frame of Routine 'small_dog_question'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = small_dog_questionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_22* updates
  if (t >= 0.0 && text_22.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_22.tStart = t;  // (not accounting for frame time here)
    text_22.frameNStart = frameN;  // exact frame index
    text_22.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_22.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_22.setAutoDraw(false);
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
  small_dog_questionComponents.forEach( function(thisComponent) {
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


function small_dog_questionRoutineEnd() {
  //------Ending Routine 'small_dog_question'-------
  small_dog_questionComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var practice_incidental_encodingComponents;
function practice_incidental_encodingRoutineBegin() {
  //------Prepare to start Routine 'practice_incidental_encoding'-------
  t = 0;
  practice_incidental_encodingClock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.500000);
  // update component parameters for each repeat
  incidental_image1_.setImage(incidental_image1);
  incidental_encoding_resp.keys = undefined;
  incidental_encoding_resp.rt = undefined;
  incidental_image2_.setImage(incidental_image2);
  // keep track of which components have finished
  practice_incidental_encodingComponents = [];
  practice_incidental_encodingComponents.push(incidental_image1_);
  practice_incidental_encodingComponents.push(incidental_encoding_resp);
  practice_incidental_encodingComponents.push(text_18);
  practice_incidental_encodingComponents.push(text_19);
  practice_incidental_encodingComponents.push(text_20);
  practice_incidental_encodingComponents.push(text_21);
  practice_incidental_encodingComponents.push(incidental_image2_);
  
  practice_incidental_encodingComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function practice_incidental_encodingRoutineEachFrame() {
  //------Loop for each frame of Routine 'practice_incidental_encoding'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = practice_incidental_encodingClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *incidental_image1_* updates
  if (t >= 0.0 && incidental_image1_.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    incidental_image1_.tStart = t;  // (not accounting for frame time here)
    incidental_image1_.frameNStart = frameN;  // exact frame index
    incidental_image1_.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (incidental_image1_.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    incidental_image1_.setAutoDraw(false);
  }
  
  // *incidental_encoding_resp* updates
  if (t >= 0.0 && incidental_encoding_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    incidental_encoding_resp.tStart = t;  // (not accounting for frame time here)
    incidental_encoding_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { incidental_encoding_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { incidental_encoding_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { incidental_encoding_resp.clearEvents(); });
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (incidental_encoding_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    incidental_encoding_resp.status = PsychoJS.Status.FINISHED;
  }

  if (incidental_encoding_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = incidental_encoding_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (incidental_encoding_resp.keys === undefined) {  // then this was the first keypress
        incidental_encoding_resp.keys = theseKeys[0].name;  // just the first key pressed
        incidental_encoding_resp.rt = theseKeys[0].rt;
      }
    }
  }
  
  
  // *text_18* updates
  if (t >= 0.0 && text_18.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_18.tStart = t;  // (not accounting for frame time here)
    text_18.frameNStart = frameN;  // exact frame index
    text_18.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_18.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_18.setAutoDraw(false);
  }
  
  // *text_19* updates
  if (t >= 0.0 && text_19.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_19.tStart = t;  // (not accounting for frame time here)
    text_19.frameNStart = frameN;  // exact frame index
    text_19.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_19.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_19.setAutoDraw(false);
  }
  
  // *text_20* updates
  if (t >= 0.0 && text_20.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_20.tStart = t;  // (not accounting for frame time here)
    text_20.frameNStart = frameN;  // exact frame index
    text_20.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_20.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_20.setAutoDraw(false);
  }
  
  // *text_21* updates
  if (t >= 0.0 && text_21.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_21.tStart = t;  // (not accounting for frame time here)
    text_21.frameNStart = frameN;  // exact frame index
    text_21.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_21.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_21.setAutoDraw(false);
  }
  
  // *incidental_image2_* updates
  if (t >= 0.0 && incidental_image2_.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    incidental_image2_.tStart = t;  // (not accounting for frame time here)
    incidental_image2_.frameNStart = frameN;  // exact frame index
    incidental_image2_.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (incidental_image2_.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    incidental_image2_.setAutoDraw(false);
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
  practice_incidental_encodingComponents.forEach( function(thisComponent) {
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


function practice_incidental_encodingRoutineEnd() {
  //------Ending Routine 'practice_incidental_encoding'-------
  practice_incidental_encodingComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('incidental_encoding_resp.keys', incidental_encoding_resp.keys);
  if (typeof incidental_encoding_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('incidental_encoding_resp.rt', incidental_encoding_resp.rt);
      }
  
  incidental_encoding_resp.stop();
  return Scheduler.Event.NEXT;
}

var sustained_attention_arrows_practiceComponents;
function sustained_attention_arrows_practiceRoutineBegin() {
  //------Prepare to start Routine 'sustained_attention_arrows_practice'-------
  t = 0;
  sustained_attention_arrows_practiceClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  image_16.setImage(Arrow_direction);
  arrows_resp.keys = undefined;
  arrows_resp.rt = undefined;
  F_press.setText('F');
  J_press.setText('J');
  left_press.setText('left');
  right_press.setText('right');
  // keep track of which components have finished
  sustained_attention_arrows_practiceComponents = [];
  sustained_attention_arrows_practiceComponents.push(image_16);
  sustained_attention_arrows_practiceComponents.push(arrows_resp);
  sustained_attention_arrows_practiceComponents.push(F_press);
  sustained_attention_arrows_practiceComponents.push(J_press);
  sustained_attention_arrows_practiceComponents.push(left_press);
  sustained_attention_arrows_practiceComponents.push(right_press);
  
  sustained_attention_arrows_practiceComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function sustained_attention_arrows_practiceRoutineEachFrame() {
  //------Loop for each frame of Routine 'sustained_attention_arrows_practice'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = sustained_attention_arrows_practiceClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *image_16* updates
  if (t >= 0.0 && image_16.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_16.tStart = t;  // (not accounting for frame time here)
    image_16.frameNStart = frameN;  // exact frame index
    image_16.setAutoDraw(true);
  }

  
  // *arrows_resp* updates
  if (t >= 0.0 && arrows_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    arrows_resp.tStart = t;  // (not accounting for frame time here)
    arrows_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { arrows_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { arrows_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { arrows_resp.clearEvents(); });
  }

  if (arrows_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = arrows_resp.getKeys({keyList: ['j', 'f', 'J', 'F'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (arrows_resp.keys === undefined) {  // then this was the first keypress
        arrows_resp.keys = theseKeys[0].name;  // just the first key pressed
        arrows_resp.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // *F_press* updates
  if (t >= 0.0 && F_press.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    F_press.tStart = t;  // (not accounting for frame time here)
    F_press.frameNStart = frameN;  // exact frame index
    F_press.setAutoDraw(true);
  }

  
  // *J_press* updates
  if (t >= 0.0 && J_press.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    J_press.tStart = t;  // (not accounting for frame time here)
    J_press.frameNStart = frameN;  // exact frame index
    J_press.setAutoDraw(true);
  }

  
  // *left_press* updates
  if (t >= 0.0 && left_press.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    left_press.tStart = t;  // (not accounting for frame time here)
    left_press.frameNStart = frameN;  // exact frame index
    left_press.setAutoDraw(true);
  }

  
  // *right_press* updates
  if (t >= 0.0 && right_press.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    right_press.tStart = t;  // (not accounting for frame time here)
    right_press.frameNStart = frameN;  // exact frame index
    right_press.setAutoDraw(true);
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
  sustained_attention_arrows_practiceComponents.forEach( function(thisComponent) {
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


function sustained_attention_arrows_practiceRoutineEnd() {
  //------Ending Routine 'sustained_attention_arrows_practice'-------
  sustained_attention_arrows_practiceComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('arrows_resp.keys', arrows_resp.keys);
  if (typeof arrows_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('arrows_resp.rt', arrows_resp.rt);
      routineTimer.reset();
      }
  
  arrows_resp.stop();
  // the Routine "sustained_attention_arrows_practice" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var pre_instruct_sustainedAttentionComponents;
function pre_instruct_sustainedAttentionRoutineBegin() {
  //------Prepare to start Routine 'pre_instruct_sustainedAttention'-------
  t = 0;
  pre_instruct_sustainedAttentionClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_14.keys = undefined;
  key_resp_14.rt = undefined;
  // keep track of which components have finished
  pre_instruct_sustainedAttentionComponents = [];
  pre_instruct_sustainedAttentionComponents.push(text_2);
  pre_instruct_sustainedAttentionComponents.push(key_resp_14);
  
  pre_instruct_sustainedAttentionComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function pre_instruct_sustainedAttentionRoutineEachFrame() {
  //------Loop for each frame of Routine 'pre_instruct_sustainedAttention'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = pre_instruct_sustainedAttentionClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_2* updates
  if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  
  // *key_resp_14* updates
  if (t >= 0.0 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_14.tStart = t;  // (not accounting for frame time here)
    key_resp_14.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_14.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_14.clearEvents(); });
  }

  if (key_resp_14.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_14.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_14.keys === undefined) {  // then this was the first keypress
        key_resp_14.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_14.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
  pre_instruct_sustainedAttentionComponents.forEach( function(thisComponent) {
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


function pre_instruct_sustainedAttentionRoutineEnd() {
  //------Ending Routine 'pre_instruct_sustainedAttention'-------
  pre_instruct_sustainedAttentionComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
  if (typeof key_resp_14.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
      routineTimer.reset();
      }
  
  key_resp_14.stop();
  // the Routine "pre_instruct_sustainedAttention" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var incidental_encoding_realComponents;
function incidental_encoding_realRoutineBegin() {
  //------Prepare to start Routine 'incidental_encoding_real'-------
  t = 0;
  incidental_encoding_realClock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.500000);
  // update component parameters for each repeat
  image_A.setImage(ImageA);
  image_c.setImage(ImageC);
  key_resp_15.keys = undefined;
  key_resp_15.rt = undefined;
  // keep track of which components have finished
  incidental_encoding_realComponents = [];
  incidental_encoding_realComponents.push(image_A);
  incidental_encoding_realComponents.push(image_c);
  incidental_encoding_realComponents.push(key_resp_15);
  incidental_encoding_realComponents.push(text_23);
  incidental_encoding_realComponents.push(text_24);
  incidental_encoding_realComponents.push(text_25);
  incidental_encoding_realComponents.push(text_26);
  
  incidental_encoding_realComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function incidental_encoding_realRoutineEachFrame() {
  //------Loop for each frame of Routine 'incidental_encoding_real'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = incidental_encoding_realClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *image_A* updates
  if (t >= 0.0 && image_A.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_A.tStart = t;  // (not accounting for frame time here)
    image_A.frameNStart = frameN;  // exact frame index
    image_A.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_A.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_A.setAutoDraw(false);
  }
  
  // *image_c* updates
  if (t >= 0.0 && image_c.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_c.tStart = t;  // (not accounting for frame time here)
    image_c.frameNStart = frameN;  // exact frame index
    image_c.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_c.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_c.setAutoDraw(false);
  }
  
  // *key_resp_15* updates
  if (t >= 0.0 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_15.tStart = t;  // (not accounting for frame time here)
    key_resp_15.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_resp_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_resp_15.status = PsychoJS.Status.FINISHED;
  }

  if (key_resp_15.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_15.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'j', 'f', 'J', 'F'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_15.keys === undefined) {  // then this was the first keypress
        key_resp_15.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_15.rt = theseKeys[0].rt;
      }
    }
  }
  
  
  // *text_23* updates
  if (t >= 0.0 && text_23.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_23.tStart = t;  // (not accounting for frame time here)
    text_23.frameNStart = frameN;  // exact frame index
    text_23.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_23.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_23.setAutoDraw(false);
  }
  
  // *text_24* updates
  if (t >= 0.0 && text_24.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_24.tStart = t;  // (not accounting for frame time here)
    text_24.frameNStart = frameN;  // exact frame index
    text_24.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_24.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_24.setAutoDraw(false);
  }
  
  // *text_25* updates
  if (t >= 0.0 && text_25.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_25.tStart = t;  // (not accounting for frame time here)
    text_25.frameNStart = frameN;  // exact frame index
    text_25.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_25.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_25.setAutoDraw(false);
  }
  
  // *text_26* updates
  if (t >= 0.0 && text_26.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_26.tStart = t;  // (not accounting for frame time here)
    text_26.frameNStart = frameN;  // exact frame index
    text_26.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text_26.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text_26.setAutoDraw(false);
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
  incidental_encoding_realComponents.forEach( function(thisComponent) {
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


function incidental_encoding_realRoutineEnd() {
  //------Ending Routine 'incidental_encoding_real'-------
  incidental_encoding_realComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
  if (typeof key_resp_15.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
      }
  
  key_resp_15.stop();
  return Scheduler.Event.NEXT;
}

var pre_instruct_final_memoryComponents;
function pre_instruct_final_memoryRoutineBegin() {
  //------Prepare to start Routine 'pre_instruct_final_memory'-------
  t = 0;
  pre_instruct_final_memoryClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_14.setText(instructions1);
  pressspace.setColor(new util.Color('black'));
  pressspace.setPos([0, (- 0.4)]);
  pressspace.setText('Press space to continue');
  key_resp_16.keys = undefined;
  key_resp_16.rt = undefined;
  image_17.setImage(Image1);
  Jkey.setText(J_key);
  F_key.setText(K_key);
  oldText.setText(yes_text);
  newtext.setText(no_text);
  // keep track of which components have finished
  pre_instruct_final_memoryComponents = [];
  pre_instruct_final_memoryComponents.push(text_14);
  pre_instruct_final_memoryComponents.push(pressspace);
  pre_instruct_final_memoryComponents.push(key_resp_16);
  pre_instruct_final_memoryComponents.push(image_17);
  pre_instruct_final_memoryComponents.push(Jkey);
  pre_instruct_final_memoryComponents.push(F_key);
  pre_instruct_final_memoryComponents.push(oldText);
  pre_instruct_final_memoryComponents.push(newtext);
  
  pre_instruct_final_memoryComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function pre_instruct_final_memoryRoutineEachFrame() {
  //------Loop for each frame of Routine 'pre_instruct_final_memory'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = pre_instruct_final_memoryClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_14* updates
  if (t >= 0.0 && text_14.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_14.tStart = t;  // (not accounting for frame time here)
    text_14.frameNStart = frameN;  // exact frame index
    text_14.setAutoDraw(true);
  }

  
  // *pressspace* updates
  if (t >= 0.0 && pressspace.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    pressspace.tStart = t;  // (not accounting for frame time here)
    pressspace.frameNStart = frameN;  // exact frame index
    pressspace.setAutoDraw(true);
  }

  
  // *key_resp_16* updates
  if (t >= 0.0 && key_resp_16.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_16.tStart = t;  // (not accounting for frame time here)
    key_resp_16.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_16.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_16.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_16.clearEvents(); });
  }

  if (key_resp_16.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_16.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'j', 'f'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_16.keys === undefined) {  // then this was the first keypress
        key_resp_16.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_16.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // *image_17* updates
  if (t >= 0.0 && image_17.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_17.tStart = t;  // (not accounting for frame time here)
    image_17.frameNStart = frameN;  // exact frame index
    image_17.setAutoDraw(true);
  }

  
  // *Jkey* updates
  if (t >= 0.0 && Jkey.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Jkey.tStart = t;  // (not accounting for frame time here)
    Jkey.frameNStart = frameN;  // exact frame index
    Jkey.setAutoDraw(true);
  }

  
  // *F_key* updates
  if (t >= 0.0 && F_key.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    F_key.tStart = t;  // (not accounting for frame time here)
    F_key.frameNStart = frameN;  // exact frame index
    F_key.setAutoDraw(true);
  }

  
  // *oldText* updates
  if (t >= 0.0 && oldText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    oldText.tStart = t;  // (not accounting for frame time here)
    oldText.frameNStart = frameN;  // exact frame index
    oldText.setAutoDraw(true);
  }

  
  // *newtext* updates
  if (t >= 0.0 && newtext.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    newtext.tStart = t;  // (not accounting for frame time here)
    newtext.frameNStart = frameN;  // exact frame index
    newtext.setAutoDraw(true);
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
  pre_instruct_final_memoryComponents.forEach( function(thisComponent) {
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


function pre_instruct_final_memoryRoutineEnd() {
  //------Ending Routine 'pre_instruct_final_memory'-------
  pre_instruct_final_memoryComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_16.keys', key_resp_16.keys);
  if (typeof key_resp_16.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_16.rt', key_resp_16.rt);
      routineTimer.reset();
      }
  
  key_resp_16.stop();
  // the Routine "pre_instruct_final_memory" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var practice_abc_memory_testComponents;
function practice_abc_memory_testRoutineBegin() {
  //------Prepare to start Routine 'practice_abc_memory_test'-------
  t = 0;
  practice_abc_memory_testClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  imageabc.setImage(Image);
  primed_memory_resp.keys = undefined;
  primed_memory_resp.rt = undefined;
  Jkey_2.setText('J');
  F_key_2.setText('F');
  old.setText('old');
  newtext_2.setText('new');
  // keep track of which components have finished
  practice_abc_memory_testComponents = [];
  practice_abc_memory_testComponents.push(imageabc);
  practice_abc_memory_testComponents.push(primed_memory_resp);
  practice_abc_memory_testComponents.push(Jkey_2);
  practice_abc_memory_testComponents.push(F_key_2);
  practice_abc_memory_testComponents.push(old);
  practice_abc_memory_testComponents.push(newtext_2);
  
  practice_abc_memory_testComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function practice_abc_memory_testRoutineEachFrame() {
  //------Loop for each frame of Routine 'practice_abc_memory_test'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = practice_abc_memory_testClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *imageabc* updates
  if (t >= 0.0 && imageabc.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    imageabc.tStart = t;  // (not accounting for frame time here)
    imageabc.frameNStart = frameN;  // exact frame index
    imageabc.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (imageabc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    imageabc.setAutoDraw(false);
  }
  
  // *primed_memory_resp* updates
  if (t >= 0.0 && primed_memory_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    primed_memory_resp.tStart = t;  // (not accounting for frame time here)
    primed_memory_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { primed_memory_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { primed_memory_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { primed_memory_resp.clearEvents(); });
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (primed_memory_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    primed_memory_resp.status = PsychoJS.Status.FINISHED;
  }

  if (primed_memory_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = primed_memory_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'j', 'f', 'J', 'F'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (primed_memory_resp.keys === undefined) {  // then this was the first keypress
        primed_memory_resp.keys = theseKeys[0].name;  // just the first key pressed
        primed_memory_resp.rt = theseKeys[0].rt;
      }
    }
  }
  
  
  // *Jkey_2* updates
  if (t >= 0.0 && Jkey_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Jkey_2.tStart = t;  // (not accounting for frame time here)
    Jkey_2.frameNStart = frameN;  // exact frame index
    Jkey_2.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Jkey_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Jkey_2.setAutoDraw(false);
  }
  
  // *F_key_2* updates
  if (t >= 0.0 && F_key_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    F_key_2.tStart = t;  // (not accounting for frame time here)
    F_key_2.frameNStart = frameN;  // exact frame index
    F_key_2.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (F_key_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    F_key_2.setAutoDraw(false);
  }
  
  // *old* updates
  if (t >= 0.0 && old.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    old.tStart = t;  // (not accounting for frame time here)
    old.frameNStart = frameN;  // exact frame index
    old.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (old.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    old.setAutoDraw(false);
  }
  
  // *newtext_2* updates
  if (t >= 0.0 && newtext_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    newtext_2.tStart = t;  // (not accounting for frame time here)
    newtext_2.frameNStart = frameN;  // exact frame index
    newtext_2.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (newtext_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    newtext_2.setAutoDraw(false);
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
  practice_abc_memory_testComponents.forEach( function(thisComponent) {
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


function practice_abc_memory_testRoutineEnd() {
  //------Ending Routine 'practice_abc_memory_test'-------
  practice_abc_memory_testComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('primed_memory_resp.keys', primed_memory_resp.keys);
  if (typeof primed_memory_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('primed_memory_resp.rt', primed_memory_resp.rt);
      }
  
  primed_memory_resp.stop();
  return Scheduler.Event.NEXT;
}

var pre_instruction_real_abc_final_memoryComponents;
function pre_instruction_real_abc_final_memoryRoutineBegin() {
  //------Prepare to start Routine 'pre_instruction_real_abc_final_memory'-------
  t = 0;
  pre_instruction_real_abc_final_memoryClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_18.keys = undefined;
  key_resp_18.rt = undefined;
  // keep track of which components have finished
  pre_instruction_real_abc_final_memoryComponents = [];
  pre_instruction_real_abc_final_memoryComponents.push(text_27);
  pre_instruction_real_abc_final_memoryComponents.push(key_resp_18);
  
  pre_instruction_real_abc_final_memoryComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function pre_instruction_real_abc_final_memoryRoutineEachFrame() {
  //------Loop for each frame of Routine 'pre_instruction_real_abc_final_memory'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = pre_instruction_real_abc_final_memoryClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_27* updates
  if (t >= 0.0 && text_27.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_27.tStart = t;  // (not accounting for frame time here)
    text_27.frameNStart = frameN;  // exact frame index
    text_27.setAutoDraw(true);
  }

  
  // *key_resp_18* updates
  if (t >= 0.0 && key_resp_18.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_18.tStart = t;  // (not accounting for frame time here)
    key_resp_18.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_18.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp_18.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp_18.clearEvents(); });
  }

  if (key_resp_18.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp_18.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_18.keys === undefined) {  // then this was the first keypress
        key_resp_18.keys = theseKeys[0].name;  // just the first key pressed
        key_resp_18.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
  pre_instruction_real_abc_final_memoryComponents.forEach( function(thisComponent) {
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


function pre_instruction_real_abc_final_memoryRoutineEnd() {
  //------Ending Routine 'pre_instruction_real_abc_final_memory'-------
  pre_instruction_real_abc_final_memoryComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('key_resp_18.keys', key_resp_18.keys);
  if (typeof key_resp_18.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp_18.rt', key_resp_18.rt);
      routineTimer.reset();
      }
  
  key_resp_18.stop();
  // the Routine "pre_instruction_real_abc_final_memory" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var questionairreComponents;
function questionairreRoutineBegin() {
  //------Prepare to start Routine 'questionairre'-------
  t = 0;
  questionairreClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  questioniarre.setText(instructions1);
  questionairre_resp.keys = undefined;
  questionairre_resp.rt = undefined;
  text_29.setText(Instructions2);
  image_18.setImage(Image1);
  image_19.setImage(Image2);
  image_20.setImage(Image3);
  image_21.setImage(Image4);
  A_txt1.setText(J_key);
  B_text.setText(K_key);
  a_text2.setText(J_key);
  C_text.setText(L_key);
  // keep track of which components have finished
  questionairreComponents = [];
  questionairreComponents.push(questioniarre);
  questionairreComponents.push(questionairre_resp);
  questionairreComponents.push(text_29);
  questionairreComponents.push(image_18);
  questionairreComponents.push(image_19);
  questionairreComponents.push(image_20);
  questionairreComponents.push(image_21);
  questionairreComponents.push(A_txt1);
  questionairreComponents.push(B_text);
  questionairreComponents.push(a_text2);
  questionairreComponents.push(C_text);
  
  questionairreComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function questionairreRoutineEachFrame() {
  //------Loop for each frame of Routine 'questionairre'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = questionairreClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *questioniarre* updates
  if (t >= 0.0 && questioniarre.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    questioniarre.tStart = t;  // (not accounting for frame time here)
    questioniarre.frameNStart = frameN;  // exact frame index
    questioniarre.setAutoDraw(true);
  }

  
  // *questionairre_resp* updates
  if (t >= 0.0 && questionairre_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    questionairre_resp.tStart = t;  // (not accounting for frame time here)
    questionairre_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { questionairre_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { questionairre_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { questionairre_resp.clearEvents(); });
  }

  if (questionairre_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = questionairre_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', 'j', 'k', 'l', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'n', 'p', 't'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (questionairre_resp.keys === undefined) {  // then this was the first keypress
        questionairre_resp.keys = theseKeys[0].name;  // just the first key pressed
        questionairre_resp.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // *text_29* updates
  if (t >= 0.0 && text_29.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_29.tStart = t;  // (not accounting for frame time here)
    text_29.frameNStart = frameN;  // exact frame index
    text_29.setAutoDraw(true);
  }

  
  // *image_18* updates
  if (t >= 0.0 && image_18.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_18.tStart = t;  // (not accounting for frame time here)
    image_18.frameNStart = frameN;  // exact frame index
    image_18.setAutoDraw(true);
  }

  
  // *image_19* updates
  if (t >= 0.0 && image_19.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_19.tStart = t;  // (not accounting for frame time here)
    image_19.frameNStart = frameN;  // exact frame index
    image_19.setAutoDraw(true);
  }

  
  // *image_20* updates
  if (t >= 0.0 && image_20.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_20.tStart = t;  // (not accounting for frame time here)
    image_20.frameNStart = frameN;  // exact frame index
    image_20.setAutoDraw(true);
  }

  
  // *image_21* updates
  if (t >= 0.0 && image_21.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_21.tStart = t;  // (not accounting for frame time here)
    image_21.frameNStart = frameN;  // exact frame index
    image_21.setAutoDraw(true);
  }

  
  // *A_txt1* updates
  if (t >= 0.0 && A_txt1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    A_txt1.tStart = t;  // (not accounting for frame time here)
    A_txt1.frameNStart = frameN;  // exact frame index
    A_txt1.setAutoDraw(true);
  }

  
  // *B_text* updates
  if (t >= 0.0 && B_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    B_text.tStart = t;  // (not accounting for frame time here)
    B_text.frameNStart = frameN;  // exact frame index
    B_text.setAutoDraw(true);
  }

  
  // *a_text2* updates
  if (t >= 0.0 && a_text2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    a_text2.tStart = t;  // (not accounting for frame time here)
    a_text2.frameNStart = frameN;  // exact frame index
    a_text2.setAutoDraw(true);
  }

  
  // *C_text* updates
  if (t >= 0.0 && C_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    C_text.tStart = t;  // (not accounting for frame time here)
    C_text.frameNStart = frameN;  // exact frame index
    C_text.setAutoDraw(true);
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
  questionairreComponents.forEach( function(thisComponent) {
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


function questionairreRoutineEnd() {
  //------Ending Routine 'questionairre'-------
  questionairreComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('questionairre_resp.keys', questionairre_resp.keys);
  if (typeof questionairre_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('questionairre_resp.rt', questionairre_resp.rt);
      routineTimer.reset();
      }
  
  questionairre_resp.stop();
  // the Routine "questionairre" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var questionairre2Components;
function questionairre2RoutineBegin() {
  //------Prepare to start Routine 'questionairre2'-------
  t = 0;
  questionairre2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  text_30.setText(instructions1);
  text_32.setText(text1);
  text_33.setText(text2);
  questionairre_resp2.keys = undefined;
  questionairre_resp2.rt = undefined;
  // keep track of which components have finished
  questionairre2Components = [];
  questionairre2Components.push(text_30);
  questionairre2Components.push(text_32);
  questionairre2Components.push(text_33);
  questionairre2Components.push(questionairre_resp2);
  
  questionairre2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function questionairre2RoutineEachFrame() {
  //------Loop for each frame of Routine 'questionairre2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = questionairre2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_30* updates
  if (t >= 0.0 && text_30.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_30.tStart = t;  // (not accounting for frame time here)
    text_30.frameNStart = frameN;  // exact frame index
    text_30.setAutoDraw(true);
  }

  
  // *text_32* updates
  if (t >= 0.0 && text_32.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_32.tStart = t;  // (not accounting for frame time here)
    text_32.frameNStart = frameN;  // exact frame index
    text_32.setAutoDraw(true);
  }

  
  // *text_33* updates
  if (t >= 0.0 && text_33.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_33.tStart = t;  // (not accounting for frame time here)
    text_33.frameNStart = frameN;  // exact frame index
    text_33.setAutoDraw(true);
  }

  
  // *questionairre_resp2* updates
  if (t >= 0.0 && questionairre_resp2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    questionairre_resp2.tStart = t;  // (not accounting for frame time here)
    questionairre_resp2.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { questionairre_resp2.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { questionairre_resp2.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { questionairre_resp2.clearEvents(); });
  }

  if (questionairre_resp2.status === PsychoJS.Status.STARTED) {
    let theseKeys = questionairre_resp2.getKeys({keyList: ['y', 'n', 'left', 'right', 'space', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'return'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      questionairre_resp2.keys = [].concat(questionairre_resp2.keys, theseKeys[0].name).filter((i) => i !== undefined);  // storing all keys
      questionairre_resp2.rt = [].concat(questionairre_resp2.rt, theseKeys[0].rt).filter((i) => i !== undefined);
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
  questionairre2Components.forEach( function(thisComponent) {
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


function questionairre2RoutineEnd() {
  //------Ending Routine 'questionairre2'-------
  questionairre2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('questionairre_resp2.keys', questionairre_resp2.keys);
  if (typeof questionairre_resp2.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('questionairre_resp2.rt', questionairre_resp2.rt);
      }
  
  questionairre_resp2.stop();
  // the Routine "questionairre2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var endComponents;
function endRoutineBegin() {
  //------Prepare to start Routine 'end'-------
  t = 0;
  endClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  exit.keys = undefined;
  exit.rt = undefined;
  // keep track of which components have finished
  endComponents = [];
  endComponents.push(text_28);
  endComponents.push(exit);
  
  endComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function endRoutineEachFrame() {
  //------Loop for each frame of Routine 'end'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = endClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_28* updates
  if (t >= 0.0 && text_28.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_28.tStart = t;  // (not accounting for frame time here)
    text_28.frameNStart = frameN;  // exact frame index
    text_28.setAutoDraw(true);
  }

  
  // *exit* updates
  if (t >= 0.0 && exit.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    exit.tStart = t;  // (not accounting for frame time here)
    exit.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { exit.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { exit.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { exit.clearEvents(); });
  }

  if (exit.status === PsychoJS.Status.STARTED) {
    let theseKeys = exit.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (exit.keys === undefined) {  // then this was the first keypress
        exit.keys = theseKeys[0].name;  // just the first key pressed
        exit.rt = theseKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
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
  endComponents.forEach( function(thisComponent) {
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


function endRoutineEnd() {
  //------Ending Routine 'end'-------
  endComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('exit.keys', exit.keys);
  if (typeof exit.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('exit.rt', exit.rt);
      routineTimer.reset();
      }
  
  exit.stop();
  // the Routine "end" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
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
