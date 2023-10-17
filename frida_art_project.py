# Painting Titles
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']
# Painting dates
dates = [1939, 1933, 1946, 1940]

# combining paintings and dates of the paintings
paintings = list(zip(paintings, dates))
print(paintings)

# appending extra paintings
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)

# how many items are in the list?
print(len(paintings))

# output the list numbers as list
audio_tour_number = list(range(1, len(paintings)+1))
print(audio_tour_number)

# Making numbered list of paintings
master_list = list(zip(audio_tour_number, paintings))
print(master_list)

# Print each item
for i in master_list:
    print(i)
