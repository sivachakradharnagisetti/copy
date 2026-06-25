<div align="center">

<!-- ANIMATED HERO BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=300&section=header&text=AI%20Sign-to-Speech&fontSize=60&fontColor=fff&animation=twinkling&fontAlignY=35&desc=🤟%20Indian%20Sign%20Language%20→%20Real-Time%20Speech%20on%20Raspberry%20Pi&descAlignY=55&descSize=18" width="100%"/>

<!-- ANIMATED TYPING EFFECT -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=500&color=00D9FF&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=80&lines=🤖+Real-Time+Embedded+AI+System;🖐️+Indian+Sign+Language+Recognition;🔊+Offline+Text-to-Speech+on+Raspberry+Pi" alt="Typing SVG" />
</a>

<br/>

<!-- VISITOR COUNTER -->
<img src="https://komarev.com/ghpvc/?username=sivanagisetti&label=Repository+Visitors&color=0e75b6&style=for-the-badge" alt="Visitors"/>

<br/><br/>

<!-- BADGES ROW 1 -->
<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow_Lite-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/MediaPipe-00C853?style=for-the-badge&logo=google&logoColor=white"/>

<br/>

<!-- BADGES ROW 2 -->
<img src="https://img.shields.io/badge/Raspberry_Pi-C51A4A?style=for-the-badge&logo=raspberry-pi&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Accuracy-~93%25-brightgreen?style=for-the-badge"/>

<br/>

<!-- BADGES ROW 3 -->
<img src="https://img.shields.io/badge/Platform-Raspberry%20Pi%203B+-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Inference-Real--Time-blue?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Mode-Offline-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Last%20Updated-June%202025-informational?style=for-the-badge"/>

</div>

---

<div align="center">

## 🌟 Project at a Glance

| 🎯 Purpose | 🖥️ Platform | 🧠 AI Model | 🔊 Output |
|:---:|:---:|:---:|:---:|
| ISL → Speech Conversion | Raspberry Pi 3B+ | TFLite + Random Forest | Offline TTS |
| **Accuracy** | **FPS** | **Latency** | **Mode** |
| ~93% | 15-20 FPS | <200ms | Fully Offline |

</div>

---

## 📋 Table of Contents

<details open>
<summary><b>Click to expand / collapse</b></summary>

