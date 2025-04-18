from pet import Pet, Dog, Cat

def display_title():
    print("""
    🐾⚡✨ Digital Pet Simulator ✨⚡🐾
    ----------------------------------
    """)

def main():
    display_title()
    
    # Create different types of pets
    print("\n🌟 Creating pets...")
    generic_pet = Pet("Pixel")
    dog = Dog("Max")
    cat = Cat("Whiskers")
    
    # Test basic functionality
    print("\n🔧 Testing basic pet actions:")
    generic_pet.eat()
    generic_pet.play()
    generic_pet.sleep()
    
    # Test dog-specific behavior
    print("\n🐶 Testing dog actions:")
    dog.bark()
    dog.train("fetch")
    dog.train("roll over")
    dog.train("play dead")
    
    # Test cat-specific behavior
    print("\n🐱 Testing cat actions:")
    cat.meow()
    cat.train("high five")
    cat.train("purr on command")
    
    # Show status of all pets
    print("\n📊 Checking status:")
    generic_pet.get_status()
    dog.get_status()
    cat.get_status()
    
    # Demonstrate special interactions
    print("\n🎭 Special interactions:")
    print("Let's see how pets respond to multiple plays when tired:")
    for _ in range(3):
        dog.play()
    
    print("\nFeeding the cat until it's full:")
    while cat.hunger > 0:
        cat.eat()
    
    # Save and load demonstration
    print("\n💾 Testing save/load functionality:")
    dog.save_state("max_save.txt")
    loaded_dog = Dog.load_state("max_save.txt")
    if loaded_dog:
        print("\n🔍 Loaded dog status:")
        loaded_dog.get_status()
        loaded_dog.show_tricks()
    
    # Show string representations
    print("\n📝 String representations:")
    print(generic_pet)
    print(dog)
    print(cat)
    
    # Final status check
    print("\n🏁 Final status of all pets:")
    pets = [generic_pet, dog, cat]
    for pet in pets:
        pet.get_status()
        pet.show_tricks()
        print()
    
    print("\n🎉 Pet simulation complete! Thanks for playing!")

if __name__ == "__main__":
    main()