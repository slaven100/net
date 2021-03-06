"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

def instantiateComponent(tcpipTftpcComponent):
    print("TCPIP TFTPC Component")
    configName = Variables.get("__CONFIGURATION_NAME")

    # Use TFTP Client Module
    tcpipTftpc = tcpipTftpcComponent.createBooleanSymbol("TCPIP_USE_TFTPC_MODULE", None)
    tcpipTftpc.setLabel("Use TFTP Client Module")
    tcpipTftpc.setVisible(False)
    tcpipTftpc.setDescription("Use TFTP Client Module")
    tcpipTftpc.setDefaultValue(True)
    # select USE_SYS_FS_NEEDED 
    #tcpipTftpc.setDependencies(tcpipTftpcModuleVisible, ["tcpipIPv4.TCPIP_STACK_USE_IPV4", "tcpipUdp.TCPIP_USE_UDP"])

    # Default Interface
    tcpipTftpcDefault = tcpipTftpcComponent.createStringSymbol("TCPIP_TFTPC_DEFAULT_IF", None)  
    tcpipTftpcDefault.setLabel("Default Interface")
    tcpipTftpcDefault.setVisible(True)
    tcpipTftpcDefault.setDescription("Default Interface")
    
    if Peripheral.moduleExists("GMAC"):
        tcpipTftpcDefault.setDefaultValue("GMAC")
    else:
        tcpipTftpcDefault.setDefaultValue("PIC32INT")
    
    # Maximum Length for Server Address
    tcpipTftpcSrvrAddrLen= tcpipTftpcComponent.createIntegerSymbol("TCPIP_TFTPC_SERVERADDRESS_LEN", None)
    tcpipTftpcSrvrAddrLen.setLabel("Maximum Length for Server Address")
    tcpipTftpcSrvrAddrLen.setVisible(True)
    tcpipTftpcSrvrAddrLen.setDescription("Maximum Length for Server Address")
    tcpipTftpcSrvrAddrLen.setDefaultValue(16)
    #tcpipTftpcSrvrAddrLen.setDependencies(tcpipTftpcMenuVisibleSingle, ["TCPIP_USE_TFTPC_MODULE"])

    # Maximum Length for a file name
    tcpipTftpcFilenameLen= tcpipTftpcComponent.createIntegerSymbol("TCPIP_TFTPC_FILENAME_LEN", None)
    tcpipTftpcFilenameLen.setLabel("Maximum Length for a file name")
    tcpipTftpcFilenameLen.setVisible(True)
    tcpipTftpcFilenameLen.setDescription("Maximum Length for a file name")
    tcpipTftpcFilenameLen.setDefaultValue(32)
    #tcpipTftpcFilenameLen.setDependencies(tcpipTftpcMenuVisibleSingle, ["TCPIP_USE_TFTPC_MODULE"])

    # Enable User Notification
    tcpipTftpcUsrNotify = tcpipTftpcComponent.createBooleanSymbol("TCPIP_TFTPC_USER_NOTIFICATION", None)
    tcpipTftpcUsrNotify.setLabel("Enable User Notification")
    tcpipTftpcUsrNotify.setVisible(True)
    tcpipTftpcUsrNotify.setDescription("Enable User Notification")
    tcpipTftpcUsrNotify.setDefaultValue(False) 
    #tcpipTftpcUsrNotify.setDependencies(tcpipTftpcMenuVisibleSingle, ["TCPIP_USE_TFTPC_MODULE"])

    # TFTP Client Task Rate in msec
    tcpipTftpcTskTickRate= tcpipTftpcComponent.createIntegerSymbol("TCPIP_TFTPC_TASK_TICK_RATE", None)
    tcpipTftpcTskTickRate.setLabel("TFTP Client Task Rate in msec")
    tcpipTftpcTskTickRate.setVisible(True)
    tcpipTftpcTskTickRate.setDescription("TFTP Client Task Rate in msec")
    tcpipTftpcTskTickRate.setDefaultValue(100)
    #tcpipTftpcTskTickRate.setDependencies(tcpipTftpcMenuVisibleSingle, ["TCPIP_USE_TFTPC_MODULE"])

    # TFTP Client Socket connection timeout in sec
    tcpipTftpcArpTimeout= tcpipTftpcComponent.createIntegerSymbol("TCPIP_TFTPC_ARP_TIMEOUT", None)
    tcpipTftpcArpTimeout.setLabel("TFTP Client Socket connection timeout in sec")
    tcpipTftpcArpTimeout.setVisible(True)
    tcpipTftpcArpTimeout.setDescription("TFTP Client Socket connection timeout in sec")
    tcpipTftpcArpTimeout.setDefaultValue(3)
    #tcpipTftpcArpTimeout.setDependencies(tcpipTftpcMenuVisibleSingle, ["TCPIP_USE_TFTPC_MODULE"])

    # TFTP Client command process timeout in sec
    tcpipTftpcCmdProcessTimeout= tcpipTftpcComponent.createIntegerSymbol("TCPIP_TFTPC_CMD_PROCESS_TIMEOUT", None)
    tcpipTftpcCmdProcessTimeout.setLabel("TFTP Client command process timeout in sec")
    tcpipTftpcCmdProcessTimeout.setVisible(True)
    tcpipTftpcCmdProcessTimeout.setDescription("TFTP Client command process timeout in sec")
    tcpipTftpcCmdProcessTimeout.setDefaultValue(3)
    #tcpipTftpcCmdProcessTimeout.setDependencies(tcpipTftpcMenuVisibleSingle, ["TCPIP_USE_TFTPC_MODULE"])

    # TFTP Client Maximum retries
    tcpipTftpcRetryMax= tcpipTftpcComponent.createIntegerSymbol("TCPIP_TFTPC_MAX_RETRIES", None)
    tcpipTftpcRetryMax.setLabel("TFTP Client Maximum retries")
    tcpipTftpcRetryMax.setVisible(True)
    tcpipTftpcRetryMax.setDescription("TFTP Client Maximum retries")
    tcpipTftpcRetryMax.setDefaultValue(3)
    #tcpipTftpcRetryMax.setDependencies(tcpipTftpcMenuVisibleSingle, ["TCPIP_USE_TFTPC_MODULE"])

    tcpipTftpcheapdependency = ["TCPIP_TFTPC_FILENAME_LEN", "tcpipUdp.TCPIP_UDP_SOCKET_DEFAULT_TX_SIZE", 
                                "tcpipStack.TCPIP_STACK_HEAP_CALC_MASK"] 
    
    # TFTP Client Heap Size
    tcpipTftpcHeapSize = tcpipTftpcComponent.createIntegerSymbol("TCPIP_TFTPC_HEAP_SIZE", None)
    tcpipTftpcHeapSize.setLabel("TFTP Client Heap Size (bytes)") 
    tcpipTftpcHeapSize.setVisible(False)
    tcpipTftpcHeapSize.setDefaultValue(tcpipTftpcHeapCalc())
    tcpipTftpcHeapSize.setReadOnly(True)
    tcpipTftpcHeapSize.setDependencies(tcpipTftpcHeapUpdate, tcpipTftpcheapdependency)  
    
    #Add to system_config.h
    tcpipTftpcHeaderFtl = tcpipTftpcComponent.createFileSymbol(None, None)
    tcpipTftpcHeaderFtl.setSourcePath("tcpip/config/tftpc.h.ftl")
    tcpipTftpcHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    tcpipTftpcHeaderFtl.setMarkup(True)
    tcpipTftpcHeaderFtl.setType("STRING")

    # Add tftpc.c file
    tcpipTftpcSourceFile = tcpipTftpcComponent.createFileSymbol(None, None)
    tcpipTftpcSourceFile.setSourcePath("tcpip/src/tftpc.c")
    tcpipTftpcSourceFile.setOutputName("tftpc.c")
    tcpipTftpcSourceFile.setOverwrite(True)
    tcpipTftpcSourceFile.setDestPath("library/tcpip/src/")
    tcpipTftpcSourceFile.setProjectPath("config/" + configName + "/library/tcpip/src/")
    tcpipTftpcSourceFile.setType("SOURCE")
    tcpipTftpcSourceFile.setEnabled(True)
    #tcpipTftpcSourceFile.setDependencies(tcpipTftpcGenSourceFile, ["TCPIP_USE_TFTPC_MODULE"])

