# nnNUnet_in_autoPET2022
nnunet_in_autoPET2022

'''
Use original nnU-Net code to train the NiFTI data:(http://www.midaslab.org/autoPET/data/nifti.zip) for the https://autopet.grand-challenge.org 


When train or test for this dataset, the input PET images have to use the nii.gz format and order by xxx_000_0000.nii.gz . 

'''


way to predict:

1. set nnunet_base path

.bashrc
add:
export nnUNet_raw_data_base="/home/nnunet_base/nnUNet_raw"
export nnUNet_preprocessed="/home/nnunet_base/nnUNet_preprocessed"
export RESULTS_FOLDER="/home/nnunet_base/nnUNet_trained_models"

source .bashrc


2. prepare/order test images with name_xxx_0000.nii.gz  e.g autoPET_001_0000.nii.gz 

3. put model file in nnunet_base/nnUNet_trained_models/nnUNet/3d_fullres/Task_000/nnUNetTrainerV2__nnUNetPlansv2.1/fold_x/


4. pip install nnunet
5. pip install -r requirements.txt
6. nnUNet_predict -i (test images path) -o (output path) -t001 -m 3d_fullres -f x
