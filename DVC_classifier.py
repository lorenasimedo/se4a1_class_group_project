import pandas as pd
import os

def DVC_Classifier(sourceDirPath):
    
        
    relatedKeywords = ['.dvcignore','dvc.yaml']

    DVC_Related=[]
    Non_DVC_Related=[]


    for root, dirs, files in os.walk(sourceDirPath):
        for name in files:
            path = os.path.join(root, name)
            print(path)
            if '.X' in path:
                
                try:
                    with open(path, 'r') as openfile:
                        content = openfile.read()
                       
                        for keyword in relatedKeywords:
                            if keyword in content:
                                DVC_Related.append(path)
                            else:
                                Non_DVC_Related.append(path)
                except:
                    print('error reading file')


    save_path = "/Users/pouya/Desktop/DVC_Classifier/DVC"
    completeName = os.path.join(save_path, "DVC_Related")

    with open(completeName, 'w') as fp:
        for item in DVC_Related:
            fp.write("{}\n".format(item))
    fp.close()

    save_path = "/Users/pouya/Desktop/DVC_Classifier/DVC"
    completeName = os.path.join(save_path, "Non_DVC_Related")

    with open(completeName, 'w') as fp:
        for item in Non_DVC_Related:
            fp.write("{}\n".format(item))
    fp.close()


DVC_Classifier('DVC-Classifier')