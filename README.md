
# Real-Time People Counter

Welcome to the **Real-Time People Counter** project! This cutting-edge application uses computer vision to detect and count people in real-time through a webcam feed. It's perfect for a variety of applications, including security monitoring, event management, and AI experimentation.

## Features

- **Real-Time Detection**: Continuously analyzes the video feed from your webcam to detect and count people in real-time. Ideal for monitoring busy areas and tracking movement.
- **Confidence Display**: Provides confidence scores for each detected person, helping you gauge the accuracy of the detection. The higher the confidence, the more reliable the detection.
- **Crossing Detection**: Tracks people crossing a predefined vertical line, allowing you to monitor specific areas or entry/exit points. You can configure the line to track movement from left to right, right to left, or both directions.
- **Customizable Colors**: Easily adjust the colors used for displaying text, lines, and markers on detected people. This feature allows you to match the visualization with your preferred color scheme or improve visibility based on your environment.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**: Download a copy of the repository to your local machine. You can do this by running:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment** (optional but recommended): Create and activate a virtual environment to manage dependencies.
   ```bash
   python -m venv venv       #Here, i named my enviroment "venv",feel free to use any name for your environment"
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:Install the required Python packages using the [requirements.txt](requirements.txt) file. This file contains all necessary libraries and their versions.
   ```bash
   pip install library_name
   ```

4. **Run the Application**: Start the people counter by executing the main script. Ensure your webcam is connected and properly configured.
   ```bash
   python main.py
   ```

5. **Configuration**: Adjust the configuration settings in `config.py` if needed to fit your specific use case or preferences.

## Contact

For any questions or feedback, reach out to [mohammedzaidmadari@gmail.com](mohammedzaidmadari@gmail.com).

