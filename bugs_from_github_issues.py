import json
import os

with open('bugs_from_github_issues.json') as f:
   data = json.load(f)

DVC_related=[]
Non_DVC_related=[]
for key, value in data.items():
    print("key:", key)
    var=key
    flag=False
    inter_dic=value
    for key, value in inter_dic.items():
        if key=='modified_files':
            inter_list=value
            for item in inter_list:
                    try:
                        if "dvc" in item:
                            flag=True
                    except:
                        print("error reading new_path")
    
    if flag==True:
        DVC_related.append(var)
    else:
        Non_DVC_related.append(var)
print("DVC_related:",DVC_related)
print("Non_DVC_related",Non_DVC_related)


save_path="/Users/pouya/Desktop/DVCC"
completeName = os.path.join(save_path, "output_DVC_related_issues")
with open (completeName, 'w') as f:
    for item in DVC_related:
        f.write(item)
        f.write(",")
        f.write("\n")
completeName = os.path.join(save_path, "output_Non_DVC_related_issues")

with open (completeName, 'w') as fp:

    for item in Non_DVC_related:
        fp.write(item)
        fp.write(",")
        fp.write("\n")
