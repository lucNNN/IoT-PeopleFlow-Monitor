# IoT-PeopleFlow-Monitor
People flow detection system using WiFi Probe Request frames and ESP32 microcontrollers. Captures MAC addresses in promiscuous mode, filters duplicates, and estimates human presence over time.

## 👥 Team members
- Frank Zhang
- Lucien Chen

## 🛠️ Hardware Setup 
- **Sniffer**: ESP32C3 (captures Probe Requests)  
- **Processor**: ESP32S3 (filters MAC addresses & uploads data)  
- **Communication**: UART serial (115200 baud)
<img width="536" height="365" alt="7e92e99a828adc6ba3fa8209726dec0" src="https://github.com/user-attachments/assets/15994e63-3be5-44b6-a0fe-76c397c9e02d" />

## 📡 How It Works  
1. Mobile devices broadcast `Probe Request` frames (IEEE 802.11)  
2. ESP32C3 in promiscuous mode captures MAC addresses  
3. ESP32S3 deduplicates MACs and counts unique devices  
4. Data sent to cloud via MQTT (OneNET)  

## 📊 My Contributions  
- Led field deployment at SAST 
- Validated 92.5% accuracy by manual traffic counting  
- Authored cost-benefit analysis report
[Embedded System Design Course Project.pdf]
[Embedded System Design Course Project.pdf](https://github.com/user-attachments/files/21460189/Embedded.System.Design.Course.Project.pdf)


