from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt

BattleTime = 30

class MachineGun:
    HPS = 20
    CPS = 15
    SPS = 15
    JT  = 2


class RocketLauncher:
    MC  = 5
    TTZ = 0
    TTS = 0
    TTR = 2
    CycleTime = (MC - 1) * TTS + TTR


class Cannon:
    MC  = 5
    TTZ = 2
    TTS = 2
    TTR = 2
    CycleTime = MC * TTZ + (MC - 1) * TTS +  TTR

MG = MachineGun()
RL = RocketLauncher()
CN = Cannon()

CurrentHeat = 0.0
ShootingTime = 0.0
CoolingTime = 0.0
T = 0
log = []

while T < 10000:
    log.append(CurrentHeat)
    ShootingFor = ((100 - CurrentHeat) / MG.HPS) * beta.rvs(8, 3)
    ShootingTime += ShootingFor
    CurrentHeat += ShootingFor * MG.HPS
    CoolingFor = (CurrentHeat / MG.CPS ) * beta.rvs(3, 8)
    CoolingTime += CoolingFor
    CurrentHeat -= CoolingFor * MG.CPS
    T += 1

print(ShootingTime)
print(CoolingTime)
print(ShootingTime/CoolingTime)

#plt.plot(log)
#plt.show()


def log(level, message):
    print "[{level}]: {msg}".format(level=level, msg=message)                   

log("debug", "Start doing something")
log("debug", "Continue with something else")
log("debug", "Finished. Profit?")

def debug(message):
    log("debug", message)