def tcpipTftpcHeapCalc():   
    
    min_TFTPC_tx_size = 528 + Database.getSymbolValue("tcpipTftpc","TCPIP_TFTPC_FILENAME_LEN")
    udpsktTxBuffSize = Database.getSymbolValue("tcpipUdp","TCPIP_UDP_SOCKET_DEFAULT_TX_SIZE")
    if(udpsktTxBuffSize >= min_TFTPC_tx_size):
        min_TFTPC_tx_size = 0
        
    heap_size = min_TFTPC_tx_size        
    return heap_size    
    
def tcpipTftpcHeapUpdate(symbol, event): 
    heap_size = tcpipTftpcHeapCalc()
    symbol.setValue(heap_size)
    if(event["id"] == "TCPIP_STACK_HEAP_CALC_MASK"):
        symbol.setVisible(event["value"])
    
# make Reboot Server option visible
def tcpipTftpcModuleVisible(tcpipDependentSymbol, tcpipIPSymbol):
    tcpipIPv4 = Database.getSymbolValue("tcpipIPv4","TCPIP_STACK_USE_IPV4")
    tcpipUdp = Database.getSymbolValue("tcpipUdp","TCPIP_USE_UDP")

    if(tcpipIPv4 and tcpipUdp):
        tcpipDependentSymbol.setVisible(True)
    else:
        tcpipDependentSymbol.setVisible(False)
        
