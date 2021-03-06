#!/usr/bin/python

import analyzePackage

class AnalyzeData:
    
    def __init__(self, analyze, path):
        self.analyze = analyze
        #self.info = analyze.takeInformation()
        self.infoAP = analyze.takeInformationAP()
        self.infoClient = analyze.takeInformationClient()
        
        self.auth = {}
        self.deauth = {}
        self.disass = {}
        
        self.rts = {}
        self.cts = {}
        self.ack = {}
        self.dataList = {}

        self.associationRequest = {}
        self.associationResponce = {}

        self.probeRequest = {}
        self.probeResponse = {}

        self.eapHandshakeSuccess = {}
        self.eapHandshakeFailed = {}
        
        self.beacon = {}
        self.numPack = {}
        
        
    #def analyze(self):
        #DATA = open("DATA.txt", "a")
        
        #DATA.write("CHANNEL STATION:\n")
        #for data in self.infoClient:
            ##print self.infoClient[data][3]
            #DATA.write(data+" --> "+ str(self.infoClient[data][3])+"\n")
            #if self.infoClient[data][3] not in self.channelClient:
                #self.channelClient.append(self.infoClient[data][3])
            
            #if int(self.infoClient[data][14]) > 0:
                #self.rtsClient[data] = self.infoClient[data][14]
            
            ##if int(self.infoClient[data][4]) > 0:
                ##self.auth[data] = self.infoClient[data][4]
            ##if int(self.infoClient[data][5]) > 0:
                ##self.deauth[data] = self.infoClient[data][5]
            ##if int(self.infoClient[data][8]) > 0:
                ##self.disass[data] = self.infoClient[data][8]
        
        #DATA.write("\nALL STATION'S CHANNEL: \n")
        #for channel in self.channelClient:
            #if channel != "-":
                #DATA.write(str(channel)+"  ")
        
        #DATA.write("\n\nCHANNEL AP:\n")
        #for data in self.infoAP:
            ##print self.infoClient[data][3]
            #DATA.write(data+" --> "+ str(self.infoAP[data][3])+"\n")
            #if self.infoAP[data][0] == "eduroam-wifiunical":
                #self.contUfficialAP += 1
            #else:
                #self.contRogueAP += 1
                
            #if int(self.infoAP[data][4]) > 0:
                #self.auth[data] = self.infoAP[data][4]
            #if int(self.infoAP[data][5]) > 0:
                #self.deauth[data] = self.infoAP[data][5]
            #if int(self.infoAP[data][8]) > 0:
                #self.disass[data] = self.infoAP[data][8]
            #if int(self.infoAP[data][14]) > 0:
                #self.rtsAP[data] = self.infoAP[data][15]
            
        #DATA.write("\n\n")
        #DATA.write("CONT CLIENT: "+str(len(self.infoClient))+"\n")
        #DATA.write("CONT AP: "+str(len(self.infoAP))+"\n")
        #DATA.write("CONT UFFICIAL AP: "+str(self.contUfficialAP)+"\n")
        #DATA.write("CONT ROGUE AP: "+str(self.contRogueAP)+"\n")
        
        #DATA.write("\n\n")
        #DATA.write("CORRUPT PACKAGE CLIENT:  MAC-PERCENTAGE-CORRUPT-TOT\n")
        
        #for data in self.infoClient:
            #cont = 0
            #if int(self.infoClient[data][12]) > 40:
                #DATA.write("\n")
                #DATA.write(data+" --> "+str(self.infoClient[data][12])+"%\t"+str(self.infoClient[data][11])+"\t"+str(self.infoClient[data][20])+"\n")
                #for macAP,macClient in self.info:
                    #if macClient == data:
                        #if cont < 1:
                            #DATA.write("\t\tSPECIFICHE: BSSID-PERCENTAGE-POWER-CORRUPT-TOT\n")
                            #cont += 1
                        #DATA.write("\t\t\t"+str(self.info[macAP,macClient][1])+"\t"+str(self.info[macAP,macClient][12])+"%"+"\t"+str(self.info[macAP,macClient][10])+"\t"+str(self.info[macAP,macClient][11])+"\t"+str(self.info[macAP,macClient][20])+"\n")
        
        #DATA.write("\n\n")
        #DATA.write("CORRUPT PACKAGE AP:  BSSID-POWER-PERCENTAGE-CORRUPT-TOT\n")
        
        #for data in self.infoAP:
            #if int(self.infoAP[data][13]) > 40:
                #DATA.write(data+" --> "+str(self.infoAP[data][11])+"\t"+str(self.infoAP[data][13])+"%\t"+str(self.infoAP[data][12])+"\t"+str(self.infoAP[data][21])+"\n")  
        
        
        #DATA.write("\n\n")
        ##DATA.write("OTHER VALUE AP:\n")
        #DATA.write("AUTH AP: \n")
        #for data in self.auth:
            #DATA.write(data+" --> "+str(self.auth[data])+"\n")
            
            
        #DATA.write("\n")
        ##DATA.write("OTHER VALUE AP:\n")
        #DATA.write("DEAUTH AP: \n")
        #for data in self.deauth:
            #DATA.write(data+" --> "+str(self.deauth[data])+"\n")
            
            
        #DATA.write("\n")
        ##DATA.write("OTHER VALUE AP:\n")
        #DATA.write("DISASS AP: \n")
        #for data in self.disass:
            #DATA.write(data+" --> "+str(self.disass[data])+"\n")
        
        #DATA.write("\n")
        #DATA.write("TOT RTS: "+len(self.rtsAP)+"  RTS AP: \n")
        #for data in self.rtsAP:
            #DATA.write(data+" --> "+str(self.rtsAP[data])+"\n")
            
        
        #DATA.write("\n\n")
        #DATA.write("TOT RTS: "+len(self.rtsClient)+"  RTS CLIENT: \n")
        #for data in self.rtsClient:
            #DATA.write(data+" --> "+str(self.rtsClient[data])+"\n")
        
        #DATA.write("\n")
        #DATA.write("ROAMING CLIENT: \n")
        
        #contRoaming = 0
        #for data in self.infoRoamingClient:
            #if len(self.infoRoamingClient[data]) > 1:
                #DATA.write(data+": \n")
                #contRoaming += 1
                #for d in self.infoRoamingClient[data]:
                    #DATA.write("\t"+d+"\n")
                #DATA.write("\n")
        
        #DATA.write("TOT ROAMING CLIENT: "+ str(contRoaming) +"\n")
        
        
        #DATA.close()
        



