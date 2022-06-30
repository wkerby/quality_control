import pandas as pd
#read the Smartsheet export table of active, closed, and potential QC projects as of Feb 2 2022 into a df
all_region_dumping_ground_DEMO_df = pd.read_excel(r'Z:\Shared\Departments\IT\PMO\QC Plan Submission\Project Lists\All Region - JP and JC Lists\All Region - Dumping Ground DEMO.xlsx')

#read the Smartsheet export table of all active, closde, and potential QC projects initiated on Dec 8 2021
old_all_region_dumping_ground_df = pd.read_excel(r'Z:\Shared\Departments\IT\PMO\QC Plan Submission\Project Lists\All Region - JP and JC Lists\Old All Region - Dumping Ground DEMO.xlsx')

#obtain a list of the JobNumberName (i.e. "Projects" in Smartsheet, which is the attribute label RRobison wanted) attribute for each job in the Smartsheet table as of Feb 2 2022
new_jobnumnamelist = list(all_region_dumping_ground_DEMO_df.loc[:, 'Projects'])

#obtain a list of the JobNumberName (i.e. "Projects" in Smartsheet) attribute for each job in the Smartsheet table initiated Dec 8 2021
old_jobnumnamelist = list(old_all_region_dumping_ground_df.loc[:,'Projects'])

#obtain a list of the JobNumberName attribute for records that appear in both the new Smartsheet job table and the old Smartsheet job table
jobnumname_return_list = [jobnumname for jobnumname in old_jobnumnamelist if jobnumname in new_jobnumnamelist]

#create a dictionary with first key, value combo being the JobNumName for each element in the jobnunname_return_list, then Region, 
#Date Uploaded (if applicable), and Submission Status (if applicable) attributed to the JobNumName ("Project") in the old Smartsheet table
index = old_all_region_dumping_ground_df.index
return_dict = {"Projects":[],"Region": [],"Date Uploaded":[], "Submission Status": []}
for jobnumname in jobnumname_return_list:
	condition = old_all_region_dumping_ground_df["Projects"] == jobnumname
	spec_index = index[condition]
	return_dict["Projects"].append(jobnumname)
	#clean up the date so it is MM/DD/YY format for Smartsheet
	date_str = str(list(old_all_region_dumping_ground_df.loc[spec_index,"Date Uploaded"])[0])
	date_strm = date_str.split('-')
	date = date_strm[1] + '/' + date_strm[2][:2] + '/' + date_strm[0][-2:]
	# timestamp = str(list(old_all_region_dumping_ground_df.loc[spec_index,"Date Uploaded"])[0])
	# date = timestamp.split("'")[1]
	# date_mod = (date[:10]).split("-")
	# date_str = date_mod[1] + '/' + date_mod[2] + '/' + date_mod[0]
	return_dict['Date Uploaded'].append(date)
	return_dict["Region"].append(str(list(old_all_region_dumping_ground_df.loc[spec_index,"Region"])[0]))
	return_dict["Submission Status"].append(str(list(old_all_region_dumping_ground_df.loc[spec_index,"Submission Status"])[0]))
	# return_dict['Date Uploaded'].append(str(list(old_all_region_dumping_ground_df.loc[spec_index,"Date Uploaded"])[0]))

#save dictionary as a df and write to a .xlsx file
return_df = pd.DataFrame(return_dict)
return_df.to_excel(r'Z:\Shared\Departments\IT\PMO\QC Plan Submission\Project Lists\All Region - JP and JC Lists\All Region - Dumping Ground DEMO Date Add.xlsx', index = False)