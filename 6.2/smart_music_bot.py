file = open("6.2/spotify.csv")
junk = file.readline()

song_data = []
name = input("Enter your name and songs that start with the same letter will be given. ").lower()

for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if songtitle[0].lower == name[0]:
		song_data.append([danceability, songtitle, artist])

print("Dance score \tSong")
for item in song_data:
	print(str(item[0]) + "\t\t" + item[1] + " by " + item[2])

for i in range(len(song_data)):
	smallest_score = song_data[i]
	smallest_index = i

	for j in range(i+1, len(song_data)):
		if song_data[j] < smallest_score:
			smallest_score = song_data[j]
			smallest_index = j

	song_data[smallest_index], song_data[i] = song_data[i], song_data[smallest_index]
print(song_data)