import tkinter as tk
from tkinter import scrolledtext
from youtubetranscript import fetch_transcript

### Transcript calls
# clear_transcript(): Clears the transcript that appears in the root
def clear_transcript():
    transcript_text_widget.config(state=tk.NORMAL)
    transcript_text_widget.delete(1.0, tk.END)

# display_transcript(): 
def display_transcript():
    # Get video URL from entry widget and get transcript
    video_url = url_entry.get()
    transcript = fetch_transcript(video_url)

    # Clear any previous transcript displayed
    clear_transcript()

    if transcript: # If transcript is available
        # Construct transcript text
        transcript_text = "Transcript:\n\n"
        for segment in transcript:
            transcript_text += segment['text'] + '\n'

        # Display transcript in text widget
        transcript_text_widget.insert(tk.END, transcript_text)
        transcript_text_widget.tag_configure("font", font=("Calibri", 12))
        transcript_text_widget.tag_add("font", "1.0", "end") 
        transcript_text_widget.config(state=tk.DISABLED)
    else: # Transcript is unavailable
        # Display message if producing a transcript fails
        transcript_text = "Failed to fetch transcript.\nPlease try a different YouTube video."
        transcript_text_widget.insert(tk.END, transcript_text)
        transcript_text_widget.tag_configure("font", font=("Calibri", 12))
        transcript_text_widget.tag_add("font", "1.0", "end") 
        transcript_text_widget.config(state=tk.DISABLED)


### Tkinter GUI Toolkit
# Create root window
root = tk.Tk()
root.title("YouTube Transcript")

# Create entry widget for URL input
url_label = tk.Label(root, text="Enter the YouTube video URL that you'd like to transcribe:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create button to get transcript
transcript_button = tk.Button(root, text="Get Transcript!", command=display_transcript)
transcript_button.pack(pady=5)

# Create scrolled text widget to display transcript with scrollbar
transcript_text_widget = scrolledtext.ScrolledText(root, width=80, height=20)
transcript_text_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Run loop
root.mainloop()