''' 

Renames the downloaded images folderwise giving them the name of the city and a serial number: e.g. city01.tif
Changes the name directly inside the existing folder, no new folders are created.

'''

import os

def rename(path):
    folder = os.listdir(path) # list of folders inside tif i.e. city named folders

    for i in range(len(folder)):
        #print(folder[i]) # folder with city name
        city_name = folder[i]
        #print(city_name)
        city_fold = os.path.join(path, folder[i])
        #print(city_fold) # path till folder with city name
        count = 1
        for file_name in os.listdir(city_fold):
            #print(file_name) 
            old = os.path.join(city_fold, file_name)
            new = os.path.join(city_fold, '{}{}.tif'.format(city_name, count))
            if os.path.isfile(new):
                continue
            else:
                os.rename(old,new)
            count += 1

def main():
    new_name = rename('data/images')
    
if __name__ == "__main__":
    main()
