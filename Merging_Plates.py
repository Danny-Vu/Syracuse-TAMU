"""
Merging xlsx plate signals from FLIPR Penta with chemical set
Python
"""
#this is to get the chemicals used in the study
import pandas as pd
df = pd.read_excel('/content/drive/MyDrive/1029 Chemical Study - Sarah-3/Donor 1083/1083 Plate Maps P1-8.xlsx')
df

#splitting the chemicals per plate
plate_chemicals_1 = df.loc[0:64, 'Chemical'].tolist()
plate_chemicals_2 = df.loc[65:129, 'Chemical'].tolist()
plate_chemicals_3 = df.loc[130:194, 'Chemical'].tolist()
plate_chemicals_4 = df.loc[195:259, 'Chemical'].tolist()
plate_chemicals_5 = df.loc[260:324, 'Chemical'].tolist()
plate_chemicals_6 = df.loc[325:389, 'Chemical'].tolist()
plate_chemicals_7 = df.loc[390:454, 'Chemical'].tolist()
plate_chemicals_8 = df.loc[455:519, 'Chemical'].tolist()
plate_chemicals_9 = df.loc[520:584, 'Chemical'].tolist()
plate_chemicals_10 = df.loc[585:649, 'Chemical'].tolist()
plate_chemicals_11 = df.loc[650:714, 'Chemical'].tolist()
plate_chemicals_12 = df.loc[715:779, 'Chemical'].tolist()
plate_chemicals_13 = df.loc[780:844, 'Chemical'].tolist()
plate_chemicals_14 = df.loc[845:909, 'Chemical'].tolist()
plate_chemicals_15 = df.loc[910:974, 'Chemical'].tolist()
plate_chemicals_16 = df.loc[975:1039, 'Chemical'].tolist()

#control group manually 
control_groups = [
'TAB_50uM_1','ISO_10uM_1','VEH_0uM_1',
'VEH_0uM_2','ISO_10uM_2','QT1_10uM_1','QT2_10uM_1','QT3_10uM_1','MEDIA_0uM_1',
'MEDIA_0uM_2','QT1_10uM_2','QT2_10uM_2','QT3_10uM_2','MEDIA_0uM_3','PRO_0.5uM_1','QT-1_10uM_1','QT-2_10uM_1','QT-3_10uM_1',
'VEH_0uM_3','VEH_0uM_4',
'ISO_10uM_3','TAB_50uM_2','TAB_50uM_3','CIS_0.1uM_1','VEH_0uM_5',
'VEH_0uM_6','CIS_0.1uM_2','QT1_10uM_3','QT2_10uM_3',
'QT3_10uM_3','MEDIA_0uM_4','MEDIA_0uM_5','QT-1_10uM_2','QT-2_10uM_2','QT-3_10uM_2','MEDIA_0uM_6','PRO_0.5uM_2',
'QT-1_10uM_3','QT-2_10uM_3','QT-3_10uM_3','VEH_0uM_7','VEH_0uM_8','CIS_0.1uM_3','PRO_0.5uM_3',
'VEH_100uM',
'VEH_10uM',
'VEH_1uM',
'VEH_0.1uM',
]

control_names = [
'TAB','ISO','VEH','VEH','ISO','QT1','QT2','QT3','MEDIA','MEDIA','QT1','QT2','QT3','MEDIA','PRO','QT-1','QT-2','QT-3','VEH','VEH','ISO','TAB','TAB','CIS','VEH','VEH','CIS','QT1','QT2','QT3','MEDIA','MEDIA','QT-1','QT-2','QT-3','MEDIA','PRO','QT-1','QT-2','QT-3','VEH','VEH','CIS','PRO','VEH','VEH','VEH','VEH']

control_dose = [
50,10,0,0,10,10,10,10,0,0,10,10,10,0,0.5,10,10,10,0,0,10,50,50,0.1,0,0,0.1,10,10,10,0,0,10,10,10,0,0.5,10,10,10,0,0,0.1,0.5,100,10,1,0.1
]

