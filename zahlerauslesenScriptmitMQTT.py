#!/usr/bin/env python3

import time
import minimalmodbus
import time
import paho.mqtt.client as mqtt

durchlaufzaehler = 0

# Konfiguration MQTT
broker_address = "192.168.1.167"
client = mqtt.Client("Garagenzaehlerauslesecleint")  # create new instance
client.connect(broker_address)  # connect to broker

# Konfiguration der Zähler Haus
Hausverbrauch = minimalmodbus.Instrument('/dev/ttyUSB0', 2)
Hausverbrauch.serial.baudrate = 9600
Hausverbrauch.serial.bytesize = 8
Hausverbrauch.serial.parity = minimalmodbus.serial.PARITY_NONE
Hausverbrauch.serial.stopbits = 1
Hausverbrauch.serial.timeout = 1
Hausverbrauch.mode = minimalmodbus.MODE_RTU

# Konfiguration der Zähler Wallbox
Wallbox = minimalmodbus.Instrument('/dev/ttyUSB0', 36)
Wallbox.serial.baudrate = 9600
Wallbox.serial.bytesize = 8
Wallbox.serial.parity = minimalmodbus.serial.PARITY_NONE
Wallbox.serial.stopbits = 1
Wallbox.serial.timeout = 1
Wallbox.mode = minimalmodbus.MODE_RTU

# Auslesen der Zähler (HV=Hausverbrauch)

