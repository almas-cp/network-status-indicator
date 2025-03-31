# Network Status Indicator

<p align="center">
  <img src="screenshot.png" alt="Network Status Indicator Screenshot" width="400">
</p>

<p align="center">
  <b>A lightweight system tray tool that monitors your network status in real-time</b>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#requirements">Requirements</a>
</p>

## ✨ Features

- **Real-time network monitoring** in your system tray
- **Visual status indication** with customizable colors and shapes
- **Network speed measurements** (download and upload)
- **Fully customizable** appearance and behavior
- **Lightweight** with minimal resource usage
- **Auto-start** option for Windows startup
- **Zero configuration** required to get started

## 📥 Installation

### Download Executable

1. Download the latest release from the [Releases](https://github.com/yourusername/network-status-indicator/releases) page
2. Run the executable file
3. The indicator will appear in your system tray

### Build from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/network-status-indicator.git

# Navigate to the directory
cd network-status-indicator

# Install dependencies
pip install -r requirements.txt

# Run the application
python network_status_indicator.py
```

## 🚀 Usage

- **Green icon**: Network is available
- **Red icon**: Network is unavailable
- **Hover**: See connection status and network speeds
- **Right-click**: Access menu options
  - Check Now: Force an immediate connection check
  - Open Settings: Configure the application
  - Quit: Exit the application

## ⚙️ Configuration

Right-click the icon and select "Open Settings" to customize:

### General
- **Check Interval**: How often to check network status (500ms-10000ms)
- **Start with Windows**: Launch automatically at system startup

### Appearance
- **Colors**: Customize available/unavailable indicator colors
- **Shape**: Choose between circle, square, or triangle
- **Size**: Adjust indicator size
- **Border**: Set border width and color

### Network
- **Target Host**: The host to ping for connectivity checks (default: 8.8.8.8)
- **Timeout**: Maximum wait time for connectivity checks (1-10 seconds)

## 🖥️ Requirements

- Windows 10 or later
- Python 3.6+ (for source installation)
- PyQt5
- aiohttp
- asyncio

## 💬 Feedback & Contributions

Feedback and contributions are welcome! Feel free to open an issue or submit a pull request.

---

<p align="center">
  Made with ❤️ for network monitoring
</p> 