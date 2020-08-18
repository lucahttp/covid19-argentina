import numpy as np
teams_list = ["File Date", "File Expiration Date", "Current Date"]
data = np.array([[1, 2, 1],
                 [0, 1, 0],
                 [2, 4, 2]])

row_format = "{:>15}" * (len(teams_list) + 1)
print(row_format.format("", *teams_list))
for team, row in zip(teams_list, data):
    print(row_format.format(team, *row))
