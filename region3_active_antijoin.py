import pandas as pd
v1_df = pd.read_excel(r'Z:\Shared\Departments\BPI\Process Improvement\QC Plan Submission\region3-v1.xlsx') #comes from Region 3 - Pilot Jobs Tracker in Smarstheet
v2_df = pd.read_excel(r'Z:\Shared\Departments\BPI\Process Improvement\QC Plan Submission\region3-active-v2.xlsx') #comes from Region 3 - Projects Master in Smartsheet
desig_list = ["Active","Inactive"]
index = v1_df.index
count = 0
# print(index[v1_df["JC Status"] == "Inactive"])
# print(index[v1_df["JC Status"] == "Active"])
for designation in desig_list:
	condition = v1_df["JC Status"] == designation
	index_list = index[condition] #why is this saying that "int object is not iterable?"
	v1_list = []
	for index in index_list:
		v1_list.append(v1_df.loc[index,"JC Number"])
	if designation == "Active":
		v2_list = list(v2_df.loc[:, "JobNumberName"].loc[v2_df["Job Status"] == designation])
	else:
		v2_list = list(v2_df.loc[:, "JobNumberName"].loc[v2_df["Job Status"] == "Closed"])
	v2_num_list = [i[:5] for i in v2_list]
	add_list = []
	for v1_num in v1_list:
		if str(v1_num) not in v2_num_list:
			add_list.append(v1_num)
		else:
			pass
	if designation == "Active":
		print('Change the following projects to ' + designation + ' on the Region 3 Projects - Master Report \nalong with a link to the submission form in the project folder for QC V2: \n' + str(add_list))
	else:
		print('Change the following projects to "Closed" on the Region 3 Projects - Master Report: \n' + str(add_list))
	count +=1
	print(count)
