from argparse import ArgumentParser
import json
from pathlib import Path
import shutil

from util import valid_slug




parser = ArgumentParser()

parser.add_argument('contest')
parser.add_argument('slugs', nargs='+')
parser.add_argument('-F', '--force', action='store_true')

args = parser.parse_args()
print(f"CONTEST IS {args.contest}")

if not args.contest:
    raise RuntimeError("invalid contest")

contest_path = Path(args.contest)
print(f"\nMAKING FOLDER {contest_path}")

if args.force:
    if contest_path.is_dir():
        print(f"\nCLEARING {contest_path}")
        shutil.rmtree(contest_path)

if contest_path.exists():
    raise RuntimeError(f"{contest_path} must not exist")

contest_path.mkdir()



(contest_path / 'raw').mkdir()

for slug in args.slugs:
    if not valid_slug(slug):
        raise RuntimeError(f"Invalid slug: {slug!r}")

    print(f"\nCREATING .MD file for {slug}")
    with (contest_path / 'raw' / f'{slug}.md').open('w') as f:
        print("PASTE MARKDOWN PROBLEM STATEMENT HERE", file=f)






print(f"\nWRITING CONFIG FILE")
config = {
    'contest_name': 'REPLACE THIS WITH THE CONTEST NAME',
    'problems': [{
        'slug': slug,
        'title': f"REPLACE THIS WITH THE PROBLEM TITLE"
    } for slug in args.slugs]
}
with (contest_path / 'config.json').open('w') as f:
    json.dump(config, f, indent=4)





print("\nDONE")
