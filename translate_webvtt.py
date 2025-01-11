from webvtt import WebVTT, Caption
from googletrans import Translator
translator = Translator()

def extract_captions(vtt_file_path):
    captions = []
    try:
        # Load the WebVTT file
        for caption in WebVTT().read(vtt_file_path):
            captions.append({
                "start": caption.start,
                "end": caption.end,
                "text": caption.text
            })
    except Exception as e:
        print(f"Error reading VTT file: {e}")
    return captions

def write_captions_to_vtt(captions, output_file_path):
    try:
        # Create a new WebVTT object
        vtt = WebVTT()
        for caption in captions:
            vtt_caption = Caption(
                start=caption['start'],
                end=caption['end'],
                text=translator.translate(caption['text'],src='de',dest='en').text
            )
            vtt.captions.append(vtt_caption)
        
        # Save to the output file
        vtt.save(output_file_path)
        print(f"Captions written to {output_file_path}")
    except Exception as e:
        print(f"Error writing VTT file: {e}")

# Example usage
if __name__ == "__main__":
    input_vtt_file_path = "example.vtt"  # Replace with the path to your input .vtt file
    output_vtt_file_path = "output.vtt"  # Path for the new .vtt file

    # Extract captions
    captions = extract_captions(input_vtt_file_path)
    
    # Write captions to a new .vtt file
    write_captions_to_vtt(captions, output_vtt_file_path)
