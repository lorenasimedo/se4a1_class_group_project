import json
import os
import requests


dataset_url = "https://github.com/lorenasimedo/se4a1_class_group_project/tree/main/data"
data = requests.get(dataset_url)
print(data)

DVC_related=[]
Non_DVC_related=[]

file_lst=['Search','deepicedrain','crop-mask','dna-seq','gmt','processing','pygmt','rootski']

for file in file_lst:
  with open(file) as f:
    data = json.load(f)

  for key, value in data.items():
      print("key:", key)
      var=key
      flag=False
      inter_dic=value
      for key, value in inter_dic.items():
          if key=='modified_files':
              inter_list=value
              for dic in inter_list:
                  for key, value in dic.items():
                      try:
                          if key=="new_path":
                              if "dvc" in value.lower():
                                  print("value++++++++++",value)
                                  flag=True
                      except:
                          print("error reading new_path")
      
      if flag==True:
          DVC_related.append([var,file])
      else:
          Non_DVC_related.append([var,file])
print("DVC_related:",DVC_related)
print("Non_DVC_related",Non_DVC_related)

save_path="/Users/pouya/Desktop/DVCC"
completeName = os.path.join(save_path, "output_DVC_related_commits")
with open (completeName, 'w') as f:
    for item in DVC_related:
        for index,i in enumerate(item):
            f.write(i)
            if(index==0):
                f.write(',')
        f.write("\n")
completeName = os.path.join(save_path, "output_Non_DVC_related_commits")

with open (completeName, 'w') as fp:

    for item in Non_DVC_related:
        for index,i in enumerate(item):
            fp.write(i)
            if(index==0):
                fp.write(',')
        fp.write("\n")
