import psutil
import configparser
from pathlib import Path
from datetime import datetime

pathtoconfig = Path("sanityconfig.conf")
path = pathtoconfig.name

def readConfig(somepath):
    readparser = configparser.RawConfigParser()
    readparser.read(somepath)
    output = readparser.get("Common", "output")
    interval = readparser.getint("Common", "interval")
    result = [output, interval]
    readparser.clear()
    return result

def writeConfigSample(somepath):
    writeparser = configparser.RawConfigParser()
    writeparser.add_section('Common')
    writeparser.set('Common', 'output', 'json')
    writeparser.set('Common', 'interval', '5')
    with open(somepath, 'w') as configfile:
        writeparser.write(configfile)
    writeparser.clear()


def defaults():
    output = "log"
    interval = 2
    result = [output, interval]
    return result

def sanityCheck(interval):
    CPU = str(psutil.cpu_percent(interval=interval, percpu=True))
    MEM =  str(psutil.swap_memory().used)
    VMEM = str(psutil.virtual_memory().used)
    IOinf = str(psutil.disk_io_counters())
    NET = str(psutil.net_if_stats())
    line = str(datetime.now().date()) + "\t" + str(datetime.now().strftime('%H:%M:%S')) + " : " + CPU + "\t" + MEM + "\t" + VMEM + "\t" + IOinf + "\t" + NET
    return line + "\n"

def executesanityCheck():
    if pathtoconfig.is_file():
        configuration = readConfig(path)
        outputpath = Path("sanity.%s" % configuration[0])
    else:
        configuration = defaults()
        outputpath = Path("sanity.%s" % configuration[0])

    if outputpath.is_file():
        m = "a"
    else:
        m = "w"
    outputfile = open(outputpath, mode=m)
    outputfile.write(sanityCheck(configuration[1]))
    outputfile.flush()
    outputfile.close()

#writeConfigSample(pathtoconfig)
executesanityCheck()
