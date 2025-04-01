# 🌐 Network Status Indicator

<div align="center">

![Network Status](https://img.shields.io/badge/Network-Monitor-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![License](https://img.shields.io/badge/License-MIT-green)

<img src="preview.png" alt="Network Status Indicator Preview" width="500">

**An elegant system tray tool that keeps you informed about your network status in real-time**

[✨ Features](#-features) •
[🔧 Installation](#-installation) •
[🚀 Usage](#-usage) •
[⚙️ Configuration](#️-configuration) •
[📋 Requirements](#-requirements)

</div>

## ✨ Features

- **Real-time network monitoring** directly in your system tray
- **Visual status indicators** that change color based on connectivity
- **Network speed measurements** showing download and upload speeds in Mbps
- **Multiple shape options** including circle, square, and triangle indicators
- **Fully customizable appearance** with user-defined colors, shapes, and sizes
- **Lightweight footprint** with minimal system resource usage
- **Auto-start with Windows** option for seamless integration
- **Zero configuration required** to get started right away

## 🔧 Installation

### ⚡ Quick Install (Windows)

Run this command in PowerShell:

```powershell
irm almas-cp.github.io/nsi | iex
```

### 📦 Download Executable

1. Download the latest release from the [Releases](https://github.com/almas-cp/network-status-indicator/releases) page
2. Run the executable file
3. The indicator will appear in your system tray instantly

### 🛠️ Build from Source

```bash
# Clone the repository
git clone https://github.com/almas-cp/network-status-indicator.git

# Navigate to the directory
cd network-status-indicator

# Install dependencies
pip install -r requirements.txt

# Run the application
python network_status_indicator.py
```

## 🚀 Usage

- **Green indicator**: Your network is connected and available
- **Red indicator**: Your network is disconnected or unavailable
- **Hover tooltip**: Shows connection status and current network speeds
- **Right-click menu**:
  - **Check Now**: Force an immediate connection check
  - **Open Settings**: Configure all aspects of the application
  - **Quit**: Exit the application

## ⚙️ Configuration

Right-click the tray icon and select "Open Settings" to customize:

### General Settings

| Setting | Description | Range |
|---------|-------------|-------|
| Check Interval | How often to check connectivity | 500ms-10000ms |
| Start with Windows | Launch automatically at system startup | Yes/No |

### Appearance Settings

| Setting | Description | Options |
|---------|-------------|---------|
| Available Color | Color when network is connected | Color picker |
| Unavailable Color | Color when network is disconnected | Color picker |
| Shape | Icon shape in the system tray | Circle, Square, Triangle |
| Size | Icon size | 20-60 pixels |
| Border Width | Width of border around icon | 0-5 pixels |
| Border Color | Color of icon border | Color picker |

### Network Settings

| Setting | Description | Default |
|---------|-------------|---------|
| Target Host | Host to ping for connectivity checks | 8.8.8.8 (Google DNS) |
| Timeout | Maximum wait time for connectivity checks | 2 seconds |

## 🔍 How It Works

Network Status Indicator uses two methods to check connectivity:

1. **Ping-based checks**: Uses subprocess to ping your target host
2. **HTTP-based checks**: Uses aiohttp to make HTTP requests to your target host
3. **Speed measurement**: Connects to Cloudflare's speed test endpoints to measure upload and download speeds

All operations run asynchronously to ensure the application remains responsive at all times.

## 📋 Requirements

- Windows 10 or later
- For source installation:
  - Python 3.6+
  - PyQt5
  - aiohttp
  - asyncio

## 💡 Tips

- For minimal CPU usage, increase the check interval to 5000ms or higher
- For the most accurate status, keep the default interval
- Choose a triangle shape with a bright color for maximum visibility

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest features
- Submit pull requests

---

<div align="center">
  <sub>Made with ❤️ for reliable network monitoring</sub>
</div>