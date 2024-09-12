#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

////////////////////////////////////////////////////////////////////////////////
* You have 120 minutes to complete the test.There are 100 points total.
*
*All solutions should compile in Coderpad.io without error or warnings
*
*Penalties:
*-1 / minute over time
* -3 for 1 or more compilation errors
* -2 for 1 or more compilation warnings
*
*Do not use outside aid or share the content of this test
*
*A main() function is provided at the bottom for your use
* /
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// 1a) Macro (10 points)
//    Create a macro (named C_TO_F) to convert from degrees Celsius to
//    Fahrenheit Macro should work for integer or floating point types Note:
//    degF = degC * (9/5) + 32
// Answer: TODO

#define C_TO_F(degC) degC *(9.0 / 5) + 32.0

////////////////////////////////////////////////////////////////////////////////
// 1b) Macro (10 points)
//    Create a macro (named INC_COND(COND, VAR)) to increment parameter VAR if
//    parameter COND evaluates to TRUE and store it to an lvalue like:
//    VAL = INC_COND(COND, VAR);
// Answer:
#define INC_COND(COND, VAR) (COND ? (++VAR, VAR) : VAR)

////////////////////////////////////////////////////////////////////////////////
// 2a) Bit Manipulation (5 points)
//    Write a function that inverts (0 -> 1 or 1 -> 0) the most significant and
//    least significant bits of the data value pointed to by b.
void invertMSBLSB(uint8_t *b) {
	// Answer: TODO
	*b ^= 0x81;

    /*This function inverts the Most Significant Bit(MSB) and Least Significant Bit(LSB) of a byte.

        Here's how it works:

        1. The function takes a pointer to a `uint8_t` (an 8 - bit unsigned integer, also known as a byte) as an argument.
        2. The `^ = ` operator is a bitwise XOR assignment operator. It performs a bitwise XOR operation on the value pointed to by `b` and `0x81` (which is `10000001` in binary), and assigns the result back to the value pointed to by `b`.
        3. The bitwise XOR operation flips the bits where the second operand has a 1. So, `0x81` has 1s at the MSB and LSB positions, so those bits in the byte are flipped.

        Here's an example of how you might use it:

        ```c
        int main() {
        uint8_t x = 0x55;  // 01010101 in binary
        invertMSBLSB(&x);
        printf("%x\n", x);  // Outputs 0xd4, which is 11010100 in binary
        return 0;
    }
    ```

        In this example, the MSB and LSB of `x` are flipped, changing `x` from `0x55` to `0xd4`.*/
}

////////////////////////////////////////////////////////////////////////////////
// 2b) Bit Manipulation (5 points)
//    Write a function that swaps the higest bits in each nibble of the byte
//    pointed to by the pointer b

void swapNibbles(uint8_t *b) {
	// Answer: TODO
	*b = ((*b & 0xF0) >> 4) | ((*b & 0x0F) << 4);

	/*This function swaps the highest bits in each nibble of a byte.
    
    		Here's how it works:
            
            		1. The function takes a pointer to a `uint8_t` (an 8 - bit unsigned integer, also known as a byte) as an argument.
                    2. The `&` operator is a bitwise AND operator. It is used to mask out the bits we want to keep in each nibble.
                    3. The `>>` operator is a right shift operator. It shifts the bits in the byte to the right by 4 positions, effectively moving the highest bits in each nibble to the rightmost positions.
                    4. The `<<` operator is a left shift operator. It shifts the bits in the byte to the left by 4 positions, effectively moving the highest bits in each nibble to the leftmost positions.
                    5. The `|` operator is a bitwise OR operator. It combines the results of the two shift operations, effectively swapping the highest bits in each nibble.
                                                    
     */
                                                            
      }




////////////////////////////////////////////////////////////////////////////////
// 2c) Bit Manipulation (5 points)
//    Write a function that swaps the 4 MSB and 4 LSB of a byte

