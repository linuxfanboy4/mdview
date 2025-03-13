# MDView - Advanced Markdown Viewer

MDView is a powerful and feature-rich command-line tool designed to render Markdown files with advanced formatting options directly in your terminal. Built with Python and leveraging the `rich` library, MDView provides a robust solution for viewing Markdown files with support for headers, bold, italic, underline, strikethrough, code blocks, blockquotes, lists, tables, and more. It is designed for developers, technical writers, and anyone who needs to preview Markdown content in a terminal environment with precision and style.

## Installation

To install MDView, simply run the following commands in your terminal:

```bash
wget https://raw.githubusercontent.com/linuxfanboy4/mdview/refs/heads/main/mdview.py
chmod +x mdview.py
```

This will download the script and make it executable. You can now use MDView to render Markdown files directly in your terminal.

## Features

MDView supports a wide range of Markdown features, including:

- **Headers**: Renders `#` to `######` with bold formatting.
- **Bold and Italic**: Supports `**bold**`, `*italic*`, and `***bold italic***` text.
- **Underline and Strikethrough**: Renders `__underline__` and `~~strikethrough~~`.
- **Code Blocks**: Renders inline code (`` `code` ``) and multi-line code blocks (``` ```code``` ```) with monospace formatting.
- **Blockquotes**: Formats `> blockquotes` with italic styling.
- **Lists**: Supports both unordered (`-`, `*`, `+`) and ordered (`1.`, `2.`, etc.) lists.
- **Tables**: Renders Markdown tables with proper alignment and borders.
- **Advanced Formatting**: Combines multiple styles, such as `**__bold underline__**` and `***__bold italic underline__***`.
- **Custom Fonts**: Utilizes terminal-compatible fonts for consistent rendering.

## Usage

To view a Markdown file, use the following command:

```bash
./mdview.py <filename>.md
```

Replace `<filename>.md` with the path to your Markdown file.

## Examples

Below are examples of how MDView renders various Markdown elements:

### Headers
```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

### Bold, Italic, and Underline
```markdown
**Bold Text**
*Italic Text*
***Bold Italic Text***
__Underline Text__
~~Strikethrough Text~~
```

### Code Blocks
```markdown
Inline `code` example.

```
Multi-line
code block
```
```

### Blockquotes
```markdown
> This is a blockquote.
> It supports multi-line content.
```

### Lists
```markdown
- Unordered List Item 1
- Unordered List Item 2
  - Nested Item

1. Ordered List Item 1
2. Ordered List Item 2
   1. Nested Item
```

### Tables
```markdown
| Column 1       | Column 2       | Column 3       |
|----------------|----------------|----------------|
| Row 1, Col 1   | Row 1, Col 2   | Row 1, Col 3   |
| Row 2, Col 1   | Row 2, Col 2   | Row 2, Col 3   |
```

### Advanced Formatting
```markdown
**__Bold Underline__**
***__Bold Italic Underline__***
```

## Customization

MDView uses ANSI escape codes to apply styles, ensuring compatibility with most modern terminals. You can extend the `ANSI_CODES` dictionary in the script to add custom styles or modify existing ones.

## Dependencies

MDView relies on the `rich` library for rendering Markdown. Ensure you have it installed by running:

```bash
pip install rich
```

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the [GitHub repository](https://github.com/linuxfanboy4/mdview).

## License

MDView is released under the MIT License. See the [LICENSE](https://github.com/linuxfanboy4/mdview/blob/main/LICENSE) file for details.

## Support

For support or questions, please open an issue on the [GitHub repository](https://github.com/linuxfanboy4/mdview).
