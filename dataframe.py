import gspread
import pandas as pd

gc = gspread.service_account(filename='service_account.json')

# "Digital Product Passport (Responses)"
sh = gc.open("re-dpp")

# select by index (0 is the first sheet) or name
worksheet = sh.get_worksheet(0) 

data = worksheet.get_all_records()

df = pd.DataFrame(data)

new_names = {
    1: "Company_Name",
    2: "Designation",
    3: "Company_Size",
    4: "Company_Type",
    5: "B1",
    6: "B2",
    7: "B3",
    8: "B4",
    9: "B5",
    10: "B6",
    11: "B7",
    12: "C1",
    13: "C2",
    14: "C3",
    15: "C4",
    16: "D1",
    17: "D2",
    18: "D3",
    19: "E1",
    20: "E2",
    21: "E3",
    22: "F1",
    23: "F2",
    24: "F3",
    25: "F4",
    26: "F5",
    27: "F6",
    28: "F7",
    29: "G1",
    30: "G2",
    31: "G3",
    32: "G4",
    33: "G5",
    34: "G6",
    35: "G7",
    36: "H1",
    37: "H2",
    38: "H3",
    39: "H4",
}

for index, new_name in new_names.items():
    old_name = df.columns[index]
    df.rename(columns={old_name: new_name}, inplace=True)

readiness_cols = ["F1", "F2", "F3", "F4", "F5", "F6", "F7"]
readiness_score = "Readiness_Score"
df[readiness_score] = df[readiness_cols].mean(axis=1)

mgmt_cols = ["C1", "C2", "C3", "C4"]
mgmt_support_score = "Mgmt_Support_Score"
df[mgmt_support_score] = df[mgmt_cols].mean(axis=1)
