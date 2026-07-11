#!/usr/bin/env python3
import re

# Read the project file
project_path = '/Users/ilyashirokov/Desktop/proga/python/wishlist-tg-api/ios/CoupleWishes.xcodeproj/project.pbxproj'
with open(project_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add the asset catalog file reference to PBXFileReference section
file_ref_pattern = r'(7BCEAC912E344D68B2D84EA8 /\* Info\.plist \*/);'
file_ref_replacement = r'7BCEAC912E344D68B2D84EA8 /* Info.plist */,\n\t\t\t9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets */;'
content = re.sub(file_ref_pattern, file_ref_replacement, content)

# Add the asset catalog to Resources group
resources_pattern = r'(6548FC690FCE442EADF16697 /\* Resources \*/ = \{\n\t\t\tisa = PBXGroup;\n\t\t\tchildren = \(\n\t\t\t\t7BCEAC912E344D68B2D84EA8 /\* Info\.plist \*/,)\n\t\t\t\t(3982C79157D048089D3255FD /\* AppTheme\.swift \*/,)'
resources_replacement = r'\1\n\t\t\t\t9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets */,\n\t\t\t\t\2'
content = re.sub(resources_pattern, resources_replacement, content)

# Add the asset catalog to PBXBuildFile section
build_file_pattern = r'(3B31A143A6394F6E910DEE27 /\* Info\.plist in Resources \*/ = \{isa = PBXBuildFile; fileRef = 7BCEAC912E344D68B2D84EA8 /\* Info\.plist \*/; \};)'
build_file_replacement = r'\1\n\t\t9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets in Resources */ = {isa = PBXBuildFile; fileRef = 9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets */; };'
content = re.sub(build_file_pattern, build_file_replacement, content)

# Write the modified content back
with open(project_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Project file updated successfully!")
