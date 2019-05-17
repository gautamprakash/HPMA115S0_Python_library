import HPMA115S0
import time
import sys
import urllib.request
import I2C_LCD_driver

myAPI = 'Y9B2USVR7W1CKW67'
baseURL = 'http://rbiot.solveninja.org:3000/update?api_key=%s' % myAPI
mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Breathe",1,0)

try:
    print("Starting")
    hpma115S0 = HPMA115S0.HPMA115S0("/dev/ttyS0")

    hpma115S0.init()
    hpma115S0.startParticleMeasurement()

    while 1:
        if (hpma115S0.readParticleMeasurement()):
            pm2_5 = (hpma115S0._pm2_5)
            mylcd.lcd_clear()
            mylcd.lcd_display_string("PM2.5: " + str(pm2_5),1,0)
            print("PM2.5: %d ug/m3" % (pm2_5))
            print("PM10: %d ug/m3" % (hpma115S0._pm10))
            conn = urllib.request.urlopen('http://rbiot.solveninja.org:3000/update?api_key='+(myAPI)+'&field1='+str(pm2_5))
            print (conn)
            print (conn.read())
            conn.close()
        time.sleep(5)

except KeyboardInterrupt:
    print("program stopped")
