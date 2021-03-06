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

def instantiateComponent(tcpipTftpsComponent):
    print("TCPIP TFTPS Component")
    configName = Variables.get("__CONFIGURATION_NAME")

    # Use TFTP Server Module
    tcpipTftps = tcpipTftpsComponent.createBooleanSymbol("TCPIP_USE_TFTPS_MODULE", None)
    tcpipTftps.setLabel("Use TFTP Server Module")
    tcpipTftps.setVisible(False)
    tcpipTftps.setDescription("Use TFTP Server Module")
    tcpipTftps.setDefaultValue(True)
    # select USE_SYS_FS_NEEDED 
    #tcpipTftps.setDependencies(tcpipTftpsModuleVisible, ["tcpipIPv4.TCPIP_STACK_USE_IPV4", "tcpipUdp.TCPIP_USE_UDP"])

    # TFTP Server Task Rate in msec
    tcpipTftpsTskTickRate= tcpipTftpsComponent.createIntegerSymbol("TCPIP_TFTPS_TASK_TICK_RATE", None)
    tcpipTftpsTskTickRate.setLabel("TFTP Server Task Rate in msec")
    tcpipTftpsTskTickRate.setVisible(True)
    tcpipTftpsTskTickRate.setDescription("TFTP Server Task Rate in msec")
    tcpipTftpsTskTickRate.setDefaultValue(60)
    #tcpipTftpsTskTickRate.setDependencies(tcpipTftpsMenuVisibleSingle, ["TCPIP_USE_TFTPS_MODULE"])
    
    # TFTP Server command process timeout in sec
    tcpipTftpsCmdProcessTimeout= tcpipTftpsComponent.createIntegerSymbol("TCPIP_TFTPS_CMD_PROCESS_TIMEOUT", None)
    tcpipTftpsCmdProcessTimeout.setLabel("TFTP Server command process timeout in sec")
    tcpipTftpsCmdProcessTimeout.setVisible(True)
    tcpipTftpsCmdProcessTimeout.setDescription("TFTP Server command process timeout in sec")
    tcpipTftpsCmdProcessTimeout.setDefaultValue(10)
    #tcpipTftpsCmdProcessTimeout.setDependencies(tcpipTftpsMenuVisibleSingle, ["TCPIP_USE_TFTPS_MODULE"])
    
    # TFTP Server Retransmit count value to retransmit the last packet sent
    tcpipTftpsRetransmitCnt= tcpipTftpsComponent.createIntegerSymbol("TCPIP_TFTPS_RETRANSMIT_COUNT", None)
    tcpipTftpsRetransmitCnt.setLabel("TFTP Server retransmit count")
    tcpipTftpsRetransmitCnt.setVisible(True)
    tcpipTftpsRetransmitCnt.setDescription("TFTP Server retransmit count")
    tcpipTftpsRetransmitCnt.setDefaultValue(3)
    #tcpipTftpsRetransmitCnt.setDependencies(tcpipTftpsMenuVisibleSingle, ["TCPIP_USE_TFTPS_MODULE"])
    
    # TFTP Server number of client can be supported at a time
    tcpipTftpsClientCnt= tcpipTftpsComponent.createIntegerSymbol("TCPIP_TFTPS_CLIENT_NUMBER", None)
    tcpipTftpsClientCnt.setLabel("TFTP Server can access number of Clients")
    tcpipTftpsClientCnt.setVisible(True)
    tcpipTftpsClientCnt.setDescription("TFTP Server can access number of Clients")
    tcpipTftpsClientCnt.setDefaultValue(3)
    #tcpipTftpsClientCnt.setDependencies(tcpipTftpsMenuVisibleSingle, ["TCPIP_USE_TFTPS_MODULE"])
    
    
    # Maximum Length for a file size
    tcpipTftpsFileSizeLen= tcpipTftpsComponent.createIntegerSymbol("TCPIP_TFTPS_DEFAULT_FILESIZE", None)
    tcpipTftpsFileSizeLen.setLabel("Maximum Length for a file size")
    tcpipTftpsFileSizeLen.setVisible(True)
    tcpipTftpsFileSizeLen.setDescription("Maximum Length for a file transmission")
    tcpipTftpsFileSizeLen.setDefaultValue(64000)
    #tcpipTftpsFileSizeLen.setDependencies(tcpipTftpsMenuVisibleSingle, ["TCPIP_USE_TFTPS_MODULE"])
    
    # Maximum Length for block size configuration
    tcpipTftpsDefBockSizeLen= tcpipTftpsComponent.createIntegerSymbol("TCPIP_TFTPS_DEFAULT_BLOCK_SIZE", None)
    tcpipTftpsDefBockSizeLen.setLabel("Maximum block size Length for a file name")
    tcpipTftpsDefBockSizeLen.setVisible(True)
    tcpipTftpsDefBockSizeLen.setDescription("Maximum block size Length for a file name")
    tcpipTftpsDefBockSizeLen.setDefaultValue(512)
    #tcpipTftpsDefBockSizeLen.setDependencies(tcpipTftpsMenuVisibleSingle, ["TCPIP_USE_TFTPS_MODULE"])
    
    # TFTP Server command process timeout in sec
    tcpipTftpsDefTimeout= tcpipTftpsComponent.createIntegerSymbol("TCPIP_TFTPS_DEFAULT_TIMEOUT", None)
    tcpipTftpsDefTimeout.setLabel("TFTP Server default timeout option")
    tcpipTftpsDefTimeout.setVisible(True)
    tcpipTftpsDefTimeout.setDescription("TFTP Server default timeout option")
    tcpipTftpsDefTimeout.setDefaultValue(10)
    #tcpipTftpsDefTimeout.setDependencies(tcpipTftpsMenuVisibleSingle, ["TCPIP_USE_TFTPS_MODULE"])
    
    # TFTP Server command source file name length
    tcpipTftpsFileNameLength= tcpipTftpsComponent.createIntegerSymbol("TCPIP_TFTPS_FILENAME_LEN", None)
    tcpipTftpsFileNameLength.setLabel("TFTP Server default file name length")
    tcpipTftpsFileNameLength.setVisible(True)
    tcpipTftpsFileNameLength.setDescription("TFTP Server default file name length")
    tcpipTftpsFileNameLength.setDefaultValue(64)
    #tcpipTftpsFileNameLength.setDependencies(tcpipTftpsMenuVisibleSingle, ["TCPIP_USE_TFTPS_MODULE"])
    
    # Default TFTP Server Mount point directory
    tcpipTftpsRootDir = tcpipTftpsComponent.createStringSymbol("TCPIP_TFTPS_MOUNT_POINT", None)
    tcpipTftpsRootDir.setLabel("TFTP Server Root Directory Path")
    tcpipTftpsRootDir.setVisible(True)
    tcpipTftpsRootDir.setDescription("TFTP Server Root Directory Path")
    tcpipTftpsRootDir.setDefaultValue("/mnt/mchpSite1/")

    # Enable User Notification
    tcpipTftpsUsrNotify = tcpipTftpsComponent.createBooleanSymbol("TCPIP_TFTPS_USER_NOTIFICATION", None)
    tcpipTftpsUsrNotify.setLabel("Enable User Notification")
    tcpipTftpsUsrNotify.setVisible(True)
    tcpipTftpsUsrNotify.setDescription("Enable User Notification")
    tcpipTftpsUsrNotify.setDefaultValue(False) 
    #tcpipTftpsUsrNotify.setDependencies(tcpipTftpcMenuVisibleSingle, ["TCPIP_USE_TFTPS_MODULE"])

    #Add to system_config.h
    tcpipTftpsHeaderFtl = tcpipTftpsComponent.createFileSymbol(None, None)
    tcpipTftpsHeaderFtl.setSourcePath("tcpip/config/tftps.h.ftl")
    tcpipTftpsHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    tcpipTftpsHeaderFtl.setMarkup(True)
    tcpipTftpsHeaderFtl.setType("STRING")

    # Add tftps.c file
    tcpipTftpsSourceFile = tcpipTftpsComponent.createFileSymbol(None, None)
    tcpipTftpsSourceFile.setSourcePath("tcpip/src/tftps.c")
    tcpipTftpsSourceFile.setOutputName("tftps.c")
    tcpipTftpsSourceFile.setOverwrite(True)
    tcpipTftpsSourceFile.setDestPath("library/tcpip/src/")
    tcpipTftpsSourceFile.setProjectPath("config/" + configName + "/library/tcpip/src/")
    tcpipTftpsSourceFile.setType("SOURCE")
    tcpipTftpsSourceFile.setEnabled(True)
    #tcpipTftpsSourceFile.setDependencies(tcpipTftpsGenSourceFile, ["TCPIP_USE_TFTPS_MODULE"])

# make Reboot Server option visible
def tcpipTftpsModuleVisible(tcpipDependentSymbol, tcpipIPSymbol):
    tcpipIPv4 = Database.getSymbolValue("tcpipIPv4","TCPIP_STACK_USE_IPV4")
    tcpipUdp = Database.getSymbolValue("tcpipUdp","TCPIP_USE_UDP")

    if(tcpipIPv4 and tcpipUdp):
        tcpipDependentSymbol.setVisible(True)
    else:
        tcpipDependentSymbol.setVisible(False)
        
def tcpipTftpsMenuVisibleSingle(symbol, event):
    if (event["value"] == True):
        print("TFTPS Menu Visible.")        
        symbol.setVisible(True)
    else:
        print("TFTPS Menu Invisible.")
        symbol.setVisible(False)

def tcpipTftpsGenSourceFile(sourceFile, event):
    sourceFile.setEnabled(event["value"])

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
    Database.setSymbolValue("tcpipTftps", "TCPIP_USE_TFTPS_MODULE", False, 2)
    
