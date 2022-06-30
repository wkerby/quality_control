import pandas as pd

#read Kyle G's job_info.csv file pulled from E1 into a df with pandas
job_info_csv_df = pd.read_csv(r'C:\Users\wkerb\OneDrive - Brasfield & Gorrie, L.L.C\SS_Data_Uploader\Job_Information.csv')

##read the All Region - JP and JC List DEMO into a df with pandas
all_region_DEMO_df = pd.read_excel(r'Z:\Shared\Departments\IT\PMO\QC Plan Submission\Project Lists\All Region - JP and JC Lists\All Region - JP and JC List DEMO.xslx')

#create a condition that searches for records in the All Region - JP and JC List DEMO with a #NO MATCH or "Submitted" Submission Status
condition = all_region_DEMO_df['Submission Status'] != "No Submission"
index = all_region_DEMO_df.index
no_match_indices = index[condition]

#obtain a list of the JobNumName ("Projects") attribute for each record in the All Region - JP and JC List DEMO if it has a #NO MATCH Submission Status or a "Submitted" status
#JobNumNames that meet this condition are #JobNumNames that are not in the All Region - Dumping Ground DEMO. Because Smartsheet's data shuttle add-on only pulled projects rows 
#into the All Region - Dumping Ground DEMO table with an "Active" status, we are considering jobs in the All Region - JP and JC List Demo that we can remove
no_match_list = list(all_region_DEMO_df.loc[no_match_indices,"Projects"])
no_match_job_nums = [jobnumname[:5] for jobnumname in no_match_list]

#confirm that the #NO MATCH project records in the All Region - JP and JC List DEMO are in fact closed according to E1 (i.e Kyle G's) job_info.csv file
index_ = job_info_csv_df.index
closed_list = []
condition = job_info_csv_df["PostingEdit"] == 'N' #PostingEdit == N indicates that the job has closed in E1
closedindex = index_[condition]

#obtain a list of all closed JobNumbers from E1 (i.e Kyle G's job_info.csv file) 
closedlist = list(job_info_csv_df.loc[closedindex,"JobNumber"])

#delete_list includes all JobNumNames that have indeed closed according to E1 (i.e Kyle G's job_info.csv file)
delete_list = [i for i in no_match_job_nums if int(i) in closed_list]

#if not in closed_list from E1, assumed that the name changed from the last time 
#Smartsheet's data shuttle ran and that the JobNumName is no longer recognized in the All Region - JP and JC List DEMO
name_change_list = [i for i in no_match_job_nums if int(i) not in closed_list]

#create dictionary that includes ProjectNumber key,value pairs and a ClosedE1 Yes/No key, value pairs
easy_csv_dict = {}
col_labels = ["ProjectNumber","ClosedE1"]
for i in col_labels:
	easy_csv_dict[i] = []
for i in delete_list:
	easy_csv_dict["ProjectNumber"].append(i)
	easy_csv_dict["ClosedE1"].append("Yes")
for i in name_change_list:
	easy_csv_dict["ProjectNumber"].append(i)
	easy_csv_dict["ClosedE1"].append("No")

#save the dictionary as a df and write to excel with pandas
final_df = pd.DataFrame(easy_csv_dict)
final_df.to_excel(r'Z:\Shared\Departments\IT\PMO\QC Plan Submission\All Region JP and JC Delete List.xlsx', index = False)



