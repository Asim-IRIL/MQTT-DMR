MQTT-DMR

MQTT API on Paho with independent Broker (on Windows) and co-located MQTT Clients (on LinuxMint)

Implementation of MQTT API for Data Management and Repository
MQTT Broker is running on separate local machine (192.168.0.113) using MS Windows.
Two MQTT Clients, as Subscribe and Publish modules, are running on a Linux Local Machine (192.168.0.125) which is Publishing values to be stored in the Database and also subscribed to that specific topic and storing it to the Database.
The Database is also located on the same Linux Local Machine
SQLite3 is used to keep the database light weight.
In addition, the stored values can also be viewed in GUI too.
Using this scenario the HTTP API can be totally removed from the current working scenario of DMR.
