# Check if two strings are anagrams

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort and compare
    return sorted(str1) == sorted(str2)

# Take input
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Check and print result
if are_anagrams(string1, string2):
    print("✅ The strings are anagrams.")
else:
    print("❌ The strings are not anagrams.")
