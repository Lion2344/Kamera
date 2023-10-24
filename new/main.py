import sdcard

import microcontroller

#sdcard.WriteNewFile(entry= 'Hallo', file_name='test.txt', method='r')
for i in range(5):
    if i == 0:
        sdcard.ReadWriteToSD(entry= i, file_name='test.txt', method='w')
    else:
        sdcard.ReadWriteToSD(entry= i, file_name='test.txt', method='a')
        
sdcard.ReadWriteToSD(entry= i, file_name='test.txt', method='r')