void swapMSBLSB(uint8_t *b) {
	// Answer: TODO
	*b = ((*b & 0x0F) << 4) | ((*b & 0xF0) >> 4);

	/*This function swaps the 4 Most Significant Bits(MSB) and 4 Least Significant Bits(LSB) of a byte.
    	
    Here's how it works:
                    			
    1. The function takes a pointer to a `uint8_t` (an 8 - bit unsigned integer, also known as a byte) as an argument.
    2. The `&` operator is a bitwise AND operator. It is used to mask out the bits we want to keep in each nibble.
    3. The `<<` operator is a left shift operator. It shifts the bits in the byte to the left by 4 positions, effectively moving the 4 LSB to the 4 MSB positions.
    4. The `>>` operator is a right shift operator. It shifts the bits in the byte to the right by 4 positions, effectively moving the 4 MSB to the 4 LSB positions.
    5. The `|` operator is a bitwise OR operator. It combines the results of the two shift operations, effectively swapping the 4 MSB and 4 LSB.
                                                                                                                                    													
                                                                                                                                                */
															
	  }

////////////////////////////////////////////////////////////////////////////////
// 3a) Debugging (5 points)
//    The function computeSquareADC() has not been producing correct
//    output consistently. Please describe all issues with the function.
// Answer: TODO



////////////////////////////////////////////////////////////////////////////////
// 3a) Debugging (5 points)
//    The function calculatePower() has not been producing correct
//    output consistently. Please describe all issues with the function
uint16_t voltage; // populated from ADC measurement in a periodic interrupt (not
// shown)
uint16_t current; // populated from ADC measurement in a periodic interrupt (not
// shown)


////////////////////////////////////////////////////////////////////////////////
// 4) Memory dump (10 points)
//    The following memory dump was taken while debugging an issue.
//
// Memory Dump:
// Address:  Byte:
// 0x1000    0xA0
// 0x1001    0x0A
// 0x1002    0xBA
// 0x1003    0x48
// 0x1004    0x2C
// 0x1005    0xB7
// 0x1006    0x3B
// 0x1007    0x82
// 0x1008    0x9C
// 0x1009    0xE5
// 0x100A    0x17
// 0x100B    0x40
// 0x100C    0xEF
// 0x100D    0x47
// 0x100E    0x0F
// 0x100F    0x98
// 0x1010    0x6F
// 0x1011    0xD5
// 0x1012    0x70
// 0x1013    0x9E
// 0x1014    0x94
// 0x1015    0x99
// 0x1016    0x4A
// 0x1017    0xBA
// 0x1018    0xCA
// 0x1019    0xB2
// 0x101A    0x32
// 0x101B    0xE6
// 0x101C    0x8E
// 0x101D    0xB9
// 0x101E    0xC5
// 0x101F    0x2E
// 0x1020    0xC3
//
// System is 32-bit, little-endian.
// A variable called myPacket is of type packet_S (typedef below).
// (Default compiler options; unpacked, naturally aligned.)
// The address of myPacket is 0x1010.
//
typedef struct {
    uint8_t count;
    uint16_t data[2];
    uint32_t timestamp;

} packet_S;



// a) What are the values of each member of myPacket?
// Answer: TODO
count = 0x6F
data[0] = 0x70D5
data[1] = 0x949E
timestamp = 0x9E4032B2 //from address 0x1015 to 0x1018
// 
// 
// 
// b) If the system was big-endian, what would the values of each member of
//    myPacket be?
// Answer: TODO
count = 0x6F
data[0] = 0xD570
data[1] = 0x9E94
timestamp = 0x32B2E6C5




////////////////////////////////////////////////////////////////////////////////
// 5) State Machine (20 points)
//
//    Complete the function below to implement the state machine shown in the
//    diagram below for an electronic gumball vending machine.
//     * The initial state of the state machine should be IDLE
//     * The function should output the current state of the state machine
//     * Unexpected or invalid input should not cause a state transition
//     * GENERIC_FAULT may be received in any state and should put the machine
//       into the FAULT state
//
//
//          COIN      +---------+
//   +--------------->|         |   BUTTON
//   |                |  READY  | ---------+
//   |    COIN_RETURN |         |          |
//   |   +----------- +---------+          |
//   |   |                                 |
//   |   V                                 V
// +---------+                        +---------+
// |         |     VEND_COMPLETE      |         |
// |  IDLE   |<-----------------------| VENDING |
// |         |                        |         |
// +---------+                        +---------+
//
//                                 +---------+
//                                 |         |
//                GENERIC_FAULT    |  FAULT  |
//             +------------------>|         |
//                                 +---------+
//

typedef enum { IDLE, READY, VENDING, FAULT } state_E;

typedef enum {
    COIN,
    COIN_RETURN,
    BUTTON,
    VEND_COMPLETE,
    GENERIC_FAULT
} input_E;

