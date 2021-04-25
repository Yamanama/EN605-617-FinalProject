from src.config.config import Config
import sys
import jetson.inference
import jetson.utils
# Based upon https://github.com/dusty-nv/jetson-inference/blob/master/python/examples/my-detection.py
class detection:
    def __init__(self, config_path) -> None:
        """Detection class
        Test harness to run a network against a real time stream
        Most likely from an attached webcam

        Args:
            config_path ([type]): the path to a config file
        """
        self.config = Config(config_path)
        # the neural net
        self.net = jetson.inference.detectNet(self.config.net.network, self.config.net.threshold)
        # the camera feed
        self.camera = jetson.utils.gstCamera(self.config.camera.width, self.config.camera.height, self.config.camera.path)
        # the display
        self.display = jetson.utils.glDisplay()
    def run(self):
        """Run the detection and present to the screen the live results
        """
        while self.display.IsOpen():
            # iterate until the display is closed
            img, width, height = self.camera.CaptureRGBA()
            # get the detections
            detections = self.net.Detect(img, width, height)
            # print to cli (useful for headless runs)
            for detection in detections:
                print(detection)
            # render the image
            self.display.RenderOnce(img, width, height)
            # set the title
            self.display.SetTitle("FPS: {:.0f}".format(self.net.GetNetworkFPS()))
if __name__ == '__main__':
    # run if main
    import glob
    # find the realtime-config file
    file_path = glob.glob('./**/realtime-config.json', recursive=True)[0]
    if file_path is not None:
        # create the detector
        detector = detection(file_path)
        # run the detector
        detector.run()
    else:
        # error and close
        print("Couldn't find the config file.")
        sys.exit(-1)