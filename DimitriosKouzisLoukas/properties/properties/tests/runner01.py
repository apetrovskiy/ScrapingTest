import os

SPIDER_NAME = "basic"
CALLBACK_NAME = "parse"
CALLBACK_ARGS = None
COMMAND_LINE = "cd {0}; scrapy parse --spider={1} --callback={2} {3}"# --cbkwargs={3}"
FILE_PATH_PREFIX = "file://"
TEST_URL_01 = "/properties/tests/test_data/1"

full_path = os.path.realpath(__file__)
working_dir = "/".join(full_path.split('/')[:-3])
print(working_dir)



stream = os.popen(COMMAND_LINE.format(working_dir, SPIDER_NAME, CALLBACK_NAME, "http://localhost:9312/properties/index_00000.html"))
#, CALLBACK_ARGS))
output = stream.read()
print(output)
