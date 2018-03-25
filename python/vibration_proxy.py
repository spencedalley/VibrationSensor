from iotile.core.hw.proxy.proxy import TileBusProxyObject
from iotile.core.utilities.typedargs.annotate import return_type, context, param
import struct

@context("VibrationProxy")
class VibrationProxyObject(TileBusProxyObject):
    """Code challenge vibration project"""

    @classmethod
    def ModuleName(cls):
        """The 6 byte name for the device"""
        return 'VIBR01'

    @param("min_val", "integer")
    @param("max_val", "integer")
    def set_min_max_threshold(self, min_val, max_val):
        args = struct.pack("<LL", min_val, max_val)
        self.rpc(0x90, 0x00, args)

    @return_type("list(float)")
    def get_min_max_threshold(self):
        min_max = self.rpc(0x90, 0x01, result_format="LL")
        return [float(i) for i in min_max]

    @return_type("float")
    def get_vibration_level(self):
        vibration_level = self.rpc(0x80, 0x00, result_format="L")[0]
        return float(vibration_level)
