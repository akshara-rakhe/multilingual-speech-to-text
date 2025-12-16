Hardware Setup

The multilingual speech-to-text system is implemented on a Raspberry Pi based embedded platform to ensure portability and low cost.

Components Used
- Raspberry Pi 4B
- USB Microphone for audio input
- 16x2 I2C LCD for text display
- Laptop system accessed via RealVNC for Devanagari script output
- Power supply and basic peripherals

Hardware Functionality
- The microphone captures real-time speech input
- Raspberry Pi performs preprocessing and speech recognition
- English output is displayed directly on the LCD
- Hindi and Marathi output are displayed on a connected laptop using VNC due to font rendering constraints

This hardware configuration enables real-time multilingual speech recognition in resource-constrained environments.
