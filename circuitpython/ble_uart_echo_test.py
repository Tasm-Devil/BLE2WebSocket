# Schreibe hier Deinen Code :-)
from adafruit_ble.uart import UARTServer
from mqtt import MQTTClient
from time import sleep

uart = UARTServer()

# Subscribed messages will be delivered to this callback
def sub_cb(topic, msg):
    print("received",topic, msg)

c = MQTTClient(uart)
c.set_callback(sub_cb)

while True:
    uart.start_advertising()
    # Wait for a connection
    while not uart.connected:
        pass
    i = 0
    if uart.connected:
        sleep(2)
        print("sub", '/nrf/#')
        c.subscribe('/nrf/#')
    while uart.connected:
        try:
            c.check_msg()
            if i % 5 == 0:
                print("pub", '/nrf/temp',str(i))
                c.publish('/nrf/temp',str(i))
            i = i + 1
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            sleep(1)
        except OSError as err:
            print("OS error: {0}".format(err))
    # When disconnected, arrive here. Go back to the top
    # and start advertising again.