import CommunicationManager as CM
import MachineLearningManager as ML
import threading
import time

#OPC UA
OpcuaURL = "opc.tcp://141.58.122.39:4840"
nodeIdsListUeb = [
    'ns=3;s="DB_OPC_UA"."IMS_5A_M0009682"."I_Eingaenge"."I_IMS5A_IL"',
    'ns=3;s="DB_OPC_UA"."IMS_5A_M0009682"."I_Eingaenge"."I_IMS5A_B4"'
]

#MQTT
MqttUrl = "141.58.103.26"
MqttPort = 1883
MqttTimeout = 60
MqttTopics = ["esp32mag"]
WSTID = "001"

#Machine Learning
ml = ML.MachineLearning()

#Communication Manager
cm = CM.CommunicationManager(WSTID)

#Prediction Thread
__startPredicitingThread = None

def __PredictErrors():
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        snapshot = cm.getDataSnapshot()
        print(snapshot)

        predictionStift = [0]

        Predict_Stift_label = cm.Station5APresent[0]
        print("Predict_Stift_label:" + str(Predict_Stift_label))
        if (Predict_Stift_label == True):
            featuresStift = [snapshot[0], snapshot[1], snapshot[2]]
            print("featuresStift: {0}".format(featuresStift))
            predictionStift = ml.predictStift(featuresStift)
            print("predictionStift: {0}\n".format(predictionStift))
            handleResults(predictionStift)
        time.sleep(0.5)


#Prediction Thread
__startPredicitingThread = threading.Thread(target=__PredictErrors, args=(), name="StartPredicting")

def handleResults(predictionStift):
    # Handle predictions
    if(predictionStift == [1]): #1: richtig
        #print('************************')
        cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeGruen"',True)
        cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeGelb"',False)
        cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeRot"',False)
    elif(predictionStift == [2]): #2: Unbekannt
        cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeGruen"', False)
        cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeGelb"', True)
        cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeRot"', False)
    elif (predictionStift == [0]):  # : falsh
        cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeGruen"', False)
        cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeGelb"', False)
        cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeRot"', True)

def startProgram():
    # Start getting OPC UA values and create 1. Thread
    cm.OPCUA_createClient(OpcuaURL)
    cm.OPCUA_subscribe(nodeIdsListUeb)

    # Start getting MQTT values and create 2. Thread
    cm.MQTT_CreateClient(MqttUrl, MqttPort, MqttTimeout)
    cm.MQTT_subscribeToTopic(MqttTopics)
    cm.MQTT_startClient()

    # Start Collecting Data from queue
    cm.startCollectingData()

    # Call Machine Learning Model to analyse captured data
    ml.prepareModels()
    global __startPredicitingThread
    __startPredicitingThread.start()

    turnOffLights()


def turnOffLights():
    cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeGruen"', False)
    cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeOrange"', False)
    cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeRed"', False)

def LightsGreen():
    cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeGruen"', True)
    cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeOrange"', False)
    cm.writeStation('ns=3;s="DB_OPC_Meldesignale"."IMS_5A_Meldungen"."LampeRed"', False)

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
            print("0")
            __startPredicitingThread.do_run = False
            __startPredicitingThread.join()
            cm.endofProgramm()
            __Run = False
        elif inputValue == "1":
            print("1")
            startProgram()
        elif inputValue == "2":
            print("2")
            turnOffLights()
        elif inputValue == "3":
            print("3")
            LightsGreen()
        else:
            print('Bitte eine Zahl zwischen 0 und 3 eingeben!')
    except ValueError as e:
        print('ValueError:', 'Bitte eine Zahl eingeben!')