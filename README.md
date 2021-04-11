# BLE2WebSocket
A browser-based WebBluetooth to WebSocket relay/getawey for devices supporting [*Nordic UART Service*](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/include/bluetooth/services/nus.html), Circuitpython in particular

This [Application is running here](https://tasm-devil.github.io/BLE2WebSocket/). Try it out!

It was designed primarily for use with [Circuitpython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython). Use [this repository](https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT) as a Starting Point.

Secure WebSocket is necessary if you run this on a https server like github.io

## Enable web-bluetooth in google chrome

Read [this article](https://github.com/WebBluetoothCG/web-bluetooth/blob/master/implementation-status.md) for getting infos on how to enable web-bluetooth in google chrome or simply open `chrome://flags/#enable-experimental-web-platform-features` and choose *Enabled*.

## Mosquitto setup
This is the perfect [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-18-04-quickstart) how to setup mosquitto with wss and certbot (*Let's Encrypt*)

## Roadmap
- Make a [Webcomponent](https://www.webcomponents.org/) out of this relay
- Rewrite and extend the GUI, using [ELM](https://elm-lang.org/).

## Contributions
Are welcome!

## License 
MIT

