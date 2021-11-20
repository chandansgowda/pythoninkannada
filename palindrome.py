from colorama import Fore,Back,Style
word = input("Enter word >> ").lower()
word_backwards = word[::-1]
if word==word_backwards:
    print(Fore.GREEN + "Its a palindrome" + Fore.RESET)
else:
    print(Fore.RED + "Its not a palindrome" + Fore.RESET)