from moviepy.editor import VideoFileClip, concatenate_videoclips

# This is perfect for my use case

# Join multiple videos into one
# Example:
# video-1.mp4
# video-2.mp4
# video-3.mp4


def merge_videos(common_name, number_of_videos):
  videos = []
  for i in range(1, number_of_videos):
    videos.append(VideoFileClip(common_name + '-' + str(i) + '.mp4'))

  final_video = concatenate_videoclips(videos)
  final_video.write_videofile('merged_video.mp4', audio_codec='aac')


merge_videos('sendgrid', 43)
