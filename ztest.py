from extractlib.document.process import process_document
import json

def main(file: str):
    result = process_document(file, split_pages_output_dir='./output', use_multithreading=False, exclude_pages=[2,3])
    # Save the HTML content to a temporary file
    with open('temp.json', 'w') as f:
        json.dump(result, f, indent=4)


if __name__ == '__main__':

    # get working directory
    import os
    target_dir = os.path.dirname(os.path.abspath(__file__))
    main(f'{target_dir}/_tempdata/100557.pdf')