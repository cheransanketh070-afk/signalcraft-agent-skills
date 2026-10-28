from pathlib import Path
import subprocess
import sys
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]

class SignalCraftRepoTests(unittest.TestCase):
    def test_validator_passes(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'validate_skills.py')], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_expected_skill_count(self):
        skills = [p for p in (ROOT / 'skills').iterdir() if p.is_dir() and (p / 'SKILL.md').is_file()]
        self.assertEqual(len(skills), 13)

    def test_each_skill_has_yaml_metadata(self):
        for folder in (ROOT / 'skills').iterdir():
            if folder.is_dir():
                text = (folder / 'SKILL.md').read_text(encoding='utf-8')
                self.assertTrue(text.startswith('---\n'), folder.name)
                self.assertIn('name:', text.split('---', 2)[1], folder.name)
                self.assertIn('description:', text.split('---', 2)[1], folder.name)

    def test_claude_zips_have_folder_at_root(self):
        zip_dir = ROOT / 'dist' / 'claude-uploads'
        zips = sorted(zip_dir.glob('*.zip'))
        self.assertEqual(len(zips), 13)
        for archive in zips:
            with zipfile.ZipFile(archive) as zf:
                names = zf.namelist()
                top = {n.split('/', 1)[0] for n in names}
                self.assertEqual(top, {archive.stem}, archive.name)
                self.assertIn(f'{archive.stem}/SKILL.md', names, archive.name)

if __name__ == '__main__':
    unittest.main()
