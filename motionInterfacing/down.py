names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.162851, -0.162851, -0.162851, -0.162851])

names.append("HeadYaw")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0, 0, 0, 0])

names.append("LAnklePitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.0837433, 0.0837433, 0.0837433, 0.0837433])

names.append("LAnkleRoll")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.106134, -0.106134, -0.106134, -0.106134])

names.append("LElbowRoll")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.417977, -0.417977, -0.417977, -0.417977])

names.append("LElbowYaw")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-1.19838, -1.19838, -1.19838, -1.19838])

names.append("LHand")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.298236, 0.298236, 0.298236, 0.298236])

names.append("LHipPitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.122061, 0.122061, 0.122061, 0.122061])

names.append("LHipRoll")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.1141, 0.1141, 0.1141, 0.1141])

names.append("LHipYawPitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.16286, -0.16286, -0.16286, -0.16286])

names.append("LKneePitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.0884454, -0.0884454, -0.0884454, -0.0884454])

names.append("LShoulderPitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([1.43487, 1.43487, 1.42428, 1.41418])

names.append("LShoulderRoll")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.217731, 0.217731, 0.238831, 0.249193])

names.append("LWristYaw")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.0928923, 0.0928923, 0.0928923, 0.0928923])

names.append("RAnklePitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.0837432, 0.0837432, 0.0837432, 0.0837432])

names.append("RAnkleRoll")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.10613, 0.10613, 0.10613, 0.10613])

names.append("RElbowRoll")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.407253, 0.407253, 0.407253, 0.407253])

names.append("RElbowYaw")
times.append([0, 0.6, 1.8, 2.3])
keys.append([1.19838, 1.19838, 1.19838, 1.19838])

names.append("RHand")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.298236, 0.298236, 0.298236, 0.298236])

names.append("RHipPitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.122061, 0.122061, 0.122061, 0.122061])

names.append("RHipRoll")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.114094, -0.114094, -0.114094, -0.114094])

names.append("RHipYawPitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.16286, -0.16286, -0.16286, -0.16286])

names.append("RKneePitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.0884454, -0.0884454, -0.0884454, -0.0884454])

names.append("RShoulderPitch")
times.append([0, 0.6, 1.8, 2.3])
keys.append([0.177277, 1.50204, 0.339555, -0.0494412])

names.append("RShoulderRoll")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.373853, -0.338996, -0.347109, -0.348429])

names.append("RWristYaw")
times.append([0, 0.6, 1.8, 2.3])
keys.append([-0.833192, -0.833192, -0.833192, -0.833192])

f = open("deneme.motion", "w")
for x in names: 
	f.write(x + ",")
f.write("\n")
index = 0
for x in times[0]: 
	f.write(str(x) + ",Pose" + str(index+1) + ",") 
	for y in keys: 
		f.write(str(y[index]) + ",")
	index = index + 1 
	f.write("\n")
f.close()