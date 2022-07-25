# nnNUnet_in_autoPET2022
nnunet_in_autoPET2022


2 model_weight_file
CT is preprocessed & train by CT's way
non CT is preprocessed & train by nonCT's way


according to paper:
n Because the intensity scale of CT scans is absolute, all CT
images are automatically normalized based on statistics of the entire respective
dataset: If the modality description in a dataset’s corresponding json desccriptor
file indicates ‘ct’, all intensity values occurring within the segmentation masks
of the training dataset are collected and the entire dataset is normalized by
clipping to the [0.5, 99.5] percentiles of these intensity values, followed by 
a zscore normalization based on the mean and standard deviation of all collected
intensity values. For MRI or other image modalities (i.e. if no ‘ct’ string is
found in the modality), simple z-score normalization is applied to the patient
individually.
If cropping reduces the average size of patients in a dataset (in voxels) by
1/4 or more the normalization is carried out only within the mask of nonzero
elements and all values outside the mask are set to 0.
