import sqlite3
import os

print("=" * 50)
print("DATABASE DIAGNOSTIC TOOL")
print("=" * 50)

# Step 1: Check if database file exists
db_file = 'petcare.db'  # or whatever your database is named
print(f"\n📁 Checking for database: {db_file}")
if os.path.exists(db_file):
    print(f"✅ Database found! Size: {os.path.getsize(db_file)} bytes")
else:
    print(f"❌ Database NOT found! Looking for: {os.path.abspath(db_file)}")
    exit()

# Step 2: Connect to database
try:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    print("✅ Successfully connected to database")
except Exception as e:
    print(f"❌ Failed to connect: {e}")
    exit()

# Step 3: List all tables
print("\n📋 TABLES IN DATABASE:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
if tables:
    for table in tables:
        print(f"  • {table[0]}")
else:
    print("  No tables found! Database is empty.")

# Step 4: Check users table specifically
print("\n👤 USERS TABLE CHECK:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
if cursor.fetchone():
    print("  ✅ Users table exists")
    
    # Show columns
    cursor.execute("PRAGMA table_info(users);")
    columns = cursor.fetchall()
    print("  📊 Columns in users table:")
    for col in columns:
        print(f"    - {col[1]} ({col[2]})")
    
    # Count users
    cursor.execute("SELECT COUNT(*) FROM users;")
    count = cursor.fetchone()[0]
    print(f"  👥 Total users registered: {count}")
    
    # Check for your specific email
    email = "maekristine56@gmail.com"
    cursor.execute("SELECT * FROM users WHERE email = ?;", (email,))
    user = cursor.fetchone()
    if user:
        print(f"  ✅ User '{email}' FOUND in database")
        print(f"     User data: {user}")
    else:
        print(f"  ❌ User '{email}' NOT found in database")
        print(f"     You need to register this email first!")
else:
    print("  ❌ Users table does NOT exist!")
    print("  You need to run init_db.py first")

# Step 5: Check if there's any data at all
print("\n🔍 SAMPLE DATA FROM ALL TABLES:")
for table in tables:
    table_name = table[0]
    try:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 1;")
        sample = cursor.fetchone()
        if sample:
            print(f"  • {table_name}: Has data ✓")
        else:
            print(f"  • {table_name}: Empty ✗")
    except:
        print(f"  • {table_name}: Error reading ✗")

conn.close()
print("\n" + "=" * 50)