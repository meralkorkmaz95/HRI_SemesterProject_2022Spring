# Choregraphe simplified export in Python.
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-0.167011, -0.167011, -0.167011, -0.167011])

names.append("HeadYaw")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0, 0, 0, 0])

names.append("LAnklePitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.0799593, 0.0799593, 0.0799593, 0.0799593])

names.append("LAnkleRoll")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-0.101338, -0.101338, -0.101338, -0.101338])

names.append("LElbowRoll")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-0.412733, -0.412733, -0.412733, -0.412733])

names.append("LElbowYaw")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-1.20194, -1.20194, -1.20194, -1.20194])

names.append("LHand")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.297266, 0.297266, 0.297266, 0.297266])

names.append("LHipPitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.12667, 0.12667, 0.12667, 0.12667])

names.append("LHipRoll")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.119064, 0.119064, 0.119064, 0.119064])

names.append("LHipYawPitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-0.16702, -0.16702, -0.16702, -0.16702])

names.append("LKneePitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-0.0844489, -0.0844489, -0.0844489, -0.0844489])

names.append("LShoulderPitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([1.42726, 1.43748, 1.41717, 1.41702])

names.append("LShoulderRoll")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.235185, 0.219808, 0.245064, 0.255514])

names.append("LWristYaw")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.0989375, 0.0989375, 0.0989375, 0.0989375])

names.append("RAnklePitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.0799592, 0.0799592, 0.0799592, 0.0799592])

names.append("RAnkleRoll")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.101335, 0.101335, 0.101335, 0.101335])

names.append("RElbowRoll")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.309634, 0.309634, 0.309634, 0.309634])

names.append("RElbowYaw")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([1.02131, 1.02131, 1.02131, 1.02131])

names.append("RHand")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.297266, 0.297266, 0.297266, 0.297266])

names.append("RHipPitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.12667, 0.12667, 0.12667, 0.12667])

names.append("RHipRoll")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-0.119058, -0.119058, -0.119058, -0.119058])

names.append("RHipYawPitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-0.16702, -0.16702, -0.16702, -0.16702])

names.append("RKneePitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-0.0844489, -0.0844489, -0.0844489, -0.0844489])

names.append("RShoulderPitch")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([0.42117, -0.789286, -1.33037, 0.449851])

names.append("RShoulderRoll")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-0.35938, -0.227031, -0.233035, -0.233035])

names.append("RWristYaw")
times.append([0, 0.233333, 0.466667, 1.03333])
keys.append([-1.10782, -1.10782, -1.10782, -1.10782])


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
