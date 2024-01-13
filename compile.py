from argparse import ArgumentParser
from collections import deque
import json
import html
from pathlib import Path
import re
import shutil
from string import ascii_uppercase
from subprocess import run
from sys import stderr
from textwrap import dedent

from util import valid_slug




parser = ArgumentParser()

parser.add_argument('contest')

args = parser.parse_args()
print(f"CONTEST IS {args.contest}")

if not args.contest:
    raise RuntimeError("invalid contest")

contest_path = Path(args.contest)

if not contest_path.is_dir():
    raise RuntimeError(f"{contest_path} must be a directory")




print("\nLOADING CONFIG")
with (contest_path / 'config.json').open() as f:
    config = json.load(f)
print(f"Contest name is {config['contest_name']}")




root = contest_path / Path('compiled')
print(f"\nCLEARING {root = !s}")
if root.is_dir(): shutil.rmtree(root)
root.mkdir(parents=True)






(root / 'raw').mkdir(parents=True)
problems = {}
slugs = []
for problem in config['problems']:

    slug = problem['slug']
    print(f"\nPROBLEM {slug}")
    title = problem['title']
    print(f"{title = !s}")
    etitle = html.escape(title)
    print(f"{etitle = !s}")

    if not valid_slug(slug):
        raise RuntimeError(f"Invalid slug: {slug!r}")

    slugs.append(slug)

    with (contest_path / 'raw' / f'{slug}.md').open() as f:
        statement = f.read()

    if slug in problems:
        raise RuntimeError(f"Duplicate problem {slug!r}")
    problems[slug] = {
        'title': title,
        'etitle': etitle,
        'statement': statement,
    }

    with (root / 'raw' / f'{slug}.md').open('w') as f:
        print(f"<!-- TITLE: {etitle} -->\n\n", file=f)
        f.write(statement)






combined_md = root / 'combined' / 'combined.md'
print(f"\nCOMBINING TO {combined_md}")
breakstr = '<br>'
(root / 'combined').mkdir(parents=True)
with combined_md.open('w') as f:
    for letter, slug in zip(ascii_uppercase, slugs):
        problem = problems[slug]
        print(f"WRITING {letter}: {slug}: ({problem['title']})", file=stderr)

        print(dedent(f"""\

            
            <!-- NEW PROBLEM -->

            <!-- {letter} - {problem['etitle']} -->

            # {letter} &ndash; {problem['etitle']} {{.problem-title}}


            <div class="problem-contents">

        """), file=f)



        for lineno, line in enumerate(problem['statement'].splitlines(), 1):

            lft = deque()
            rgt = deque()
            i, j = 0, len(line)
            while (k := line.find(breakstr, i, j)) != -1:
                K = k + len(breakstr)
                assert line[k: K] == breakstr
                if line[i: k].strip(): break
                lft.append(line[i: k])
                lft.append('\n\n')
                i = K

            while (k := line.rfind(breakstr, i, j)) != -1:
                K = k + len(breakstr)
                assert line[k: K] == breakstr
                if line[K: j].strip(): break
                rgt.appendleft(line[K: j])
                rgt.appendleft('\n\n')
                j = k


            nline = ''.join((*lft, line[i: j], *rgt))
            if line != nline:
                print(f"REPLACING {breakstr} in line {lineno:>4}: {line!r}: {nline!r}")
                line = nline

            print(line, file=f)


        print(dedent(f"""\

            </div>
            
            <!-- <div class="problem-end"></div> -->

            <!-- END PROBLEM -->

            
        """), file=f)






template = Path('template.html')
combined_html = root / 'combined' / 'combined.html'
print(f"\nCONVERTING TO HTML {combined_html} WITH TEMPLATE {template}")
run(['pandoc', '-s', combined_md, '-o', combined_html, '--template', template, '--metadata', f"title={config['contest_name']}"])

# TODO use proper template (with CSS)




combined_pdf = root / f'{args.contest}.pdf'
print(f"\nCONVERTING TO PDF {combined_pdf}")
from weasyprint import HTML
HTML(combined_html).write_pdf(combined_pdf)



print("\nDONE")
