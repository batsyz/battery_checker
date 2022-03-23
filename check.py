from os.path import isfile
from re import findall
from subprocess import run, DEVNULL
from tempfile import gettempdir

def theNumbers (biggerNumber, smallerNumber):
   divideFirst = smallerNumber / biggerNumber
   multiplySecond = divideFirst * 100
   roundOffValue = round(multiplySecond, 2)
   if roundOffValue >= 90:
      print("{} percentage efficiency!\nYour battery is in excellent condition.".format(roundOffValue))
   elif roundOffValue >= 60:
      print("{} percentage efficiency!\nYour battery is in good condition.".format(roundOffValue))
   else:
      print("{} percentage efficiency!\nConsider changing your battery ASAP!".format(roundOffValue))
   run('del "{}"\\batteryreport.xml /Q /A'.format(TEMPDIR), shell=True, text=True, stdout=DEVNULL, stderr=DEVNULL)
   return

# Check for file existance
TEMPDIR = gettempdir()
if isfile(TEMPDIR + '\\batteryreport.xml') == False:
   run("powercfg /BATTERYREPORT /OUTPUT %TEMP%\\batteryreport.xml /XML", shell=True, text=True, stdout=DEVNULL, stderr=DEVNULL)

# Open the report and search for matching pattern
with open (TEMPDIR + '\\batteryreport.xml', 'r') as batteryReport:
   openReport = batteryReport.read()
getValues = findall(r"<Capacity>(.+?)</Capacity>", openReport)
biggerNumber = int(getValues[0])
smallerNumber = int(getValues[1])

# Call the function
theNumbers (biggerNumber, smallerNumber)
#EOF
