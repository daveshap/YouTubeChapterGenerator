import os

# Define the directory containing the transcripts
transcripts_dir = 'transcripts'
output_file = 'output.txt'

# Get a list of text files in the transcripts directory
text_files = [f for f in os.listdir(transcripts_dir) if f.endswith('.txt')]

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate over each file in the text files list
    for filename in text_files:
        # Construct the full file path
        file_path = os.path.join(transcripts_dir, filename)
        # Open the transcript file in read mode
        with open(file_path, 'r') as infile:
            # Read the content of the file
            content = infile.read()
            # Write the formatted content to the output file
            outfile.write(f"Video: {filename}\n")
            outfile.write("Transcript: ")
            outfile.write(content)
            outfile.write("\n\n")  # Add extra newlines for separation

print(f"All transcripts have been concatenated into {output_file}.")
