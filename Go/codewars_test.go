package codewars

import (
	"math"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCountBy(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   int
		n   int
		res []int
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: 1, n: 1, res: []int{1}},
			{x: 1, n: 2, res: []int{1, 2}},
			{x: 1, n: 10, res: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}},
			{x: 2, n: 5, res: []int{2, 4, 6, 8, 10}},
			{x: 3, n: 5, res: []int{3, 6, 9, 12, 15}},
			{x: 50, n: 5, res: []int{50, 100, 150, 200, 250}},
			{x: 100, n: 5, res: []int{100, 200, 300, 400, 500}},
		},
	}

	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			CountBy(testCase.x, testCase.n),
		)
	}
}

func TestAreTheyTheSame(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   []int
		n   []int
		res bool
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19, 11 * 11},
				res: true,
			},
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19},
				res: false,
			},
			{
				x:   nil,
				n:   []int{11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19},
				res: false,
			},
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{121, 14641, 20736, 361, 25921, 361, 20736, 361},
				res: true,
			},
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{231, 14641, 20736, 361, 25921, 361, 20736, 361},
				res: false,
			},
			{
				x:   []int{121, 144, 19, 161, 19, 144, 19, 11},
				n:   []int{121, 14641, 20736, 36100, 25921, 361, 20736, 361},
				res: false,
			},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			Comp(testCase.x, testCase.n),
		)
	}
}

func TestTribonacci(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   [3]float64
		n   int
		res []float64
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: [3]float64{1, 1, 1}, n: 10, res: []float64{1, 1, 1, 3, 5, 9, 17, 31, 57, 105}},
			{x: [3]float64{0, 0, 1}, n: 10, res: []float64{0, 0, 1, 1, 2, 4, 7, 13, 24, 44}},
			{x: [3]float64{0, 1, 1}, n: 10, res: []float64{0, 1, 1, 2, 4, 7, 13, 24, 44, 81}},
			{x: [3]float64{1, 0, 0}, n: 10, res: []float64{1, 0, 0, 1, 1, 2, 4, 7, 13, 24}},
			{x: [3]float64{0, 0, 0}, n: 10, res: []float64{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}},
			{x: [3]float64{1, 2, 3}, n: 10, res: []float64{1, 2, 3, 6, 11, 20, 37, 68, 125, 230}},
			{x: [3]float64{3, 2, 1}, n: 10, res: []float64{3, 2, 1, 6, 9, 16, 31, 56, 103, 190}},
			{x: [3]float64{1, 1, 1}, n: 1, res: []float64{1}},
			{x: [3]float64{300, 200, 100}, n: 0, res: []float64{}},
			{
				x:   [3]float64{0.5, 0.5, 0.5},
				n:   30,
				res: []float64{0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5}},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			Tribonacci(testCase.x, testCase.n),
		)
	}
}

func TestCountDivisible(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   uint64
		y   uint64
		k   uint64
		res uint64
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: 6, y: 11, k: 2, res: 3},
			{x: 11, y: 345, k: 17, res: 20},
			{x: 0, y: 1, k: 7, res: 1},
			{x: 20, y: 20, k: 8, res: 0},
			// performance testing
			{x: 1005, y: math.MaxUint64, k: 109, res: 169236184162472941},
			{x: 1005, y: uint64(math.MaxInt64), k: 109, res: 84618092081236466},
			{x: 101, y: uint64(math.MaxInt64), k: 11, res: 838488366986797791},
			{x: 1005, y: uint64(math.MaxInt32), k: 109, res: 19701675},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			DivisibleCount(testCase.x, testCase.y, testCase.k),
		)
	}
}

func TestMumbling(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   string
		res string
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: "ZpglnRxqenU", res: "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"},
			{x: "NyffsGeyylB", res: "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"},
			{x: "MjtkuBovqrU", res: "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"},
			{x: "EvidjUnokmM", res: "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"},
			{x: "HbideVbxncC", res: "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"},
			{x: "H", res: "H"},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			Accum(testCase.x),
		)
	}
}

func TestNextPerfectSquare(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   int64
		res int64
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: 121, res: 144},
			{x: 625, res: 676},
			{x: 319225, res: 320356},
			{x: 15241383936, res: 15241630849},
			{x: 155, res: -1},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			FindNextSquare(testCase.x),
		)
	}
}

func TestSumDigitPow(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   uint64
		y   uint64
		res []uint64
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: 1, y: 10, res: []uint64{1, 2, 3, 4, 5, 6, 7, 8, 9}},
			{x: 1, y: 100, res: []uint64{1, 2, 3, 4, 5, 6, 7, 8, 9, 89}},
			{x: 10, y: 89, res: []uint64{89}},
			{x: 10, y: 100, res: []uint64{89}},
			{x: 90, y: 100, res: nil},
			{x: 89, y: 135, res: []uint64{89, 135}},
			{x: 424, y: 670, res: []uint64{518, 598}},
			{x: 12157692622039623539, y: 12157692622039623539, res: []uint64{12157692622039623539}},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			SumDigPow(testCase.x, testCase.y),
		)
	}
}

