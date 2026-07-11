#!/usr/bin/env python3

# Create a minimal, valid project.pbxproj file
project_content = '''// !$*UTF8*!
{
\tarchiveVersion = 1;
\tclasses = {
\t};
\tobjectVersion = 56;
\tobjects = {

/* Begin PBXBuildFile section */
\t\t1E3B438FACB5408A915609DB /* CoupleWishesApp.swift in Sources */ = {isa = PBXBuildFile; fileRef = 82A75C66F6D943A4942FE05B /* CoupleWishesApp.swift */; };
\t\t4D8722E486534474B42F312E /* AuthViewModel.swift in Sources */ = {isa = PBXBuildFile; fileRef = 9B31A1BFAA02422FB80DD36B /* AuthViewModel.swift */; };
\t\t3140EE3F61254D7AABB999E4 /* CoupleViewModel.swift in Sources */ = {isa = PBXBuildFile; fileRef = 4F9A29C56B1745C59BFDF4E4 /* CoupleViewModel.swift */; };
\t\t0C60278A04CD427CA2BB6623 /* WishlistViewModel.swift in Sources */ = {isa = PBXBuildFile; fileRef = 6F521F586D8042C38DB116FC /* WishlistViewModel.swift */; };
\t\t822FCA1856ED4106AA72A5D6 /* AppTheme.swift in Sources */ = {isa = PBXBuildFile; fileRef = 3982C79157D048089D3255FD /* AppTheme.swift */; };
\t\tBC3FC692BDFA4B68AC257632 /* Couple.swift in Sources */ = {isa = PBXBuildFile; fileRef = 169767D413C141FFBE893866 /* Couple.swift */; };
\t\t985D735287BD4F009C6628C4 /* User.swift in Sources */ = {isa = PBXBuildFile; fileRef = 8FF280C2D05141F3B8E443DD /* User.swift */; };
\t\tE7064281A4C443A98342F595 /* Wish.swift in Sources */ = {isa = PBXBuildFile; fileRef = E7001DEFF1D74F23872D1631 /* Wish.swift */; };
\t\t4A11AFCE0B8B49FAABEACA7D /* AuthView.swift in Sources */ = {isa = PBXBuildFile; fileRef = F6B5F319FD73468EA5596234 /* AuthView.swift */; };
\t\tEE0830A1EF2D42BAB6457E3D /* CoupleSetupView.swift in Sources */ = {isa = PBXBuildFile; fileRef = ED825E3BE1D0461DB9F0FDEA /* CoupleSetupView.swift */; };
\t\tCFAB48AE398C459CB3975B39 /* SettingsView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 2DE76FC608A14267A08E8EEF /* SettingsView.swift */; };
\t\tD06811B707F143F09F04288D /* WishFormView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 8C8789CDA01B4CC8936766D1 /* WishFormView.swift */; };
\t\t88FB18CA669042F0945C2F01 /* WishlistView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 3ED88709EF2949FCB9DFB58C /* WishlistView.swift */; };
\t\t4347164E4635484894BD100C /* APIError.swift in Sources */ = {isa = PBXBuildFile; fileRef = B1B1BC5ADBA5400BBC147B5E /* APIError.swift */; };
\t\tDF523732DEC24678915CB3D7 /* APIService.swift in Sources */ = {isa = PBXBuildFile; fileRef = FA1B1CE371CE4287A1187FDF /* APIService.swift */; };
\t\t0F8FFB9E3E7247A3980ADD7D /* SessionManager.swift in Sources */ = {isa = PBXBuildFile; fileRef = 2A039B264C96450E95C45937 /* SessionManager.swift */; };
\t\t3B31A143A6394F6E910DEE27 /* Info.plist in Resources */ = {isa = PBXBuildFile; fileRef = 7BCEAC912E344D68B2D84EA8 /* Info.plist */; };
\t\t9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets in Resources */ = {isa = PBXBuildFile; fileRef = 9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
\t\tCB000400D4454E849B01B677 /* CoupleWishes.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = CoupleWishes.app; sourceTree = BUILT_PRODUCTS_DIR; };
\t\t82A75C66F6D943A4942FE05B /* CoupleWishesApp.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CoupleWishesApp.swift; sourceTree = "<group>"; };
\t\t9B31A1BFAA02422FB80DD36B /* AuthViewModel.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AuthViewModel.swift; sourceTree = "<group>"; };
\t\t4F9A29C56B1745C59BFDF4E4 /* CoupleViewModel.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CoupleViewModel.swift; sourceTree = "<group>"; };
\t\t6F521F586D8042C38DB116FC /* WishlistViewModel.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = WishlistViewModel.swift; sourceTree = "<group>"; };
\t\t3982C79157D048089D3255FD /* AppTheme.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AppTheme.swift; sourceTree = "<group>"; };
\t\t169767D413C141FFBE893866 /* Couple.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Couple.swift; sourceTree = "<group>"; };
\t\t8FF280C2D05141F3B8E443DD /* User.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = User.swift; sourceTree = "<group>"; };
\t\tE7001DEFF1D74F23872D1631 /* Wish.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Wish.swift; sourceTree = "<group>"; };
\t\tF6B5F319FD73468EA5596234 /* AuthView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AuthView.swift; sourceTree = "<group>"; };
\t\tED825E3BE1D0461DB9F0FDEA /* CoupleSetupView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CoupleSetupView.swift; sourceTree = "<group>"; };
\t\t2DE76FC608A14267A08E8EEF /* SettingsView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SettingsView.swift; sourceTree = "<group>"; };
\t\t8C8789CDA01B4CC8936766D1 /* WishFormView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = WishFormView.swift; sourceTree = "<group>"; };
\t\t3ED88709EF2949FCB9DFB58C /* WishlistView.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = WishlistView.swift; sourceTree = "<group>"; };
\t\tB1B1BC5ADBA5400BBC147B5E /* APIError.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = APIError.swift; sourceTree = "<group>"; };
\t\tFA1B1CE371CE4287A1187FDF /* APIService.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = APIService.swift; sourceTree = "<group>"; };
\t\t2A039B264C96450E95C45937 /* SessionManager.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SessionManager.swift; sourceTree = "<group>"; };
\t\t7BCEAC912E344D68B2D84EA8 /* Info.plist */ = {isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
\t\t9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets */ = {isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
\t\t5BCBB150648C45E6B64DA81B /* Frameworks */ = {
\t\t\tisa = PBXFrameworksBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
\t\t8D55E4A810FD4F768B0D6330 /* Products */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\tCB000400D4454E849B01B677 /* CoupleWishes.app */,
\t\t\t);
\t\t\tname = Products;
\t\t\tsourceTree = "<group>";
\t\t};
\t\t3577CFF7FA164B9BA49EADBB /* CoupleWishes */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t82A75C66F6D943A4942FE05B /* CoupleWishesApp.swift */,
\t\t\t\tC864003C505A4750A9528368 /* Models */,
\t\t\t\t6548FC690FCE442EADF16697 /* Resources */,
\t\t\t\tA1C3DDA678B14240BEDDC959 /* Services */,
\t\t\t\t70A16BAAB287436E9A0ED732 /* ViewModels */,
\t\t\t\t14F245058F434A2E8B58340D /* Views */,
\t\t\t);
\t\t\tpath = CoupleWishes;
\t\t\tsourceTree = "<group>";
\t\t};
\t\t5A18BFDC5F7C493C85C56794 /* CoupleWishes */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t82A75C66F6D943A4942FE05B /* CoupleWishesApp.swift */,
\t\t\t\tC864003C505A4750A9528368 /* Models */,
\t\t\t\t6548FC690FCE442EADF16697 /* Resources */,
\t\t\t\tA1C3DDA678B14240BEDDC959 /* Services */,
\t\t\t\t70A16BAAB287436E9A0ED732 /* ViewModels */,
\t\t\t\t14F245058F434A2E8B58340D /* Views */,
\t\t\t);
\t\t\tpath = CoupleWishes;
\t\t\tsourceTree = "<group>";
\t\t};
\t\tC864003C505A4750A9528368 /* Models */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t);
\t\t\tpath = Models;
\t\t\tsourceTree = "<group>";
\t\t};
\t\t6548FC690FCE442EADF16697 /* Resources */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t7BCEAC912E344D68B2D84EA8 /* Info.plist */,
\t\t\t\t3982C79157D048089D3255FD /* AppTheme.swift */,
\t\t\t\t9F4C8D2A1B3C4D5E6F7A8B9C /* Assets.xcassets */,
\t\t\t);
\t\t\tpath = Resources;
\t\t\tsourceTree = "<group>";
\t\t};
\t\tA1C3DDA678B14240BEDDC959 /* Services */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t);
\t\t\tpath = Services;
\t\t\tsourceTree = "<group>";
\t\t};
\t\t70A16BAAB287436E9A0ED732 /* ViewModels */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t);
\t\t\tpath = ViewModels;
\t\t\tsourceTree = "<group>";
\t\t};
\t\t14F245058F434A2E8B58340D /* Views */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t);
\t\t\tpath = Views;
\t\t\tsourceTree = "<group>";
\t\t};
\t\tF3F751CD5C3C4023ACAA65F6 = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t5A18BFDC5F7C493C85C56794 /* CoupleWishes */,
\t\t\t\t8D55E4A810FD4F768B0D6330 /* Products */,
\t\t\t);
\t\t\tsourceTree = "<group>";
\t\t};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
\t\t97E216A4ADA14E739A51F7BE /* CoupleWishes */ = {
\t\t\tisa = PBXNativeTarget;
\t\t\tbuildConfigurationList = 467B441F486F404A8977A145 /* Build configuration list for PBXNativeTarget "CoupleWishes" */;
\t\t\tbuildPhases = (
\t\t\t\t9DD057689AF14C08993E183F /* Sources */,
\t\t\t\t5BCBB150648C45E6B64DA81B /* Frameworks */,
\t\t\t\tCA3928C9805C4CCCB53FE443 /* Resources */,
\t\t\t);
\t\t\tbuildRules = (
\t\t\t);
\t\t\tdependencies = (
\t\t\t);
\t\t\tname = CoupleWishes;
\t\t\tproductName = CoupleWishes;
\t\t\tproductReference = CB000400D4454E849B01B677 /* CoupleWishes.app */;
\t\t\tproductType = "com.apple.product-type.application";
\t\t};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
\t\tE2F8AD5FAB3A41778155C730 /* Project object */ = {
\t\t\tisa = PBXProject;
\t\t\tattributes = {
\t\t\t\tBuildIndependentTargetsInParallel = 1;
\t\t\t\tLastSwiftUpdateCheck = 1600;
\t\t\t\tLastUpgradeCheck = 1600;
\t\t\t\tTargetAttributes = {
\t\t\t\t\t97E216A4ADA14E739A51F7BE = {
\t\t\t\t\t\tCreatedOnToolsVersion = 16.0;
\t\t\t\t\t};
\t\t\t\t};
\t\t\t};
\t\t\tbuildConfigurationList = E7C9396228B144E2989119B7 /* Build configuration list for PBXProject "CoupleWishes" */;
\t\t\tcompatibilityVersion = "Xcode 14.0";
\t\t\tdevelopmentRegion = en;
\t\t\thasScannedForEncodings = 0;
\t\t\tknownRegions = (
\t\t\t\ten,
\t\t\t\tBase,
\t\t\t);
\t\t\tmainGroup = F3F751CD5C3C4023ACAA65F6;
\t\t\tproductRefGroup = 8D55E4A810FD4F768B0D6330 /* Products */;
\t\t\tprojectDirPath = "";
\t\t\tprojectRoot = "";
\t\t\ttargets = (
\t\t\t\t97E216A4ADA14E739A51F7BE /* CoupleWishes */,
\t\t\t);
\t\t};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
\t\tCA3928C9805C4CCCB53FE443 /* Resources */ = {
\t\t\tisa = PBXResourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
\t\t9DD057689AF14C08993E183F /* Sources */ = {
\t\t\tisa = PBXSourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t\t1E3B438FACB5408A915609DB /* CoupleWishesApp.swift in Sources */,
\t\t\t\t4D8722E486534474B42F312E /* AuthViewModel.swift in Sources */,
\t\t\t\t3140EE3F61254D7AABB999E4 /* CoupleViewModel.swift in Sources */,
\t\t\t\t0C60278A04CD427CA2BB6623 /* WishlistViewModel.swift in Sources */,
\t\t\t\t822FCA1856ED4106AA72A5D6 /* AppTheme.swift in Sources */,
\t\t\t\tBC3FC692BDFA4B68AC257632 /* Couple.swift in Sources */,
\t\t\t\t985D735287BD4F009C6628C4 /* User.swift in Sources */,
\t\t\t\tE7064281A4C443A98342F595 /* Wish.swift in Sources */,
\t\t\t\t4A11AFCE0B8B49FAABEACA7D /* AuthView.swift in Sources */,
\t\t\t\tEE0830A1EF2D42BAB6457E3D /* CoupleSetupView.swift in Sources */,
\t\t\t\tCFAB48AE398C459CB3975B39 /* SettingsView.swift in Sources */,
\t\t\t\tD06811B707F143F09F04288D /* WishFormView.swift in Sources */,
\t\t\t\t88FB18CA669042F0945C2F01 /* WishlistView.swift in Sources */,
\t\t\t\t4347164E4635484894BD100C /* APIError.swift in Sources */,
\t\t\t\tDF523732DEC24678915CB3D7 /* APIService.swift in Sources */,
\t\t\t\t0F8FFB9E3E7247A3980ADD7D /* SessionManager.swift in Sources */,
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
\t\tAB6E143231794A4E9EC50B12 /* Debug */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = dwarf;
\t\t\t\tENABLE_TESTABILITY = YES;
\t\t\t\tGCC_DYNAMIC_NO_PIC = NO;
\t\t\t\tGCC_OPTIMIZATION_LEVEL = 0;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;
\t\t\t\tMTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
\t\t\t\tONLY_ACTIVE_ARCH = YES;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG ;
\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = -Onone;
\t\t\t};
\t\t\tname = Debug;
\t\t};
\t\tCF1198ECA7804276A111F3AA /* Release */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = dwarf-with-dsym;
\t\t\t\tENABLE_TESTABILITY = NO;
\t\t\t\tGCC_DYNAMIC_NO_PIC = NO;
\t\t\t\tGCC_OPTIMIZATION_LEVEL = s;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;
\t\t\t\tMTL_ENABLE_DEBUG_INFO = NO;
\t\t\t\tONLY_ACTIVE_ARCH = NO;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_ACTIVE_COMPILATION_CONDITIONS = "";
\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = -O;
\t\t\t};
\t\t\tname = Release;
\t\t};
\t\t2954544D719E4CB5BECA02C1 /* Debug */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tCODE_SIGN_STYLE = Automatic;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_TEAM = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tGENERATE_INFOPLIST_FILE = NO;
\t\t\t\tINFOPLIST_FILE = CoupleWishes/Resources/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.couplewishes.app;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t};
\t\t\tname = Debug;
\t\t};
\t\tA85B347872014427BDA22A39 /* Release */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tCODE_SIGN_STYLE = Automatic;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_TEAM = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tGENERATE_INFOPLIST_FILE = NO;
\t\t\t\tINFOPLIST_FILE = CoupleWishes/Resources/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.couplewishes.app;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t};
\t\t\tname = Release;
\t\t};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
\t\tE7C9396228B144E2989119B7 /* Build configuration list for PBXProject "CoupleWishes" */ = {
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\tAB6E143231794A4E9EC50B12 /* Debug */,
\t\t\t\tCF1198ECA7804276A111F3AA /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t};
\t\t467B441F486F404A8977A145 /* Build configuration list for PBXNativeTarget "CoupleWishes" */ = {
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t2954544D719E4CB5BECA02C1 /* Debug */,
\t\t\t\tA85B347872014427BDA22A39 /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t};
/* End XCConfigurationList section */
\t};
\trootObject = E2F8AD5FAB3A41778155C730 /* Project object */;
}
'''

# Write the project file
project_path = '/Users/ilyashirokov/Desktop/proga/python/wishlist-tg-api/ios/CoupleWishes.xcodeproj/project.pbxproj'
with open(project_path, 'w', encoding='utf-8') as f:
    f.write(project_content)

print("Project file created successfully!")
