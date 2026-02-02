# IoT Integration

Recommended approach: MQTT + Home Assistant as the integration hub.

Device Model
- Devices expose capabilities (temperature control, on/off, preset)
- Adapter layer maps natural commands to device-specific payloads

Security
- Use TLS for MQTT (mqtts)
- Auth with username/password or client certificates
- Validate device capabilities before sending commands

Example MQTT topics
- `home/kitchen/oven/command` — payload: `{ "action": "set_temp", "value": 180 }`
- `home/kitchen/oven/state` — oven reports status

Home Assistant
- Integrate via MQTT discovery for many devices
- Use Home Assistant automations for complex workflows (preheat when timer starts)

Edge Cases
- Device offline: inform user and queue command or ask to retry
- Conflicting commands: ask for clarification before executing

Testing
- Simulate devices using `mosquitto_pub` in tests
- Add unit tests for adapter translation layer