# Combining plates per donor | assuming you have both baseline and treated plates and it is organized 
donor = 1083

for i,value in enumerate(all_plates_1083, start = 1):
  sig = pd.read_excel('/content/drive/MyDrive/plates/1083/' + value)
  adjusted_i = (i + 1) // 2 #integer division to iterate every two values
  plate_chemicals_var = globals()[f"plate_chemicals_{adjusted_i}"]

  group = ['treated','baseline'] #flipping them since we start at 1
  new_i = i % 2
  Group = group[new_i] #changes between baseline and treated
  File = []
  Dosage = ['100','10','1','0.1']
  Drugname_df = []
  Dose_df = []

  for i in range(4):
    Dose = Dosage[i]
    for x in range(0,22):
      chem = plate_chemicals_var[x] #this one
      additional_string = 'uM'
      concatenated_string = chem + '_' + Dosage[i] + additional_string
      File.append(concatenated_string)
      Drugname_df.append(chem)
      Dose_df.append(Dose)
  for i in range(22):
    File.append(control_groups[i])
    Drugname_df.append(control_names[i])
    Dose_df.append(control_dose[i])
  for i in range(4):
    Dose = Dosage[i]
    for x in range(22,44):
      chem = plate_chemicals_var[x] #this one
      additional_string = 'uM'
      concatenated_string = chem + '_' + Dosage[i] + additional_string
      File.append(concatenated_string)
      Drugname_df.append(chem)
      Dose_df.append(Dose)
  for i in range(22,44):
    File.append(control_groups[i])
    Drugname_df.append(control_names[i])
    Dose_df.append(control_dose[i])

  for x in range(44,65):
    chem = plate_chemicals_var[x] #this one
    additional_string = 'uM'
    concatenated_string = chem + '_' + Dosage[0] + additional_string
    File.append(concatenated_string)
    Drugname_df.append(chem)
    Dose_df.append(Dosage[0])

  File.append(control_groups[44])
  Drugname_df.append(control_names[44])
  Dose_df.append(control_dose[44])

  for x in range(44,65):
    chem = plate_chemicals_var[x] #this one
    additional_string = 'uM'
    concatenated_string = chem + '_' + Dosage[1] + additional_string
    File.append(concatenated_string)
    Drugname_df.append(chem)
    Dose_df.append(Dosage[1])

  File.append(control_groups[45])
  Drugname_df.append(control_names[45])
  Dose_df.append(control_dose[45])

  for x in range(44,65):
    chem = plate_chemicals_var[x] #this one
    additional_string = 'uM'
    concatenated_string = chem + '_' + Dosage[2] + additional_string
    File.append(concatenated_string)
    Drugname_df.append(chem)
    Dose_df.append(Dosage[2])

  File.append(control_groups[46])
  Drugname_df.append(control_names[46])
  Dose_df.append(control_dose[46])
  for x in range(44,65):
    chem = plate_chemicals_var[x] #this one
    additional_string = 'uM'
    concatenated_string = chem + '_' + Dosage[3] + additional_string
    File.append(concatenated_string)
    Drugname_df.append(chem)
    Dose_df.append(Dosage[3])

  File.append(control_groups[47])
  Drugname_df.append(control_names[47])
  Dose_df.append(control_dose[47])

  #make them into dataframes
  File = pd.DataFrame(File)
  Drugname_df = pd.DataFrame(Drugname_df)
  Dose_df = pd.DataFrame(Dose_df)

  data = sig.iloc[:,4:805]
  data.columns = data.columns[:1].tolist() + list(range(len(data.columns) - 1)) #renaming the signal

  y =  pd.concat([File,Drugname_df,Dose_df,filtered_df['Well']], axis=1)
  y.columns = ['File','Drugname','Dose','Well']
  y['Donor'] = donor
  y['Plate'] = adjusted_i
  y['Group'] = Group

  temp = y.merge(data, on='Well', how='inner')
  all_plate_signals = pd.concat([all_plate_signals,temp],axis=0)

