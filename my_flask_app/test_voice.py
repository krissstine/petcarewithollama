# Save this as test_voice.py
import pyttsx3
import time

print("🎤 Testing Text-to-Speech...")

try:
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Get available voices
    voices = engine.getProperty('voices')
    print(f"✅ Found {len(voices)} voices")
    
    # Set properties
    engine.setProperty('rate', 150)  # Speed
    engine.setProperty('volume', 0.9)  # Volume
    
    # Test speaking
    print("🔊 Speaking: 'Hello, I am your PH PetCare voice assistant'")
    engine.say("Hello, I am your PH PetCare voice assistant")
    engine.runAndWait()
    
    # Test Filipino-accented voice if available
    for voice in voices:
        if 'filipino' in voice.name.lower() or 'english' in voice.name.lower():
            print(f"✅ Using voice: {voice.name}")
            engine.setProperty('voice', voice.id)
            break
    
    engine.say("How can I help you with your pet today?")
    engine.runAndWait()
    
    print("✅ Voice test complete!")
    
except Exception as e:
    print(f"❌ Error: {e}")