from pytube import YouTube

link = input("Enter the link to Download: ")

if link == "":
    print("Paste a YouTube link to download")
else:
    yt = YouTube(link)
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Define the desired resolutions in priority order
    desired_resolutions = ["2160p", "1440p", "1080p", "720p"]

    yd = None  # Initialize stream object

    for res in desired_resolutions:
        # Attempt to find a progressive stream with video and audio
        stream = yt.streams.filter(res=res, progressive=True, file_extension="mp4").first()
        if stream:
            yd = stream
            break  # Stop if a suitable stream is found

    if yd:
        yd.download(output_path=r'{Enter Download Path}') #replace your download path location
        print(f"Video downloaded successfully in {yd.resolution} resolution with audio.")
    else:
        print("No suitable stream with audio available for download.")