state_E currState = IDLE; // set default current state to be IDLE
state_E stateMachine(input_E input) {

    // Answer: TODO
    switch (input) {
        case COIN:
		if (currState == IDLE) {
			currState = READY;
		}
		break;
        case COIN_RETURN:
            if (currState == READY) {
                currState = IDLE;
			}
            break;
		case BUTTON:
			if (currState == READY) {
				currState = VENDING;
			}
			break;
		case VEND_COMPLETE:
			if (currState == VENDING) {
				currState = IDLE;
			}
			break;
		case GENERIC_FAULT:
			currState = FAULT;
			break;
		default:
			break;
	}
	return currState;



  //////////////////////////////////////////////////////////////////////////
  // 5) State Machines
  //
  //  Complete the funtion below to implement the state machine shown in the
  //  diagram below for a traffic light.
  //    * The initial state of the state machine should be RED
  //    * The function should output the current state of the state machine
  //    * Unexpected or invalid input should not cause a state transition
  //    * EMERGENCY_SERVICE_BEACON may be received in any state and should put the
  //    machine
  //      into the FREEN state
  //    * TIMER_MIA may be received in any state nd should out the machine into
  //    the FAULT
  //      state.
  //
  //
  //  PED_WALK_BUTTON   +---------+
  //   +--------------->|         |   TIMER
  //   |                |  YELLOW | ---------+
  //   |    TIMER       |         |          |
  //   |   +----------> +---------+          |
  //   |   |                                 |
  //   |   |                                 V
  // +---------+                        +---------+
  // |         |     TIMER              |         |
  // |  GREEN  |<-----------------------|   RED   |
  // |         |<-----------------------|         |
  // +---------+  INDUCTIVE_SENSOR      +---------+
  //
  //                                 +---------+
  //                                 |         |
  //    EMBERGENCY_SERVICE_BEACON    |  GREEN  |
  //             +------------------>|         |
  //                                 +---------+
  //
  //                                 +---------+
  //                                 |         |
  //                   TIMER_MIA     |  FALSE  |
  //             +------------------>|         |
  //                                 +---------+
  //
    typedef enum { YELLOW, GREEN, FAULT_, RED } STATE;

    typedef enum {
        PED_WALK_BUTTON,
        TIMER,
        INDUCTIVE_SENSOR,
        EMERGENCY_SERVICE_BEACON,
        TIMER_MIA
    } INPUT;

    STATE currState = RED; // set default current state to be RED
    STATE stateMachine(INPUT input) {
		// Answer: TODO
		switch (input) {
			case PED_WALK_BUTTON:
				if (currState == RED) {
					currState = GREEN;
				}
				break;
			case TIMER:
				if (currState == YELLOW) {
					currState = RED;
				}
				break;
			case INDUCTIVE_SENSOR:
				if (currState == GREEN) {
					currState = RED;
				}
				break;
			case EMERGENCY_SERVICE_BEACON:
				currState = GREEN;
				break;
			case TIMER_MIA:
				currState = FAULT_;
				break;
			default:
				break;
		}
		return currState;
	}


    ///////////////////////////////////////////////////////////////////////////
    // 6) Interpolation (20 points)
    // Given two arrays of n > 1 values arrX[] (sorted ascending) and arrY[]
    // (sorted acending), write an interpolation function that satisfies the
    // following:
    //
    // * Interpolation(arrX[i]) returns arrY[i], for 0<=i<n
    // * Interpolation(val) returns the one-dimensional interpolated value
    //   of val if arrX[0] <= val <= arrX[n-1]. That is: val shallbe found
    //   between arrX[i-1] and arrX[i] and the return value shall be the
    //   interpolation of arrY[i-1] and arrY[i].
    // * Interpolation(val) returns -1 for any other case
    //////////////////////////////////////////////////////////////////////////

    double interpolation(int n, double arrX[], double arrY[], double val) {
        //TODO

        if (val < arrX[0] || val > arrX[n - 1]) {
			return -1;
		}

        for (int i = 1; i < n; i++) {
            if (val == arrX[i]) {
                return arrY[i];
			}
            if (val < arrX[i]) {
				double x0 = arrX[i - 1];
				double x1 = arrX[i];
				double y0 = arrY[i - 1];
				double y1 = arrY[i];
				return y0 + (val - x0) * (y1 - y0) / (x1 - x0);
    }
