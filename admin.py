#!usr/bin/env python

import threading
import os
import re
import sys
import urllib2

from threading import Thread

def main():

 sublink = open("admin.txt", "r")
address = "http://site.com"
request = ("address"+"/"+"sublink")
print("Scanning For Admin Panel")
if request in request == "200":
 vuln =open("vuln.txt", "w")
print("Found Admin Panel!")
 


def checkUrl(url):
    r = requests.get(url, timeout=20)
    #print r.status_code
    return str(r.status_code)

def printStatus(url, status):
 if status == "200":
        print("Server is up!")
 if status != "200":
        print("Server is down!")

def checkRobot(self,address):
        print("Checking for robot file")
        path = ("robot.txt","robots.txt")
        keyword = ["admin","Administrator","controlpanel", "phpmyadmin"
                   "wp-admin","cpanel","userpanel","client","account", "pma"]
        url = ("address" + "keyword" in "robots.txt")
        if url == "200":
             vuln =open("vuln.txt", "w")
             print("Admin page found")
class wordlist:
    def __init__(self):
        try:
            self.load = [i.replace('\n', '') for i in open('admin.txt').readlines()]
        except IOError:
            print("[!] I/O Error, admin.txt not found")
       
class MyThread(Thread):
    def __init__(self, val):
        Thread.__init__(self)
        self.val = val
 
 
    def run(self):
        for i in range(1, self.val):
            print('Value %d in thread %s' % (i, self.getName()))
            secondsToSleep = randint(1,10)
            print('%s sleeping fo %d seconds...' % (self.getName(), secondsToSleep))
            time.sleep(secondsToSleep)




reply = str(raw_input(bcolors.BOLD +' Do you want to continue scan for more possible results? (y/n): ')).lower().strip()
