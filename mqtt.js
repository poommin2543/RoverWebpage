const mqtt = require('mqtt');

// connection options
const connectionOptions = {
    protocol: "wss",
    host: "mqttt.noom.website",
    port: 0,
    endpoint: "/mqtt",
    clean: true,
    connectionTimeout: 20000,
    reconnectPeriod: 3000,
    clientId: "mx1000" + Math.random().toString(16).substring(2),
    username: "icsco",
    password: "icsco",
};

const { protocol, host, port, endpoint, ...options } = connectionOptions;
const connectUrl = `${protocol}://${host}:${port}${endpoint}`; // Fixed the syntax error here

// Create connection 
const client = mqtt.connect(connectUrl, options);

// Handle onConnect Event 
client.on('connect', () => {
    console.log("MQTT Service UP!");
    const topic = 'heartbeat/mx1000';
    const payload = 'UP!';
    // Send a message every second
    setInterval(function () {
        client.publish(topic, payload);
        console.log('Sent message to broker');
    }, 1000);

});

// Handle onConnection Error Event 
client.on('error', (err) => {
    console.log("MQTT service not initiate: ", err);
});
