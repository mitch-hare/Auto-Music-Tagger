# Imports
import music_tag
import glob

#Grab files
files = glob.glob(".\\Files\*.m4a")

#Takes a list of numbered tracks that are missing a tracknum (ie 1,2,3,5,6 or 2,3,4,5,6) and corrects the track numbers to not have gaps.
def fix_missing_tracknums():
    file_list = []
    for file in files:
        f = music_tag.load_file(file)
        #filename = (f.split("\\")[-1]).strip(".m4a")
        track_number = f['tracknumber']
        file_list.append([file,int(track_number)])
    sorted_list = sorted(file_list, key=lambda entry: entry[1])
    i = 0
    for entry in sorted_list:
        i += 1
        f = music_tag.load_file(entry[0])
        f['tracknumber'] = i
        f.save()


if __name__ == "__main__":
    # Insert whichever functions you like here
    fix_missing_tracknums()