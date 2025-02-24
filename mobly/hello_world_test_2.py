from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device


class HelloWorldTest(base_test.BaseTestClass):

  def setup_class(self):
    self.ads = self.register_controller(android_device)
    self.dut = self.ads[0]
    self.dut.load_snippet('mbs', android_device.MBS_PACKAGE)

  def test_hello(self):
    self.dut.mbs.makeToast('Hello World!')

  def test_bye(self):
    self.dut.mbs.makeToast('Goodbye! >>>>')

  def test_favorite_food(self):
    food = self.user_params.get('favorite_food')
    if food:
      self.dut.mbs.makeToast(">>> I'd like to eat %s." % food)
    else:
      self.dut.mbs.makeToast(">>> I'm not hungry.")    

if __name__ == '__main__':
  test_runner.main()