#run for all donors and append to the all_plate_signals dataframe

donor = 1368

for i,value in enumerate(all_plates_1368, start = 1):
  sig = pd.read_excel('/content/drive/MyDrive/plates/1368/' + value)
  adjusted_i = (i + 1) // 2 #integer division to iterate every two values
  plate_chemicals_var = globals()[f"plate_chemicals_{adjusted_i}"]

  group = ['treated','baseline'] #flipping them since we start at 1
  new_i = i % 2
  Group = group[new_i] #changes between baseline and treated
  File = []
  Dosage = ['100','10','1','0.1']
  Drugname_df = []
  Dose_df = []

  for i in range(4):
    Dose = Dosage[i]
    for x in range(0,22):
      chem = plate_chemicals_var[x] #this one
      additional_string = 'uM'
      concatenated_string = chem + '_' + Dosage[i] + additional_string
      File.append(concatenated_string)
      Drugname_df.append(chem)
      Dose_df.append(Dose)
  for i in range(22):
    File.append(control_groups[i])
    Drugname_df.append(control_names[i])
    Dose_df.append(control_dose[i])
  for i in range(4):
    Dose = Dosage[i]
    for x in range(22,44):
      chem = plate_chemicals_var[x] #this one
      additional_string = 'uM'
      concatenated_string = chem + '_' + Dosage[i] + additional_string
      File.append(concatenated_string)
      Drugname_df.append(chem)
      Dose_df.append(Dose)
  for i in range(22,44):
    File.append(control_groups[i])
    Drugname_df.append(control_names[i])
    Dose_df.append(control_dose[i])

  for x in range(44,65):
    chem = plate_chemicals_var[x] #this one
    additional_string = 'uM'
    concatenated_string = chem + '_' + Dosage[0] + additional_string
    File.append(concatenated_string)
    Drugname_df.append(chem)
    Dose_df.append(Dosage[0])

  File.append(control_groups[44])
  Drugname_df.append(control_names[44])
  Dose_df.append(control_dose[44])

  for x in range(44,65):
    chem = plate_chemicals_var[x] #this one
    additional_string = 'uM'
    concatenated_string = chem + '_' + Dosage[1] + additional_string
    File.append(concatenated_string)
    Drugname_df.append(chem)
    Dose_df.append(Dosage[1])

  File.append(control_groups[45])
  Drugname_df.append(control_names[45])
  Dose_df.append(control_dose[45])

  for x in range(44,65):
    chem = plate_chemicals_var[x] #this one
    additional_string = 'uM'
    concatenated_string = chem + '_' + Dosage[2] + additional_string
    File.append(concatenated_string)
    Drugname_df.append(chem)
    Dose_df.append(Dosage[2])

  File.append(control_groups[46])
  Drugname_df.append(control_names[46])
  Dose_df.append(control_dose[46])
  for x in range(44,65):
    chem = plate_chemicals_var[x] #this one
    additional_string = 'uM'
    concatenated_string = chem + '_' + Dosage[3] + additional_string
    File.append(concatenated_string)
    Drugname_df.append(chem)
    Dose_df.append(Dosage[3])

  File.append(control_groups[47])
  Drugname_df.append(control_names[47])
  Dose_df.append(control_dose[47])

  #make them into dataframes
  File = pd.DataFrame(File)
  Drugname_df = pd.DataFrame(Drugname_df)
  Dose_df = pd.DataFrame(Dose_df)

  data = sig.iloc[:,4:805]
  data.columns = data.columns[:1].tolist() + list(range(len(data.columns) - 1)) #renaming the signal

  y =  pd.concat([File,Drugname_df,Dose_df,filtered_df['Well']], axis=1)
  y.columns = ['File','Drugname','Dose','Well']
  y['Donor'] = donor
  y['Plate'] = adjusted_i
  y['Group'] = Group

  temp = y.merge(data, on='Well', how='inner')
  all_plate_signals = pd.concat([all_plate_signals,temp],axis=0)

