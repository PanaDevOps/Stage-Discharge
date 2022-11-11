import splitfolders

input_folder = 'Datasets'

splitfolders.ratio(input_folder, output='train_test_val_images', 
			seed=42, ratio=(.6,.2,.2),
			group_prefix=None)

splitfolders.fixed(input_folder, output='train_test_val_images',
			seed=42, fixed=(100,100),
			oversample=False, group_prefix=None)