# coding: utf-8
##############################################################################
# Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
#
# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.
#
# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
# PARTICULAR PURPOSE.
#
# IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
# INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
# WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
# BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
##############################################################################
autoConnectTableGMAC = [["BASIC CONFIGURATION", "tcpipNetConfig_0:NETCONFIG_MAC_Dependency", "DRIVER LAYER", "drvGmac:libdrvGmac"]]
autoConnectTableEthmac = [["BASIC CONFIGURATION", "tcpipNetConfig_0:NETCONFIG_MAC_Dependency", "DRIVER LAYER", "drvPic32mEthmac:libdrvPic32mEthmac"]]
autoConnectTableEMAC0 = [["BASIC CONFIGURATION", "tcpipNetConfig_0:NETCONFIG_MAC_Dependency", "DRIVER LAYER", "drvEmac0:libdrvMac0"]]
autoConnectTableEMAC1 = [["BASIC CONFIGURATION", "tcpipNetConfig_0:NETCONFIG_MAC_Dependency", "DRIVER LAYER", "drvEmac1:libdrvMac1"]]
autoConnectTableWINC = [["BASIC CONFIGURATION", "tcpipNetConfig_0:NETCONFIG_MAC_Dependency", "DRIVER LAYER", "drvWifiWinc:libdrvWincMac"]]
################################################################################
#### Business Logic ####
################################################################################

