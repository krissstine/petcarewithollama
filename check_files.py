import os

print(f"Current directory: {os.getcwd()}")
print("\nFiles in current directory:")
for file in os.listdir('.'):
    size = os.path.getsize(file) if os.path.isfile(file) else 0
    print(f"  - {file} ({size} bytes)")

print("\n" + "="*50)
if os.path.exists('index.html'):
    print("✅ index.html FOUND!")
    # Show first few lines of index.html
    with open('index.html', 'r') as f:
        first_lines = f.readlines()[:5]
        print("\nFirst 5 lines of index.html:")
        for line in first_lines:
            print(f"  {line.strip()}")
else:
    print("❌ index.html NOT FOUND!")
    print("Make sure index.html is in this folder!")