import time
import board
import analogio

piezo = analogio.AnalogIn(board.A1)

lastVoltage = 0.0
checkDelaySeconds = 0.001

while True:
    currentVoltage = piezo.value / 65536
    # print("(", currentVoltage, ")")
    if (currentVoltage > 0.15):
        print("Hit!")
        while (currentVoltage > 0.15):
            print("(", currentVoltage, ")")
            currentVoltage = piezo.value / 65536
            time.sleep(checkDelaySeconds)
        print("Stop Hit!")
        print("( 0 )")
        print("( 0 )")
        print("( 0 )")
    time.sleep(checkDelaySeconds)
