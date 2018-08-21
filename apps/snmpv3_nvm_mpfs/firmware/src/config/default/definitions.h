/*******************************************************************************
  System Definitions

  File Name:
    definitions.h

  Summary:
    project system definitions.

  Description:
    This file contains the system-wide prototypes and definitions for a project.

 *******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017-2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
 *******************************************************************************/
//DOM-IGNORE-END

#ifndef DEFINITIONS_H
#define DEFINITIONS_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include "crypto/crypto.h"
#include "peripheral/clk/plib_clk.h"
#include "peripheral/pio/plib_pio.h"
#include "peripheral/nvic/plib_nvic.h"
#include "peripheral/mpu/plib_mpu.h"
#include "bsp/bsp.h"
#include "system/int/sys_int.h"
#include "system/ports/sys_ports.h"
#include "system/dma/sys_dma.h"
#include "osal/osal.h"
#include "driver/memory/drv_memory.h"
#include "driver/memory/drv_memory_efc0.h"
#include "driver/usart/drv_usart_definitions.h"
#include "driver/usart/drv_usart.h"
#include "peripheral/efc/plib_efc0.h"
#include "net/pres/net_pres.h"
#include "net/pres/net_pres_encryptionproviderapi.h"
#include "net/pres/net_pres_transportapi.h"
#include "net/pres/net_pres_socketapi.h"
#include "system/console/sys_console.h"
#include "system/console/sys_debug.h"
#include "system/console/sys_command.h"
#include "system/fs/sys_fs.h"
#include "system/fs/sys_fs_media_manager.h"
#include "system/fs/mpfs/mpfs.h"
#include "system/time/sys_time.h"
#include "peripheral/tc/plib_tc0.h"
#include "library/tcpip/tcpip.h"
#include "driver/gmac/drv_gmac.h"
#include "driver/miim/drv_miim.h"
#include "system/sys_time_h2_adapter.h"
#include "system/sys_int_h2_adapter.h"
#include "system/sys_clk_h2_adapter.h"
#include "system/sys_random_h2_adapter.h"
#include "system/sys_reset_h2_adapter.h"
#include "peripheral/trng/plib_trng0.h"
#include "peripheral/usart/plib_usart1.h"
#include "app.h"



// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: System Functions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* System Initialization Function

  Function:
    void SYS_Initialize( void *data )

  Summary:
    Function that initializes all modules in the system.

  Description:
    This function initializes all modules in the system, including any drivers,
    services, middleware, and applications.

  Precondition:
    None.

  Parameters:
    data            - Pointer to the data structure containing any data
                      necessary to initialize the module. This pointer may
                      be null if no data is required and default initialization
                      is to be used.

  Returns:
    None.

  Example:
    <code>
    SYS_Initialize ( NULL );

    while ( true )
    {
        SYS_Tasks ( );
    }
    </code>

  Remarks:
    This function will only be called once, after system reset.
*/

void SYS_Initialize( void *data );

// *****************************************************************************
/* System Tasks Function

  Function:
    void SYS_Tasks ( void );

  Summary:
    Function that performs all polled system tasks.

  Description:
    This function performs all polled system tasks by calling the state machine
    "tasks" functions for all polled modules in the system, including drivers,
    services, middleware and applications.

  Precondition:
    The SYS_Initialize function must have been called and completed.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    SYS_Initialize ( NULL );

    while ( true )
    {
        SYS_Tasks ( );
    }
    </code>

  Remarks:
    If the module is interrupt driven, the system will call this routine from
    an interrupt context.
*/

void SYS_Tasks ( void );

// *****************************************************************************
// *****************************************************************************
// Section: Type Definitions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* System Objects

  Summary:
    Structure holding the system's object handles

  Description:
    This structure contains the object handles for all objects in the
    MPLAB Harmony project's system configuration.

  Remarks:
    These handles are returned from the "Initialize" functions for each module
    and must be passed into the "Tasks" function for each module.
*/

typedef struct
{
    SYS_MODULE_OBJ  drvMiim;
    SYS_MODULE_OBJ  drvMemory0;
    SYS_MODULE_OBJ  drvUsart0;
    SYS_MODULE_OBJ  netPres;

    SYS_MODULE_OBJ  sysConsole0;
    SYS_MODULE_OBJ  sysDebug;

    SYS_MODULE_OBJ  sysTime;
    SYS_MODULE_OBJ  tcpip;

} SYSTEM_OBJECTS;


// *****************************************************************************
// *****************************************************************************
// Section: extern declarations
// *****************************************************************************
// *****************************************************************************



extern SYSTEM_OBJECTS sysObj;

//DOM-IGNORE-BEGIN
#ifdef __cplusplus
}
#endif
//DOM-IGNORE-END

#endif /* DEFINITIONS_H */
/*******************************************************************************
 End of File
*/
