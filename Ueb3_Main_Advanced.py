import CommunicationManager as CM
import MachineLearningManager as ML
import threading
import time

# OPC UA
# [Aufgabe3] Parameter eintragen
OpcuaURL = ""
nodeIdsListUeb = [
    '...',
    '...'
]

# MQTT
# [Aufgabe3] Parameter eintragen
MqttUrl = ""
MqttPort = 
MqttTimeout = 60
MqttTopics = ["esp32mag"]
WSTID = "001"

# [Aufgabe3,4] Objekte der Helferklassen instanziieren



#[Vorgegeben] Prediction Thread Erstellung
__startPredicitingThread = None

def __PredictErrors():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
		# [Aufgabe3] Arrays mit den Features für die Analyse Modelle erstellen und füllen

        # [Aufgabe4] Anschließend Modelle für Vorhersagen nutzen und Antworten auswerten

        # [Aufgabe5] Vorhersagen nur unter Station 5A machen

		# [Vorgegeben] 0.5 Sekunden Pause um eine zyklische Vorhersage der Modelle zu ermöglichen
        time.sleep(0.5) 

#[Vorgegeben] Prediction Thread Zuweisung
__startPredicitingThread = threading.Thread(target=__PredictErrors, args=(), name="StartPredicting")


#[Aufgabe3] Methode für die Interpretation von Modell-Vorhersagen implementieren
def handleResults(predictionStift):
    if(predictionStift == [1]):
        # [Aufgabe3] Mit OPC UA Write die Warnlampen ansprechen
	#...
	#...
	#...


def startProgram():

    # [Aufgabe4] Clients erstellen und Subcription anlegen

    # [Aufgabe4] Datenspeicherung starten

    # [Aufgabe4] Modelle für die Nutzung vorbereiten
	
	
	#[Vorgegeben] globalen PredictionThread in startProgram-Umgebung laden
    global __startPredicitingThread
    # [Aufgabe3] __startPredicitingThread starten, um mit der zyklischen Analyse zu starten


print("Program Running")
print("Sie haben folgende Optionen:")
print("0 : Programm beenden")
print("1 : Programm starten")
print("2 : Lichter unter 5A ausschalten")
print("3 : Licht unter 5A auf Grün setzen")
__Run = True


while __Run == True:
    try:
        #[Aufgabe4] Benutzereingabe erfassen
        if 'Benutzereingabe' == "0":
			__startPredicitingThread.do_run = False
			# [Aufgabe4] Thread beenden

            # [Aufgabe3] Datenerfassung beenden

            # [Aufgabe4] Dieses Programm beenden

        elif 'Benutzereingabe' == "1":
			# [Aufgabe4] Programm starten
        elif 'Benutzereingabe' == "2":
			# [Aufgabe4] Lichter unter 5A ausschalten
        elif 'Benutzereingabe' == "3":
			# [Aufgabe4] Licht unter 5A auf Grün setzen
        else:
            print('Bitte eine Zahl zwischen 0 und 3 eingeben!')
    except ValueError as e:
        print('ValueError:', 'Bitte eine Zahl eingeben!')

