import unittest
from courseprocesser import processcourse
import codecs
import json

class TestCourseProcessing(unittest.TestCase):
    def test_Single(self):
    	# basic test
        course = codecs.open("testdata/BUSF-SHU 206.testjson", "r", "utf-8").read()
        course = json.loads(course)
        processcourse(course)
        self.assertEqual(course["name"], "BUSF-SHU 206")
        self.assertEqual(course["title"], "Investing And Financing In And With China")
        section = course["components"][0]
        self.assertEqual(section["number"], 19819)
        self.assertEqual(section["section"], "001")
        # self.assertEqual(section["status"], "Wait List (5)")
        self.assertEqual(section["location"], "Shanghai")
        self.assertEqual(section["componentType"], "Lecture")
        self.assertEqual(section["notes"], "This course satisfies the following: Major: BUSF: additional finance elective;BUSM: non-marketing elective")
        self.assertEqual(section["units"], 4)
        self.assertEqual(section["classtimes"], [{
                "day": 0,
                "starttime": [13, 15],
                "endtime": [16, 15]
            }])
        self.assertEqual(section["instructor"], "Yu, Da")

    def test_ignoreTestdates(self):
    	# ignore any single-day classtimes. eg: 12/15/2016-12/15/2016, 2-5.
        course = codecs.open("testdata/CHIN-SHU 2-1S1.testjson", "r", "utf-8").read()
        course = json.loads(course)
        processcourse(course)
        section = course["components"][0]
        self.assertEqual(len(section["classtimes"]), 2)

    def test_multipleDateLines(self):
    	# some classes have sessions at eg. Mon/Wed 1pm, then one on Thu 3pm.
    	course = codecs.open("testdata/CHIN-SHU 403.testjson", "r", "utf-8").read()
        course = json.loads(course)
        processcourse(course)
        section = course["components"][0]
        self.assertEqual(len(section["classtimes"]), 3)

    def test_hasTopic(self):
    	course = codecs.open("testdata/BUSF-SHU 220.testjson", "r", "utf-8").read()
        course = json.loads(course)
        processcourse(course)
        section = course["components"][0]
        self.assertEqual(section["topic"], "Chinese and International Accounting")
        self.assertEqual(len(section["classtimes"]), 2)

    def test_Components(self):
        course = codecs.open("testdata/CSCI-SHU 101.testjson", "r", "utf-8").read()
        course = json.loads(course)
        processcourse(course)
        self.assertIn("requiredcomponents", course)
        reqs = course["requiredcomponents"]
        self.assertIn("Lecture", reqs)
        self.assertIn("Recitation", reqs)

unittest.main()