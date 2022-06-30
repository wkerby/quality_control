import pandas as pd
import datetime

#designate the api token for smartsheet. want to eventually use the Smartsheet API to retrive data from its tables w/o a manual export to csv or xlsx
#SMARTSHEET_ACCESS_TOKEN = R9hJyekhhUWpcJDlBF4RRpyINxPcGwpyMEn8S

#create a timestamp
timestamp = str(datetime.datetime.now())[:-15]

#load the job_information.csv from OneDrive into python as a df
try:
	project_information_df = pd.read_csv(r'C:\\Users\\WKerby\\OneDrive - Brasfield & Gorrie, L.L.C\\SS_Data_Uploader\\Job_Information.csv')

	#load an exported csv or xlsx file of the All Region - Dumping Ground DEMO table from Smartsheet
	all_region_dg_df = pd.read_excel(r'Z:\\Departments\\IT\\PMO\\QC Plan Submission\\Project Lists\\All Region - JP and JC Lists\\All Region - JP and JC List Dumping Ground DEMO 04-06-2022.xlsx')
except FileNotFoundError:
	print("File could not be found.")
else:
	#retrieve the indices of all entries in the table
	index = project_information_df.index

	#retrieve a list of all closed project number_names from the df
	project_information_df_closed = list(project_information_df.loc[:,"JobNumberName"].loc[project_information_df["PostingEdit"] == 'N'])

	#retrieve a list of all project number_names from the all region - dumping ground DEMO
	all_region_dumping_ground_demo_projects = list(all_region_dg_df.loc[:, "Projects"])

	#remove any duplicates from the project number_names all region - dumping ground DEMO list
	all_region_dumping_ground_demo_projects_set = list(set(all_region_dumping_ground_demo_projects))

	#retrieve all closed jobs in the project number_names all region - dumping ground DEMO set
	all_region_dumping_ground_demo_projects_closed = []
	for jobnumbername in all_region_dumping_ground_demo_projects_set:
		if jobnumbername in project_information_df_closed:
			all_region_dumping_ground_demo_projects_closed.append(jobnumbername)
		else:
			pass

	if len(all_region_dumping_ground_demo_projects_closed) > 0:

		#create dictionary of all closed jobs in the project number_names all region - dumping ground DEMO set
		all_region_dumping_ground_demo_projects_closed_dict = {'Projects':[]}
		for jobnumbername in all_region_dumping_ground_demo_projects_closed:
			all_region_dumping_ground_demo_projects_closed_dict["Projects"].append(jobnumbername)

		#create a new df from the all_region_dumping_ground_demo_projects_closed_dict
		all_region_dumping_ground_demo_projects_closed_df = pd.DataFrame(all_region_dumping_ground_demo_projects_closed_dict)

		#write the dictionary as a .xlsx file and exclued the indices
		try:
			all_region_dumping_ground_demo_projects_closed_df.to_excel(r'Z:\\Departments\\IT\\PMO\\QC Plan Submission\\Project Lists\\Closed Job Lists\\ClosedJobsRun' + timestamp + '.xlsx', index = False)
		except OSError:
			print("Something went wrong writing to the file!")

	else:
		print("No new closed projects.")







