# Complete the solution so that it strips all
# text that follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out


def strip_comments(strng, markers):
    inside_section = False
    result = ""

    for char in strng:
        if char in markers and not inside_section:
            inside_section = True
            result = result.replace(char, "")
        elif char == "\n" and inside_section:
            inside_section = False
            result += char
        elif not inside_section:
            result += char
    return '\n'.join(line.rstrip() for line in result.split('\n'))

print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']))