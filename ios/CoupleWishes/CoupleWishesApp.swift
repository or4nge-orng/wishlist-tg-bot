import SwiftUI

@main
struct CoupleWishesApp: App {
    @State private var session = SessionManager.shared
    @State private var authViewModel = AuthViewModel()
    @State private var coupleViewModel = CoupleViewModel()
    @State private var wishlistViewModel = WishlistViewModel()

    var body: some Scene {
        WindowGroup {
            RootView(
                session: session,
                authViewModel: authViewModel,
                coupleViewModel: coupleViewModel,
                wishlistViewModel: wishlistViewModel
            )
            .tint(AppTheme.accent)
        }
    }
}

struct RootView: View {
    let session: SessionManager
    @Bindable var authViewModel: AuthViewModel
    @Bindable var coupleViewModel: CoupleViewModel
    @Bindable var wishlistViewModel: WishlistViewModel

    var body: some View {
        Group {
            if !session.isLoggedIn {
                AuthView(viewModel: authViewModel) {
                    Task { await authViewModel.refreshSession() }
                }
            } else if !session.hasCouple {
                CoupleSetupView(viewModel: coupleViewModel) {
                    Task { await authViewModel.refreshSession() }
                }
            } else {
                WishlistView(
                    viewModel: wishlistViewModel,
                    coupleViewModel: coupleViewModel
                )
            }
        }
        .animation(.easeInOut, value: session.isLoggedIn)
        .animation(.easeInOut, value: session.hasCouple)
        .task {
            if session.isLoggedIn {
                await authViewModel.refreshSession()
            }
        }
    }
}

#Preview {
    RootView(
        session: SessionManager.shared,
        authViewModel: AuthViewModel(),
        coupleViewModel: CoupleViewModel(),
        wishlistViewModel: WishlistViewModel()
    )
}