while(1):
    fehler = "nein"

    try:
        HV_A_Phase_Spannung = round(Hausverbrauch.read_float(0, functioncode=4, number_of_registers=2), 2)
        HV_B_Phase_Spannung = round(Hausverbrauch.read_float(2, functioncode=4, number_of_registers=2), 2)
        HV_C_Phase_Spannung = round(Hausverbrauch.read_float(4, functioncode=4, number_of_registers=2), 2)

        HV_A_Phase_Strom = round(Hausverbrauch.read_float(8, functioncode=4, number_of_registers=2), 3)
        HV_B_Phase_Strom = round(Hausverbrauch.read_float(10, functioncode=4, number_of_registers=2), 3)
        HV_C_Phase_Strom = round(Hausverbrauch.read_float(12, functioncode=4, number_of_registers=2), 3)

        HV_KompletteWirkleistung = round(Hausverbrauch.read_float(16, functioncode=4, number_of_registers=2), 2)
        HV_A_Phase_Wirkleistung = round(Hausverbrauch.read_float(18, functioncode=4, number_of_registers=2), 2)
        HV_B_Phase_Wirkleistung = round(Hausverbrauch.read_float(20, functioncode=4, number_of_registers=2), 2)
        HV_C_Phase_Wirkleistung = round(Hausverbrauch.read_float(22, functioncode=4, number_of_registers=2), 2)

        HV_KompletteBlindleistung = round(Hausverbrauch.read_float(24, functioncode=4, number_of_registers=2), 2)
        HV_A_Phase_Blindleistung = round(Hausverbrauch.read_float(26, functioncode=4, number_of_registers=2), 2)
        HV_B_Phase_Blindleistung = round(Hausverbrauch.read_float(28, functioncode=4, number_of_registers=2), 2)
        HV_C_Phase_Blindleistung = round(Hausverbrauch.read_float(30, functioncode=4, number_of_registers=2), 2)

        HV_A_Phase_Leistungsfaktor = round(Hausverbrauch.read_float(42, functioncode=4, number_of_registers=2), 2)
        HV_B_Phase_Leistungsfaktor = round(Hausverbrauch.read_float(44, functioncode=4, number_of_registers=2), 2)
        HV_C_Phase_Leistungsfaktor = round(Hausverbrauch.read_float(46, functioncode=4, number_of_registers=2), 2)

        HV_Frequenz = round(Hausverbrauch.read_float(54, functioncode=4, number_of_registers=2), 2)

        HV_Gesamte_verbrauchte_Wirkleistung = round(Hausverbrauch.read_float(256, functioncode=4, number_of_registers=2), 2)
        HV_Gesamte_verbrauchte_Blindleistung = round(Hausverbrauch.read_float(1024, functioncode=4, number_of_registers=2), 2)
    except:
        print("Etwas ist beim einlesen des Hauszählers schief gelaufen")
        fehler = "ja"

    time.sleep(1)

    # Auslesen WallboxZaehler

    try:

        WB_A_Phase_Spannung = round(Wallbox.read_float(0, functioncode=4, number_of_registers=2), 2)
        WB_B_Phase_Spannung = round(Wallbox.read_float(2, functioncode=4, number_of_registers=2), 2)
        WB_C_Phase_Spannung = round(Wallbox.read_float(4, functioncode=4, number_of_registers=2), 2)

        WB_A_Phase_Strom = round(Wallbox.read_float(8, functioncode=4, number_of_registers=2), 3)
        WB_B_Phase_Strom = round(Wallbox.read_float(10, functioncode=4, number_of_registers=2), 3)
        WB_C_Phase_Strom = round(Wallbox.read_float(12, functioncode=4, number_of_registers=2), 3)

        WB_KompletteWirkleistung = round(Wallbox.read_float(16, functioncode=4, number_of_registers=2), 2)
        WB_A_Phase_Wirkleistung = round(Wallbox.read_float(18, functioncode=4, number_of_registers=2), 2)
        WB_B_Phase_Wirkleistung = round(Wallbox.read_float(20, functioncode=4, number_of_registers=2), 2)
        WB_C_Phase_Wirkleistung = round(Wallbox.read_float(22, functioncode=4, number_of_registers=2), 2)

        WB_KompletteBlindleistung = round(Wallbox.read_float(24, functioncode=4, number_of_registers=2), 2)
        WB_A_Phase_Blindleistung = round(Wallbox.read_float(26, functioncode=4, number_of_registers=2), 2)
        WB_B_Phase_Blindleistung = round(Wallbox.read_float(28, functioncode=4, number_of_registers=2), 2)
        WB_C_Phase_Blindleistung = round(Wallbox.read_float(30, functioncode=4, number_of_registers=2), 2)

        WB_A_Phase_Leistungsfaktor = round(Wallbox.read_float(42, functioncode=4, number_of_registers=2), 2)
        WB_B_Phase_Leistungsfaktor = round(Wallbox.read_float(44, functioncode=4, number_of_registers=2), 2)
        WB_C_Phase_Leistungsfaktor = round(Wallbox.read_float(46, functioncode=4, number_of_registers=2), 2)

        WB_Frequenz = round(Wallbox.read_float(54, functioncode=4, number_of_registers=2), 2)

        WB_Gesamte_verbrauchte_Wirkleistung = round(Wallbox.read_float(256, functioncode=4, number_of_registers=2), 2)
        WB_Gesamte_verbrauchte_Blindleistung = round(Wallbox.read_float(1024, functioncode=4, number_of_registers=2), 2)
    except:
        print("Irgendwas ist beim Auslesen des Wallboxzählers schief gelaufen")
        fehler = "ja"

# HausPrints - str convertiert Float zu String, f' {varibale: .2f} kürzt Nachkommastellen

    try:

        print("Hausverbrauchszähler:\n")
        print(str(HV_A_Phase_Spannung) + "V -Phase A")
        print(str(HV_B_Phase_Spannung) + "V -Phase B")
        print(str(HV_C_Phase_Spannung) + "V -Phase C\n")

        print(str(HV_A_Phase_Strom) + "A -Phase A")
        print(str(HV_B_Phase_Strom) + "A -Phase B")
        print(str(HV_C_Phase_Strom) + "A -Phase C\n")

        print(str(HV_KompletteWirkleistung) + "W -Alle Phasen")
        print(str(HV_A_Phase_Wirkleistung) + "W -Phase A")
        print(str(HV_B_Phase_Wirkleistung) + "W -Phase B")
        print(str(HV_C_Phase_Wirkleistung) + "W -Phase C\n")

        print(str(HV_KompletteBlindleistung) + "W -Alle Phasen Blindleistung")
        print(str(HV_A_Phase_Leistungsfaktor) + "φ -Phase A")
        print(str(HV_B_Phase_Leistungsfaktor) + "φ -Phase B")
        print(str(HV_C_Phase_Leistungsfaktor) + "φ -Phase C\n")

        print(str(HV_Frequenz)+"Hz\n")

        print(str(HV_Gesamte_verbrauchte_Blindleistung) + "kWh Gesamte Verbrauchte Blind -Wh\n")
        print(str(HV_Gesamte_verbrauchte_Wirkleistung) + "kWh Gesamte Verbrauchte kWh\n")
    except:
        print("Irgendwas ist beim Ausgeben der Hausdaten schief gelaufen/n")
        fehler = "ja"

