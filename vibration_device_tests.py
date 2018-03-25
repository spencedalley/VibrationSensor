from nose.tools import *

from iotile.core.hw.hwmanager import HardwareManager

def test_vibration_device():
    with HardwareManager(port='virtual:./vibration_device.py') as hw:
        hw.connect_direct('1')
        con = hw.controller()

        # test no min/max set
        min_val, max_val = con.get_min_max_threshold()
        assert_equal(min_val, 0, "Expected min value of 0 when not set. Got `%f`"
                     % min_val)
        assert_equal(max_val, 0, "Expected max value of 0 when not set. Got `%f`"
                     % max_val)

        vibration_level = con.get_vibration_level()
        assert_equal(vibration_level, 0,
                     "Expected vibration level to be 0 when min/max not set. Got "
                     "`%f`" % vibration_level)

        # test expected behavior (i.e. return values between min and max values)
        min_max_pairs = [(1, 1), (1, 2), (1, 1000), (1000, 2000)]

        for (min_val, max_val) in min_max_pairs:
            con.set_min_max_threshold(min_val, max_val)

            min_reported, max_reported = con.get_min_max_threshold()
            assert_equal(min_reported, min_val,
                         "Minimum thresholds do not match after setting on device"
                         "Minimum on device: %f, Expected Minimum: %f"
                         % (min_reported, min_val))
            assert_equal(max_reported, max_val,
                         "Maximum thresholds do not match after setting on device"
                         "Maximum on device: %f, Expected Maximum: %f"
                         % (max_reported, max_val))

            for i in range(1000):
                vibration_level = con.get_vibration_level()
                assert_true(min_val <= vibration_level <= max_val,
                            "Vibration level not between %f and %f. Real value %f"
                            % (min_val, max_val, vibration_level))
