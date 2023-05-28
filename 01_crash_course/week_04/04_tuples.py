# tuples are immutable!
fullname = ("Grace", "M", "Hopper")

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(result)
print(type(result))

hours, minutes, seconds = result
print(hours, minutes, seconds)


def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")])