- [🌟 Project Overview](#-project-overview)
- [🎯 Problem Statement](#-problem-statement)
- [🚀 Features](#-features)
- [🏗️ System Architecture](#%EF%B8%8F-system-architecture)
- [🔄 Complete Workflow](#-complete-workflow)
- [🤖 AI Pipeline](#-ai-pipeline)
- [🖥️ Hardware Setup](#%EF%B8%8F-hardware-setup)
- [💻 Software Stack](#-software-stack)
- [📊 Dataset & Preprocessing](#-dataset--preprocessing)
- [🧠 Model Details](#-model-details)
- [📸 Screenshots & Demo](#-screenshots--demo)
- [⚡ Quick Start](#-quick-start)
- [🔧 Installation Guide](#-installation-guide)
- [▶️ Running the Project](#%EF%B8%8F-running-the-project)
- [📈 Performance Metrics](#-performance-metrics)
- [📁 Project Structure](#-project-structure)
- [🗺️ Roadmap](#%EF%B8%8F-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👤 Author](#-author)
- [📚 References](#-references)

</details>

---

## 🌟 Project Overview

<div align="center">

> *"Empowering the deaf and speech-impaired community through real-time AI"*

</div>

**AI-Powered Sign-to-Speech Conversion** is a fully embedded, offline AI system built on **Raspberry Pi 3B+** that translates **Indian Sign Language (ISL)** hand gestures into **audible speech** in real time — no cloud, no internet, no interpreters needed.

The system uses **MediaPipe Hands** to extract 21 3D hand landmarks from camera input, feeds them into a **TensorFlow Lite / Random Forest classifier** trained on custom ISL gesture data, and converts predictions to natural speech using **pyttsx3/eSpeak**.

<div align="center">

| Target Users | Use Cases |
|:---|:---|
| 🏥 Hearing-impaired individuals | Hospital communication |
| 🗣️ Speech-impaired individuals | School accessibility |
| 🏫 Special education teachers | Public service centers |
| 👨‍💻 Assistive technology researchers | Smart home interaction |

</div>

---

## 🎯 Problem Statement

<table>
<tr>
<td width="50%">

### ❌ The Challenge
- **63 million** hearing-impaired people in India alone
- Sign language is unknown to most of the general public
- **Lack of interpreters** in hospitals, schools, and public offices
- Existing solutions are either expensive glove-based hardware or require cloud connectivity
- Communication barrier leads to **social isolation** and limited opportunities

</td>
<td width="50%">

### ✅ Our Solution
- **Camera-based** — no special hardware gloves needed
- **Fully offline** — works without internet
- **Portable** — runs on a ₹3,000 Raspberry Pi
- **Real-time** — <200ms gesture-to-speech latency
- **Open-source** — freely available for everyone

</td>
</tr>
</table>

---

## 🚀 Features

<div align="center">

```
┌─────────────────────────────────────────────────────────────────┐
│                    🌟 CORE FEATURES                              │
├─────────────────────┬───────────────────────────────────────────┤
│ 🤖 Real-time AI     │ Live gesture recognition at 15-20 FPS     │
│ 🔌 Fully Offline    │ No internet or cloud required             │
│ ⚡ Low Latency      │ End-to-end <200ms response time           │
│ 📦 Portable         │ Runs on Raspberry Pi 3B+                  │
│ 🎯 High Accuracy    │ ~93% gesture recognition accuracy         │
│ 🔊 Natural Speech   │ eSpeak/pyttsx3 offline TTS                │
│ 🖐️ 21 Landmarks     │ Full hand skeleton tracking               │
│ 📷 Any Camera       │ Works with USB cam or Pi Camera           │
│ 🪶 Lightweight      │ <5MB TFLite model footprint               │
│ 🔧 Modular Code     │ Easy to extend and customize              │
└─────────────────────┴───────────────────────────────────────────┘
```

</div>

---

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph INPUT["📥 INPUT LAYER"]
        CAM[📷 Camera\nRaspberry Pi Camera V2\nor USB Webcam]
    end

    subgraph PROCESSING["⚙️ PROCESSING LAYER — Raspberry Pi 3B+"]
        direction TB
        CV[🖼️ OpenCV\nFrame Capture & Preprocessing]
        MP[🤖 MediaPipe Hands\n21 Landmark Detection]
        FE[📐 Feature Extractor\nCoordinate Normalization]
        MDL[🧠 AI Model\nTFLite / Random Forest Classifier]
    end

    subgraph OUTPUT["📤 OUTPUT LAYER"]
        TXT[📝 Text Generation\nGesture → Word Mapping]
        TTS[🔊 Text-to-Speech\npyttsx3 / eSpeak Offline]
        SPK[🔈 Speaker Output]
    end

    CAM -->|Video Frames| CV
    CV -->|RGB Frames| MP
    MP -->|21 Landmarks| FE
    FE -->|Feature Vector 42D| MDL
    MDL -->|Predicted Class| TXT
    TXT -->|Text String| TTS
    TTS -->|Audio| SPK

    style INPUT fill:#1a1a2e,color:#fff,stroke:#00d9ff
    style PROCESSING fill:#16213e,color:#fff,stroke:#00d9ff
    style OUTPUT fill:#0f3460,color:#fff,stroke:#00d9ff
```

---

```mermaid
graph LR
    subgraph HW["🔧 Hardware Components"]
        RPI[🍓 Raspberry Pi 3B+\nBCM2837B0 Cortex-A53\n1.4GHz / 1GB RAM]
        CAM2[📷 Pi Camera V2\n8MP Sony IMX219\n1080p30 / 720p60]
        SPK2[🔈 3W 4Ω Speaker\nClass D Amplifier]
        SD[💾 16GB SD Card\nRaspberry Pi OS]
        PWR[⚡ 5V/2.5A\nPower Supply]
    end

    subgraph SW["💻 Software Stack"]
        PY[🐍 Python 3.9+]
        OCV[👁️ OpenCV 4.x]
        MDP[🤲 MediaPipe 0.10]
        TFL[🧠 TFLite Runtime]
        NP[🔢 NumPy]
        TTS2[🔊 pyttsx3/eSpeak]
    end

    RPI --- CAM2
    RPI --- SPK2
    RPI --- SD
    RPI --- PWR

    style HW fill:#1a1a2e,color:#fff
    style SW fill:#16213e,color:#fff
```

---

## 🔄 Complete Workflow

```mermaid
flowchart TD
    A([👤 User performs\nISL Hand Gesture]) --> B[📷 Camera Captures\nLive Video Frame]
    B --> C[🖼️ OpenCV Preprocessing\nResize · RGB Convert · Denoise]
    C --> D{🤲 MediaPipe Detects\nHand in Frame?}
    D -- ❌ No Hand --> E[⏭️ Skip Frame\nContinue Loop]
    E --> B
    D -- ✅ Hand Found --> F[📍 Extract 21 Hand\nLandmarks x,y,z]
    F --> G[📐 Normalize Coordinates\nRelative to Wrist]
    G --> H[🔢 Build Feature Vector\n42 floats per frame]
    H --> I[🧠 AI Classifier\nTFLite / Random Forest]
    I --> J{🎯 Confidence\n> Threshold?}
    J -- ❌ Low Confidence --> K[⚠️ Show 'Unknown'\nDon't Speak]
    J -- ✅ High Confidence --> L[📝 Map to Word/Phrase\ne.g. Hello · Family · Please]
    L --> M[🔊 pyttsx3 / eSpeak\nText-to-Speech Engine]
    M --> N[🔈 Speaker Outputs\nAudible Speech]
    N --> O[🖥️ OpenCV Overlay\nShow Prediction on Screen]
    O --> B

    style A fill:#00d9ff,color:#000
    style N fill:#00c853,color:#000
    style I fill:#ff6f00,color:#fff
```

---

## 🤖 AI Pipeline

### MediaPipe Hand Landmark Detection

```mermaid
sequenceDiagram
    participant CAM as 📷 Camera
    participant OCV as 🖼️ OpenCV
    participant MP as 🤲 MediaPipe
    participant FE as 📐 Feature Extractor
    participant CLS as 🧠 Classifier
    participant TTS as 🔊 TTS Engine
    participant SPK as 🔈 Speaker

    CAM->>OCV: Raw BGR Frame (640×480)
    OCV->>OCV: Convert BGR → RGB
    OCV->>MP: RGB Frame
    MP->>MP: Palm Detection Model
    MP->>MP: Hand Landmark Model (21 pts)
    MP->>FE: 21 Landmarks (x, y, z)
    FE->>FE: Normalize relative to wrist
    FE->>FE: Flatten to 42-dim vector
    FE->>CLS: Feature Vector [f₁, f₂, ..., f₄₂]
    CLS->>CLS: Random Forest / TFLite Inference
    CLS->>TTS: Predicted Label + Confidence
    TTS->>TTS: Text → Phonemes → Waveform
    TTS->>SPK: Audio Signal
    SPK-->>CAM: Loop continues
```

### The 21 Hand Landmarks

```
                    8   12  16  20
                    |   |   |   |
                7   11  15  19
                |   |   |   |
            6   10  14  18
            |   |   |   |
        5   9   13  17
        |   |   |   |
    4   3   2   1   0(WRIST)
    |
  THUMB
  
  0: WRIST          11: MIDDLE_FINGER_DIP
  1: THUMB_CMC      12: MIDDLE_FINGER_TIP
  2: THUMB_MCP      13: RING_FINGER_MCP
  3: THUMB_IP       14: RING_FINGER_PIP
  4: THUMB_TIP      15: RING_FINGER_DIP
  5: INDEX_MCP      16: RING_FINGER_TIP
  6: INDEX_PIP      17: PINKY_MCP
  7: INDEX_DIP      18: PINKY_PIP
  8: INDEX_TIP      19: PINKY_DIP
  9: MIDDLE_MCP     20: PINKY_TIP
 10: MIDDLE_PIP
```

---

## 🖥️ Hardware Setup

<div align="center">

| Component | Specification | Purpose |
|:---:|:---:|:---:|
| ![RPi](https://img.shields.io/badge/Raspberry_Pi_3B+-C51A4A?style=flat-square&logo=raspberry-pi) | BCM2837B0 · 1.4GHz · 1GB RAM | Main processing unit |
| 📷 Pi Camera V2 | 8MP Sony IMX219 · 1080p30 | Hand gesture capture |
| 🔈 Speaker | 3W · 4Ω · Class D Amp | Speech audio output |
| 💾 MicroSD Card | 16GB SanDisk Ultra | OS + project files |
| ⚡ Power Supply | 5V / 2.5A Micro-USB | Stable power delivery |
| 🖥️ HDMI Monitor | Optional · Any HDMI | Display predictions |

</div>

### Hardware Connection Diagram

```
┌─────────────────────────────────────────────────────┐
│                  RASPBERRY PI 3B+                    │
│                                                      │
│  ┌──────────┐    ┌──────────────────────────────┐   │
│  │ CSI Port ├────┤   Pi Camera Module V2        │   │
│  └──────────┘    │   (Ribbon Cable Connection)  │   │
│                  └──────────────────────────────┘   │
│  ┌──────────┐    ┌──────────────────────────────┐   │
│  │  USB 2.0 ├────┤   USB Webcam (Alternative)   │   │
│  └──────────┘    └──────────────────────────────┘   │
│  ┌──────────┐    ┌──────────────────────────────┐   │
│  │3.5mm Jack├────┤   Speaker + Amplifier        │   │
│  └──────────┘    └──────────────────────────────┘   │
│  ┌──────────┐    ┌──────────────────────────────┐   │
│  │   HDMI   ├────┤   Monitor (Optional)         │   │
│  └──────────┘    └──────────────────────────────┘   │
│  ┌──────────┐    ┌──────────────────────────────┐   │
│  │MicroUSB  ├────┤   5V/2.5A Power Supply       │   │
│  └──────────┘    └──────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

### 📸 Hardware Photos

<table>
<tr>
<td align="center" width="50%">

**Raspberry Pi 3 Model B+**

![Raspberry Pi 3B+](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Raspberry-Pi-3B_plus.jpg/440px-Raspberry-Pi-3B_plus.jpg)

*BCM2837B0 · 1.4GHz Quad-Core · 1GB LPDDR2*

</td>
<td align="center" width="50%">

**Pi Camera Module V2**

![Pi Camera](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/RPi-Camera.jpg/320px-RPi-Camera.jpg)

*8MP Sony IMX219 · Direct CSI Connection*

</td>
</tr>
</table>

---

## 💻 Software Stack

```mermaid
graph TD
    subgraph OS["🐧 Raspberry Pi OS (Debian Bullseye)"]
        subgraph LANG["🐍 Python 3.9+"]
            subgraph CV["👁️ Computer Vision"]
                OCV2[OpenCV 4.8\nFrame Processing\nDisplay Overlay]
                MP2[MediaPipe 0.10\nHand Tracking\nLandmark Detection]
            end
            subgraph AI["🧠 AI / ML"]
                TFL2[TensorFlow Lite\nModel Inference\nEdge Optimized]
                SK[Scikit-Learn\nRandom Forest\nModel Training]
                NP2[NumPy\nNumerical Arrays\nFeature Vectors]
            end
            subgraph TTS3["🔊 Text-to-Speech"]
                PY2[pyttsx3\nOffline TTS\nCross-Platform]
                ESP[eSpeak\nLightweight TTS\nMulti-Language]
            end
        end
    end

    style OS fill:#2d2d2d,color:#fff
    style CV fill:#1a3a1a,color:#fff
    style AI fill:#1a1a3a,color:#fff
    style TTS3 fill:#3a1a1a,color:#fff
```

---

## 📊 Dataset & Preprocessing

<details>
<summary><b>🗂️ Click to expand Dataset Details</b></summary>

### Dataset Overview

| Property | Value |
|:---|:---|
| Type | Custom ISL Gesture Dataset |
| Collection Method | Webcam + Pi Camera |
| Gestures Supported | Hello, Goodbye, Please, Thank You, Yes, No, Help, Family, School, Water |
| Samples per Gesture | 100–200 images |
| Total Samples | ~1,500 gesture samples |
| Format | Pickle files (.pkl) containing landmark arrays |
| Landmark Features | 42 float values (21 landmarks × x,y coordinates) |

### Preprocessing Pipeline

```mermaid
flowchart LR
    A[📹 Raw Video\nCapture] --> B[🖼️ Frame\nExtraction]
    B --> C[✋ MediaPipe\nLandmark Detection]
    C --> D[📐 Coordinate\nNormalization]
    D --> E[💾 Store as\nPickle .pkl]
    E --> F[🔀 Train/Test\nSplit 80/20]
    F --> G[🧠 Model\nTraining]

    style A fill:#ff6f00,color:#fff
    style G fill:#00c853,color:#fff
```

### Data Augmentation

- **Horizontal Flipping** — handles both left and right hands
- **Brightness Variation** — 0.7x to 1.3x brightness range
- **Rotation** — ±15° rotation tolerance
- **Scale Variation** — 0.9x to 1.1x hand size variation

</details>

---

## 🧠 Model Details

<details>
<summary><b>🔬 Click to expand Model Architecture</b></summary>

### Classifier Architecture

```
Input Layer:  [42 features] — 21 landmarks × (x,y)
      ↓
Random Forest Classifier
  ├── 100 Decision Trees
  ├── Max Depth: 20
  ├── Min Samples Split: 2
  ├── Feature Sampling: sqrt(n_features)
  └── Voting: Majority Vote

Output Layer: [N classes] — One per gesture label
```

### TensorFlow Lite Model (Alternative)

```
Input:  (1, 42)  ← 42-dim feature vector
  → Dense(128, ReLU) + BatchNorm + Dropout(0.3)
  → Dense(64, ReLU)  + BatchNorm + Dropout(0.2)
  → Dense(N, Softmax) ← N = number of gestures

Model Size:    ~2.3 MB (.tflite)
Inference:     <50ms on Raspberry Pi 3B+
Memory Usage:  ~120MB RAM during inference
```

### Performance Summary

| Metric | Value |
|:---|:---|
| Gesture Recognition Accuracy | **~93%** |
| Facial Expression Accuracy | **~91%** |
| Overall Live System Accuracy | **~90%** |
| Average Inference Time | **<50ms** |
| End-to-End Latency | **<200ms** |
| Model Size | **~2.3MB** |
| RAM Usage | **~120MB** |
| FPS (Raspberry Pi 3B+) | **15–20 FPS** |

</details>

---

## 📸 Screenshots & Demo

### 🖐️ Live Gesture Predictions

> *Real output from the working prototype at Aditya University, June 2025*

<table>
<tr>
<td align="center" width="50%">

**Prediction: "Hello"**

![Hello Gesture](assets/images/gesture_hello.jpg)

*MediaPipe landmarks overlaid in real-time*

</td>
<td align="center" width="50%">

**Prediction: "Family"**

![Family Gesture](assets/images/gesture_family.jpg)

*Dual-hand ISL gesture detection*

</td>
</tr>
<tr>
<td align="center" width="50%">

**Prediction: "Please"**

![Please Gesture](assets/images/gesture_please.jpg)

*Single-hand gesture with high confidence*

</td>
<td align="center" width="50%">

**Prediction: "School"**

![School Gesture](assets/images/gesture_school.jpg)

*Complex two-hand gesture correctly classified*

</td>
</tr>
</table>

### 🎥 Demo Videos

> *Watch the system in action*

| Demo | Description | Link |
|:---|:---|:---:|
| 🤲 MediaPipe Hands | Google's official MediaPipe hand tracking | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=BaCo_mMFGTA) |
| 🤖 TFLite on RPi | TensorFlow Lite on Raspberry Pi demo | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=aimSGOAUI8Y) |
| 🖐️ Sign Language AI | ISL recognition reference | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=fl9V-K-hPyE) |
| 🍓 RPi Camera Setup | Raspberry Pi camera module setup | [![YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=flat-square&logo=youtube)](https://www.youtube.com/watch?v=GImeVqHQzsE) |

> 📌 *Place your own demo recording at `assets/videos/demo.mp4` for local playback*

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/sivanagisetti/ai-sign-to-speech-conversion.git
cd ai-sign-to-speech-conversion

# 2. Create virtual environment
python3 -m venv venv && source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the main program
python src/main.py
```

> 🎉 A camera window will open. Perform any trained ISL gesture — the system speaks it aloud!

---

## 🔧 Installation Guide

<details>
<summary><b>🍓 Raspberry Pi Setup</b></summary>

### Step 1: Flash Raspberry Pi OS

```bash
# Download Raspberry Pi Imager from:
# https://www.raspberrypi.com/software/

# Select: Raspberry Pi OS (64-bit)
# Flash to 16GB+ MicroSD card
```

### Step 2: Enable Camera

```bash
sudo raspi-config
# Navigate to: Interface Options → Camera → Enable
sudo reboot
```

### Step 3: Install System Dependencies

```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y \
    python3-pip \
    python3-venv \
    python3-opencv \
    espeak \
    libatlas-base-dev \
    libjasper-dev \
    libqtgui4 \
    libqt4-test \
    libhdf5-dev \
    git
```

### Step 4: Install Python Dependencies

```bash
git clone https://github.com/sivanagisetti/ai-sign-to-speech-conversion.git
cd ai-sign-to-speech-conversion
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Test Camera

```bash
python3 -c "import cv2; cap = cv2.VideoCapture(0); print('Camera OK' if cap.isOpened() else 'Camera Error')"
```

</details>

<details>
<summary><b>🖥️ PC/Laptop Setup (Development)</b></summary>

```bash
# Works on Ubuntu 20.04+, Windows 10+, macOS 11+
git clone https://github.com/sivanagisetti/ai-sign-to-speech-conversion.git
cd ai-sign-to-speech-conversion
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
# venv\Scripts\activate     # Windows
pip install -r requirements.txt
python src/main.py
```

</details>

---

## ▶️ Running the Project

### 1. Collect Your Own Gesture Dataset

```bash
python src/dataset/dataset_creator.py --gesture "hello" --samples 200
# Repeat for each gesture you want to train
```

### 2. Train the Classifier

```bash
python src/training/trainer.py
# Outputs: models/gesture_classifier.pkl
```

### 3. Run Real-Time Prediction

```bash
python src/main.py
```

### 4. Run with Custom Options

```bash
python src/main.py \
    --camera 0 \
    --model models/gesture_classifier.pkl \
    --confidence 0.85 \
    --tts-engine espeak \
    --display
```

### Command Reference

| Command | Description |
|:---|:---|
| `python src/main.py` | Run the full real-time system |
| `python src/training/trainer.py` | Train a new gesture model |
| `python src/dataset/dataset_creator.py` | Collect gesture training data |
| `python src/testing/evaluate.py` | Run accuracy evaluation |
| `python -m pytest tests/` | Run all unit tests |

---

## 📈 Performance Metrics

<div align="center">

### Accuracy

```
Gesture Recognition:     ████████████████████░  93%
Facial Expressions:      ███████████████████░░  91%
Live System Accuracy:    ██████████████████░░░  90%
```

### Speed (Raspberry Pi 3B+)

```
Frame Capture:           ████████████████████  ~33ms  (30fps input)
MediaPipe Detection:     █████████████░░░░░░░  ~80ms
Feature Extraction:      ████░░░░░░░░░░░░░░░░  ~5ms
Model Inference:         ██████░░░░░░░░░░░░░░  ~50ms
TTS Synthesis:           ████████░░░░░░░░░░░░  ~100ms
─────────────────────────────────────────────────────
Total End-to-End:        ████████████░░░░░░░░  ~170ms
```

### System Resources

| Resource | Usage |
|:---|:---|
| CPU Usage (idle) | ~15% |
| CPU Usage (inference) | ~60–75% |
| RAM Usage | ~120MB / 1GB |
| Model Size (.pkl) | ~1.2MB |
| Model Size (.tflite) | ~2.3MB |
| SD Card Space (full project) | ~800MB |

</div>

---

## 📁 Project Structure

```
ai-sign-to-speech-conversion/
│
├── dataset/
│   ├── bye.csv
│   ├── correct.csv
│   ├── dull.csv
│   ├── family.csv
│   ├── father.csv
│   ├── good evening.csv
│   ├── good morning.csv
│   ├── hello.csv
│   ├── help.csv
│   ├── i love you.csv
│   ├── indian.csv
│   ├── mother.csv
│   ├── my.csv
│   ├── name.csv
│   ├── please.csv
│   ├── school.csv
│   ├── scold.csv
│   ├── smile.csv
│   ├── sorry.csv
│   ├── topic.csv
│   ├── trust me.csv
│   ├── understand.csv
│   ├── welcome.csv
│   └── wrong.csv
│
├── collect_data.py
├── train_model.py
├── predict_live.py
│
├── gesture_model.pkl
├── model.pkl
├── label_map.json
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── images/
│   ├── project_banner.png
│   ├── workflow.png
│   ├── dataset_collection.png
│   ├── training.png
│   ├── prediction.png
│   └── output.png
│
├── videos/
│   ├── demo.mp4
│   └── demo.gif
│
└── screenshots/
    ├── screenshot1.png
    ├── screenshot2.png
    ├── screenshot3.png
    └── screenshot4.png
```

---

## 🗺️ Roadmap

```mermaid
gantt
    title AI Sign-to-Speech — Development Roadmap
    dateFormat  YYYY-MM
    section ✅ Completed
    Dataset Collection          :done, 2025-01, 2025-02
    MediaPipe Integration       :done, 2025-02, 2025-03
    Random Forest Classifier    :done, 2025-03, 2025-04
    Raspberry Pi Deployment     :done, 2025-04, 2025-05
    Real-time Testing & Tuning  :done, 2025-05, 2025-06
    Project Expo Presentation   :done, 2025-06, 2025-07

    section 🔄 In Progress
    TFLite Model Optimization   :active, 2025-07, 2025-08
    GitHub Repository           :active, 2025-07, 2025-08

    section 🔮 Planned
    Sentence Formation (LSTM)   :2025-09, 2025-11
    Multi-Language TTS          :2025-10, 2025-12
    Mobile App (Android)        :2026-01, 2026-04
    IoT Smart Device Control    :2026-03, 2026-06
    Cloud Model Sync            :2026-06, 2026-09
```

### Upcoming Features

- [ ] 🔤 **Full Sentence Formation** — LSTM/Transformer sequence model
- [ ] 🌍 **Multi-Language Speech** — Telugu, Hindi, Tamil TTS support
- [ ] 📱 **Android App** — Flutter-based mobile companion
- [ ] 🏠 **IoT Integration** — Gesture-controlled smart home devices
- [ ] ☁️ **Cloud Model Sync** — Auto-update models via Wi-Fi
- [ ] 😊 **Emotion Recognition** — Facial expression + gesture combined
- [ ] 🎓 **Extended Vocabulary** — 50+ ISL gestures

---

## 📚 Literature Review

<details>
<summary><b>📖 Click to expand Literature Survey</b></summary>

| # | Authors | Year | Method | Accuracy | Limitation |
|:---:|:---|:---:|:---|:---:|:---|
| 1 | Shweta S Shinde et al. | 2016 | MATLAB + MFCC | 90% | Not portable (MATLAB) |
| 2 | L Latha et al. | 2018 | RPi + MATLAB | — | Requires MATLAB license |
| 3 | K Avinash et al. | 2019 | Flex Sensors + Arduino | — | Hardware gloves needed |
| 4 | Kaggle/ISL Dataset | 2021 | CNN (VGG) | 98.5% | Only static gestures |
| 5 | Sign Lang to Text | 2022 | CNN-based | 99.8% | American SL only |
| 6 | RNN-CTC System | 2022 | RNN + LSTM + CTC | — | High compute needed |
| **Ours** | **NVS Chakradhar et al.** | **2025** | **MediaPipe + RF/TFLite** | **~93%** | **ISL, edge device, offline** |

</details>

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Fork → Clone → Branch → Commit → Push → PR
git checkout -b feature/new-gesture-support
git commit -m "feat: add support for 10 new ISL gestures"
git push origin feature/new-gesture-support
```

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 👤 Author

<div align="center">

<img src="https://avatars.githubusercontent.com/u/sivanagisetti?s=120" width="100" style="border-radius:50%" alt="Siva"/>

### Nagisetti Venkata Siva Chakradhar

*B.Tech ECE · Aditya Engineering College, Surampalem*
*GATE 2025 Qualified (Score: 323)*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-sivanagisetti-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/sivanagisetti)
[![GitHub](https://img.shields.io/badge/GitHub-sivanagisetti-black?style=for-the-badge&logo=github)](https://github.com/sivanagisetti)
[![Email](https://img.shields.io/badge/Email-sivanagisetti2004%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:sivanagisetti2004@gmail.com)

</div>

### 👥 Team — Batch 04, Aditya University In-House Internship (May–Jul 2025)

| Name | Roll No | Role |
|:---|:---|:---|
| J. Nikhil Sai | 22A91A0419 | Project Lead |
| **N.V.S. Chakradhar** | **23A95A0416** | **Hardware & Edge Deployment** |
| K. Sravanthi | 23A91A04F8 | Dataset & Preprocessing |
| M. Mounika | 23A91A04G9 | Model Training |
| M. Saran Teja | 23A91A04H0 | Testing & Evaluation |

**Faculty Mentors:** Dr. K. Ayyappa Swamy · Dr. BH. Vara Prasad · Mr. CH. Govinda

---

## 📚 References

1. [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) — Google's Hand Tracking Solution
2. [TensorFlow Lite](https://www.tensorflow.org/lite/convert) — Edge ML Framework
3. [OpenCV](https://opencv.org/) — Real-time Computer Vision
4. [Scikit-learn](https://scikit-learn.org/) — Machine Learning for Python
5. [pyttsx3](https://pyttsx3.readthedocs.io/) — Offline Text-to-Speech

---

<div align="center">

## ⭐ Support This Project

**If this project helped you or inspired you, please give it a star!**

[![Star History Chart](https://api.star-history.com/svg?repos=sivanagisetti/ai-sign-to-speech-conversion&type=Date)](https://star-history.com/#sivanagisetti/ai-sign-to-speech-conversion&Date)

---

*🤟 Built with passion for accessibility and assistive technology*

*Aditya University, Surampalem · ECE Department · In-House Internship 2025*

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
