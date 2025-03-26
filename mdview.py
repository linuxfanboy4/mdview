#!/usr/bin/env python3    
import sys    
import re    
import requests    
import markdown    
from rich.console import Console    
from rich.markdown import Markdown    
from markdown2 import markdown as markdown_to_html    
from pygments import highlight    
from pygments.lexers import get_lexer_by_name    
from pygments.formatters import TerminalFormatter    

ANSI_CODES = {    
    'bold': '\033[1m', 'italic': '\033[3m', 'underline': '\033[4m', 'reset': '\033[0m',    
    'bold_italic': '\033[1m\033[3m', 'bold_underline': '\033[1m\033[4m',    
    'italic_underline': '\033[3m\033[4m', 'bold_italic_underline': '\033[1m\033[3m\033[4m',    
    'strikethrough': '\033[9m', 'italic_bold_underline': '\033[3m\033[1m\033[4m',    
    'double_underline': '\033[21m', 'inverse': '\033[7m', 'hidden': '\033[8m',    
    'fraktur': '\033[20m', 'normal': '\033[22m', 'blink': '\033[5m', 'reverse': '\033[7m',    
    'faint': '\033[2m', 'yellow': '\033[33m', 'blue': '\033[34m', 'green': '\033[32m'    
}    

def apply_ansi_style(text, *styles):    
    return f"{''.join(ANSI_CODES.get(style, '') for style in styles)}{text}{ANSI_CODES['reset']}"    

def highlight_code(code, lang):    
    try:    
        lexer = get_lexer_by_name(lang, stripall=True)    
        return highlight(code, lexer, TerminalFormatter())    
    except:    
        return apply_ansi_style(code, 'italic')    

def render_markdown(text):    
    text = re.sub(r'^(#{1,6})\s*(.*)', lambda m: apply_ansi_style(m.group(2), 'bold_underline'), text, flags=re.M)    
    text = re.sub(r'\*\*\*(.*?)\*\*\*', lambda m: apply_ansi_style(m.group(1), 'bold_italic'), text)    
    text = re.sub(r'\*\*(.*?)\*\*', lambda m: apply_ansi_style(m.group(1), 'bold'), text)    
    text = re.sub(r'\*(.*?)\*', lambda m: apply_ansi_style(m.group(1), 'italic'), text)    
    text = re.sub(r'__(.*?)__', lambda m: apply_ansi_style(m.group(1), 'underline'), text)    
    text = re.sub(r'~~(.*?)~~', lambda m: apply_ansi_style(m.group(1), 'strikethrough'), text)    
    text = re.sub(r'^\> (.*)', lambda m: apply_ansi_style(m.group(1), 'italic_blue'), text, flags=re.M)    
    text = re.sub(r'^[*-+]\s+(.*)', lambda m: f"- {apply_ansi_style(m.group(1), 'green')}", text, flags=re.M)    
    text = re.sub(r'^\d+\.\s+(.*)', lambda m: f"1. {apply_ansi_style(m.group(1), 'yellow')}", text, flags=re.M)    
    text = re.sub(r'`([^`]+)`', lambda m: apply_ansi_style(m.group(1), 'inverse'), text)    
    text = re.sub(r'([^]+)([^)]+)', lambda m: apply_ansi_style(f"{m.group(1)} ({m.group(2)})", 'blue'), text)    
    text = re.sub(r' (.*)', lambda m: f"[ ] {apply_ansi_style(m.group(1), 'faint')}", text)    
    text = re.sub(r'x (.*)', lambda m: f"[✔] {apply_ansi_style(m.group(1), 'green')}", text)    

    code_blocks = re.findall(r'```(\w+)?\n(.*?)```', text, re.S)    
    for lang, code in code_blocks:    
        highlighted = highlight_code(code, lang if lang else "plaintext")    
        text = text.replace(f"```{lang}\n{code}```", highlighted)    

    tables = re.findall(r'\|(.+)\|\n\|[-\s|]+\|\n((?:\|.+\|\n?)+)', text)    
    for header, rows in tables:    
        header_cells = header.split("|")    
        row_cells = [row.split("|") for row in rows.strip().split("\n")]    
        formatted_table = apply_ansi_style("| " + " | ".join(header_cells) + " |", 'bold_underline')    
        for row in row_cells:    
            formatted_table += "\n| " + " | ".join(row) + " |"    
        text = text.replace(f"|{header}|\n|{'-' * len(header)}|\n{rows}", formatted_table)    

    return text    

def fetch_github_raw(url):    
    try:    
        response = requests.get(url)    
        response.raise_for_status()    
        return response.text    
    except requests.exceptions.RequestException as e:    
        print(f"Error fetching file: {e}")    
        sys.exit(1)    

def view_markdown(content, word_limit=None, output_html=False):    
    content = render_markdown(content)    
    if output_html:    
        content = markdown_to_html(content, extras=["tables", "fenced-code-blocks", "strike", "task_list"])    

    words = content.split()    
    if word_limit:    
        content = ' '.join(words[:word_limit])    

    console = Console()    
    markdown = Markdown(content)    
    console.print(markdown)    

def get_file_content(filename_or_url):    
    if filename_or_url.startswith('https://raw.githubusercontent.com'):    
        return fetch_github_raw(filename_or_url)    
    else:    
        try:    
            with open(filename_or_url, 'r') as file:    
                return file.read()    
        except FileNotFoundError:    
            print(f"File {filename_or_url} not found.")    
            sys.exit(1)    

def convert_to_html(content):    
    return markdown_to_html(content, extras=["tables", "fenced-code-blocks", "strike", "task_list"])    

if __name__ == '__main__':    
    if len(sys.argv) < 2:    
        print("Usage: view <filename>.md or <GitHub raw link> [word_limit] [--html]")    
        sys.exit(1)    

    filename_or_url = sys.argv[1]    
    word_limit = None    
    output_html = False    

    if len(sys.argv) == 3 and sys.argv[2].isdigit():    
        word_limit = int(sys.argv[2])    
    elif len(sys.argv) > 3 and sys.argv[2] == '--html':    
        output_html = True    
        if len(sys.argv) == 4 and sys.argv[3].isdigit():    
            word_limit = int(sys.argv[3])    

    content = get_file_content(filename_or_url)    
    view_markdown(content, word_limit, output_html)
