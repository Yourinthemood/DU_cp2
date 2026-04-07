import pandas as pd

class QuickStats:
    def report(self, characters):
        if not characters:
            print("No characters")
            return
        
        data = []
        for c in characters:
            attrs = c['attributes'] if c['attributes'] else c['base_attributes']
            data.append({
                'Name': c['name'],
                'Class': c['class'],
                'Level': c['level'],
                'Damage': attrs[0],
                'Dexterity': attrs[1],
                'Intelligence': attrs[2],
                'Constitution': attrs[3],
                'Charisma': attrs[4]
            })
        
        df = pd.DataFrame(data)
        print("\n=== STATISTICS ===")
        print(f"Total Characters: {len(df)}")
        print(f"Average Level: {df['Level'].mean():.1f}")
        print(f"Highest Level: {df['Level'].max()}")
        print(f"Lowest Level: {df['Level'].min()}")
        print(f"\nAverage Damage: {df['Damage'].mean():.1f}")
        print(f"Average Dexterity: {df['Dexterity'].mean():.1f}")
        print(f"Average Intelligence: {df['Intelligence'].mean():.1f}")
        print(f"Average Constitution: {df['Constitution'].mean():.1f}")
        print(f"Average Charisma: {df['Charisma'].mean():.1f}")