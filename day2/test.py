def check_split_string_equally(s, num_parts): # split s into num parts, and return if all parts are equal
        if len(s) % num_parts != 0:
            return False
        one_part_length = len(s) // num_parts

        first_part = s[:one_part_length]
        print(first_part)

        start = one_part_length
        end = start + one_part_length
        for i in range(num_parts-1):
            part = s[start:end]
            start = end
            end += one_part_length
            if part != first_part:
                return False
            print(part)
        return True


print(check_split_string_equally("1111", 4))


# take string
# add it to itself
# remove first and last character
# 123123
# 2312312312

# 100