from PIL import Image, ImageDraw
import os

# Create a simple heart-shaped icon
size = 1024
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Heart shape coordinates (simplified)
center_x, center_y = size // 2, size // 2 + 50
width = 300
height = 300

# Draw heart
draw.ellipse((center_x - width, center_y - height, center_x, center_y), fill=(232, 77, 112))
draw.ellipse((center_x, center_y - height, center_x + width, center_y), fill=(232, 77, 112))
draw.polygon([(center_x - width, center_y), (center_x + width, center_y), (center_x, center_y + 250)], fill=(232, 77, 112))

# Save different sizes
sizes = [(20, 2), (29, 2), (40, 2), (60, 2), (20, 1), (29, 1), (40, 1), (76, 1), (83.5, 2), (1024, 1)]
base_path = '/Users/ilyashirokov/Desktop/proga/python/wishlist-tg-api/ios/CoupleWishes/Resources/Assets.xcassets/AppIcon.appiconset/'

for size_val, scale in sizes:
    actual_size = int(size_val * scale)
    resized = img.resize((actual_size, actual_size), Image.Resampling.LANCZOS)
    filename = f'AppIcon-{int(size_val)}x{int(size_val)}@{scale}x.png'
    resized.save(os.path.join(base_path, filename), 'PNG')
    print(f'Created {filename}')

print('All app icon images created successfully!')