############################################################################
#### Code Generation ####
############################################################################
def instantiateComponent(tcpipAutoConfigDriverComponent):

    tcpipAutoConfigStackGroup = Database.findGroup("TCP/IP STACK")
    if (tcpipAutoConfigStackGroup == None):
        tcpipAutoConfigStackGroup = Database.createGroup(None, "TCP/IP STACK")
        
    tcpipAutoConfigDriverGroup = Database.findGroup("DRIVER LAYER")
    if (tcpipAutoConfigDriverGroup == None):
        tcpipAutoConfigDriverGroup = Database.createGroup("TCP/IP STACK", "DRIVER LAYER")

    # Enable Driver Configurator
    tcpipAutoConfigDrvEnable = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_DRV_ENABLE", None)
    tcpipAutoConfigDrvEnable.setVisible(False)
    tcpipAutoConfigDrvEnable.setDefaultValue(True)
    if Peripheral.moduleExists("GMAC"): 
        # Enable GMAC
        tcpipAutoConfigGMAC = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_GMAC", None)
        tcpipAutoConfigGMAC.setLabel("GMAC")
        tcpipAutoConfigGMAC.setVisible(True)
        tcpipAutoConfigGMAC.setDescription("Enable GMAC")
        tcpipAutoConfigGMAC.setDependencies(tcpipAutoConfigGMACEnable, ["TCPIP_AUTOCONFIG_ENABLE_GMAC"])    
    elif "PIC32M" in Variables.get("__PROCESSOR"):
        # Enable Ethernet MAC
        tcpipAutoConfigEthmac = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_ETHMAC", None)
        tcpipAutoConfigEthmac.setLabel("ETHMAC")
        tcpipAutoConfigEthmac.setVisible(True)
        tcpipAutoConfigEthmac.setDescription("Enable ETHMAC")
        tcpipAutoConfigEthmac.setDependencies(tcpipAutoConfigETHMACEnable, ["TCPIP_AUTOCONFIG_ENABLE_ETHMAC"])  
    elif Peripheral.moduleExists( "EMAC" ):
        tcpipAutoConfigEMAC0 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_EMAC0", None)
        tcpipAutoConfigEMAC0.setLabel("EMAC0")
        tcpipAutoConfigEMAC0.setVisible(True)
        tcpipAutoConfigEMAC0.setDescription("Enable EMAC0")
        tcpipAutoConfigEMAC0.setDependencies(tcpipAutoConfigEMAC0Enable, ["TCPIP_AUTOCONFIG_ENABLE_EMAC0"])     
        tcpipAutoConfigEMAC1 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_EMAC1", None)
        tcpipAutoConfigEMAC1.setLabel("EMAC1")
        tcpipAutoConfigEMAC1.setVisible(True)
        tcpipAutoConfigEMAC1.setDescription("Enable EMAC1")
        tcpipAutoConfigEMAC1.setDependencies(tcpipAutoConfigEMAC1Enable, ["TCPIP_AUTOCONFIG_ENABLE_EMAC1"]) 
        
    # Enable MIIM_Driver
    tcpipAutoConfigMIIM_Driver = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", None)
    tcpipAutoConfigMIIM_Driver.setLabel("MIIM_Driver")
    tcpipAutoConfigMIIM_Driver.setVisible(True)
    tcpipAutoConfigMIIM_Driver.setDescription("Enable MIIM_Driver")
    tcpipAutoConfigMIIM_Driver.setDependencies(tcpipAutoConfigMIIMDriverEnable, ["TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver"])        
    
    # Enable KSZ8041
    tcpipAutoConfigKSZ8041 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_KSZ8041", None)
    tcpipAutoConfigKSZ8041.setLabel("KSZ8041")
    tcpipAutoConfigKSZ8041.setVisible(True)
    tcpipAutoConfigKSZ8041.setDescription("Enable KSZ8041") 
    tcpipAutoConfigKSZ8041.setDependencies(tcpipAutoConfigKSZ8041Enable, ["TCPIP_AUTOCONFIG_ENABLE_KSZ8041"])  
    
    # Enable KSZ8061
    tcpipAutoConfigKSZ8061 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_KSZ8061", None)
    tcpipAutoConfigKSZ8061.setLabel("KSZ8061")
    tcpipAutoConfigKSZ8061.setVisible(True)
    tcpipAutoConfigKSZ8061.setDescription("Enable KSZ8061") 
    tcpipAutoConfigKSZ8061.setDependencies(tcpipAutoConfigKSZ8061Enable, ["TCPIP_AUTOCONFIG_ENABLE_KSZ8061"])   

    # Enable KSZ8081
    tcpipAutoConfigKSZ8081 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_KSZ8081", None)
    tcpipAutoConfigKSZ8081.setLabel("KSZ8081")
    tcpipAutoConfigKSZ8081.setVisible(True)
    tcpipAutoConfigKSZ8081.setDescription("Enable KSZ8081") 
    tcpipAutoConfigKSZ8081.setDependencies(tcpipAutoConfigKSZ8081Enable, ["TCPIP_AUTOCONFIG_ENABLE_KSZ8081"])   

    # Enable KSZ8091
    tcpipAutoConfigKSZ8091 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_KSZ8091", None)
    tcpipAutoConfigKSZ8091.setLabel("KSZ8091")
    tcpipAutoConfigKSZ8091.setVisible(True)
    tcpipAutoConfigKSZ8091.setDescription("Enable KSZ8091") 
    tcpipAutoConfigKSZ8091.setDependencies(tcpipAutoConfigKSZ8091Enable, ["TCPIP_AUTOCONFIG_ENABLE_KSZ8091"])
    
    # Enable KSZ8863
    tcpipAutoConfigKSZ8863 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_KSZ8863", None)
    tcpipAutoConfigKSZ8863.setLabel("KSZ8863")
    tcpipAutoConfigKSZ8863.setVisible(True)
    tcpipAutoConfigKSZ8863.setDescription("Enable KSZ8863") 
    tcpipAutoConfigKSZ8863.setDependencies(tcpipAutoConfigKSZ8863Enable, ["TCPIP_AUTOCONFIG_ENABLE_KSZ8863"]) 
    
    # Enable LAN8740
    tcpipAutoConfigLAN8740 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_LAN8740", None)
    tcpipAutoConfigLAN8740.setLabel("LAN8740")
    tcpipAutoConfigLAN8740.setVisible(True)
    tcpipAutoConfigLAN8740.setDescription("Enable LAN8740")
    tcpipAutoConfigLAN8740.setDependencies(tcpipAutoConfigLAN8740Enable, ["TCPIP_AUTOCONFIG_ENABLE_LAN8740"])       
    
    # Enable LAN8700
    tcpipAutoConfigLAN8700 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_LAN8700", None)
    tcpipAutoConfigLAN8700.setLabel("LAN8700")
    tcpipAutoConfigLAN8700.setVisible(True)
    tcpipAutoConfigLAN8700.setDescription("Enable LAN8700")
    tcpipAutoConfigLAN8700.setDependencies(tcpipAutoConfigLAN8700Enable, ["TCPIP_AUTOCONFIG_ENABLE_LAN8700"]) 
    
    # Enable LAN8720
    tcpipAutoConfigLAN8720 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_LAN8720", None)
    tcpipAutoConfigLAN8720.setLabel("LAN8720")
    tcpipAutoConfigLAN8720.setVisible(True)
    tcpipAutoConfigLAN8720.setDescription("Enable LAN8720")
    tcpipAutoConfigLAN8720.setDependencies(tcpipAutoConfigLAN8720Enable, ["TCPIP_AUTOCONFIG_ENABLE_LAN8720"]) 
    
    # Enable LAN9303
    tcpipAutoConfigLAN9303 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_LAN9303", None)
    tcpipAutoConfigLAN9303.setLabel("LAN9303")
    tcpipAutoConfigLAN9303.setVisible(True)
    tcpipAutoConfigLAN9303.setDescription("Enable LAN9303")
    tcpipAutoConfigLAN9303.setDependencies(tcpipAutoConfigLAN9303Enable, ["TCPIP_AUTOCONFIG_ENABLE_LAN9303"]) 
    
    # Enable DP83640
    tcpipAutoConfigDP83640 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_DP83640", None)
    tcpipAutoConfigDP83640.setLabel("DP83640")
    tcpipAutoConfigDP83640.setVisible(True)
    tcpipAutoConfigDP83640.setDescription("Enable DP83640")
    tcpipAutoConfigDP83640.setDependencies(tcpipAutoConfigDP83640Enable, ["TCPIP_AUTOCONFIG_ENABLE_DP83640"]) 
    
    # Enable DP83848
    tcpipAutoConfigDP83848 = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_DP83848", None)
    tcpipAutoConfigDP83848.setLabel("DP83848")
    tcpipAutoConfigDP83848.setVisible(True)
    tcpipAutoConfigDP83848.setDescription("Enable DP83848")
    tcpipAutoConfigDP83848.setDependencies(tcpipAutoConfigDP83848Enable, ["TCPIP_AUTOCONFIG_ENABLE_DP83848"]) 
    
    # Enable IP101GR
    tcpipAutoConfigIP101GR = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_IP101GR", None)
    tcpipAutoConfigIP101GR.setLabel("IP101GR")
    tcpipAutoConfigIP101GR.setVisible(True)
    tcpipAutoConfigIP101GR.setDescription("Enable IP101GR")
    tcpipAutoConfigIP101GR.setDependencies(tcpipAutoConfigIP101GREnable, ["TCPIP_AUTOCONFIG_ENABLE_IP101GR"]) 
    
    # Enable WINC MAC
    tcpipAutoConfigWINC = tcpipAutoConfigDriverComponent.createBooleanSymbol("TCPIP_AUTOCONFIG_ENABLE_WINC", None)
    tcpipAutoConfigWINC.setLabel("WINC")
    tcpipAutoConfigWINC.setVisible(True)
    tcpipAutoConfigWINC.setDescription("Enable WINC")
    tcpipAutoConfigWINC.setDependencies(tcpipAutoConfigWINCEnable, ["TCPIP_AUTOCONFIG_ENABLE_WINC"])    
