"""
•	Problem Statement:
    •	Python exercise 1 tutorial, we have to create a dictionary similar to the
        real-world dictionary. There is no limit to the definition you provide to any word, as this exercise is
        just for your practice.
    •	The details and functionalities that are essential and must be present are:
    •	The user will give the word as input. Suppose that the word is present in your dictionary along with
        its definition or meaning.
    •	The program will print the meaning or definition of that word.
•	For example:
    •	The user inputs the word: “programming”
    •	The output will be:
    •	"the process of writing computer programs"
    •	Your primary focus should be towards writing a neat and efficient code, using only the knowledge from our previously done
        tutorials.
"""


myDictionary = {
    "consider" : {"deem to be" : "At the moment, artemisinin-based therapies are considered the best treatment, "
                                 "but cost about $10 per dose - far too much for impoverished communities."},

    "minute": {
        "infinitely or immeasurably small" : "The minute stain on the document was not visible to the naked eye."
    },

    "accord" : {
        "concurrence of opinion" : "The committee worked in accord on the bill, and it eventually passed."
    },

    "evident" : { "clearly revealed to the mind or the senses or judgment":
        "That confidence was certainly evident in the way Smith handled the winning play with 14 seconds left on the clock."
    },

    "practice" : { "a customary way of operation or behavior" :
        "He directed and acted in plays every season and became known for exploring Elizabethan theatre practices."
    }
}


print("                                                         Welcome to Python Dictionary")
print("                                                             Powered by MAB CORP\n\n\n")

print("                     ******************************************************************************************************************")
print("                                                                     Keys")
print("                     ******************************************************************************************************************")
print("                                        ",myDictionary.keys(),"\n\n\n");

key = input("                       Enter The Key Value You Want To Search : ")
print("                     The Searched Word's Meaning and The Usage in Sentence is as Follows:\n", myDictionary[key])




