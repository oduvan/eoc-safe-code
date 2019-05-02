"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "1#+2=13",
            "answer": -1
        },
        {
            "input": "123*45#=5#088",
            "answer": 6
        }
    ],
    "Extra": [
        {
            "input": "-5#*-1=5#",
            "answer": 0
        },
        {
            "input": "##*##=302#",
            "answer": 5
        },
        {
            "input": "#*11=##",
            "answer": 2
        },
        {
            "input": "19--45=5#",
            "answer": -1
        },
        {
            "input": "24-35=-##",
            "answer": 1
        },
        {
            "input": "642*3=1#26",
            "answer": 9
        },
        {
            "input": "-#*2=-14",
            "answer": 7
        },
        {
            "input": "-2+-8=-1#",
            "answer": 0
        },
        {
            "input": "#3#*4#=34639",
            "answer": 7
        },
        {
            "input": "-2*#=-8",
            "answer": 4
        },
        {
            "input": "##--11=11",
            "answer": -1
        },
        {
            "input": "#9+3=22",
            "answer": 1
        },
        {
            "input": "11*#=##",
            "answer": 2
        },
        {
            "input": "#9+3=12",
            "answer": -1
        }

    ]
}
