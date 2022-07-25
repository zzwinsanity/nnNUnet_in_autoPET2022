import os
import shutil
import string

data_dir = '/autofs/vast/MK6240/CanonicalData/kuang/autoPET2022/FDG-PET-CT-Lesions/'
destination_imageTr_dir = '/autofs/vast/MK6240/CanonicalData/kuang/ziwei/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task59_autoPET/imageTr'
destination_labelTr_dir = '/autofs/vast/MK6240/CanonicalData/kuang/ziwei/nnUNetFrame/DATASET/nnUNet_raw/nnUNet_raw_data/Task59_autoPET/labelsTr'


#access all the subfolders in the directory
patient_num = 0
for sub_folder in os.listdir(data_dir):
        print(sub_folder)
        #extract case name from each subfolder name
        subFolder_name = sub_folder.strip().split('_')[1]
        # print(subFolder_name)

        for file in os.listdir(data_dir+'PETCT_'+subFolder_name):
                print(file)
                patient_num += 1 
                for image in os.listdir(data_dir+'PETCT_'+subFolder_name+'/'+file):
                        # print(image)
                    
                    imageName = image.strip().split('.')[0]
                        # print(imageName)
                    if imageName == 'SUV':
                           
                        patient_image_num_zfilled = 'autoPET_' + str(patient_num).zfill(4) + '_0000' + '.nii.gz'
                        print(patient_image_num_zfilled)
                        # shutil.copyfile(os.path.join(data_dir+'PETCT_'+subFolder_name+'/'+file,str(image)), os.path.join(destination_imageTr_dir,patient_image_num_zfilled))
                        shutil.copyfile(os.path.join(data_dir+'PETCT_'+subFolder_name+'/'+file,str(image)), os.path.join(destination_imageTr_dir,patient_image_num_zfilled))
                    if imageName == 'SEG':
                        
                        patient_label_num_zfilled = 'autoPET_' + str(patient_num).zfill(4) + '.nii.gz'
                        print(patient_label_num_zfilled)
                        shutil.copyfile(os.path.join(data_dir+'PETCT_'+subFolder_name+'/'+file,str(image)), os.path.join(destination_labelTr_dir,patient_label_num_zfilled))
                        
        # if patient_num == 900:

            # break

                    
                            
                                #move the file to its destination directory
#               new_Image_name = imageName + 'count' +  '0000' + '.nii.gz'
#               new_Label_name = imageName + 'count' +'nii.gz'

#               count = 000 

                #cp data_dir+'PETCT_'+subFolder_name/file destination_dir+new_fileName

#               cp
#               cp 
                       