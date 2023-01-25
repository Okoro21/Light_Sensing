/*
 * This is the header file for the SPIsensor struct
 * Implementation operations that are declared within this module are contained within SPIsensor.c
 */

#ifndef INC_SPISENSOR_H
#define INC_SPISENSOR_H

#include "stm32f7xx_hal.h"

/* Size of data buffer*/
#define BUFSIZE 256

/*
 * The max output value of the photosensor is not known
 * Therefore, I decided to map the largest that we have seen from the sensor (3000) to 1000, and the
 * lowest value that we seen is still zero
 */

#define V_CONVERSION 0.3333


/*
 * ADC_ptr should be assigned to the &hadcx (x = 1,2,3 ...). hadcx corresponds to the current ADC peripheral being used
 * ADC_vals is a container which stores the ADC values read from the light sensor
 * rawADC
 * count
 * ready_check is a flag that is set to 1 once the ADC_vals has reached max capacity
 */

struct SPI_sensor
{
	ADC_HandleTypeDef *ADC_ptr;
	uint16_t ADC_vals[BUFSIZE];
	uint16_t count;
	int ready_check;
};

typedef struct SPI_sensor SPI_sensor;

/*
 * Pre Function call: SPI_sensor struct has been instantiated within calling function
 * Post Function call: count and ready_check members have been set to zero
 */

void SetMembers(SPI_sensor *my_struct);

#endif /* INC_SPISENSOR_H */
