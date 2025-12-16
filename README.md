# Multilingual Speech-to-Text Recognition System

This project presents a multilingual speech-to-text system capable of recognizing English, Hindi, and Marathi speech in real time on low-cost embedded hardware.

The system is designed to work in both online and offline modes, making it suitable for environments with unstable or limited internet connectivity.

## Project Overview

Most existing speech-to-text systems rely heavily on cloud computing or high-performance hardware.  
This project addresses that limitation by implementing a lightweight, hybrid speech recognition system on a Raspberry Pi platform.

Key highlights:
- Multilingual support: English, Hindi, Marathi
- Runs on Raspberry Pi
- Hybrid recognition (Online and Offline)
- Real-time transcription
- Low cost and portable

## Technologies Used

- Python
- Google Speech Recognition API (Online mode)
- Offline speech recognizer (Whisper-small)
- MFCC (Mel Frequency Cepstral Coefficients)
- Raspberry Pi 4B
- USB Microphone
- 16x2 I2C LCD
- RealVNC for Devanagari script display

## System Architecture

1. Audio is captured using a microphone connected to Raspberry Pi  
2. Noise reduction and silence trimming are applied  
3. MFCC features are extracted  
4. Language is selected by the user  
5. Recognition mode selection:
   - Online: Google Speech Recognition API
   - Offline: Local speech recognition model  
6. Output display:
   - English output on LCD
   - Hindi and Marathi output on laptop using VNC

## Languages Supported

| Language |    Mode            | Display      |
| English  | Online and Offline | LCD          |
| Hindi    | Online and Offline | Laptop (VNC) |
| Marathi  | Online and Offline | Laptop (VNC) |

## Performance Summary

- English accuracy approximately 92 percent
- Hindi accuracy approximately 89 percent
- Marathi accuracy approximately 88 percent
- Real-time response on Raspberry Pi
- Functional under mild noise conditions

## Applications

- Classroom transcription
- Assistive technology
- Low-resource and rural environments
- Embedded speech-based interfaces

## Academic Context

This project was developed as an academic project in the  
Department of Electronics and Telecommunication Engineering,  
Vishwakarma Institute of Technology, Pune.

## Future Work

- Improved noise robustness
- Addition of more languages
- Conversion of languages
- Enhanced offline accuracy for Indian languages
- Optimized feature extraction for lower latency
- Full Devanagari display support on embedded screens


