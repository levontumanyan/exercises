"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longest_common_prefix(strings):
	prefix = strings[0]
	for string in strings:
		minimum = min(prefix, string)
		for i in range(len(minimum)):
			if (string[i] != prefix[i]):
				prefix = prefix[:i]
				break
	return prefix

def longest_common_prefix(strings):
    if not strings:
        return ""
        
    prefix = strings[0]
    for string in strings:
        while prefix != string[:len(prefix)]:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

def longest_common_prefix(strings):
	if not strings:
		return ""
	
	prefix = strings[0]
      
	for string in strings:
		while prefix != string[:(len(prefix))]:
			prefix = prefix[:-1]
	
	return prefix


print(longest_common_prefix(["hello", "he", "heyooo", "hoe"]))
print(longest_common_prefix(["hello", "heyooo"]))
