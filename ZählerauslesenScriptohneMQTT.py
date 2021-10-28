#!/usr/bin/env python3

import time
import minimalmodbus

# Konfiguration der Zähler
Hausverbrauch = minimalmodbus.Instrument('/dev/ttyUSB1', 2)
Hausverbrauch.serial.baudrate = 9600
Hausverbrauch.serial.bytesize = 8
Hausverbrauch.serial.parity = minimalmodbus.serial.PARITY_NONE
Hausverbrauch.serial.stopbits = 1
Hausverbrauch.serial.timeout = 1
Hausverbrauch.mode = minimalmodbus.MODE_RTU

# Auslesen der Zähler (HV=Hausverbrauch)

HV_A_Phase_Spannung = Hausverbrauch.read_float(0, functioncode=4, number_of_registers=2) 
HV_B_Phase_Spannung = Hausverbrauch.read_float(2, functioncode=4, number_of_registers=2) 
HV_C_Phase_Spannung = Hausverbrauch.read_float(4, functioncode=4, number_of_registers=2) 

HV_A_Phase_Strom = Hausverbrauch.read_float(8, functioncode=4, number_of_registers=2)
HV_B_Phase_Strom = Hausverbrauch.read_float(10, functioncode=4, number_of_registers=2) 
HV_C_Phase_Strom = Hausverbrauch.read_float(12, functioncode=4, number_of_registers=2) 

HV_KompletteWirkleistung = Hausverbrauch.read_float(16, functioncode=4, number_of_registers=2) 
HV_A_Phase_Wirkleistung = Hausverbrauch.read_float(18, functioncode=4, number_of_registers=2) 
HV_B_Phase_Wirkleistung = Hausverbrauch.read_float(20, functioncode=4, number_of_registers=2) 
HV_C_Phase_Wirkleistung = Hausverbrauch.read_float(22, functioncode=4, number_of_registers=2) 

HV_KompletteBlindleistung = Hausverbrauch.read_float(24, functioncode=4, number_of_registers=2)
HV_A_Phase_Blindleistung = Hausverbrauch.read_float(26, functioncode=4, number_of_registers=2) 
HV_B_Phase_Blindleistung = Hausverbrauch.read_float(28, functioncode=4, number_of_registers=2) 
HV_C_Phase_Blindleistung = Hausverbrauch.read_float(30, functioncode=4, number_of_registers=2) 

HV_A_Phase_Leistungsfaktor = Hausverbrauch.read_float(42, functioncode=4, number_of_registers=2) 
HV_B_Phase_Leistungsfaktor = Hausverbrauch.read_float(44, functioncode=4, number_of_registers=2) 
HV_C_Phase_Leistungsfaktor = Hausverbrauch.read_float(46, functioncode=4, number_of_registers=2) 

HV_Frequenz = Hausverbrauch.read_float(54, functioncode=4, number_of_registers=2)

HV_Gesamte_verbrauchte_Wirkleistung = Hausverbrauch.read_float(256, functioncode=4, number_of_registers=2) 
HV_Gesamte_verbrauchte_Blindleistung = Hausverbrauch.read_float(1024, functioncode=4, number_of_registers=2) 

#Prints - str convertiert Float zu String, f' {varibale: .2f} kürzt Nachkommastellen

print(str(f'{HV_A_Phase_Spannung :.2f}')+"V -Phase A")
print(str(f'{HV_B_Phase_Spannung:.2f}')+"V -Phase B")
print(str(f'{HV_C_Phase_Spannung:.2f}')+"V -Phase C\n")

print(str(f'{HV_A_Phase_Strom:.3f}')+"A -Phase A")
print(str(f'{HV_B_Phase_Strom:.3f}')+"A -Phase B")
print(str(f'{HV_C_Phase_Strom:.3f}')+"A -Phase C\n")

print(str(f'{HV_KompletteWirkleistung:.2f}')+"W -Alle Phasen")
print(str(f'{HV_A_Phase_Wirkleistung:.2f}')+"W -Phase A")
print(str(f'{HV_B_Phase_Wirkleistung:.2f}')+"W -Phase B")
print(str(f'{HV_C_Phase_Wirkleistung:.2f}')+"W -Phase C\n")

print(str(f'{HV_A_Phase_Leistungsfaktor:.2f}')+"φ -Phase A")
print(str(f'{HV_B_Phase_Leistungsfaktor:.2f}')+"φ -Phase B")
print(str(f'{HV_C_Phase_Leistungsfaktor:.2f}')+"φ -Phase C\n")

print(str(f'{HV_Frequenz:.2f}')+"Hz\n")

print(str(f'{HV_Gesamte_verbrauchte_Wirkleistung:.4f}')+"kWh Gesamte Verbrauchte kWh\n")

 
