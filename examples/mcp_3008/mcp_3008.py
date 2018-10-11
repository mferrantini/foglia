import time

import Adafruit_MCP3008.MCP3008 as MCP3008

# SPI Port and device id
# Note: SPI must be enabled on rPi
SPI_PORT = 0
SPI_DEVICE = 0

# MCP3008 Setup
mcp = MCP3008(spi = SPI.SpiDev(SPI_PORT, SPI_DEVICE))

while True:
    # Read the analog input on the MCP3008 first input
    value_1 = mcp.read_adc(0)

    # Five seconds between each reading
    time.sleep(5)