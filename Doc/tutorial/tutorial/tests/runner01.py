import os

SPIDER_NAME = "quotes3"
CALLBACK_NAME = "parse"
CALLBACK_ARGS = None
COMMAND_LINE = "cd {0}; scrapy parse --spider={1} --callback={2} {3}"# --cbkwargs={3}"
FILE_PATH_PREFIX = "file://"
TEST_URL_01 = "/tutorial/tests/test_data/1"

full_path = os.path.realpath(__file__)
working_dir = "/".join(full_path.split('/')[:-3])
print(working_dir)



stream = os.popen(COMMAND_LINE.format(working_dir, SPIDER_NAME, CALLBACK_NAME, FILE_PATH_PREFIX + working_dir + TEST_URL_01)) #, CALLBACK_ARGS))
output = stream.read()
print(output)
