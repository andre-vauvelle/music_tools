# music_tools.py
import argparse
import os
import eyed3

parse = argparse.ArgumentParser(description='Tool to help manage my music')
parse.add_argument('-t',
		   '--tracks_dir',
		   type=str,
		   help='the path to tracks',
		   default='/Users/andre/Music/Music/Media/Music/Unknown Artist/Unknown Album',
		   required=False)
parse.add_argument('-d',
		   '--delimiter',
		   type=str,
		   help='string to split the track artist on',
		   default='_',
		   required=False)
parse.add_argument('-n',
		   '--n_tracks',
		   type=int,
		   help='number of tracks to use on',
		   default=9999,
		   required=False)
parse.add_argument('-test',
		   '--test',
		   type=bool,
		   help='test without saving',
		   default=False,
		   required=False)

args = parse.parse_args()

def split_title(
	tracks_dir='/Users/andre/Music/Music/Media/Music/Unknown Artist/Unknown Album',
	delimiter = '_',
	n_tracks=9999,
	test=False):
	"""
	Splits the current title on a delimiter and renames the title and sets the artist name 
	"""	
	print('Using delimiter: {}'.format(delimiter))
	for fn in os.listdir(tracks_dir)[:n_tracks]:
		track_path = os.path.join(tracks_dir, fn)
		track_eye = eyed3.load(track_path)
		current_name = track_eye.tag.title
		try:
			split_track  = current_name.split(delimiter)
			new_artist_name, new_title_name = '&'.join(split_track[:-1]), split_track[-1] 
			track_eye.tag.title = new_title_name.strip()
			track_eye.tag.artist = new_artist_name.strip()
			print('Split: {} -> title: {} by: {}'.format(current_name, new_title_name, new_artist_name))
			if not test:
				track_eye.tag.save()
		except Exception as e:
			print('Could not split: {} \n Error: {}'.format(current_name, e))
	

split_title(args.tracks_dir, args.delimiter, args.n_tracks, args.test)



	 
