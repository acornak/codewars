"""
Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another.
The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite,
"WEST" and "EAST" too.

Going to one direction and coming back the opposite direction right away is a needless effort.
Since this is the wild west, with dreadful weather and not much water,
it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable,
better stay to the same place! So the task is to give to the man a simplified version of the plan.
A better plan in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]

Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH"
is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore,
the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly
opposite but they become directly opposite after the reduction of "EAST" and "WEST"
so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns an array of strings
with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.
"""
import unittest


def remove_from_list(arr: list[str]) -> tuple[list[str], int]:
    """
    Remove contradicting directions from list
    """
    if len(arr) <= 1:
        return arr, 0

    helper_dict = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    res = []

    index = 0
    # loop through the input array
    while index < len(arr) - 1:
        # check next if not contradicting
        if arr[index] != helper_dict[arr[index + 1]]:
            res.append(arr[index])
            index += 1
        # if contradicting, move 2 elements
        else:
            index += 2
        # if last element, check last 3 elements
        if index == len(arr) - 1:
            # if elem -1 and -2 are contradicting, check if elem -2 wasn't already removed
            if arr[index] == helper_dict[arr[index - 1]]:
                # if so, add elem -1 to list
                if arr[index - 1] == helper_dict[arr[index - 2]]:
                    res.append(arr[index])
            else:
                res.append(arr[index])

    return res, len(arr) - len(res)


def dir_reduc(arr: list[str]) -> list[str]:
    """
    Direction Reduction
    """
    res, removed = remove_from_list(arr)
    while removed != 0:
        res, removed = remove_from_list(res)

    return res


class DirectionReductionTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        test = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        res = dir_reduc(test)
        self.assertEqual(res, ["WEST"])

        # test argument mutation
        self.assertEqual(
            test, ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        )

    def test_2(self):
        """
        Test 2
        """
        test = ["NORTH", "WEST", "SOUTH", "EAST"]
        res = dir_reduc(test)
        self.assertEqual(res, ["NORTH", "WEST", "SOUTH", "EAST"])

        # test argument mutation
        self.assertEqual(test, ["NORTH", "WEST", "SOUTH", "EAST"])

    def test_3(self):
        """
        Test 3
        """
        test = [
            "NORTH",
            "SOUTH",
            "EAST",
            "WEST",
            "NORTH",
            "NORTH",
            "SOUTH",
            "NORTH",
            "WEST",
            "EAST",
        ]
        res = dir_reduc(test)
        self.assertEqual(res, ["NORTH", "NORTH"])

        # test argument mutation
        self.assertEqual(
            test,
            [
                "NORTH",
                "SOUTH",
                "EAST",
                "WEST",
                "NORTH",
                "NORTH",
                "SOUTH",
                "NORTH",
                "WEST",
                "EAST",
            ],
        )

    def test_4(self):
        """
        Test 4
        """
        test = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]
        res = dir_reduc(test)
        self.assertEqual(res, [])

        # test argument mutation
        self.assertEqual(test, ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"])

    def test_5(self):
        """
        Test 5
        """
        test = [
            "SOUTH",
            "SOUTH",
            "EAST",
            "WEST",
            "EAST",
            "NORTH",
            "NORTH",
            "WEST",
            "EAST",
            "WEST",
            "EAST",
        ]
        res = dir_reduc(test)
        self.assertEqual(res, ["SOUTH", "SOUTH", "EAST", "NORTH", "NORTH"])

        # test argument mutation
        self.assertEqual(
            test,
            [
                "SOUTH",
                "SOUTH",
                "EAST",
                "WEST",
                "EAST",
                "NORTH",
                "NORTH",
                "WEST",
                "EAST",
                "WEST",
                "EAST",
            ],
        )

    def test_6(self):
        """
        Test 6
        """
        test = [
            "WEST",
            "NORTH",
            "SOUTH",
            "EAST",
            "WEST",
            "WEST",
            "WEST",
            "WEST",
            "EAST",
            "WEST",
            "SOUTH",
            "EAST",
            "EAST",
            "EAST",
            "NORTH",
            "SOUTH",
            "EAST",
            "EAST",
            "NORTH",
        ]
        res = dir_reduc(test)
        self.assertEqual(
            res, ["WEST", "SOUTH", "WEST", "SOUTH", "EAST", "EAST", "SOUTH"]
        )

        # test argument mutation
        self.assertEqual(
            test,
            [
                "WEST",
                "NORTH",
                "SOUTH",
                "EAST",
                "WEST",
                "WEST",
                "WEST",
                "WEST",
                "EAST",
                "WEST",
                "SOUTH",
                "EAST",
                "EAST",
                "EAST",
                "NORTH",
                "SOUTH",
                "EAST",
                "EAST",
                "NORTH",
            ],
        )

    def test_7(self):
        """
        Test 7
        """
        test = [
            "WEST",
            "NORTH",
            "SOUTH",
            "SOUTH",
            "WEST",
            "EAST",
            "WEST",
            "SOUTH",
            "EAST",
            "EAST",
            "SOUTH",
            "SOUTH",
            "NORTH",
            "NORTH",
            "NORTH",
            "SOUTH",
            "SOUTH",
        ]
        res = dir_reduc(test)
        self.assertEqual(res, ["EAST", "EAST", "NORTH", "WEST", "NORTH", "EAST"])

        # test argument mutation
        self.assertEqual(
            test,
            [
                "WEST",
                "NORTH",
                "SOUTH",
                "SOUTH",
                "WEST",
                "EAST",
                "WEST",
                "SOUTH",
                "EAST",
                "EAST",
                "SOUTH",
                "SOUTH",
                "NORTH",
                "NORTH",
                "NORTH",
                "SOUTH",
                "SOUTH",
            ],
        )


if __name__ == "__main__":
    unittest.main()
