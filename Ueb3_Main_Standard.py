import CommunicationManager as CM
import MachineLearningManager as ML
import threading
import time

# OPC UA
# [Aufgabe3] Parameter eintragen
OpcuaURL = ""
nodeIdsListUeb = [
    'ns=3;s="DB_OPC_UA"."IMS_5A_M0009682"."I_Eingaenge"."I_IMS5A_IL"',
    'ns=3;s="DB_OPC_UA"."IMS_5A_M0009682"."I_Eingaenge"."I_IMS5A_IR"'
]

# MQTT
# [Aufgabe3] Parameter eintragen
MqttUrl = ""
MqttPort =
MqttTimeout = 60
MqttTopics = ["esp32mag"]
WSTID = "001"

#Machine Learning
#[Aufgabe4] Instanz von MachineLearningManager erstellen


#Communication Manager
#[Aufgabe3] Instanz von CommunicationManager erstellen


#Prediction Thread
__startPredicitingThread = None

def __PredictErrors():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        # [Aufgabe3] Aktuellen Snapshot vom CommunicationManager erfassen

		# [Aufgabe3] Drei Arrays mit den Features für die Analyse Modelle erstellen. Diese Arrays mit Informationen aus dem Snapshot füllen
        #  Beispiel für Feature-Arrays (Parameter sind beispielhaft und nicht korrekt):
        # featuresStift = [snapshot[0], snapshot[2], snapshot[5]]  ???

        # [Aufgabe4] Modelle für Vorhersagen nutzen und Antworten auswerten

        # [Aufgabe5] Signal von Communication Manager bekommen, um Vorhersagen nur unter Station 5A machen.

        # [Aufgabe5] Vorhersagen nur unter Station 5A machen

		# [Vorgegeben] 0.5 Sekunden Pause um eine zyklische Vorhersage der Modelle zu ermöglichen
        time.sleep(0.5)

#Prediction Thread
__startPredicitingThread = threading.Thread(target=__PredictErrors, args=(), name="StartPredicting")


#[Aufgabe4] Methode für die zyklische Interpretation der Ergebnisse aus __PredictErrors implementieren und aufrufen
def handleResults(predictionStift):
    if(predictionStift == [1]):
        # Beispiel für OPC UA Write, um Warnlampe anzusprechen:
		#cm.writeStation('ns=3;s="DB_OPC_Meldesignale_13"."IMS_1_Meldungen"."LampeGelb"',False)
        #...
    #elif(predictionStift == [0]):
	#...
	#...
	#...


def startProgram():

    # [Aufgabe3] OPC UA Client erstellen und wichtige Parameter subscriben

    # [Aufgabe3] MQTT Client erstellen und wichtige Parameter subscriben

    # [Aufgabe3] Datenspeicherung starten

    # [Aufgabe4] machine learning Modelle für die Nutzung vorbereiten


    global __startPredicitingThread
    # [Aufgabe4] __startPredicitingThread starten, um mit der zyklischen Analyse zu starten


def turnOffLights():
    # [Aufgabe4] Methode implementieren, die alle Warnlampen unter Station 5A ausschaltet

def LightsGreen():
    # [Aufgabe4] Methode implementieren, die Lampe unter Station 5A auf Grün schaltet


# Definitionsabschnitt beendet
# Ausführung startet ab hier

print("Program Running")
print("Sie haben folgende Optionen:")
print("0 : Programm beenden")
print("1 : Programm starten")
print("2 : Lichter unter 5A ausschalten")
print("3 : Licht unter 5A auf Grün setzen")
__Run = True


while __Run == True:
    try:
        inputValue = input()
        if inputValue == "0":
			__startPredicitingThread.do_run = False
			# [Aufgabe4] Thread beenden (join)

            # [Aufgabe3] OPC UA und MQTT Datenerfassung beenden

            # [Aufgabe4] Dieses Programm beenden (Endlosschleife deaktivieren)

        elif inputValue == "1":
            # [Aufgabe4] Programmfunktionalität starten

        elif inputValue == "2":
            # [Aufgabe4] Alle Lichter am 5A ausschalten

        elif inputValue == "3":
            # [Aufgabe4] Licht am 5A auf Grün schalten

        else:
            print('Bitte eine Zahl zwischen 0 und 3 eingeben!')
    except ValueError as e:
        print('ValueError:', 'Bitte eine Zahl eingeben!')

