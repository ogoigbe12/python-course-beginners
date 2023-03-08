from pathlib import Path

# path = Path('email')
# print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)