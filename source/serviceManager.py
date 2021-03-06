
"""
title           : serviceManger.py
description     : This class operates as Service Manager in PiCasso Architecture. It provides following functions:
                  a) instantiate Monitoring DB (InfluxDB container)
                  b) instantiate Monitoring web interface (grafana container)
                  c) create thread for monitoring Manager to fetch data from SEG
source          :
author          : Adisorn Lertsinsrubtavee
date            : 22 June 2017
version         : 1.0
contributors    :
usage           :
notes           :
compile and run : It is a python module imported by a main python programme.
python_version  : Python 2.7.12
====================================================
"""
import os
import sys
import time
import traceback
from threading import Timer, Thread, Event

from modules.DecisionEngine.decisionEngine_thread import Decision_Engine
from modules.Monitoring.monitoringManager_thread import Monitoring_Manager
from modules.ServiceRepo.serviceRepo_thread import Service_Repo


class ServiceManager(object):
    def __init__(self):
        self.namePrefix1 = '/picasso/monitoring/SEG_1/'
        self.namePrefix2 = '/picasso/monitoring/SEG_2/'
        self.namePrefix3 = '/picasso/monitoring/SEG_3/'
        self.namePrefix4 = '/picasso/monitoring/SEG_4/'
        self.namePrefix5 = '/picasso/monitoring/SEG_5/'
        self.namePrefix6 = '/picasso/monitoring/SEG_6/'
        self.namePrefix7 = '/picasso/monitoring/SEG_7/'
        self.namePrefix8 = '/picasso/monitoring/SEG_8/'
        self.namePrefix9 = '/picasso/monitoring/SEG_9/'
        self.namePrefix10 = '/picasso/monitoring/SEG_X/'
        self.namePrefix_DE = '/picasso/service_deployment_pull/'
        self.monitoring_frequency = 30

    def run(self):
        try:
            #instantiate DB here
            print 'Instantiate monitoring DB'
            os.system("docker rm -f $(docker ps -a -q)")
            os.system("docker run -p 8083:8083 -p 8086:8086 -d -v /home/picasso/influxdb:/var/lib/influxdb --name influxdb tutum/influxdb")
            # #instantiate Grafana
            os.system("docker run -d -p 3000:3000 --link influxdb --name grafana grafana/grafana")
            #Create Thread
            stopFlag = Event()
            print 'Start Monitoring Manager'
            # SEG1_monitoring = Monitoring_Manager(1, "Monitoring-Thread-1", 1, self.namePrefix1, stopFlag, self.monitoring_frequency)
            # SEG1_monitoring.start()
            # #
            # SEG2_monitoring = Monitoring_Manager(2, "Monitoring-Thread-2", 1, self.namePrefix2, stopFlag, self.monitoring_frequency)
            # SEG2_monitoring.start()
            #
            # SEG3_monitoring = Monitoring_Manager(3, "Monitoring-Thread-3", 1, self.namePrefix3, stopFlag, self.monitoring_frequency)
            # SEG3_monitoring.start()
            #
            # SEG4_monitoring = Monitoring_Manager(4, "Monitoring-Thread-4", 1, self.namePrefix4, stopFlag, self.monitoring_frequency)
            # SEG4_monitoring.start()
            #
            # SEG5_monitoring = Monitoring_Manager(5, "Monitoring-Thread-5", 1, self.namePrefix5, stopFlag, self.monitoring_frequency)
            # SEG5_monitoring.start()
            #
            # SEG6_monitoring = Monitoring_Manager(6, "Monitoring-Thread-6", 1, self.namePrefix6, stopFlag, self.monitoring_frequency)
            # SEG6_monitoring.start()
            #
            # SEG7_monitoring = Monitoring_Manager(7, "Monitoring-Thread-7", 1, self.namePrefix7, stopFlag, self.monitoring_frequency)
            # SEG7_monitoring.start()
            #
            # SEG8_monitoring = Monitoring_Manager(8, "Monitoring-Thread-8", 1, self.namePrefix8, stopFlag, self.monitoring_frequency)
            # SEG8_monitoring.start()
            #
            # SEG9_monitoring = Monitoring_Manager(9, "Monitoring-Thread-9", 1, self.namePrefix9, stopFlag, self.monitoring_frequency)
            # SEG9_monitoring.start()
            #
            # SEG10_monitoring = Monitoring_Manager(10, "Monitoring-Thread-10", 1, self.namePrefix10, stopFlag, self.monitoring_frequency)
            # SEG10_monitoring.start()

            print 'Start Decision Engine'
            DE = Decision_Engine(11, "DecisionEngine-Thread", self.namePrefix_DE)
            DE.start()

            #ServiceRepo = Service_Repo(8, "ServiceRepo-Thread", 2200)
            #ServiceRepo.start()

        except RuntimeError as e:
            print "ERROR: %s" %  e

        return True

if __name__ == '__main__':

    #nameInput  = raw_input('Enter Name of Content ')
    print 'Start Service Manager'
    try:
        ServiceManager().run()
    except:
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)
