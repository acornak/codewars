// Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

// For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

// As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

// If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

// https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/go

package codewars

import (
	"strings"
)

func FirstNonRepeating(str string) string {
	count := make(map[string]int)

	for _, char := range str {
		count[strings.ToLower(string(char))] += 1
	}

	for _, char := range str {
		if count[strings.ToLower(string(char))] == 1 {
			return string(char)
		}
	}

	return ""
}
