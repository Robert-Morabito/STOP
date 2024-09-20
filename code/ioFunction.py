import json
import sys
import argparse
from typing import List, Dict, Any

def load_json_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load data from a JSON file.

    :param file_path: Path to the JSON file.
    :return: List of dictionaries representing the loaded data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading JSON data: {e}", file=sys.stderr)
        return []

def save_json_data(data: List[Dict[str, Any]], file_path: str):
    """
    Save data to a JSON file.

    :param data: Data to be saved.
    :param file_path: Path to the JSON file where data will be saved.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving JSON data: {e}", file=sys.stderr)

def parse_arguments():
    """
    Parse command-line arguments.

    :return: Namespace object with arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, required=True,
                        help='Path to the JSON file containing the input dataset.')
    parser.add_argument('--output_path', type=str,
                        help='Optional path for output file (if not appending or overwriting original)')
    parser.add_argument('--model', type=str, required=True, nargs='+', 
                        choices=['gpt-3.5-turbo-0125', 'gpt-4-0125-preview', 'google/gemma-7b-it', 'mistralai/Mistral-7B-Instruct-v0.1',
                        'mistralai/Mixtral-8x7B-Instruct-v0.1', 'meta-llama/Llama-2-7b-chat-hf', 'meta-llama/Llama-2-13b-chat-hf',
                        'meta-llama/Llama-2-70b-chat-hf', 'meta-llama/Meta-Llama-3-8B-Instruct', 'meta-llama/Meta-Llama-3-70B-Instruct'],
                        help="""LLM used for testing, currently supports: 
                        gpt-3.5-turbo-0125, 
                        gpt-4-0125-preview, 
                        google/gemma-7b-it, 
                        mistralai/Mistral-7B-Instruct-v0.1, 
                        mistralai/Mixtral-8x7B-Instruct-v0.1, 
                        meta-llama/Llama-2-7b-chat-hf,
                        meta-llama/Llama-2-13b-chat-hf, 
                        meta-llama/Llama-2-70b-chat-hf, 
                        meta-llama/Meta-Llama-3-8B-Instruct,
                        meta-llama/Meta-Llama-3-70B-Instruct
                        """)
    parser.add_argument('--openai_key', type=str,
                        help='OpenAI API key')
    parser.add_argument('--anyscale_key', type=str,
                        help='Anyscale API key')
    parser.add_argument('--anthropic_key', type=str,
                        help='Anthropic API key')
    return parser.parse_args()
