<#--
/*******************************************************************************
  SMTP Freemarker Template File

  Company:
    Microchip Technology Inc.

  File Name:
    smtp.h.ftl

  Summary:
    SMTP Freemarker Template File

  Description:

*******************************************************************************/

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
<#if TCPIP_USE_SMTP_CLIENT == true>
/*** SMTP Configuration ***/
#define TCPIP_STACK_USE_SMTP_CLIENT
#define TCPIP_SMTP_SERVER_REPLY_TIMEOUT 	${TCPIP_SMTP_SERVER_REPLY_TIMEOUT}
#define TCPIP_SMTP_WRITE_READY_SPACE 	    ${TCPIP_SMTP_WRITE_READY_SPACE}
#define TCPIP_SMTP_MAX_WRITE_SIZE   	    ${TCPIP_SMTP_MAX_WRITE_SIZE}
#define TCPIP_SMTP_TASK_TICK_RATE			${TCPIP_SMTP_TASK_TICK_RATE}
</#if>

<#--
/*******************************************************************************
 End of File
*/
-->