func TestFirstNonRepeating(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   string
		res string
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: "a", res: "a"},
			{x: "stress", res: "t"},
			{x: "moonmen", res: "e"},
			{x: "", res: ""},
			{x: "abba", res: ""},
			{x: "aa", res: ""},
			{x: "~><#~><", res: "#"},
			{x: "hello world, eh?", res: "w"},
			{x: "sTreSS", res: "T"},
			{x: "Go hang a salami, I'm a lasagna hog!", res: ","},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			FirstNonRepeating(testCase.x),
		)
	}
}

func TestRgbToHex(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		r   int
		g   int
		b   int
		res string
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{r: 0, g: 0, b: 0, res: "000000"},
			{r: 1, g: 2, b: 3, res: "010203"},
			{r: 255, g: 255, b: 255, res: "FFFFFF"},
			{r: 254, g: 253, b: 252, res: "FEFDFC"},
			{r: -20, g: 275, b: 125, res: "00FF7D"},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			RGB(testCase.r, testCase.g, testCase.b),
		)
	}
}

func TestComplementaryDNA(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   string
		res string
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: "AAAA", res: "TTTT"},
			{x: "ATTGC", res: "TAACG"},
			{x: "GTAT", res: "CATA"},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			DNAStrand(testCase.x),
		)
	}
}

func TestDirectionReduction(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   []string
		res []string
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: []string{"NORTH", "SOUTH", "EAST", "WEST"}, res: []string{}},
			{x: []string{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}, res: []string{"WEST"}},
			{x: []string{"NORTH", "WEST", "SOUTH", "EAST"}, res: []string{"NORTH", "WEST", "SOUTH", "EAST"}},
			{x: []string{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"}, res: []string{"NORTH"}},
			{x: []string{"SOUTH", "SOUTH", "EAST", "WEST", "EAST", "NORTH", "NORTH", "WEST", "EAST", "WEST", "EAST"},
				res: []string{"SOUTH", "SOUTH", "EAST", "NORTH", "NORTH"}},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			DirReduc(testCase.x),
		)
	}
}

func TestReverseList(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   []int
		res []int
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: nil, res: nil},
			{x: []int{1, 2, 3, 4}, res: []int{4, 3, 2, 1}},
			{x: []int{2, 4, 5, 6}, res: []int{6, 5, 4, 2}},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			ReverseList(testCase.x),
		)
	}
}

func TestRangeExtraction(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   []int
		res string
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: []int{-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20}, res: "-6,-3-1,3-5,7-11,14,15,17-20"},
			{x: []int{-3, -2, -1, 2, 10, 15, 16, 18, 19, 20, 22}, res: "-3--1,2,10,15,16,18-20,22"},
			{x: []int{-3, -2}, res: "-3,-2"},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			range_extraction(testCase.x),
		)
	}
}

func TestSnail(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   [][]int
		res []int
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, res: []int{1, 2, 3, 6, 9, 8, 7, 4, 5}},
			{x: [][]int{{1, 2, 3, 1}, {4, 5, 6, 4}, {7, 8, 9, 7}, {7, 8, 9, 7}}, res: []int{1, 2, 3, 1, 4, 7, 7, 9, 8, 7, 7, 4, 5, 6, 9, 8}},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			Snail(testCase.x),
		)
	}
}

func TestRot13(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   string
		res string
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: "EBG13 rknzcyr.", res: "ROT13 example."},
			{x: "This is my first ROT13 excercise!", res: "Guvf vf zl svefg EBG13 rkprepvfr!"},
			{x: "123", res: "123"},
			{x: "@[`{", res: "@[`{"},
			{x: "How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.", res: "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes."},
			{x: "Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)", res: "This is actually the first kata I ever made. Thanks for finishing it! :)"},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			Rot13(testCase.x),
		)
	}
}

func TestFindTheNumberPlate(t *testing.T) {
	assert := assert.New(t)
	type TestCase struct {
		x   int
		res string
	}

	type TestCases struct {
		sliceTestCases []TestCase
	}

	testCases := TestCases{
		sliceTestCases: []TestCase{
			{x: 3, res: "aaa004"},
			{x: 1487, res: "baa489"},
			{x: 40000, res: "oba041"},
			{x: 17558423, res: "zzz999"},
			{x: 43056, res: "rba100"},
			{x: 234567, res: "aja802"},
		},
	}
	for _, testCase := range testCases.sliceTestCases {
		assert.Equal(
			testCase.res,
			FindTheNumberPlate(testCase.x),
		)
	}
}
