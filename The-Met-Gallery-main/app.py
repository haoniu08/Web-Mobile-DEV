'''
Hao Niu
CS 5001, Fall 2023
Final Project

This is the file that runs this application
'''

import sys
from streamlit.web import cli as stcli

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "main.py"]
    sys.exit(stcli.main())
