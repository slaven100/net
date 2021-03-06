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

######################  TCP/IP LIBRARY  ######################
def loadModule():
    print("Load Module: Harmony TCP/IP Stack")
    processor = Variables.get("__PROCESSOR")
    ###########  TCP/IP LIBRARY General Configurations  ########### 
    tcpipStackComponent = Module.CreateSharedComponent("tcpipStack", "TCPIP CORE", "/Libraries/TCPIP/CORE/", "tcpip/config/tcpip_stack.py")
    tcpipStackComponent.addCapability("libtcpipStack","TCPIP_CORE",True)
    tcpipStackComponent.addDependency("Core_NetConfig_Dependency", "NETCONFIG", None, True, True)
    tcpipStackComponent.addDependency("Core_SysTime_Dependency", "SYS_TIME", None, True, True)
    tcpipStackComponent.addDependency("Core_SysConsole_Dependency", "SYS_CONSOLE", None, False, False)
    tcpipStackComponent.setDisplayType("TCP/IP Library")
        
    tcpipNetConfigComponent = Module.CreateGeneratorComponent("tcpipNetConfig", "NETCONFIG", "/Libraries/TCPIP/CORE/","tcpip/config/tcpip_network_config_common.py","tcpip/config/tcpip_network_config.py")
    tcpipNetConfigComponent.addDependency("NETCONFIG_MAC_Dependency", "MAC")
    tcpipNetConfigComponent.addCapability("libtcpipNetConfig","NETCONFIG",True)
    tcpipNetConfigComponent.setDisplayType("TCP/IP Library")
    
    tcpipCmdComponent = Module.CreateComponent("tcpipCmd", "TCPIP CMD", "/Libraries/TCPIP/CORE/", "tcpip/config/tcpip_cmd.py")
    tcpipCmdComponent.addCapability("libtcpipCmd","TCPIP_CMD",True) 
    tcpipCmdComponent.addDependency("TcpipCmd_SysCmd_Dependency", "SYS_COMMAND", None, True, True)
    tcpipCmdComponent.setDisplayType("TCP/IP Library")

    ###########  TCP/IP LIBRARY Network Layer Configurations  ###########
    tcpipArpComponent = Module.CreateComponent("tcpipArp", "ARP", "/Libraries/TCPIP/Layer3-NETWORK/", "tcpip/config/tcpip_arp.py")
    tcpipArpComponent.addCapability("libtcpipArp","ARP", True)
    tcpipArpComponent.setDisplayType("TCP/IP Library")
    
    tcpipIcmpComponent = Module.CreateComponent("tcpipIcmp", "ICMPv4", "/Libraries/TCPIP/Layer3-NETWORK/", "tcpip/config/tcpip_icmp.py")
    tcpipIcmpComponent.addCapability("libtcpipIcmp","ICMPv4",True)  
    tcpipIcmpComponent.addDependency("Icmp_IPv4_Dependency", "IPv4", None, True, True)
    tcpipIcmpComponent.setDisplayType("TCP/IP Library")

    tcpipIgmpComponent = Module.CreateComponent("tcpipIgmp", "IGMP", "/Libraries/TCPIP/Layer3-NETWORK/", "tcpip/config/tcpip_igmp.py")
    tcpipIgmpComponent.addCapability("libtcpipIgmp","IGMP",True)
    tcpipIgmpComponent.addDependency("Igmp_IPv4_Dependency", "IPv4", None, True, True)
    tcpipIgmpComponent.setDisplayType("TCP/IP Library")
    
    tcpipIPv4Component = Module.CreateSharedComponent("tcpipIPv4", "IPv4", "/Libraries/TCPIP/Layer3-NETWORK/", "tcpip/config/tcpip_ipv4.py")
    tcpipIPv4Component.addCapability("libTcpipIPv4","IPv4",True)
    tcpipIPv4Component.addCapability("libTcpipIPv4IP","IP",True)
    #tcpipIPv4Component.addDependency("Ipv4_Stack_Dependency", "TCPIP_CORE", None, True, True)  
    tcpipIPv4Component.addDependency("Ipv4_Arp_Dependency", "ARP", None, True, True)    
    tcpipIPv4Component.setDisplayType("TCP/IP Library")
    
    tcpipIPv6Component = Module.CreateSharedComponent("tcpipIPv6", "IPv6", "/Libraries/TCPIP/Layer3-NETWORK/", "tcpip/config/tcpip_ipv6.py")
    tcpipIPv6Component.addCapability("libTcpipIPv6","IPv6",True)
    tcpipIPv6Component.addCapability("libTcpipIPv6IP","IP",True)
    tcpipIPv6Component.addDependency("Ipv6_Ndp_Dependency", "NDP", None, True, True)
    tcpipIPv6Component.addDependency("Ipv6_Icmpv6_Dependency", "ICMPv6", None, True, True)
    tcpipIPv6Component.setDisplayType("TCP/IP Library")
    
    tcpipIcmpv6Component = Module.CreateComponent("tcpipIcmpv6", "ICMPv6", "/Libraries/TCPIP/Layer3-NETWORK/", "tcpip/config/tcpip_icmpv6.py")
    tcpipIcmpv6Component.addCapability("libtcpipIcmpv6","ICMPv6",True)  
    tcpipIcmpv6Component.setDisplayType("TCP/IP Library")
    
    tcpipNdpComponent = Module.CreateComponent("tcpipNdp", "NDP", "/Libraries/TCPIP/Layer3-NETWORK/", "tcpip/config/tcpip_ndp.py")
    tcpipNdpComponent.addCapability("libtcpipNdp","NDP",True)
    tcpipNdpComponent.setDisplayType("TCP/IP Library")

    ###########  TCP/IP LIBRARY Transport Layer Configurations  ###########
    tcpipTcpComponent = Module.CreateSharedComponent("tcpipTcp", "TCP", "/Libraries/TCPIP/Layer4-TRANSPORT/", "tcpip/config/tcpip_tcp.py")
    tcpipTcpComponent.addCapability("libtcpipTcp","TCP",True)
    tcpipTcpComponent.addDependency("Tcp_IP_Dependency", "IP", None, True, True)
    tcpipTcpComponent.setDisplayType("TCP/IP Library")
    
    tcpipUdpComponent = Module.CreateSharedComponent("tcpipUdp", "UDP", "/Libraries/TCPIP/Layer4-TRANSPORT/", "tcpip/config/tcpip_udp.py")
    tcpipUdpComponent.addCapability("libtcpipUdp","UDP",True)
    tcpipUdpComponent.addDependency("Udp_IP_Dependency", "IP", None, True, True)
    tcpipUdpComponent.setDisplayType("TCP/IP Library")

    ###########  TCP/IP LIBRARY Application Layer Configurations  ###########   
    tcpipAnnounceComponent = Module.CreateComponent("tcpipAnnounce", "ANNOUNCE", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_announce.py")
    tcpipAnnounceComponent.addCapability("libtcpipAnnounce","ANNOUNCE",True)
    tcpipAnnounceComponent.addDependency("Announce_IPv4_Dependency", "IPv4", None, True, True)
    tcpipAnnounceComponent.addDependency("Announce_UDP_Dependency", "UDP", None, True, True)    
    tcpipAnnounceComponent.setDisplayType("TCP/IP Library")
    
    tcpipBerkeleyApiComponent = Module.CreateComponent("tcpipBerkeleyApi", "Berkeley API", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_berkeley_api.py")
    tcpipBerkeleyApiComponent.addCapability("libtcpipBerkeleyApi","BSD",True)   
    tcpipBerkeleyApiComponent.addDependency("BSD_TCP_Dependency", "TCP", None, True, True)
    tcpipBerkeleyApiComponent.addDependency("BSD_UDP_Dependency", "UDP", None, True, True)
    tcpipBerkeleyApiComponent.addDependency("BSD_NETPRES_Dependency", "net_pres", True, True)
    tcpipBerkeleyApiComponent.addDependency("BSD_DNSC_Dependency", "DNSC", None, True, True)
    tcpipBerkeleyApiComponent.setDisplayType("TCP/IP Library")
    
    tcpipDdnsComponent = Module.CreateComponent("tcpipDdns", "DDNS", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_ddns.py")
    tcpipDdnsComponent.addCapability("libtcpipDdns","DDNS",True)    
    tcpipDdnsComponent.addDependency("Ddns_UDP_Dependency", "UDP", None, True, True)
    tcpipDdnsComponent.addDependency("Ddns_IPv4_Dependency", "IPv4", None, True, True)  
    tcpipDdnsComponent.setDisplayType("TCP/IP Library")
    
    tcpipDhcpComponent = Module.CreateComponent("tcpipDhcp", "DHCP CLIENT", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_dhcp.py")
    tcpipDhcpComponent.addCapability("libtcpipDhcp","DHCPC",True)
    tcpipDhcpComponent.addDependency("Dhcpc_IPv4_Dependency", "IPv4", None, True, True)
    tcpipDhcpComponent.addDependency("Dhcpc_UDP_Dependency", "UDP", None, True, True)
    tcpipDhcpComponent.setDisplayType("TCP/IP Library")
    
    tcpipDhcpsComponent = Module.CreateComponent("tcpipDhcps", "DHCP SERVER", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_dhcps.py")
    tcpipDhcpsComponent.addCapability("libtcpipDhcps","DHCPS",True)
    tcpipDhcpsComponent.addDependency("Dhcps_IPv4_Dependency", "IPv4", None, True, True)
    tcpipDhcpsComponent.addDependency("Dhcps_UDP_Dependency", "UDP", None, True, True)  
    tcpipDhcpsComponent.setDisplayType("TCP/IP Library")
    
    tcpipDnsComponent = Module.CreateComponent("tcpipDns", "DNS CLIENT", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_dns.py")
    tcpipDnsComponent.addCapability("libtcpipDns","DNSC",True)  
    tcpipDnsComponent.addDependency("Dns_UDP_Dependency", "UDP", None, True, True)
    tcpipDnsComponent.setDisplayType("TCP/IP Library")
    
    tcpipDnssComponent = Module.CreateComponent("tcpipDnss", "DNS SERVER", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_dnss.py")
    tcpipDnssComponent.addCapability("libtcpipDnss","DNSS",True)    
    tcpipDnssComponent.addDependency("Dnss_UDP_Dependency", "UDP", None, True, True)    
    tcpipDnssComponent.setDisplayType("TCP/IP Library")
    
    tcpipFtpsComponent = Module.CreateComponent("tcpipFtps", "FTP SERVER", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_ftps.py")
    tcpipFtpsComponent.addCapability("libtcpipFtps","FTPS",True)    
    tcpipFtpsComponent.addDependency("Ftps_TCP_Dependency", "TCP", None, True, True)    
    tcpipFtpsComponent.addDependency("Ftps_TcpipFs_Dependency", "SYS_FS", None, True, True)
    tcpipFtpsComponent.setDisplayType("TCP/IP Library")
    
    tcpipHttpNetComponent = Module.CreateComponent("tcpipHttpNet", "HTTPNET SERVER", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_httpnet.py")
    tcpipHttpNetComponent.addCapability("libtcpipHttpNet","HTTPNET",True)   
    tcpipHttpNetComponent.addDependency("HttpNet_TCP_Dependency", "TCP", None, True, True)  
    tcpipHttpNetComponent.addDependency("HttpNet_TcpipFs_Dependency", "SYS_FS", None, True, True)
    tcpipHttpNetComponent.addDependency("HttpNet_NetPres_Dependency", "net_pres", True, True)
    tcpipHttpNetComponent.setDisplayType("TCP/IP Library")

    if "SAMA5" not in processor:    
        tcpipHttpComponent = Module.CreateComponent("tcpipHttp", "HTTP SERVER", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_http.py")
        tcpipHttpComponent.addCapability("libtcpipHttp","HTTP",True)
        tcpipHttpComponent.addDependency("Http_TCP_Dependency", "TCP", None, True, True)
        tcpipHttpComponent.addDependency("Http_TcpipFs_Dependency", "SYS_FS", None, True, True)
        tcpipHttpComponent.addDependency("Http_Crypto_Dependency", "LIB_CRYPTO", None, True, True)
        tcpipHttpComponent.setDisplayType("TCP/IP Library")

    tcpipIperfComponent = Module.CreateComponent("tcpipIperf", "IPERF", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_iperf.py")
    tcpipIperfComponent.addCapability("libtcpipIperf","IPERF",True)
    tcpipIperfComponent.addDependency("Iperf_TCP_Dependency", "TCP", None, True, True)
    tcpipIperfComponent.addDependency("Iperf_UDP_Dependency", "UDP", None, True, True)
    tcpipIperfComponent.setDisplayType("TCP/IP Library")

    tcpipFtpcComponent = Module.CreateComponent("tcpipFtpc", "FTP CLIENT", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_ftpc.py")
    tcpipFtpcComponent.addCapability("libtcpipFtpc","FTPC",True)
    tcpipFtpcComponent.addDependency("FTPC_TCP_Dependency", "TCP", None, True, True)    
    tcpipFtpcComponent.addDependency("FTPC_TcipFs_Dependency", "SYS_FS", None, True, True)
    tcpipFtpcComponent.setDisplayType("TCP/IP Library")
    
    tcpipNbnsComponent = Module.CreateComponent("tcpipNbns", "NBNS", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_nbns.py")
    tcpipNbnsComponent.addCapability("libtcpipNbns","NBNS",True)
    tcpipNbnsComponent.addDependency("Nbns_IPv4_Dependency", "IPv4", None, True, True)
    tcpipNbnsComponent.addDependency("Nbns_UDP_Dependency", "UDP", None, True, True)    
    tcpipNbnsComponent.setDisplayType("TCP/IP Library")
    
    # tcpipRebootComponent = Module.CreateComponent("tcpipReboot", "REBOOT", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_reboot.py")
    # tcpipRebootComponent.addCapability("libtcpipReboot","REBOOT",True)
    # tcpipRebootComponent.addDependency("Reboot_IPv4_Dependency", "IPv4", None, True, True)
    # tcpipRebootComponent.addDependency("Reboot_UDP_Dependency", "UDP", None, True, True)
    # tcpipRebootComponent.setDisplayType("TCP/IP Library")

    tcpipSmtpcComponent = Module.CreateComponent("tcpipSmtpc", "SMTP CLIENT", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_smtpc.py")
    tcpipSmtpcComponent.addCapability("libtcpipSmtpc","SMTPC",True)
    tcpipSmtpcComponent.addDependency("Smtpc_TCP_Dependency", "TCP", None, True, True)  
    tcpipSmtpcComponent.addDependency("Smtpc_NetPres_Dependency", "net_pres", True, True)
    tcpipSmtpcComponent.addDependency("Smtpc_DNSC_Dependency", "DNSC", None, True, True)
    tcpipSmtpcComponent.addDependency("Smtpc_TcpipFs_Dependency", "SYS_FS", None, True, True)
    tcpipSmtpcComponent.setDisplayType("TCP/IP Library")
    
    tcpipSnmpComponent = Module.CreateComponent("tcpipSnmp", "SNMP", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_snmp.py")
    tcpipSnmpComponent.addCapability("libtcpipSnmp","SNMP",True)    
    tcpipSnmpComponent.addDependency("Snmp_UDP_Dependency", "UDP", None, True, True)    
    tcpipSnmpComponent.addDependency("Snmp_TcpipFs_Dependency", "SYS_FS", None, True, True)
    tcpipSnmpComponent.setDisplayType("TCP/IP Library")

    if "SAMA5" not in processor:    
        tcpipSnmpv3Component = Module.CreateComponent("tcpipSnmpv3", "SNMPV3", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_snmpv3.py")
        tcpipSnmpv3Component.addCapability("libtcpipSnmpv3","SNMPV3",True)  
        tcpipSnmpv3Component.addDependency("Snmpv3_SNMP_Dependency", "SNMP", None, True, True)
        tcpipSnmpv3Component.setDisplayType("TCP/IP Library")

    tcpipSntpComponent = Module.CreateComponent("tcpipSntp", "SNTP", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_sntp.py")
    tcpipSntpComponent.addCapability("libtcpipSntp","SNTP",True)    
    tcpipSntpComponent.addDependency("Sntp_DNSC_Dependency", "DNSC", None, True, True)
    tcpipSntpComponent.setDisplayType("TCP/IP Library")
    
    tcpipTelnetComponent = Module.CreateComponent("tcpipTelnet", "TELNET", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_telnet.py")
    tcpipTelnetComponent.addCapability("libtcpipTelnet","TELNET",True)
    tcpipTelnetComponent.addDependency("Telnet_TcpipCmd_Dependency", "TCPIP_CMD", None, True, True)
    tcpipTelnetComponent.addDependency("Telnet_NetPres_Dependency", "net_pres", True, True)
    tcpipTelnetComponent.setDisplayType("TCP/IP Library")
    
    tcpipTftpcComponent = Module.CreateComponent("tcpipTftpc", "TFTP CLIENT", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_tftpc.py")
    tcpipTftpcComponent.addCapability("libtcpipTftpc","TFTPC",True)
    tcpipTftpcComponent.addDependency("Tftpc_IPv4_Dependency", "IPv4", None, True, True)
    tcpipTftpcComponent.addDependency("Tftpc_UDP_Dependency", "UDP", None, True, True)  
    #tcpipTftpcComponent.addDependency("Tftpc_MAC_Dependency", "MAC")
    tcpipTftpcComponent.addDependency("Tftpc_TcpipFs_Dependency", "SYS_FS", None, True, True)
    tcpipTftpcComponent.setDisplayType("TCP/IP Library")
    
    tcpipTftpsComponent = Module.CreateComponent("tcpipTftps", "TFTP SERVER", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_tftps.py")
    tcpipTftpsComponent.addCapability("libtcpipTftps","TFTPS",True)
    tcpipTftpsComponent.addDependency("Tftps_IPv4_Dependency", "IPv4", None, True, True)
    tcpipTftpsComponent.addDependency("Tftps_UDP_Dependency", "UDP", None, True, True)  
    #tcpipTftpsComponent.addDependency("Tftps_MAC_Dependency", "MAC")
    tcpipTftpsComponent.addDependency("Tftps_TcpipFs_Dependency", "SYS_FS", None, True, True)
    tcpipTftpsComponent.setDisplayType("TCP/IP Library")
    
    tcpipZeroConfComponent = Module.CreateComponent("tcpipZeroConf", "ZEROCONF", "/Libraries/TCPIP/Layer7-APPLICATION/", "tcpip/config/tcpip_zeroconf.py")
    tcpipZeroConfComponent.addCapability("libtcpipZeroConf","ZEROCONF",True)
    tcpipZeroConfComponent.addDependency("ZeroConf_IPv4_Dependency", "IPv4", None, True, True)
    tcpipZeroConfComponent.addDependency("ZeroConf_UDP_Dependency", "UDP", None, True, True)
    tcpipZeroConfComponent.setDisplayType("TCP/IP Library")

    ###########  TCP/IP LIBRARY Datalink & Physical Layer Configurations  ###########
    if Peripheral.moduleExists("GMAC"):
        drvGmacComponent = Module.CreateComponent("drvGmac", "GMAC", "/Harmony/Drivers/MAC Driver/Internal/", "driver/gmac/config/drv_intmac_gmac.py")
        drvGmacComponent.addCapability("libdrvGmac","MAC")
        drvGmacComponent.addDependency("GMAC_PHY_Dependency", "PHY", None, True, True)  
    elif Peripheral.moduleExists("EMAC"):
        aDrvMacComponent_0 = Module.CreateComponent("drvEmac0", "EMAC0", "/Harmony/Drivers/MAC Driver/Internal/", "driver/emac/config/drv_intmac_emac.py")
        aDrvMacComponent_0.addCapability( "libdrvMac0", "MAC")
        aDrvMacComponent_0.addDependency("MAC_PHY_Dependency0", "PHY", None, True, True)
        aDrvMacComponent_1 = Module.CreateComponent("drvEmac1", "EMAC1", "/Harmony/Drivers/MAC Driver/Internal/", "driver/emac/config/drv_intmac_emac.py")
        aDrvMacComponent_1.addCapability( "libdrvMac1", "MAC")
        aDrvMacComponent_1.addDependency("MAC_PHY_Dependency1", "PHY", None, True, True)
    elif "PIC32M" in Variables.get("__PROCESSOR"):
        drvPic32mEthmacComponent = Module.CreateComponent("drvPic32mEthmac", "ETHMAC", "/Harmony/Drivers/MAC Driver/Internal/", "driver/ethmac/config/drv_intmac_ethmac.py")
        drvPic32mEthmacComponent.addCapability("libdrvPic32mEthmac","MAC")
        drvPic32mEthmacComponent.addDependency("ETHMAC_PHY_Dependency", "PHY", None, True, True)
            
    ## MIIM Driver
    drvMiimComponent = Module.CreateComponent("drvMiim", "MIIM Driver", "/Harmony/Drivers/", "driver/miim/config/drv_miim.py")
    drvMiimComponent.addCapability("libdrvMiim","MIIM",True)    
    
    ################# ETHERNET PHY Driver ##############################################
    #Driver for Micrel KSZ8041 PHY
    drvExtPhyKsz8041Component = Module.CreateComponent("drvExtPhyKsz8041", "KSZ8041", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_ksz8041.py")
    drvExtPhyKsz8041Component.addCapability("libdrvExtPhyKsz8041","PHY",True)   
    drvExtPhyKsz8041Component.addDependency("KSZ8041_MIIM_Dependency", "MIIM", None, True, True)  
    
    #Driver for Micrel KSZ8061 PHY
    drvExtPhyKsz8061Component = Module.CreateComponent("drvExtPhyKsz8061", "KSZ8061", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_ksz8061.py")
    drvExtPhyKsz8061Component.addCapability("libdrvExtPhyKsz8061","PHY",True)   
    drvExtPhyKsz8061Component.addDependency("KSZ8061_MIIM_Dependency", "MIIM", None, True, True)    
    
    #Driver for Micrel KSZ8081 PHY
    drvExtPhyKsz8081Component = Module.CreateComponent("drvExtPhyKsz8081", "KSZ8081", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_ksz8081.py")
    drvExtPhyKsz8081Component.addCapability("libdrvExtPhyKsz8081","PHY",True)   
    drvExtPhyKsz8081Component.addDependency("KSZ8081_MIIM_Dependency", "MIIM", None, True, True)    
    
    #Driver for Micrel KSZ8091 PHY
    drvExtPhyKsz8091Component = Module.CreateComponent("drvExtPhyKsz8091", "KSZ8091", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_ksz8091.py")
    drvExtPhyKsz8091Component.addCapability("libdrvExtPhyKsz8091","PHY",True)   
    drvExtPhyKsz8091Component.addDependency("KSZ8091_MIIM_Dependency", "MIIM", None, True, True)    
        
    #Driver for Micrel KSZ8863 PHY
    drvExtPhyKsz8863Component = Module.CreateComponent("drvExtPhyKsz8863", "KSZ8863", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_ksz8863.py")
    drvExtPhyKsz8863Component.addCapability("libdrvExtPhyKsz8863","PHY",True)   
    drvExtPhyKsz8863Component.addDependency("KSZ8863_MIIM_Dependency", "MIIM", None, True, True)  
    
    #Driver for SMSC LAN8700 PHY
    drvExtPhyLan8700Component = Module.CreateComponent("drvExtPhyLan8700", "LAN8700", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_lan8700.py")
    drvExtPhyLan8700Component.addCapability("libdrvExtPhyLan8700","PHY",True)   
    drvExtPhyLan8700Component.addDependency("LAN8700_MIIM_Dependency", "MIIM", None, True, True)       
    
    #Driver for SMSC LAN8720PHY
    drvExtPhyLan8720Component = Module.CreateComponent("drvExtPhyLan8720", "LAN8720", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_lan8720.py")
    drvExtPhyLan8720Component.addCapability("libdrvExtPhyLan8720","PHY",True)   
    drvExtPhyLan8720Component.addDependency("LAN8720_MIIM_Dependency", "MIIM", None, True, True) 
    
    #Driver for SMSC LAN8740 PHY
    drvExtPhyLan8740Component = Module.CreateComponent("drvExtPhyLan8740", "LAN8740", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_lan8740.py")
    drvExtPhyLan8740Component.addCapability("libdrvExtPhyLan8740","PHY",True)   
    drvExtPhyLan8740Component.addDependency("LAN8740_MIIM_Dependency", "MIIM", None, True, True)        
    
    #Driver for SMSC LAN9303PHY
    drvExtPhyLan9303Component = Module.CreateComponent("drvExtPhyLan9303", "LAN9303", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_lan9303.py")
    drvExtPhyLan9303Component.addCapability("libdrvExtPhyLan9303","PHY",True)   
    drvExtPhyLan9303Component.addDependency("LAN9303_MIIM_Dependency", "MIIM", None, True, True) 
    
    #Driver for SMSC DP83640PHY
    drvExtPhyDp83640Component = Module.CreateComponent("drvExtPhyDp83640", "DP83640", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_dp83640.py")
    drvExtPhyDp83640Component.addCapability("libdrvExtPhyDp83640","PHY",True)   
    drvExtPhyDp83640Component.addDependency("DP83640_MIIM_Dependency", "MIIM", None, True, True) 
    
    #Driver for SMSC DP83848PHY
    drvExtPhyDp83848Component = Module.CreateComponent("drvExtPhyDp83848", "DP83848", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_dp83848.py")
    drvExtPhyDp83848Component.addCapability("libdrvExtPhyDp83848","PHY",True)   
    drvExtPhyDp83848Component.addDependency("DP83848_MIIM_Dependency", "MIIM", None, True, True) 
    
    #Driver for SMSC IP101GRPHY
    drvExtPhyIp101grComponent = Module.CreateComponent("drvExtPhyIp101gr", "IP101GR", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_ip101gr.py")
    drvExtPhyIp101grComponent.addCapability("libdrvExtPhyIp101gr","PHY",True)   
    drvExtPhyIp101grComponent.addDependency("IP101GR_MIIM_Dependency", "MIIM", None, True, True)     
    
    #Driver for ENCX24J600
    drvExtMacEncx24j600Component = Module.CreateGeneratorComponent("drvExtMacEncx24j600", "ENCX24J600", "/Harmony/Drivers/External Ethernet Controller", "driver/encx24j600/config/drv_encx24j600_common.py", "driver/encx24j600/config/drv_encx24j600.py")
    drvExtMacEncx24j600Component.addCapability("libdrvExtMacEncx24j600","MAC",None, False)   
    drvExtMacEncx24j600Component.addDependency("ENCX24J600_SPI", "DRV_SPI", None, False, True)   
    
    #Driver for ENC28J60
    drvExtMacEnc28j60Component = Module.CreateGeneratorComponent("drvExtMacEnc28j60", "ENC28J60", "/Harmony/Drivers/External Ethernet Controller", "driver/enc28j60/config/drv_enc28j60_common.py", "driver/enc28j60/config/drv_enc28j60.py")
    drvExtMacEnc28j60Component.addCapability("libdrvExtMacEnc28j60","MAC",None, False)  
    drvExtMacEnc28j60Component.addDependency("ENC28J60_SPI", "DRV_SPI", None, False, True)   
        
    ########################## Harmony Network Presentation Module #################################    
    netPresComponent = Module.CreateGeneratorComponent("netPres", "Presentation Layer", "/Harmony/Harmony Networking","net_pres/pres/config/netPres_common.py","net_pres/pres/config/netPres.py")
    netPresComponent.addCapability("libNetPres","net_pres",True)    
    netPresComponent.addDependency("NetPres_Crypto_Dependency", "TLS Provider", None, False, False)
    
    ############################### TCP/IP STACK CONFIGURATOR #####################################
    #tcpipAutoConfigComponent = Module.CreateComponent("tcpip_template", "TCP/IP Stack Configurator", "/Libraries/TCPIP/", "tcpip/config/tcpip_templates.py")

    tcpipAutoConfigAppsComponent = Module.CreateComponent("tcpip_apps_config", "TCP/IP Application Layer Configurator", "/Libraries/TCPIP/", "tcpip/config/tcpip_configurator_apps.py")

    tcpipAutoConfigTransportComponent = Module.CreateComponent("tcpip_transport_config", "TCP/IP Transport Layer Configurator", "/Libraries/TCPIP/", "tcpip/config/tcpip_configurator_transport.py")

    tcpipAutoConfigNetworkComponent = Module.CreateComponent("tcpip_network_config", "TCP/IP Network Layer Configurator", "/Libraries/TCPIP/", "tcpip/config/tcpip_configurator_network.py")

    tcpipAutoConfigDriverComponent = Module.CreateComponent("tcpip_driver_config", "TCP/IP Driver Layer Configurator", "/Libraries/TCPIP/", "tcpip/config/tcpip_configurator_driver.py")

    tcpipAutoConfigBasicComponent = Module.CreateComponent("tcpip_basic_config", "TCP/IP Basic Configurator", "/Libraries/TCPIP/", "tcpip/config/tcpip_configurator_basic.py")
    
    ########################## Thirdy-Party Modules #################################   
    # Wolfmqtt 
    wolfmqttComponent = Module.CreateComponent("lib_wolfmqtt", "wolfMQTT Library", "/Third Party Libraries/wolfSSL/", "third_party_adapter/wolfMQTT/config/wolfmqtt.py")
    wolfmqttComponent.addCapability("lib_wolfmqtt","wolfmqtt",True)   
    wolfmqttComponent.addDependency("WolfMqtt_NetPres_Dependency", "net_pres", None, True, False)