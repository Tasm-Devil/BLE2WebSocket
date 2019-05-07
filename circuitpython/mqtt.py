class MQTTException(Exception):
    pass

class MQTTClient:

    def __init__(self, uartServer):
        self.uartServer = uartServer

    def _send_str(self, s):
        self.uartServer.write(s)

#    def _recv_len(self):
#        pass

    def set_callback(self, f):
        self.cb = f

#    def set_last_will(self, topic, msg):
#        pass

#    def connect(self):
#        pass

#    def disconnect(self):
#        pass

#    def ping(self):
#        pass

    def publish(self, topic, msg):
        string = "pub " + topic + "," + msg
        self._send_str(string + "\n")

    def subscribe(self, topic, qos=0):
        string = "sub " + topic
        self._send_str(string + "\n")

    # Wait for a single incoming MQTT message and process it.
    # Subscribed messages are delivered to a callback previously
    # set by .set_callback() method. Other (internal) MQTT
    # messages processed internally.
#    def wait_msg(self):
#        pass

    # Checks whether a pending message from server is available.
    # If not, returns immediately with None. Otherwise, does
    # the same processing as wait_msg.
    def check_msg(self):
        if (self.uartServer.in_waiting > 0):
            # readline returns b'' if nothing was read.
            pre = self.uartServer.read(4)
            if (pre == b'msg '):
                msg = self.uartServer.readline().decode('UTF-8')[0:-1] # remove "\n"
                self.cb(*msg.split(","))