from __future__ import division
import argparse
import csv
import mimetypes
import smtplib
import re
import sys
import shutil
import tinys3
from subprocess import call
from multiprocessing import Pool, Manager
from os import path
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from scrapy_balloons.stats.stats_collector import *
from scrapy_balloons.constant import *
from scrapy_balloons.utils.basefunctions import object_to_json
from scrapy_balloons.utils.datetimefunctions import time_display

MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = '587'
MAIL_FROM = 'scraper.skilledup@gmail.com'
MAIL_PASS = 'Skilledup2014'

# S3 CREDENTIAL
S3_ACCESS_KEY = 'AKIAJ35FIFXQ5SLKT25A'
S3_SECRET_KEY = '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'
S3_ENDPOINT = 's3-us-west-1.amazonaws.com'

TIME_NOTIFICATION_BY_EMAIL = 36000
TIMEOUT_SCRAPER = 86400
S3_REPORTS_BUCKET = "test-skilledup-products"
S3_REPORTS_FOLDER = "rerun_all_reports"


COMPRESS_NAME = 'compress'
LOGS_NAME = 'logs'
OUTPUT_NAME = 'output'
SUMMARY_JSON_NAME = 'summary.json'
SUMMARY_CSV_NAME = "summary.csv"
LISTENER_KILL_SIGNAL = 'KILL'

if __name__ == "__main__":
    conn = tinys3.Connection(S3_ACCESS_KEY, S3_SECRET_KEY, tls=True, endpoint=S3_ENDPOINT)
    data = list(conn.list("%s/json"%(S3_REPORTS_FOLDER) ,S3_REPORTS_BUCKET))
    file_names = [i['key'] for i in data]
    for name in file_names:
        output = conn.get(name,S3_REPORTS_BUCKET)
        import pdb
        pdb.set_trace()


