import board
from adafruit_ht16k33.matrix import Matrix8x8x2

i2c = board.I2C()
matrix = Matrix8x8x2(i2c)

matrix.brightness = 0.5

matrix.fill(matrix.LED_YELLOW)

for x in range(8):
  matrix[x, 0] = matrix.LED_GREEN
  
for x in range(8):
  matrix[x, 7]= matrix.LED_GREEN
  
for y in range(8):
  matrix[0, y]= matrix.LED_GREEN
  
for y in range(8):
  matrix[7, y]= matrix.LED_GREEN


for y in range(4):
  matrix[2, y+2]= matrix.LED_RED


for y in range(4):
  matrix[5, y+2]= matrix.LED_RED


for x in range(4):
  matrix[x+2, 2]= matrix.LED_RED


for x in range(4):
  matrix[x+2, 5]= matrix.LED_RED


# matrix[3, 0] = matrix.LED_YELLOW
# matrix[4, 7] = matrix.LED_YELLOW
# matrix[7, 5] = matrix.LED_YELLOW
# matrix[7, 2] = matrix.LED_YELLOW

# matrix.shift(2, 0, True)	# loop pixels to the right by 2
# matrix.shift(-1, 0, True)	# loop pixels to the left by 1
# matrix.shift(0, -3, True)	# loop pixels down by 3
# matrix.shift(-2, 2, True)	# loop pixels left by 2 and up by 2