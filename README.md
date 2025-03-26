# MDView - Advanced Markdown Viewer

MDView is a powerful and feature-rich command-line tool designed to render Markdown files with advanced formatting options directly in your terminal. Built with Python and leveraging the `rich` and `markdown2` libraries, MDView provides a robust solution for viewing Markdown files with support for headers, bold, italic, underline, strikethrough, code blocks, blockquotes, lists, tables, and more. It is designed for developers, technical writers, and anyone who needs to preview Markdown content in a terminal environment with precision and style.

## Installation

To install MDView, follow these steps:

1. Download the script and requirements:
```bash
wget https://raw.githubusercontent.com/linuxfanboy4/mdview/refs/heads/main/mdview.py
wget https://raw.githubusercontent.com/linuxfanboy4/mdview/refs/heads/main/requirements.txt
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make the script executable:
```bash
chmod +x mdview.py
```

Alternatively, you can use the Docker container:
```bash
docker run -it ghcr.io/linuxfanboy4/mdview
```

Optionally, install using `pip`:
```bash
pip install git-https://github.com/linuxfanboy4/mdview.git
```

## Features

MDView supports a comprehensive range of Markdown features with ANSI styling:

- **Headers**: Renders `#` to `######` with bold formatting
- **Text Styles**:
  - `**bold**`, `*italic*`, `***bold italic***`
  - `__underline__`, `~~strikethrough~~`
  - Combined styles like `**__bold underline__**`
- **Code Elements**:
  - Inline code (`` `code` ``)
  - Multi-line code blocks (``` ```code``` ```) with syntax highlighting based on the language (leveraging Pygments)
- **Blockquotes**: `>` with italic styling
- **Lists**:
  - Unordered (`-`, `*`, `+`)
  - Ordered (`1.`, `2.`, etc.)
- **Tables**: Advanced table rendering
- **Advanced Formatting**:
  - Nested styles like `***__bold italic underline__***`
  - Custom ANSI escape codes for precise styling

## Usage

Basic usage:
```bash
./mdview.py <filename>.md
```

Additional options:
```bash
./mdview.py <filename>.md [word_limit] [--html]
```

- `<filename>.md`: Markdown file or GitHub raw URL
- `word_limit`: Optional limit of words to display
- `--html`: Output as HTML instead of terminal rendering

Examples:
```bash
# View local file
./mdview.py README.md

# View with word limit
./mdview.py README.md 100

# Output as HTML
./mdview.py README.md --html

# View from GitHub raw URL
./mdview.py https://raw.githubusercontent.com/user/repo/main/README.md
```

## Technical Details

MDView uses:
- Python's `re` module for advanced pattern matching
- `rich` library for beautiful terminal output
- `markdown2` for HTML conversion
- `pygments` for syntax highlights in code blocks based on the language
- Custom ANSI escape code handling for precise styling

The script includes comprehensive regular expressions to handle:
- Nested formatting combinations
- Complex Markdown structures
- Edge cases in Markdown parsing

## Examples

### Advanced Formatting
```markdown
**__Bold Underline__**
***__Bold Italic Underline__***
`inline code` with **bold** and *italic*
```

### GitHub Integration
```bash
./mdview.py https://raw.githubusercontent.com/linuxfanboy4/mdview/main/README.md
```

## Dependencies

MDView requires:
- Python 3.x
- `rich` library
- `markdown2` library
- `requests` (for GitHub raw URLs)
- `pygments` library

These are automatically installed with the `requirements.txt` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/linuxfanboy4/mdview).

## License

MDView is released under the MIT License. See the [LICENSE](https://github.com/linuxfanboy4/mdview/blob/main/LICENSE) file for details.

## Support

For support or questions, please open an issue on the [GitHub repository](https://github.com/linuxfanboy4/mdview).
