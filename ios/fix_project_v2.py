#!/usr/bin/env python3

# Read the project file
project_path = '/Users/ilyashirokov/Desktop/proga/python/wishlist-tg-api/ios/CoupleWishes.xcodeproj/project.pbxproj'
with open(project_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the Resources group to include Assets.xcassets
old_resources = '''\t\t6548FC690FCE442EADF16697 /* Resources */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t7BCEAC912E344D68B2D84EA8 /* Info.plist */,
\t\t\t\t3982C79157D048089D3255FD /* AppTheme.swift */,
\t\t\t);
\t\t\tpath = Resources;
\t\t\tsourceTree = "<group>";
\t\t};'''

new_resources = '''\t\t6548FC690FCE442EADF16697 /* Resources */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t7BCEAC912E344D68B2D84EA8 /* Info.plist */,
\t\t\t\t3982C79157D048089D3255FD /* AppTheme.swift */,
\t\t\t\t9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets */,
\t\t\t);
\t\t\tpath = Resources;
\t\t\tsourceTree = "<group>";
\t\t};'''

content = content.replace(old_resources, new_resources)

# Fix the PBXBuildFile section to include Assets.xcassets
old_build_file = '''\t\t3B31A143A6394F6E910DEE27 /* Info.plist in Resources */ = {isa = PBXBuildFile; fileRef = 7BCEAC912E344D68B2D84EA8 /* Info.plist */; };
/* End PBXBuildFile section */'''

new_build_file = '''\t\t3B31A143A6394F6E910DEE27 /* Info.plist in Resources */ = {isa = PBXBuildFile; fileRef = 7BCEAC912E344D68B2D84EA8 /* Info.plist */; };
\t\t9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets in Resources */ = {isa = PBXBuildFile; fileRef = 9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets */; };
/* End PBXBuildFile section */'''

content = content.replace(old_build_file, new_build_file)

# Write the modified content back
with open(project_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Project file fixed successfully!")
