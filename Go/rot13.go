// How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
// I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.
// Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.
// Test examples:

// "EBG13 rknzcyr." -->
// "ROT13 example."

// "This is my first ROT13 excercise!" -->
// "Guvf vf zl svefg EBG13 rkprepvfr!"

package codewars

import (
	"unicode"
)

func Rot13(msg string) string {
	var res string
	for _, char := range msg {
		if unicode.IsLetter(char) {
			helper := int(char) + 13
			if unicode.IsUpper(char) {
				if helper > 90 {
					helper = helper - 91 + 65
				}
			} else {
				if helper > 122 {
					helper = helper - 123 + 97
				}
			}
			res = res + string(rune(helper))
		} else {
			res = res + string(char)
		}
	}
	return res
}
