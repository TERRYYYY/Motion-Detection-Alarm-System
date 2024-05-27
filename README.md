# Motion Detection Alarm System

This project is a simple motion detector system using OpenCV and Python. It captures video from a webcam, processes the frames to detect motion, and triggers an alarm when significant motion is detected.

## Features

- Real-Time Motion Detection: Continuously captures frames from a webcam and compares consecutive frames to detect motion.
- Alarm System: Triggers a beeping alarm when motion is detected for a sustained period.
- User Controls: Allows the user to enable or disable the motion detection alarm mode and quit the application using keyboard inputs.
- Threaded Alarm: Utilizes threading to handle the alarm beeping concurrently with motion detection.

## Requirements
- Python 3+
- OpenCV
- Imutils
- Winsound (Windows only)

## Installation

1. Clone the repository:

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
https://github.com/TERRYYYY/Motion-Detection-Alarm-System.git
```
2. Install the required packages:

```bash
pip install opencv-python imutils
```

## Usage

Run the main.py script on the terminal:

```bash
python main.py
```
2. Install the required packages:

```bash
pip install opencv-python imutils
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.