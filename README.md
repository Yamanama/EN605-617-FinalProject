# EN605-617-FinalProject
Object Detection using a custom trained network to detect a specific object

## Disclaimer
This project stems from the [jetson inference](https://github.com/dusty-nv/jetson-inference) project provided by NVIDIA as part of the jetson Nano project. 

There exists a nontrivial amount of configuration to build the jetson inference modules and their corresponding python bindings. For more information use the link above.


## Test Harness
[Real Time Detection](src/realtime/detection.py) is made to run the trained networks

### Configuration
[config.json example](src/realtime/realtime-config.json)
```
{
    "net": {
        "threshold": 0.9,
        "network": "ssd-inception-v2"
    },
    "camera": {
        "width": 1920,
        "height": 1080,
        "path": "/dev/video0"
    }
}
```
- `net` holds configuration values for the network
- `camera` holds configuration values for the camera hosting the video stream

### Execution
To execute the test harness use the following command from the root of this repository:
```
python -m src.realtime.detection
```

## Training
A [sample](training/data/Annotations) of the annotations from a training run are included for posterity

Due to file sizes only the annotations are included in this repository.

***Training the network encapsulation a large portion of this project***