def tcpipTftpcMenuVisibleSingle(symbol, event):
    if (event["value"] == True):
        print("TFTPC Menu Visible.")        
        symbol.setVisible(True)
    else:
        print("TFTPC Menu Invisible.")
        symbol.setVisible(False)

def tcpipTftpcGenSourceFile(sourceFile, event):
    sourceFile.setEnabled(event["value"])
    
def onAttachmentConnected(source, target):
    if (source["id"] == "Tftpc_MAC_Dependency"):    
        tcpipTftpcIf = source["component"].getSymbolByID("TCPIP_TFTPC_DEFAULT_IF")
        tcpipTftpcIf.clearValue()
        tcpipTftpcIf.setValue(target["component"].getDisplayName(), 2)
       
 
def onAttachmentDisconnected(source, target):
    if (source["id"] == "Tftpc_MAC_Dependency"):    
        source["component"].clearSymbolValue("TCPIP_TFTPC_DEFAULT_IF")

#Set symbols of other components
def setVal(component, symbol, value):
    triggerDict = {"Component":component,"Id":symbol, "Value":value}
    if(Database.sendMessage(component, "SET_SYMBOL", triggerDict) == None):
        print "Set Symbol Failure" + component + ":" + symbol + ":" + str(value)
        return False
    else:
        return True

#Handle messages from other components
def handleMessage(messageID, args):
    retDict= {}
    if (messageID == "SET_SYMBOL"):
        print "handleMessage: Set Symbol"
        retDict= {"Return": "Success"}
        Database.setSymbolValue(args["Component"], args["Id"], args["Value"])
    else:
        retDict= {"Return": "UnImplemented Command"}
    return retDict
      
      
def destroyComponent(component):
    Database.setSymbolValue("tcpipTftpc", "TCPIP_USE_TFTPC_MODULE", False, 2)