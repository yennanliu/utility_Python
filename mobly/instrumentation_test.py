# https://github.com/google/mobly/blob/master/docs/instrumentation_tutorial.md

from mobly import base_instrumentation_test
from mobly import test_runner
from mobly.controllers import android_device

class InstrumentationTest(base_instrumentation_test.BaseInstrumentationTestClass):
    def setup_class(self):
        self.dut = self.register_controller(android_device)[0]

    def test_instrumentation(self):
        self.run_instrumentation_test(self.dut, 'com.example.package.test')


if __name__ == '__main__':
  test_runner.main()