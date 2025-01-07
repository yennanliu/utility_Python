from mobly import base_test
from mobly import test_runner
from mobly.controllers import android_device


class ManyGreetingsTest(base_test.BaseTestClass):

    # When a test run starts, Mobly calls this function to figure out what
    # tests need to be generated. So you need to specify what tests to generate
    # in this function.
    def pre_run(self):
        messages = [('Hello', 'World'), ('Aloha', 'Obama'),
                    ('konichiwa', 'Satoshi')]
        # Call `generate_tests` function to specify the tests to generate. This
        # function can only be called within `pre_run`. You could
        # call this function multiple times to generate multiple groups of
        # tests.
        self.generate_tests(
            # Specify the function that has the common logic shared by these
            # generated tests.
            test_logic=self.make_toast_logic,
            # Specify a function that creates the name of each test.
            name_func=self.make_toast_name_function,
            # A list of tuples, where each tuple is a set of arguments to be
            # passed to the test logic and name function.
            arg_sets=messages)

    def setup_class(self):
        self.ads = self.register_controller(android_device)
        self.dut = self.ads[0]
        self.dut.load_snippet('mbs', android_device.MBS_PACKAGE)

    # The common logic shared by a group of generated tests.
    def make_toast_logic(self, greeting, name):
        self.dut.mbs.makeToast('%s, %s!' % (greeting, name))

    # The function that generates the names of each test case based on each
    # argument set. The name function should have the same signature as the
    # actual test logic function.
    def make_toast_name_function(self, greeting, name):
        return 'test_greeting_say_%s_to_%s' % (greeting, name)


if __name__ == '__main__':
    test_runner.main()