# Wallbox Prints

    try:
        print("WallboxZähler\n")
        print(str(WB_A_Phase_Spannung) + "V -Phase A")
        print(str(WB_B_Phase_Spannung) + "V -Phase B")
        print(str(WB_C_Phase_Spannung) + "V -Phase C\n")

        print(str(WB_A_Phase_Strom) + "A -Phase A")
        print(str(WB_B_Phase_Strom) + "A -Phase B")
        print(str(WB_C_Phase_Strom) + "A -Phase C\n")

        print(str(WB_KompletteWirkleistung) + "W -Alle Phasen")
        print(str(WB_A_Phase_Wirkleistung) + "W -Phase A")
        print(str(WB_B_Phase_Wirkleistung) + "W -Phase B")
        print(str(WB_C_Phase_Wirkleistung) + "W -Phase C\n")

        print(str(WB_KompletteBlindleistung) + "W -Alle Phasen Blindleistung")
        print(str(WB_A_Phase_Leistungsfaktor) + "φ -Phase A")
        print(str(WB_B_Phase_Leistungsfaktor) + "φ -Phase B")
        print(str(WB_C_Phase_Leistungsfaktor) + "φ -Phase C\n")

        print(str(WB_Frequenz)+"Hz\n")

        print(str(WB_Gesamte_verbrauchte_Blindleistung) + "kWh Gesamte Verbrauchte Blind -Wh\n")
        print(str(WB_Gesamte_verbrauchte_Wirkleistung) + "kWh Gesamte Verbrauchte kWh\n")
        durchlaufzaehler = durchlaufzaehler+1
        print(str(durchlaufzaehler) + "mal Durchgelaufen")
    except:
        print("Irgendwas ist beim Ausgeben der Wallboxdaten schief gelaufen")
        fehler = "ja"

