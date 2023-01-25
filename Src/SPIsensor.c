

#include "SPIsensor.h"
#include <string.h>

void SetMembers(SPI_sensor *my_struct)
{
	my_struct -> count = 0;
	my_struct -> ready_check = 0;

	memset(my_struct -> ADC_vals, 0, BUFSIZE * sizeof(uint16_t));
}
