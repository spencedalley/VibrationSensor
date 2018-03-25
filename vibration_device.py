import random

from iotile.core.hw.virtual.virtualdevice import VirtualIOTileDevice, rpc

class VibrationVirtualDevice(VirtualIOTileDevice):
    """A simple virtual IOTile device that has an RPC to generate vibration data

        Args:
            args (dict): Any arguments that you want to pass to create this device.
    """

    def __init__(self, args):
        super(VibrationVirtualDevice, self).__init__(1, "VIBR01")
        self.min = None
        self.max = None
        self.INVALID_THRESHOLD = 0

    @rpc(8, 0x0004, "", "H6sBBBB")
    def controller_status(self):
        """Return the name of the controller as a 6 byte string"""
        status = (1 << 1) | (1 << 0)
        return [0xFFFF, self.name, 0, 0, 1, status]

    @rpc(8, 0x9000, "LL")
    def set_min_max_threshold(self, min_val, max_val):
        """Set min and max vibration threshold for device"""
        self.min, self.max = min_val, max_val
        return []

    @rpc(8, 0x9001, "", "LL")
    def get_min_max_threshold(self):
        """Set min and max vibration threshold for device

        Returns:
            list  a list with two values containing the min and max vibration
                  threshold where a [0, 0] value indicates the min/max threshold
                  has not been set
        """
        return [self.min or self.INVALID_THRESHOLD,
                self.max or self.INVALID_THRESHOLD]

    @rpc(8, 0x8000, "", "L")
    def get_vibration_level(self):
        """Get current vibration level from device

        Returns:
            list  a list with a single value containing the current device
                  vibration level where a [0] value indicates that the min and
                  max vibration thresholds have not been set.
        """
        return [random.randint(self.min, self.max)] if self.min and self.max else [self.INVALID_THRESHOLD]

