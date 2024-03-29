Throwaway scripts to generate a PDF from markdown problem statements.


# Requirements

- You must have [pandoc](https://pandoc.org/installing.html). Here's the version on my computer:
    ```
    pandoc 1.19.2.4
    Compiled with pandoc-types 1.17.0.5, texmath 0.9.4.4, skylighting 0.3.3.1
    ```
    It'll probably work with later versions (though I haven't checked).

- Install [weasyprint](https://pypi.org/project/weasyprint/):
    ```
    python3 -m pip install weasyprint==52.5
    ```
    The specific version "52.5" probably isn't needed if you aren't encountering [this issue](https://stackoverflow.com/questions/68720486/how-to-fix-function-symbol-pango-context-set-round-glyph-positions-error
).

- You need internet access while running this.


# Usage

For this example, suppose you want to create the PDF for a contest site called `manila2023`, and that this contest has four problems whose slugs are, *in order*,

- `first-prob`
- `second-prob`
- `third-prob`
- `fourth-prob`

Here are the steps:

1. Run
    ```
    python3 initialize.py manila2023 first-prob second-prob third-prob fourth-prob
    ```
    - This creates the folder `manila2023` with some files inside it.

2. Open each `.md` file in `manila2023/raw/` and paste the Markdown problem statement for each problem.
    - This is the most time-consuming part.

3. Open `manila2023/config.json`, and replace the contest name and each problem title with the correct ones.
    - *Use the correct capitalization and punctuation*! These will appear in the PDF.

4. Run
    ```
    python3 compile.py manila2023
    ```
    - The PDF should now be in `manila2023/compiled/manila2023.pdf`


As an example, the statements for `chennai2023/` have been included in this repo, and you can just try running
```
python3 compile.py chennai2023
```
to produce a PDF in `chennai2023/compiled/chennai2023.pdf`.


# Customization

The file `template.html` will be used as the template. You can edit it (including CSS) to customize the page. For example, you can change the font style and/or size with CSS.


# Future

It would be nice if the .md files can be downloaded easily. In some sites with an API, that may be possible. CodeDrills uses gRPC so life is harder :(
