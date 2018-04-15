# select the file to convert
name = raw_input("Enter the name of the txt file to convert: ")
vxl_file = open(name + ".txt", "r")
obj_file = open(name + ".obj", "w")

# create voxel list from the txt file
blocks = []
for line in vxl_file:
	blocks.append([int(i) for i in line.split()])

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
