# MQTT (Message Queuing Telemetry Transport)

[TOC]



## Res
🏠 https://mqtt.org

↗ [mosquitto](mosquitto/mosquitto.md)
↗ [paho mqtt](../../../../🔑%20CS_Core/👩‍💻%20Languages%20Programming/🛠️%20Programming%20Tools%20Chain/🚠%20Runtimes%20&%20SDKs/Python%20Runtimes%20Environments/Python%20Third-party%20Libs/Networking%20&%20Streaming/paho%20mqtt/paho%20mqtt.md)



## Intro
MQTT is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth. MQTT today is used in a wide variety of industries, such as automotive, manufacturing, telecommunications, oil and gas, etc.


### Publish/Subscribe
In this concept, a device publish a message on topics or it subscribes to topics to receive messages.

![](https://miro.medium.com/v2/resize:fit:1400/1*mjudWMsl1Zc04Idr_dK1Rg.png)
<small>Figure 1: Publish/Subscribe</small>

For example:
Client 1(Raspberry PI) publishes a message on the topic “home/server”. Client 2 (Windows Device) subscribed on the same topic. So that published message can be received by the client 2.


### Messages
These are the information exchanged between the clients.


### Topics
Topics are the interest of the clients on which they what to send or receive the message.

For Example:
In the Figure 1, Publish/Subscribe client 1 has interest in sending message on the topic “home/server” and client 2 has the interest on receiving message on that same topic.


### Broker
Broker is responsible for delivering messages between clients. Simply it acts like a postman. Unlike postman delivers the message to an address, broker deliver the messages on the basis of topics client are subscribed on.

![](https://miro.medium.com/v2/resize:fit:1400/1*Kq-4M1L0SaNfytokY1dDnQ.png)
<small>Broker Example</small>

For example:
Client 1 publishes three different messages on three different topics. These messages are received by the broker. Then Broker decides which client is interested on which topics and delivers the message to the clients on the basis of subscribed topics.

Broker are of two types Internal broker and External Broker (lets keep this broker for another day). Since we are interested in exchanging message within local network and for the sake of this tutorial we will only talk about internal broker. There are several brokers you can use. In our project we will use Mosquitto broker which will be installing in the Raspberry pi (it can installed on any of your devices).



## Ref
[MQTT | Wikipedia]: https://en.wikipedia.org/wiki/MQTT
[What is MQTT? | AWS]: https://aws.amazon.com/what-is/mqtt/
[MQTT Essentials]: https://www.hivemq.com/mqtt-essentials/

[👍  Stream live video from client to server using OpenCV and Paho-MQTT]: https://medium.com/@pritam.mondal.0711/stream-live-video-from-client-to-server-using-opencv-and-paho-mqtt-674d3327e8b3

[👍 How to install and use Mosquitto for Windows.pdf]: https://team-ethernet.github.io/guides/How%20to%20install%20and%20use%20Mosquitto%20for%20Windows.pdf

