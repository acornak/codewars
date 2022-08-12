// The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

// Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

// The following are examples of expected output values:

// kata.rgb(255, 255, 255) -- returns FFFFFF
// kata.rgb(255, 255, 300) -- returns FFFFFF
// kata.rgb(0, 0, 0) -- returns 000000
// kata.rgb(148, 0, 211) -- returns 9400D3

// https://www.codewars.com/kata/513e08acc600c94f01000001/go

package codewars

import "fmt"

func validate(val int) int {
	if val < 0 {
		return 0
	}
	if val > 255 {
		return 255
	}
	return val
}

func RGB(r, g, b int) string {
	return fmt.Sprintf("%02X%02X%02X", validate(r), validate(g), validate(b))
}
