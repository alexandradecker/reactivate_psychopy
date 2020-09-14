import pandas as pd
import random

TRIAL = 0
IMAGE_A = 1
LOCATION1 = 2
CORRECT_CAT = 3
LOCATION2 = 4
LOCATION3 = 5
CORRECT_IMG = 6

# return a tuple of dicts from the intentional encoding file; 
# ({listNum: [trialNum]}: obj-face, {listNum: [trialNum]}: obj-scence)
def get_pairs(file):
    obj_face  = {}
    obj_scene = {}
    df = pd.read_excel(file)

    for i in range(1, 5):
        obj_face[i] = df.loc[(df['ListNum'] == i) & (df['CategoryB'] == 'object-face')]['Trial'].values.tolist()
        obj_scene[i] = df.loc[(df['ListNum'] == i) & (df['CategoryB'] == 'object-scene')]['Trial'].values.tolist()
    
    return obj_face, obj_scene

# replaces the trial number with actual rows from the test file
def collect_data(file, pairs):
    df = pd.read_excel(file)
    for i in range(1, 5):
        for j in range(6):
            pairs[0][i][j] = df.loc[(df['trial'] == pairs[0][i][j])].values.tolist()[0]
            pairs[1][i][j] = df.loc[(df['trial'] == pairs[1][i][j])].values.tolist()[0]

    return pairs

# combine the values of two sets for same keys
def combine_sets(set1, set2):
    combined = {}
    for (k, v1), (_, v2) in zip(set1.items(), set2.items()):
        combined[k] = v1 + v2

    return combined

# balance the pics in each list so they appear equally, returns a dict key: list num, value: rows
def reorganize_location_within_list(list_num_file, test_file):
    obj_face, obj_scene = collect_data(test_file, get_pairs(list_num_file))

    # maybe there's a better way to do this?
    for i in range(1, 5):
        obj_face[i][2][LOCATION1], obj_face[i][2][LOCATION2] = obj_face[i][2][LOCATION2], obj_face[i][2][LOCATION1]
        obj_face[i][3][LOCATION1], obj_face[i][3][LOCATION2] = obj_face[i][3][LOCATION2], obj_face[i][3][LOCATION1]
        obj_scene[i][2][LOCATION1], obj_scene[i][2][LOCATION2] = obj_scene[i][2][LOCATION2], obj_scene[i][2][LOCATION1]
        obj_scene[i][3][LOCATION1], obj_scene[i][3][LOCATION2] = obj_scene[i][3][LOCATION2], obj_scene[i][3][LOCATION1]
        
        # 2 rows swap to loc 3
        obj_face[i][4][LOCATION1], obj_face[i][4][LOCATION3] = obj_face[i][4][LOCATION3], obj_face[i][4][LOCATION1]
        obj_face[i][5][LOCATION1], obj_face[i][5][LOCATION3] = obj_face[i][5][LOCATION3], obj_face[i][5][LOCATION1]
        obj_scene[i][4][LOCATION1], obj_scene[i][4][LOCATION3] = obj_scene[i][4][LOCATION3], obj_scene[i][4][LOCATION1]
        obj_scene[i][5][LOCATION1], obj_scene[i][5][LOCATION3] = obj_scene[i][5][LOCATION3], obj_scene[i][5][LOCATION1]

    return combine_sets(obj_face, obj_scene)

# return a tranposed matrix
def transpose(mat):
    return list(zip(*mat))

# return a matrix representing a table, ordered by list_num
def reorder_by_list_num(dataset):
    # randomnize within the lists
    for i in range(1, 5):
        random.shuffle(dataset[i])
    
    return [lst for i in range(1, 5) for lst in dataset[i]]

def write_to_file(file, data):
    transposed_data = transpose(data)
    columns = {'trial': list(range(1, 49)),
          'image_a': transposed_data[IMAGE_A],
          'location_1': transposed_data[LOCATION1],
          'correct_category_pair': transposed_data[CORRECT_CAT],
          'location_2 (faces)': transposed_data[LOCATION2],
          'location_3 (scenes)': transposed_data[LOCATION3],
          'correct_image': transposed_data[CORRECT_IMG]}

    # new df
    df = pd.DataFrame(columns, columns = transpose(columns.items())[0])
    # write to text.xlsx in current path
    df.to_excel ('./test.xlsx', header=True, index=False)

def generate_test_set(list_num_file, test_file):
    table = reorder_by_list_num(reorganize_location_within_list(list_num_file, test_file))
    write_to_file('./retrieval_practice.xlsx', table)
