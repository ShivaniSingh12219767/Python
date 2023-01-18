# RegEx- Regular Expression
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern.
import re
value="This is a string"
output=re.search("^This.*string$", value)
print(output)

pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"   #(* character password)
# r=raw string(Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their special meaning.
# The 'r' prefix tells Python not to look at the \ characters and not to replace them with special characters. Basically that means raw data.)
# ^=starts with 
# .= any character 
# [] = A set of characters 
# () = Capture and Group
# {} = Exactly the specified number of occurences (Length of Password-fixed or variable)
# ? = Zero or one occurences
# * = Zero or more occurences
