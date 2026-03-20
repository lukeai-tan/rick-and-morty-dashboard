class Character:
    def __init__(self, data):
        self.id = data.get('id')

        self.name = data.get('name')

        self.status = data.get('status')

        self.species = data.get('species')

        # Origin location
        self.origin = data.get('origin', {}).get('name', 'Unknown')

        # Current location or last known location
        self.current = data.get('location', {}).get('name', 'Unknown')
        
        self.image = data.get('image')

    def __repr__(self):
        return f"<Character: {self.name}>"