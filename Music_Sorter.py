import sys
import os
import errno
import shutil

from tinytag import TinyTag

Downloads = r'F:\$Alexander$\Music\complete'
Library = r'F:\Complete Music Lib'
# Temp = r'F:\temp_sorted'

os.chdir(Downloads)

print(os.getcwd())

albumDir = os.listdir()

def get_artist(song):
    if TinyTag.is_supported(song) == True:
        tag = TinyTag.get(song)
        return tag.artist

def get_album(song):
	if TinyTag.is_supported(song) == True:
		tag = TinyTag.get(song)
		return tag.album

def move(dir, start):
	print('First track is ' + dir[int(start)] + ' by ' + get_artist(dir[int(start)]))
	dest_folder = os.path.join(Library, get_artist(dir[int(start)]))
	source_folder = os.path.join(Downloads, album)
	try:
		os.mkdir(dest_folder)
		print("Directory '%s' created" %get_artist(dir[int(start)]))
	except OSError as e:
		if e.errno == errno.EEXIST:
			print("Directory '%s' already exists" %get_artist(dir[int(start)]))
		else:
			raise
	new_album_folder = os.path.join(dest_folder, get_album(dir[int(start)]))
	try:
		try:
			os.mkdir(new_album_folder)
			print("Directory '%s' created" %get_album(dir[int(start)]))
		except NotADirectoryError:
			new_album_folder = os.path.join(dest_folder, "bad_name")
			os.mkdir(new_album_folder)
		except FileNotFoundError:
			new_album_folder = os.path.join(dest_folder, "bad_name")
			os.mkdir(new_album_folder)
	except OSError as e:
		if e.errno == errno.EEXIST:
			print("Directory '%s' already exists" %get_album(dir[int(start)]))
		else:
			raise
	for song in dir:
		if TinyTag.is_supported(song) == True:
			dest_file = os.path.join(new_album_folder, song)
			source_file = os.path.join(source_folder, song)
			shutil.copyfile(source_file, dest_file)
			print('File moved')
		else:
			print('Not supported')
	# done_folder = os.path.join(Temp, album)
	# shutil.rmtree(source_folder)

for album in albumDir:
	os.chdir(album)
	songDir = os.listdir()

	
	if TinyTag.is_supported(songDir[0]) == True:
		move(songDir, 0)
	else:
		for i in range(0, len(songDir)):
			if TinyTag.is_supported(songDir[i]) == True:
				move(songDir, i)
			else:
				print('INVALID')

	os.chdir('..')