########################################################################################################
def finalizeComponent(tcpipAutoConfigDriverComponent):
    tcpipAutoConfigDriverGroup = Database.findGroup("DRIVER LAYER")
    tcpipAutoConfigDriverGroup.addComponent(tcpipAutoConfigDriverComponent.getID())
    
    if(Database.getSymbolValue("tcpip_apps_config", "TCPIP_AUTOCONFIG_APPS_ENABLE") != True) and (Database.getSymbolValue("tcpip_transport_config", "TCPIP_AUTOCONFIG_TRANS_ENABLE") != True) and (Database.getSymbolValue("tcpip_network_config", "TCPIP_AUTOCONFIG_NET_ENABLE") != True) and (Database.getSymbolValue("tcpip_basic_config", "TCPIP_AUTOCONFIG_BASIC_ENABLE") != True):
        Database.setActiveGroup("DRIVER LAYER") 
#######################################################################################################
def enableTcpipAutoConfigDrv(enable):

    if(enable == True):
        tcpipAutoConfigAppsGroup = Database.findGroup("APPLICATION LAYER")
        if (tcpipAutoConfigAppsGroup == None):
            tcpipAutoConfigAppsGroup = Database.createGroup("TCP/IP STACK", "APPLICATION LAYER")
            
        tcpipAutoConfigTransportGroup = Database.findGroup("TRANSPORT LAYER")
        if (tcpipAutoConfigTransportGroup == None):
            tcpipAutoConfigTransportGroup = Database.createGroup("TCP/IP STACK", "TRANSPORT LAYER")

        tcpipAutoConfigNetworkGroup = Database.findGroup("NETWORK LAYER")
        if (tcpipAutoConfigNetworkGroup == None):
            tcpipAutoConfigNetworkGroup = Database.createGroup("TCP/IP STACK", "NETWORK LAYER")
            
        tcpipAutoConfigDriverGroup = Database.findGroup("DRIVER LAYER")
        if (tcpipAutoConfigDriverGroup == None):
            tcpipAutoConfigDriverGroup = Database.createGroup("TCP/IP STACK", "DRIVER LAYER")

        tcpipAutoConfigBasicGroup = Database.findGroup("BASIC CONFIGURATION")
        if (tcpipAutoConfigBasicGroup == None):
            tcpipAutoConfigBasicGroup = Database.createGroup("TCP/IP STACK", "BASIC CONFIGURATION")
        
        if(Database.getComponentByID("tcpip_apps_config") == None):
            res = tcpipAutoConfigAppsGroup.addComponent("tcpip_apps_config")
            res = Database.activateComponents(["tcpip_apps_config"], "APPLICATION LAYER", False)
            
        if(Database.getComponentByID("tcpip_transport_config") == None):
            res = tcpipAutoConfigTransportGroup.addComponent("tcpip_transport_config")
            res = Database.activateComponents(["tcpip_transport_config"], "TRANSPORT LAYER", False)
        
        if(Database.getComponentByID("tcpip_network_config") == None):
            res = tcpipAutoConfigNetworkGroup.addComponent("tcpip_network_config")
            res = Database.activateComponents(["tcpip_network_config"], "NETWORK LAYER", False)
            
        if(Database.getComponentByID("tcpip_basic_config") == None):
            res = tcpipAutoConfigBasicGroup.addComponent("tcpip_basic_config")
            res = Database.activateComponents(["tcpip_basic_config"], "BASIC CONFIGURATION", False)         
            
        if(Database.getSymbolValue("tcpip_basic_config", "TCPIP_AUTOCONFIG_ENABLE_STACK") != True):
            Database.setSymbolValue("tcpip_basic_config", "TCPIP_AUTOCONFIG_ENABLE_STACK", True, 2)
            
        if(Database.getSymbolValue("tcpip_basic_config", "TCPIP_AUTOCONFIG_ENABLE_NETCONFIG") != True):
            Database.setSymbolValue("tcpip_basic_config", "TCPIP_AUTOCONFIG_ENABLE_NETCONFIG", True, 2)             