# Hauszaehlerdaten publizieren
    try:
        client.publish("zaehler/Hauszaehler/AktuelleSpannungPhase1", HV_A_Phase_Spannung)
        client.publish("zaehler/Hauszaehler/AktuelleSpannungPhase2", HV_B_Phase_Spannung)
        client.publish("zaehler/Hauszaehler/AktuelleSpannungPhase3", HV_C_Phase_Spannung)

        client.publish("zaehler/Hauszaehler/AktuellerStromPhase1", HV_A_Phase_Strom)
        client.publish("zaehler/Hauszaehler/AktuellerStromPhase2", HV_B_Phase_Strom)
        client.publish("zaehler/Hauszaehler/AktuellerStromPhase3", HV_C_Phase_Strom)

        client.publish("zaehler/Hauszaehler/AktuelleWirkleistungGesamt", HV_KompletteWirkleistung)
        client.publish("zaehler/Hauszaehler/AktuelleWirkleistungPhase1", HV_A_Phase_Wirkleistung)
        client.publish("zaehler/Hauszaehler/AktuelleWirkleistungPhase2", HV_B_Phase_Wirkleistung)
        client.publish("zaehler/Hauszaehler/AktuelleWirkleistungPhase3", HV_C_Phase_Wirkleistung)

        client.publish("zaehler/Hauszaehler/AktuelleBlindleistungGesamt", HV_KompletteBlindleistung)
        client.publish("zaehler/Hauszaehler/AktuelleWirkleistungPhase1", HV_A_Phase_Blindleistung)
        client.publish("zaehler/Hauszaehler/AktuelleWirkleistungPhase2", HV_B_Phase_Blindleistung)
        client.publish("zaehler/Hauszaehler/AktuelleWirkleistungPhase3", HV_C_Phase_Blindleistung)

        client.publish("zaehler/Hauszaehler/Leistungsfaktor1", HV_A_Phase_Leistungsfaktor)
        client.publish("zaehler/Hauszaehler/Leistungsfaktor2", HV_B_Phase_Leistungsfaktor)
        client.publish("zaehler/Hauszaehler/Leistungsfaktor3", HV_C_Phase_Leistungsfaktor)

        client.publish("zaehler/Hauszaehler/Frequenz", HV_Frequenz)

        client.publish("zaehler/Hauszaehler/WirkleisungGesamt", HV_Gesamte_verbrauchte_Wirkleistung)
        client.publish("zaehler/Hauszaehler/BlindleistungGesamt", HV_Gesamte_verbrauchte_Blindleistung)

    except:
        print("Irgendwas ist beim publizieren der Hausverbrauchsdaten schief gelaufen")
        fehler = "ja"

 #  Wallboxzaehler publizieren

    try:
        client.publish("zaehler/Wallboxzaehler/AktuelleSpannungPhase1", WB_A_Phase_Spannung)
        client.publish("zaehler/Wallboxzaehler/AktuelleSpannungPhase2", WB_B_Phase_Spannung)
        client.publish("zaehler/Wallboxzaehler/AktuelleSpannungPhase3", WB_C_Phase_Spannung)

        client.publish("zaehler/Wallboxzaehler/AktuellerStromPhase1", WB_A_Phase_Strom)
        client.publish("zaehler/Wallboxzaehler/AktuellerStromPhase2", WB_B_Phase_Strom)
        client.publish("zaehler/Wallboxzaehler/AktuellerStromPhase3", WB_C_Phase_Strom)

        client.publish("zaehler/Wallboxzaehler/AktuelleWirkleistungGesamt", WB_KompletteWirkleistung)
        client.publish("zaehler/Wallboxzaehler/AktuelleWirkleistungPhase1", WB_A_Phase_Wirkleistung)
        client.publish("zaehler/Wallboxzaehler/AktuelleWirkleistungPhase2", WB_B_Phase_Wirkleistung)
        client.publish("zaehler/Wallboxzaehler/AktuelleWirkleistungPhase3", WB_C_Phase_Wirkleistung)

        client.publish("zaehler/Wallboxzaehler/AktuelleBlindleistungGesamt", WB_KompletteBlindleistung)
        client.publish("zaehler/Wallboxzaehler/AktuelleWirkleistungPhase1", WB_A_Phase_Blindleistung)
        client.publish("zaehler/Wallboxzaehler/AktuelleWirkleistungPhase2", WB_B_Phase_Blindleistung)
        client.publish("zaehler/Wallboxzaehler/AktuelleWirkleistungPhase3", WB_C_Phase_Blindleistung)

        client.publish("zaehler/Wallboxzaehler/Leistungsfaktor1", WB_A_Phase_Leistungsfaktor)
        client.publish("zaehler/Wallboxzaehler/Leistungsfaktor2", WB_B_Phase_Leistungsfaktor)
        client.publish("zaehler/Wallboxzaehler/Leistungsfaktor3", WB_C_Phase_Leistungsfaktor)

        client.publish("zaehler/Wallboxzaehler/Frequenz", WB_Frequenz)

        client.publish("zaehler/Wallboxzaehler/WirkleisungGesamt", WB_Gesamte_verbrauchte_Wirkleistung)
        client.publish("zaehler/Wallboxzaehler/BlindleistungGesamt", WB_Gesamte_verbrauchte_Blindleistung)

    except:
        print("Irgendwas ist beim publizieren der Wallboxdaten schief gelaufen")
        fehler = "ja"

    client.publish("zaehler/Fehler", fehler)
    time.sleep(10)