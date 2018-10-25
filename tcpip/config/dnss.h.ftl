<#--
/*******************************************************************************
  DNS Server Freemarker Template File

  Company:
    Microchip Technology Inc.

  File Name:
    dns.h.ftl

  Summary:
    DNS Server Freemarker Template File

  Description:

*******************************************************************************/
-->

<#--
/*******************************************************************************
Copyright (c) 2014 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/
-->
<#if TCPIP_USE_DNSS == true>
/*** DNS Server Configuration ***/
#define TCPIP_STACK_USE_DNS_SERVER
#define TCPIP_DNSS_HOST_NAME_LEN		    		${TCPIP_DNSS_HOST_NAME_LEN}
<#if TCPIP_DNSS_REPLY_BOARD_ADDR == true>
#define TCPIP_DNSS_REPLY_BOARD_ADDR				true
<#else>
#define TCPIP_DNSS_REPLY_BOARD_ADDR				false
</#if>
#define TCPIP_DNSS_CACHE_PER_IPV4_ADDRESS			${TCPIP_DNSS_CACHE_PER_IPV4_ADDRESS}
#define TCPIP_DNSS_CACHE_PER_IPV6_ADDRESS			${TCPIP_DNSS_CACHE_PER_IPV6_ADDRESS}
#define TCPIP_DNSS_TTL_TIME							${TCPIP_DNSS_TTL_TIME}
#define TCPIP_DNSS_TASK_PROCESS_RATE			    ${TCPIP_DNSS_TASK_PROCESS_RATE}
<#if TCPIP_DNSS_DELETE_OLD_LEASE == true>
#define TCPIP_DNSS_DELETE_OLD_LEASE				true
<#else>
#define TCPIP_DNSS_DELETE_OLD_LEASE				false
</#if>

/***Maximum DNS server Cache entries. It is the sum of TCPIP_DNSS_CACHE_PER_IPV4_ADDRESS and TCPIP_DNSS_CACHE_PER_IPV6_ADDRESS.***/
#define TCPIP_DNSS_CACHE_MAX_SERVER_ENTRIES     (TCPIP_DNSS_CACHE_PER_IPV4_ADDRESS+TCPIP_DNSS_CACHE_PER_IPV6_ADDRESS)
</#if>

<#--
/*******************************************************************************
 End of File
*/
-->
