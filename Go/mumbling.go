// This time no story, no theory. The examples below show you how to write function accum:

// Examples:
// accum("abcd") -> "A-Bb-Ccc-Dddd"
// accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
// accum("cwAt") -> "C-Ww-Aaa-Tttt"
// The parameter of accum is a string which includes only letters from a..z and A..Z.

// https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/go

package codewars

import "strings"

func Accum(s string) string {
	var res string

	for pos, char := range s {
		if pos != 0 {
			res += "-"
		}
		res += strings.ToUpper(string(char)) + strings.Repeat(strings.ToLower(string(char)), pos)
	}
	return res
}
