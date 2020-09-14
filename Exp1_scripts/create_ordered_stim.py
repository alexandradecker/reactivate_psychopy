import numpy as np
import list_assignment as la
import final_test as ft
import reorder_test_set as rts

la.group("../intentional_encoding_test.xlsx")

rts.generate_test_set("../intentional_encoding_test.xlsx", "../test_encoding.xlsx")

#%%

ft.generate_final_test("4_intentional_encoding.xlsx", "final_memory_test.xlsx")