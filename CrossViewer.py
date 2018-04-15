import png

# select the files to convert
name1 = raw_input("Enter the name of the front view png image: ")
idata1 = png.Reader(name1 + ".png").read()
name2 = raw_input("Enter the name of the right side view png image: ")
idata2 = png.Reader(name2 + ".png").read()
name3 = raw_input("Enter the name of the top view png image: ")
idata3 = png.Reader(name3 + ".png").read()
nameo = raw_input("Enter the name to output as: ")
vxl_file = open(nameo + ".txt", "w")
obj_file = open(nameo + ".obj", "w")
maxValue = input("Choose a maximum value (0-255) for thresholding: ")

# check that drawing dimensions are consistent
assert idata1[0] == idata3[0], "x dimensions are not consistent"
assert idata1[1] == idata2[1], "z dimensions are not consistent"
assert idata2[0] == idata3[1], "y dimensions are not consistent"
print "Dimensions are consistent."

# threshold images (screw opencv I dont need them)
thresh1 = []
for row in idata1[2]:
	prow = []
	i = 0
	while i < len(row):
		if (row[i] <= maxValue or row[i + 1] <= maxValue or row[i + 2] <= maxValue):
			prow.append(True)
		else:
			prow.append(False)
		i += 3
	thresh1.append(prow)
print "Done thresholding front view."

thresh2 = []
for row in idata2[2]:
	prow = []
	i = 0
	while i < len(row):
		if (row[i] <= maxValue or row[i + 1] <= maxValue or row[i + 2] <= maxValue):
			prow.append(True)
		else:
			prow.append(False)
		i += 3
	thresh2.append(prow)
print "Done thresholding right side view."

thresh3 = []
for row in idata3[2]:
	prow = []
	i = 0
	while i < len(row):
		if (row[i] <= maxValue or row[i + 1] <= maxValue or row[i + 2] <= maxValue):
			prow.append(True)
		else:
			prow.append(False)
		i += 3
	thresh3.append(prow)
print "Done thresholding top view."

# write voxels into a list (slightly more optimal than running the other 2 programs separately)
blocks = []
for i in range(idata1[0]):
	for j in range(idata3[1]):
		for k in range(idata1[1]):
			if (thresh1[k][i] and thresh2[k][-j - 1] and thresh3[j][i]):
				vxl_file.write(str(i) + " " + str(-k - 1) + " " + str(j) +  "\n")
				blocks.append([i, -k - 1, j])
print "Done creating voxel list."

vxl_file.close()

# write vertices of each voxel in output file
for b in blocks:
	x1 = str(b[0])
	y1 = str(b[1])
	z1 = str(b[2])
	x2 = str(b[0] + 1)
	y2 = str(b[1] + 1)
	z2 = str(b[2] + 1)
	obj_file.write("v " + x1 + " " + y1 + " " + z1 + "\n")
	obj_file.write("v " + x2 + " " + y1 + " " + z1 + "\n")
	obj_file.write("v " + x1 + " " + y2+ " " + z1 + "\n")
	obj_file.write("v " + x1 + " " + y1 + " " + z2 + "\n")
	obj_file.write("v " + x1 + " " + y2 + " " + z2 + "\n")
	obj_file.write("v " + x2 + " " + y1 + " " + z2 + "\n")
	obj_file.write("v " + x2 + " " + y2 + " " + z1 + "\n")
	obj_file.write("v " + x2 + " " + y2 + " " + z2 + "\n")

# write faces of each voxel in output file
for i in range(len(blocks)):
	vtx = [str(j) for j in range(8 * i + 1, 8 * i + 9)]
	obj_file.write("f " + vtx[0] + " " + vtx[1] + " " + vtx[5] + " " + vtx[3] + "\n")
	obj_file.write("f " + vtx[0] + " " + vtx[3] + " " + vtx[4] + " " + vtx[2] + "\n")
	obj_file.write("f " + vtx[0] + " " + vtx[1] + " " + vtx[6] + " " + vtx[2] + "\n")
	obj_file.write("f " + vtx[7] + " " + vtx[5] + " " + vtx[3] + " " + vtx[4] + "\n")
	obj_file.write("f " + vtx[7] + " " + vtx[5] + " " + vtx[1] + " " + vtx[6] + "\n")
	obj_file.write("f " + vtx[7] + " " + vtx[4] + " " + vtx[2] + " " + vtx[6] + "\n")

obj_file.close()
print "Done!"
