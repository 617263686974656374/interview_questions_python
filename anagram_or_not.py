# Program check if the given strings are anagram or not

def anagram(word1,word2):
    if(sorted(word1) == sorted(word2)):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

word1= input("Enter a first word: ")
word2= input("Enter a second word: ")

anagram(word1, word2)
