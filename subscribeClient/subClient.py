# Import the AWS IoT SDK for Python
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Define the client ID, host, port, and credentials
client_id = "your_client_id"
host = "your_host"
port = 443 # Use port 443 for WebSocket connection
root_ca = "path_to_root_ca"
private_key = "path_to_private_key"
certificate = "path_to_certificate"

# Create an AWS IoT MQTT Client object
client = AWSIoTMQTTClient(client_id, useWebsocket=True)

# Configure the endpoint, port, and credentials
client.configureEndpoint(host, port)
client.configureCredentials(root_ca, private_key, certificate)

# Configure other connection parameters
client.configureAutoReconnectBackoffTime(1, 32, 20)
client.configureOfflinePublishQueueing(-1)
client.configureDrainingFrequency(2)
client.configureConnectDisconnectTimeout(10)
client.configureMQTTOperationTimeout(5)

# Define a callback function to handle incoming messages
def message_callback(client, userdata, message):
    print("Received a message on topic %s: %s\n" % (message.topic, message.payload))

# Connect to the AWS IoT platform
client.connect()

# Subscribe to a topic of your choice
topic = "your_topic"
client.subscribe(topic, 1, message_callback)

# Keep the program running and wait for messages
while True:
    pass
