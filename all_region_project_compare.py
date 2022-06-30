import pandas as pd

#read the All Region - JP and JC List Dumping Ground DEMO into a df with pandas
all_region_dumping_ground_DEMO_df = pd.read_excel(r'Z:\Shared\Departments\IT\PMO\QC Plan Submission\Project Lists\All Region - JP and JC Lists\All Region - JP and JC List Dumping Ground DEMO 02-03-2022.xlsx')

#read the All Region - JP and JC List DEMO into a df with pandas
all_region_DEMO_df = pd.read_excel(r'Z:\Shared\Departments\IT\PMO\QC Plan Submission\Project Lists\All Region - JP and JC Lists\All Region - JP and JC List DEMO 02-03-2022.xlsx')

#obtain a list of the JobNumName ("Projects") attribute for each record in the All Region - JP and JC List Dumping Ground DEMO
dumping_ground_project_list = list(all_region_dumping_ground_DEMO_df.loc[:,'Projects'])

#obtain a list of the JobNumName ("Projects") attribute for each record in the All Region - JP and JC DEMO
all_project_list = list(all_region_DEMO_df.loc[:,'Projects'])

#create a single key, value pair dictionary of JobNumNames (i.e. "Projects") that are not in the All Region - JP and JC List Dumping Ground DEMO but are in the All Region - JP and JC List DEMO
#i.e a right outer join if All Region - JP and JC List DEMO, the larger of the two tables, is the "left" table and the All Region - JP and JC List Dumping Ground DEMO
#is the "right" table
project_list = [project in dumping_ground_project_list if project not in all_project_list]
# for project in dumping_ground_project_list:
# 	if project not in all_project_list:
# 		project_list.append(project)

final_dict = {'Projects': []}
final_dict['Projects'] = project_list

#store the dictionary as a df and write to excel
final_df = pd.DataFrame(final_dict)
final_df.to_excel(r'Z:\Shared\Departments\IT\PMO\QC Plan Submission\Project Lists\All Region - JP and JC Lists\All Region - JP and JC List Compare_1.xlsx', index = False)

