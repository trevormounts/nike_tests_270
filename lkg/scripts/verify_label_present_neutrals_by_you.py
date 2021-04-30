'''
This script verifies a label is present on the screen.
Using label_count you can check for the presence of n examples of the same label on the screen
Replace <your_label> below with the label name you gave your element in the test.ai GUI.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    context.verify(labels=["ttl_neutrals_by_you"], label_count=1)