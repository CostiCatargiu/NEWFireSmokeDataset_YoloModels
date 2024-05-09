import os, os.path
import shutil

# dataset_dir = '/home/constantin/Doctorat/FireDataset/DatasetAllTrainYOLOV8_deleteNULL/'
dataset_dir = '/home/constantin/Doctorat/FireDataset/RoboflowDS/yolov8/'

images_type = ['train','valid', 'test']
file_type = ['images', 'labels']

count = 0
fire = 0
other = 0
smoke = 0
null = 0
count_list = []
for img_typ in images_type:
    count_ = 0
    null_ = 0
    fire_ = 0
    other_ = 0
    smoke_ = 0
    for file_typ in file_type:
        if file_typ == 'images':
            image_source_path = dataset_dir + img_typ + '/' + file_typ + '/'
            images_names = os.listdir(image_source_path)
            for i in range(0, len(images_names)):
                count+=1
                count_+=1

        if file_typ == 'labels':
            labels_source_path = dataset_dir + img_typ + '/' + file_typ + '/'
            labels_names = os.listdir(labels_source_path)
            for i in range(0, len(labels_names)):
                original = labels_source_path + '/' + '{}'.format(labels_names[i])
                if os.path.getsize(original) == 0:
                    null+=1
                    null_+=1
                with open(original, 'r') as file:
                    line = file.readlines()
                # print(line)
                for l in line:
                    obj = l.split(" ")
                    # print("objo", obj[0])
                    if int(obj[0]) == 0:
                        fire+=1
                        fire_+=1
                    if int(obj[0]) == 1:
                        other+=1
                        other_+=1
                    if int(obj[0]) == 2:
                        smoke+=1
                        smoke_+=1

    count_list.append(count_)
    # print("Number of images in {img_typ} set is: {count}")
    print("-----------------------------------------------------------------------------------------------")
    print("Number of images in " + str(img_typ) + " set is: " + str(count_))
    print("Number of NULL images in " + str(img_typ) + " set is: " + str(null_))
    print("-----------------------------------------------------------------------------------------------")
    print("Number of FIRE instances in " + str(img_typ) + " set is: " + str(fire_))
    print("Number of OTHER instances in " + str(img_typ) + " set is: " + str(other_))
    print("Number of SMOKE instances in " + str(img_typ) + " set is: " + str(smoke_))
    print("-----------------------------------------------------------------------------------------------")

print('Number of fire instances:', fire)
print('Number of other instances:', other)
print('Number of smoke instances:', smoke)
print("-----------------------------------------------------------------------------------------------")

print('Number of images:', count)
print('Number of null images:', null)
print("-----------------------------------------------------------------------------------------------")

print(f"Proportion of images is: Train images:{(count_list[0]/count)*100:.2f}%")
print(f"Proportion of images is: Valid images:{(count_list[1]/count)*100:.2f}%")
print(f"Proportion of images is: Test images:{(count_list[2]/count)*100:.2f}%")