#################Business Logic- Driver Layer ######################################### 
def tcpipAutoConfigGMACEnable(symbol, event):
    tcpipAutoConfigDriverGroup = Database.findGroup("DRIVER LAYER")
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvGmac"],"DRIVER LAYER")   
        tcpipAutoConfigDriverGroup.setAttachmentVisible("drvGmac", "libdrvGmac")
        res = Database.connectDependencies(autoConnectTableGMAC)
    else:
        res = Database.deactivateComponents(["drvGmac"])
        
def tcpipAutoConfigETHMACEnable(symbol, event):
    tcpipAutoConfigDriverGroup = Database.findGroup("DRIVER LAYER")
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvPic32mEthmac"],"DRIVER LAYER")   
        tcpipAutoConfigDriverGroup.setAttachmentVisible("drvPic32mEthmac", "libdrvPic32mEthmac")
        res = Database.connectDependencies(autoConnectTableEthmac)
    else:
        res = Database.deactivateComponents(["drvPic32mEthmac"])
    
def tcpipAutoConfigEMAC0Enable(symbol, event):
    tcpipAutoConfigDriverGroup = Database.findGroup("DRIVER LAYER")
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvEmac0"],"DRIVER LAYER")   
        tcpipAutoConfigDriverGroup.setAttachmentVisible("drvEmac0", "libdrvMac0")
        res = Database.connectDependencies(autoConnectTableEMAC0)
    else:
        res = Database.deactivateComponents(["drvEmac0"])
    
