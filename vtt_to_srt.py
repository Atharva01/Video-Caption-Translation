from webvtt import WebVTT

def vtt_to_srt(vtt_file, srt_file):
    try:
        with open(srt_file, "w", encoding="utf-8") as srt:
            counter = 1
            for caption in WebVTT().read(vtt_file):
                srt.write(f"{counter}\n")
                srt.write(f"{caption.start.replace('.', ',')} --> {caption.end.replace('.', ',')}\n")
                srt.write(f"{caption.text}\n\n")
                counter += 1
        print(f"Converted '{vtt_file}' to '{srt_file}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    vtt_file = "output.vtt"  # Replace with your .vtt file
    srt_file = "output.srt"  # Desired output .srt file
    vtt_to_srt(vtt_file, srt_file)
