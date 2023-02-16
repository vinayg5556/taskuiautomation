#!/bin/bash
pytest --disable-warnings -s ..//Tests/test_search.py --html=..//Reports/completeTestsReport.html --verbose --capture=tee-sys