def loadModule():
	print("Load Module: Harmony TCP/IP Stack")

	tcpipStackComponent = Module.CreateSharedComponent("tcpipStack", "TCPIP CORE", "/Libraries/TCPIP/CORE/", "library/config/tcpip_stack.py")
	tcpipStackComponent.addCapability("libtcpipStack","TCPIP_CORE")
	tcpipStackComponent.addDependency("Core_Rtos_Dependency", "RTOS")
	#tcpipStackComponent.addDependency("Tcpip_NetConfig_Dependency", "NET_CONFIG")
	tcpipStackComponent.addDependency("Core_Heap_Dependency", "HEAP")
	tcpipStackComponent.addDependency("Core_SysFs_Dependency", "SYSFSWRAPPER")
	tcpipStackComponent.addDependency("Core_NetConfig_Dependency", "NETCONFIG")
	
	
	tcpipHeapComponent = Module.CreateComponent("tcpipHeap", "HEAP", "/Libraries/TCPIP/CORE/", "library/config/tcpip_heap.py")
	tcpipHeapComponent.addCapability("libtcpipRtos","HEAP")	
	
	tcpipRtosComponent = Module.CreateComponent("tcpipRtos", "RTOS", "/Libraries/TCPIP/CORE/", "library/config/tcpip_rtos.py")
	tcpipRtosComponent.addCapability("libtcpipRtos","RTOS")	
	tcpipRtosComponent.addDependency("Rtos_Osal_Dependency", "OSAL")
	
	tcpipIPv4Component = Module.CreateSharedComponent("tcpipIPv4", "IPv4", "/Libraries/TCPIP/Layer3-NETWORK/", "library/config/tcpip_ipv4.py")
	tcpipIPv4Component.addCapability("libTcpipIPv4","IPv4")
	tcpipIPv4Component.addCapability("libTcpipIPv4IP","IP")
	tcpipIPv4Component.addDependency("Ipv4_Stack_Dependency", "TCPIP_CORE")	
	
	tcpipIPv6Component = Module.CreateSharedComponent("tcpipIPv6", "IPv6", "/Libraries/TCPIP/Layer3-NETWORK/", "library/config/tcpip_ipv6.py")
	tcpipIPv6Component.addCapability("libTcpipIPv6","IPv6")
	tcpipIPv6Component.addCapability("libTcpipIPv6IP","IP")
	tcpipIPv6Component.addDependency("Ipv6_Stack_Dependency", "TCPIP_CORE")
	
	tcpipNdpComponent = Module.CreateComponent("tcpipNdp", "NDP", "/Libraries/TCPIP/Layer3-NETWORK/", "library/config/tcpip_ndp.py")
	tcpipNdpComponent.addCapability("libtcpipNdp","NDP")
	tcpipNdpComponent.addDependency("Ndp_IPv6_Dependency", "IPv6")
	
	tcpipTcpComponent = Module.CreateComponent("tcpipTcp", "TCP", "/Libraries/TCPIP/Layer4-TRANSPORT/", "library/config/tcpip_tcp.py")
	tcpipTcpComponent.addCapability("libtcpipTcp","TCP")
	tcpipTcpComponent.addDependency("Tcp_IP_Dependency", "IP")
		
	tcpipUdpComponent = Module.CreateComponent("tcpipUdp", "UDP", "/Libraries/TCPIP/Layer4-TRANSPORT/", "library/config/tcpip_udp.py")
	tcpipUdpComponent.addCapability("libtcpipUdp","UDP")
	tcpipUdpComponent.addDependency("Udp_IP_Dependency", "IP")

	tcpipNetConfigComponent = Module.CreateGeneratorComponent("tcpipNetConfig", "NETCONFIG", "/Libraries/TCPIP/CORE/","library/config/tcpip_network_config_common.py","library/config/tcpip_network_config.py")
	tcpipNetConfigComponent.addCapability("libtcpipNetConfig","NETCONFIG")
	tcpipNetConfigComponent.addDependency("NETCONFIG_MAC_Dependency", "MAC")
	
	tcpipArpComponent = Module.CreateComponent("tcpipArp", "ARP", "/Libraries/TCPIP/Layer3-NETWORK/", "library/config/tcpip_arp.py")
	tcpipArpComponent.addCapability("libtcpipArp","ARP")
	tcpipArpComponent.addDependency("Arp_IPv4_Dependency", "IPv4")
	
	tcpipBerkeleyApiComponent = Module.CreateComponent("tcpipBerkeleyApi", "BSD", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_berkeley_api.py")
	tcpipBerkeleyApiComponent.addCapability("libtcpipBerkeleyApi","BSD")	
	tcpipBerkeleyApiComponent.addDependency("BSD_TCP_Dependency", "TCP")
	tcpipBerkeleyApiComponent.addDependency("BSD_UDP_Dependency", "UDP")
	
	tcpipDhcpComponent = Module.CreateComponent("tcpipDhcp", "DHCP CLIENT", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_dhcp.py")
	tcpipDhcpComponent.addCapability("libtcpipDhcp","DHCPC")
	tcpipDhcpComponent.addDependency("Dhcpc_IPv4_Dependency", "IPv4")
	tcpipDhcpComponent.addDependency("Dhcpc_UDP_Dependency", "UDP")
	
	tcpipDhcpsComponent = Module.CreateComponent("tcpipDhcps", "DHCP SERVER", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_dhcps.py")
	tcpipDhcpsComponent.addCapability("libtcpipDhcps","DHCPS")
	tcpipDhcpsComponent.addDependency("Dhcps_IPv4_Dependency", "IPv4")
	tcpipDhcpsComponent.addDependency("Dhcps_UDP_Dependency", "UDP")	
	
	tcpipDnsComponent = Module.CreateComponent("tcpipDns", "DNS", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_dns.py")
	tcpipDnsComponent.addCapability("libtcpipDns","DNS")	
	tcpipDnsComponent.addDependency("Dns_UDP_Dependency", "UDP")
	
	tcpipDnssComponent = Module.CreateComponent("tcpipDnss", "DNS SERVER", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_dnss.py")
	tcpipDnssComponent.addCapability("libtcpipDnss","DNSS")	
	tcpipDnssComponent.addDependency("Dnss_UDP_Dependency", "UDP")	
	
	tcpipDdnsComponent = Module.CreateComponent("tcpipDdns", "DDNS", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_ddns.py")
	tcpipDdnsComponent.addCapability("libtcpipDdns","DDNS")	
	tcpipDdnsComponent.addDependency("Ddns_UDP_Dependency", "UDP")	
	tcpipDdnsComponent.addDependency("Ddns_IPv4_Dependency", "IPv4")	
	
	tcpipFtpsComponent = Module.CreateComponent("tcpipFtps", "FTP SERVER", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_ftps.py")
	tcpipFtpsComponent.addCapability("libtcpipDdns","FTPS")	
	tcpipFtpsComponent.addDependency("Ftps_TCP_Dependency", "TCP")	
	tcpipFtpsComponent.addDependency("Ftps_IPv4_Dependency", "IPv4")	
	
	tcpipIcmpComponent = Module.CreateComponent("tcpipIcmp", "ICMP", "/Libraries/TCPIP/Layer3-NETWORK/", "library/config/tcpip_icmp.py")
	tcpipIcmpComponent.addCapability("libtcpipIcmp","ICMP")	
	tcpipIcmpComponent.addDependency("Icmp_IPv4_Dependency", "IPv4")
	
	tcpipTelnetComponent = Module.CreateComponent("tcpipTelnet", "TELNET", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_telnet.py")
	tcpipTelnetComponent.addCapability("libtcpipTelnet","TELNET")	
	tcpipTelnetComponent.addDependency("Telnet_TCP_Dependency", "TCP")
	
	tcpipIperfComponent = Module.CreateComponent("tcpipIperf", "IPERF", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_iperf.py")
	tcpipIperfComponent.addCapability("libtcpipIperf","IPERF")
	tcpipIperfComponent.addDependency("Iperf_TCP_Dependency", "TCP")
	tcpipIperfComponent.addDependency("Iperf_UDP_Dependency", "UDP")
	
	tcpipRebootComponent = Module.CreateComponent("tcpipReboot", "REBOOT", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_reboot.py")
	tcpipRebootComponent.addCapability("libtcpipReboot","REBOOT")
	tcpipRebootComponent.addDependency("Reboot_IPv4_Dependency", "IPv4")
	tcpipRebootComponent.addDependency("Reboot_UDP_Dependency", "UDP")
	
	#Commented as per Adrian's review comment
	# tcpipSmtpComponent = Module.CreateComponent("tcpipSmtp", "SMTP", "/Libraries/TCPIP/", "library/config/tcpip_smtp.py")
	# tcpipSmtpComponent.addCapability("libtcpipSmtp","SMTP")	
	# tcpipSmtpComponent.addDependency("Smtp_TCP_Dependency", "TCP")
	
	tcpipSmtpcComponent = Module.CreateComponent("tcpipSmtpc", "SMTP CLIENT", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_smtpc.py")
	tcpipSmtpcComponent.addCapability("libtcpipSmtpc","SMTPC")	
	tcpipSmtpcComponent.addDependency("Smtpc_TCP_Dependency", "TCP")	
	
	tcpipSntpComponent = Module.CreateComponent("tcpipSntp", "SNTP", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_sntp.py")
	tcpipSntpComponent.addCapability("libtcpipSntp","SNTP")	
	tcpipSntpComponent.addDependency("Sntp_UDP_Dependency", "UDP")

	tcpipIgmpComponent = Module.CreateComponent("tcpipIgmp", "IGMP", "/Libraries/TCPIP/Layer3-NETWORK/", "library/config/tcpip_igmp.py")
	tcpipIgmpComponent.addCapability("libtcpipIgmp","IGMP")
	tcpipIgmpComponent.addDependency("Igmp_IPv4_Dependency", "IPv4")
	
	tcpipTftpcComponent = Module.CreateComponent("tcpipTftpc", "TFTP CLIENT", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_tftpc.py")
	tcpipTftpcComponent.addCapability("libtcpipTftpc","TFTPC")
	tcpipTftpcComponent.addDependency("Tftpc_IPv4_Dependency", "IPv4")
	tcpipTftpcComponent.addDependency("Tftpc_UDP_Dependency", "UDP")	

	tcpipZeroConfComponent = Module.CreateComponent("tcpipZeroConf", "ZEROCONF", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_zeroconf.py")
	tcpipZeroConfComponent.addCapability("libtcpipZeroConf","ZEROCONF")
	tcpipZeroConfComponent.addDependency("ZeroConf_IPv4_Dependency", "IPv4")
		
	tcpipCmdComponent = Module.CreateComponent("tcpipCmd", "CMD", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_cmd.py")
	tcpipCmdComponent.addCapability("libtcpipCmd","CMD")	
	tcpipCmdComponent.addDependency("Cmd_TCP_Dependency", "TCP")	
	
	tcpipAnnounceComponent = Module.CreateComponent("tcpipAnnounce", "ANNOUNCE", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_announce.py")
	tcpipAnnounceComponent.addCapability("libtcpipAnnounce","ANNOUNCE")
	tcpipAnnounceComponent.addDependency("Announce_IPv4_Dependency", "IPv4")
	tcpipAnnounceComponent.addDependency("Announce_UDP_Dependency", "UDP")	
	
	tcpipNbnsComponent = Module.CreateComponent("tcpipNbns", "NBNS", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_nbns.py")
	tcpipNbnsComponent.addCapability("libtcpipNbns","NBNS")
	tcpipNbnsComponent.addDependency("Nbns_IPv4_Dependency", "IPv4")
	tcpipNbnsComponent.addDependency("Nbns_UDP_Dependency", "UDP")	

	tcpipHttpComponent = Module.CreateComponent("tcpipHttp", "HTTP", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_http.py")
	tcpipHttpComponent.addCapability("libtcpipHttp","HTTP")	
	tcpipHttpComponent.addDependency("Http_TCP_Dependency", "TCP")

	tcpipHttpNetComponent = Module.CreateComponent("tcpipHttpNet", "HTTPNET", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_httpnet.py")
	tcpipHttpNetComponent.addCapability("libtcpipHttpNet","HTTPNET")	
	tcpipHttpNetComponent.addDependency("HttpNet_TCP_Dependency", "TCP")	
	
	tcpipSnmpComponent = Module.CreateComponent("tcpipSnmp", "SNMP", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_snmp.py")
	tcpipSnmpComponent.addCapability("libtcpipSnmp","SNMP")	
	tcpipSnmpComponent.addDependency("Snmp_UDP_Dependency", "UDP")	
	
	tcpipSnmpv3Component = Module.CreateComponent("tcpipSnmpv3", "SNMPV3", "/Libraries/TCPIP/Layer7-APPLICATION/", "library/config/tcpip_snmpv3.py")
	tcpipSnmpv3Component.addCapability("libtcpipSnmpv3","SNMPV3")	
	tcpipSnmpv3Component.addDependency("Snmpv3_SNMP_Dependency", "SNMP")
	
	tcpipSysFsWrapperComponent = Module.CreateComponent("tcpipSysFsWrapper", "SYSFSWRAPPER", "/Libraries/TCPIP/CORE/", "library/config/tcpip_sysfs_wrapper.py")
	tcpipSysFsWrapperComponent.addCapability("libtcpipSysFsWrapper","SYSFSWRAPPER")	
	tcpipSysFsWrapperComponent.addDependency("SysFsWarapper_TCP_Dependency", "TCP")	
	tcpipSysFsWrapperComponent.addDependency("SysFsWarapper_UDP_Dependency", "UDP")	
	
	########################## Driver Modules ####################################################
	## niyas : decide on moving driver to core repo
	if "SAME70" in Variables.get("__PROCESSOR"):
		drvSamv71GmacComponent = Module.CreateComponent("drvSamv71Gmac", "GMAC", "/Harmony/Drivers/MAC Driver/Internal/", "driver/gmac/config/drv_intmac_gmac.py")
		drvSamv71GmacComponent.addCapability("libdrvSamv71Gmac","MAC")
		drvSamv71GmacComponent.addDependency("GMAC_PHY_Dependency", "PHY")	
	elif "PIC32M" in Variables.get("__PROCESSOR"):
		drvPic32mEthmacComponent = Module.CreateComponent("drvPic32mEthmac", "ETHMAC", "/Harmony/Drivers/MAC Driver/Internal/", "driver/ethmac/config/drv_intmac_ethmac.py")
		drvPic32mEthmacComponent.addCapability("libdrvPic32mEthmac","MAC")
		drvPic32mEthmacComponent.addDependency("ETHMAC_PHY_Dependency", "PHY")
	
	drvExtMacEncx24jComponent = Module.CreateComponent("drvExtMacEncx24j", "ENCX24J600", "/Harmony/Drivers/MAC Driver/External/", "driver/encx24j600/config/drv_extmac_encx24j600.py")
	drvExtMacEncx24jComponent.addCapability("libdrvExtMacEncx24j","MAC")
	
	drvExtMacEnc28jComponent = Module.CreateComponent("drvExtMacEnc28j", "ENC28J60", "/Harmony/Drivers/MAC Driver/External/", "driver/enc28j60/config/drv_extmac_enc28j60.py")
	drvExtMacEnc28jComponent.addCapability("libdrvExtMacEnc28j","MAC")	
	
	drvWifiWinc1500Component = Module.CreateComponent("drvWifiWinc1500", "WINC1500", "/Harmony/Drivers/MAC Driver/WiFi/", "driver/winc1500/config/drv_wifi_winc1500.py")
	drvWifiWinc1500Component.addCapability("libdrvExtMacEnc28j","MAC")	
	
	## niyas : decide on moving driver to core repo
	drvMiimComponent = Module.CreateComponent("drvMiim", "MIIM Driver", "/Harmony/Drivers/", "driver/miim/config/drv_miim.py")
	drvMiimComponent.addCapability("libdrvMiim","MIIM")	
	
	## niyas : decide on moving driver to core repo
	drvExtPhyKsz8061Component = Module.CreateComponent("drvExtPhyKsz8061", "KSZ8061", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_ksz8061.py")
	drvExtPhyKsz8061Component.addCapability("libdrvExtPhyKsz8061","PHY")	
	drvExtPhyKsz8061Component.addDependency("KSZ8061_MIIM_Dependency", "MIIM")	
	
	drvExtPhyKsz8041Component = Module.CreateComponent("drvExtPhyKsz8041", "KSZ8041", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_ksz8041.py")
	drvExtPhyKsz8041Component.addCapability("libdrvExtPhyKsz8041","PHY")	
	drvExtPhyKsz8041Component.addDependency("KSZ8041_MIIM_Dependency", "MIIM")	
	
	drvExtPhyLan8740Component = Module.CreateComponent("drvExtPhyLan8740", "LAN8740", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_lan8740.py")
	drvExtPhyLan8740Component.addCapability("libdrvExtPhyLan8740","PHY")	
	drvExtPhyLan8740Component.addDependency("LAN8740_MIIM_Dependency", "MIIM")		
	
	drvExtPhyLan8720Component = Module.CreateComponent("drvExtPhyLan8720", "LAN8720", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_lan8720.py")
	drvExtPhyLan8720Component.addCapability("libdrvExtPhyLan8720","PHY")	
	drvExtPhyLan8720Component.addDependency("LAN8720_MIIM_Dependency", "MIIM")
	
	drvExtPhyLan8700Component = Module.CreateComponent("drvExtPhyLan8700", "LAN8700", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_lan8700.py")
	drvExtPhyLan8700Component.addCapability("libdrvExtPhyLan8700","PHY")	
	drvExtPhyLan8700Component.addDependency("LAN8700_MIIM_Dependency", "MIIM")	
	
	drvExtPhyLan9303Component = Module.CreateComponent("drvExtPhyLan9303", "LAN9303", "/Harmony/Drivers/PHY Driver", "driver/ethphy/config/drv_extphy_lan9303.py")
	drvExtPhyLan9303Component.addCapability("libdrvExtPhyLan9303","PHY")	
	drvExtPhyLan9303Component.addDependency("LAN9303_MIIM_Dependency", "MIIM")		