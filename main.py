import random


def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)


def random_char(start, end):
    return chr(random.randint(start, end))


uppercase = [random_char(65, 90) for i in range(2)]
lowercase = [random_char(97, 122) for i in range(2)]
digits = [random_char(48, 57) for i in range(2)]
punctuation = [random_char(33, 38) for i in range(2)]

password = ''.join(uppercase + lowercase + digits + punctuation)
print(shuffle(password))
