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
maxValue = input("Choose a maximum value (0-255) for thresholding: ")

# check that drawing dimensions are consistent
assert idata1[0] == idata3[0], "x dimensions are not consistent"
assert idata1[1] == idata2[1], "z dimensions are not consistent"
assert idata2[0] == idata3[1], "y dimensions are not consistent"

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

# write voxels into the file
for i in range(idata1[0]):
	for j in range(idata3[1]):
		for k in range(idata1[1]):
			if (thresh1[k][i] and thresh2[k][-j - 1] and thresh3[j][i]):
				vxl_file.write(str(i) + " " + str(-k - 1) + " " + str(j) +  "\n")

vxl_file.close()