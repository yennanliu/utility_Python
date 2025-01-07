# https://github.com/google/mobly/blob/master/docs/instrumentation_tutorial.md

from mobly import base_instrumentation_test
from mobly import test_runner
from mobly.controllers import android_device

class InstrumentationTest(base_instrumentation_test.BaseInstrumentationTestClass):
    def setup_class(self):

        print(">>> InstrumentationTest start")
        print(">>> android_device = " + str(android_device))
        self.dut = self.register_controller(android_device)[0]
        print(">>> self.dut  = " + str(self.dut))

    def test_instrumentation(self):
        print("dummy test_instrumentation run")
        #self.run_instrumentation_test(self.dut, 'com.example.package.test')
        #self.dut.run_instrumentation_test('self.dut', android_device.MBS_PACKAGE)


if __name__ == '__main__':
  test_runner.main()