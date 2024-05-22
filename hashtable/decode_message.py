"""
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.
"""

def decode_message(key, message):
	input_to_output = {}
	encrypted_message = ""
	for ch in key:
		if ch not in input_to_output and ch != " ":
			input_to_output[ch] = chr(97 + len(input_to_output))
	
	for ch in message:
		if ch == " ":
			encrypted_message += " "
		else:
			encrypted_message += input_to_output[ch]
	return encrypted_message

print(decode_message("eljuxhpwnyrdgtqkviszcfmaboooo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))