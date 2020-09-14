import pandas as pd
import random

IMAGE_A = 1
IMAGE_B = 2
IMAGE_C = 3

def transpose(mat):
    return list(zip(*mat))

def collect_groups(file):
    data = pd.read_excel(file).values.tolist()
    return [(row[IMAGE_A], row[IMAGE_B], row[IMAGE_C]) for row in data]

# returns a dict {key=image_category type: value=row}
def catagorize_images(file):
    all_images = {'A': [],
                  'B': [],
                  'C': [],
                  'new': []}

    df = pd.read_excel(file)
    for k in all_images.keys():
        # exclude trial number
        all_images[k] = df.loc[df['image_type'] == k].values.tolist()
    
    return all_images

# returns a ORDERED (that is read from the file) list of [(C, B)] from [(A, B, C)]
def indirectly_paired(groups):
    # take first half
    groups = groups[:len(groups) // 2]
    random.shuffle(groups)

    return [group[1:][::-1] for group in groups]

def not_indirectly_paired(groups):
    # take second half and randomnize
    groups = groups[len(groups) // 2:]
    random.shuffle(groups)

    groups = groups + groups[:1]

    return [(groups[i][2], groups[i + 1][1]) for i in range(len(groups) - 1)]

# return a list of (C, B) with their coresponding rows
def get_prop_of_pairs(pairs, catagorized_images):
    cb_pairs = []

    for i in range(len(pairs)):
        C = list(filter(lambda row: row[0] == pairs[i][0], catagorized_images['C']))[0]
        B = list(filter(lambda row: row[0] == pairs[i][1], catagorized_images['B']))[0]

        cb_pairs.append((C, B))

    return cb_pairs

# adding a pair type to every row. i.e. n/a for A and new images and directly/indirectly paired for C-B pairs
def denote_type(data, pair_type):
    # for pairs
    if type(data[0]) == tuple:
        for i in range(len(data)):
            data[i] = (data[i][0] + [pair_type], data[i][1] + [pair_type])
    # for A and new images
    else:
        for i in range(len(data)):
            data[i].append(pair_type)

    return data

# flatten the tuple elements in lst
def flatten_tuples(lst):
    flat = []
    for l in lst:
        if type(l) == tuple:
            flat.extend([l[0], l[1]])
        else:
            flat.append(l)

    return flat

def write_to_file(file, indirect_pairs, not_indirect_pairs, catagorized_images):
    # ignore B and C since they are extracted out
    table = denote_type(catagorized_images['A'], 'n/a') + \
            denote_type(catagorized_images['new'], 'n/a') + \
            denote_type(indirect_pairs, 'indirect') + \
            denote_type(not_indirect_pairs, 'direct')

    random.shuffle(table)
    table = transpose(flatten_tuples(table))

    columns = {
        'Image': table[0],
        'image_type': table[1],
        'category': table[2],
        'trial_number': list(range(1, 193)),
        'pair_indicator': table[4]
    }

    # new df
    df = pd.DataFrame(columns, columns = transpose(columns.items())[0])
    # create a file in current path
    df.to_excel (file, header=True, index=False)

def generate_final_test(intentional_encoding_file, final_memory_test_file):
    groups = collect_groups(intentional_encoding_file)
    all_images = catagorize_images(final_memory_test_file)
    random.shuffle(groups)

    ip = indirectly_paired(groups)
    nip = not_indirectly_paired(groups)

    ip = get_prop_of_pairs(ip, all_images)
    nip = get_prop_of_pairs(nip, all_images)

    write_to_file('./priming_recognition_test.xlsx', ip, nip, all_images)