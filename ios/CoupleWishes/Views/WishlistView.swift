import SwiftUI

struct WishlistView: View {
    @Bindable var viewModel: WishlistViewModel
    @Bindable var coupleViewModel: CoupleViewModel

    @State private var showAddWish = false
    @State private var wishToEdit: Wish?
    @State private var showSettings = false

    var body: some View {
        NavigationStack {
            Group {
                if viewModel.isLoading && viewModel.wishes.isEmpty {
                    ProgressView("Loading wishes...")
                } else if viewModel.wishes.isEmpty {
                    emptyState
                } else {
                    wishList
                }
            }
            .background(AppTheme.background)
            .navigationTitle("Our Wishes")
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    Button {
                        showSettings = true
                    } label: {
                        Image(systemName: "gearshape")
                    }
                }
                ToolbarItem(placement: .topBarTrailing) {
                    Button {
                        showAddWish = true
                    } label: {
                        Image(systemName: "plus.circle.fill")
                            .foregroundStyle(AppTheme.accent)
                    }
                }
            }
            .refreshable {
                await viewModel.loadWishlist()
            }
            .sheet(isPresented: $showAddWish) {
                WishFormView(mode: .create, viewModel: viewModel)
            }
            .sheet(item: $wishToEdit) { wish in
                WishFormView(mode: .edit(wish), viewModel: viewModel)
            }
            .sheet(isPresented: $showSettings) {
                SettingsView(coupleViewModel: coupleViewModel)
            }
            .task {
                await viewModel.loadWishlist()
            }
        }
    }

    private var emptyState: some View {
        VStack(spacing: 20) {
            Spacer()
            Image(systemName: "gift")
                .font(.system(size: 64))
                .foregroundStyle(AppTheme.accentLight)
            Text("No wishes yet")
                .font(.title2.bold())
            Text("Tap + to add your first wish")
                .foregroundStyle(AppTheme.secondaryText)
            Button("Add Wish") { showAddWish = true }
                .buttonStyle(PrimaryButtonStyle())
                .padding(.horizontal, 48)
            Spacer()
        }
        .padding()
    }

    private var wishList: some View {
        ScrollView {
            VStack(spacing: 16) {
                coupleHeader
                totalBanner

                ForEach(viewModel.wishes) { wish in
                    WishCard(
                        wish: wish,
                        addedBy: viewModel.couple?.users.first(where: { $0.id == wish.userAddedId })?.username
                    )
                    .onTapGesture { wishToEdit = wish }
                    .contextMenu {
                        Button("Edit") { wishToEdit = wish }
                        Button("Delete", role: .destructive) {
                            Task { await viewModel.deleteWish(wish) }
                        }
                    }
                }
            }
            .padding()
        }
    }

    private var coupleHeader: some View {
        HStack(spacing: 12) {
            Image(systemName: "heart.fill")
                .foregroundStyle(AppTheme.accent)
            if let partner = coupleViewModel.partnerName {
                Text("with \(partner)")
                    .font(.subheadline.weight(.medium))
            } else {
                Text("Waiting for partner...")
                    .font(.subheadline)
                    .foregroundStyle(AppTheme.secondaryText)
            }
            Spacer()
            if let count = viewModel.couple?.users.count {
                Text("\(count)/2")
                    .font(.caption.weight(.semibold))
                    .padding(.horizontal, 10)
                    .padding(.vertical, 4)
                    .background(AppTheme.accentLight)
                    .clipShape(Capsule())
            }
        }
        .cardStyle()
    }

    private var totalBanner: some View {
        HStack {
            Text("Total")
                .font(.subheadline)
                .foregroundStyle(AppTheme.secondaryText)
            Spacer()
            Text(viewModel.formattedTotal)
                .font(.title3.bold())
                .foregroundStyle(AppTheme.accent)
        }
        .cardStyle()
    }
}

struct WishCard: View {
    let wish: Wish
    let addedBy: String?

    var body: some View {
        HStack(spacing: 14) {
            wishImage

            VStack(alignment: .leading, spacing: 6) {
                Text(wish.name)
                    .font(.headline)
                    .lineLimit(2)

                Text(wish.formattedPrice)
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(AppTheme.accent)

                if let addedBy {
                    Text("by \(addedBy)")
                        .font(.caption)
                        .foregroundStyle(AppTheme.secondaryText)
                }

                if wish.hasURL {
                    Label("Has link", systemImage: "link")
                        .font(.caption2)
                        .foregroundStyle(AppTheme.secondaryText)
                }
            }

            Spacer()

            Image(systemName: "chevron.right")
                .font(.caption)
                .foregroundStyle(AppTheme.secondaryText)
        }
        .cardStyle()
    }

    @ViewBuilder
    private var wishImage: some View {
        if wish.hasImage, let urlString = wish.image, let url = URL(string: urlString) {
            AsyncImage(url: url) { image in
                image.resizable().aspectRatio(contentMode: .fill)
            } placeholder: {
                placeholderImage
            }
            .frame(width: 64, height: 64)
            .clipShape(RoundedRectangle(cornerRadius: 10))
        } else {
            placeholderImage
        }
    }

    private var placeholderImage: some View {
        RoundedRectangle(cornerRadius: 10)
            .fill(AppTheme.accentLight)
            .frame(width: 64, height: 64)
            .overlay {
                Image(systemName: "gift.fill")
                    .foregroundStyle(AppTheme.accent.opacity(0.6))
            }
    }
}

#Preview {
    WishlistView(viewModel: WishlistViewModel(), coupleViewModel: CoupleViewModel())
}