def tcpipAutoConfigEMAC1Enable(symbol, event):
    tcpipAutoConfigDriverGroup = Database.findGroup("DRIVER LAYER")
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvEmac1"],"DRIVER LAYER")   
        tcpipAutoConfigDriverGroup.setAttachmentVisible("drvEmac1", "libdrvMac1")
        res = Database.connectDependencies(autoConnectTableEMAC1)
    else:
        res = Database.deactivateComponents(["drvEmac1"])
def tcpipAutoConfigMIIMDriverEnable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvMiim"],"DRIVER LAYER")   
    else:
        res = Database.deactivateComponents(["drvMiim"])

    
def tcpipAutoConfigKSZ8041Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyKsz8041"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyKsz8041"])
        
def tcpipAutoConfigKSZ8061Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyKsz8061"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyKsz8061"])
    
    
def tcpipAutoConfigKSZ8081Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyKsz8081"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyKsz8081"])
    
def tcpipAutoConfigKSZ8091Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyKsz8091"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyKsz8091"])
    
def tcpipAutoConfigKSZ8863Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyKsz8863"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyKsz8863"])
       
def tcpipAutoConfigLAN8740Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyLan8740"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyLan8740"])
        
def tcpipAutoConfigLAN8700Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyLan8700"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyLan8700"])
        
def tcpipAutoConfigLAN8720Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyLan8720"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyLan8720"])
        
def tcpipAutoConfigLAN9303Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyLan9303"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyLan9303"])
        
def tcpipAutoConfigDP83640Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyDp83640"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyDp83640"])
        
def tcpipAutoConfigDP83848Enable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyDp83848"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyDp83848"])
        
def tcpipAutoConfigIP101GREnable(symbol, event):
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvExtPhyIp101gr"],"DRIVER LAYER")  
        if(Database.getSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver") != True):
            Database.setSymbolValue("tcpip_driver_config", "TCPIP_AUTOCONFIG_ENABLE_MIIM_Driver", True, 2)      
    else:
        res = Database.deactivateComponents(["drvExtPhyIp101gr"])
                      
def tcpipAutoConfigWINCEnable(symbol, event):
    tcpipAutoConfigDriverGroup = Database.findGroup("DRIVER LAYER")
    tcpipAutoConfigStackGroup = Database.findGroup("TCP/IP STACK")
    enableTcpipAutoConfigDrv(True)
    if (event["value"] == True):
        res = Database.activateComponents(["drvWifiWinc"],"DRIVER LAYER")   
        Database.setSymbolValue("drvWifiWinc", "DRV_WIFI_WINC_DRIVER_MODE", "Ethernet Mode")
        Database.setSymbolValue("drvWifiWinc", "DRV_WIFI_WINC_USE_TCPIP_STACK", True)
        tcpipAutoConfigDriverGroup.setAttachmentVisible("drvWifiWinc", "libdrvWincMac")
        tcpipAutoConfigDriverGroup.setAttachmentVisible("drvWifiWinc", "spi")
        tcpipAutoConfigStackGroup.setAttachmentVisible("DRIVER LAYER", "drvWifiWinc:spi")
        res = Database.connectDependencies(autoConnectTableWINC)        
    else:
        res = Database.deactivateComponents(["drvWifiWinc"])            
