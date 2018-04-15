CrossViewer
===========
Convert a 3-view drawing into a 3D model
----------------------------------------

### Input:
* 3 .png images showing the front, right side, and top views of the object
  * Images must have consistent dimensions (i.e. If your front image is 32x64, your side image must have a height of 64, and your top image must have a width of 32.)
  * Images should be fairly low-resolution (Recommended maximum is 256 pixels on each side.)

### Output:
* 1 .txt file describing the voxels (See format specification file in this repository.)
* 1 .obj file 3D model of the object

### How To Use:
* Run CrossViewer.py.
* Enter the names of your 3 image files (without the ".png").
* Enter the name you want the output to be saved under (without the ".txt" or ".obj").
* Enter a maximum threshold value. Any pixel in the images which has at least one RGB value less than or equal to this value will be considered part of the object.
* Allow it to run. This may take a few seconds depending on the size of the images.
* When the program prints "Done!" the .obj file has been successfully created.
